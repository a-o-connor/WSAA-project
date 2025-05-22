from flask import Flask, request, jsonify, render_template
import car_dao_wsaa
import private_cars_cso_dao
import pymysql

app = Flask(__name__, static_url_path="", static_folder="staticpages")

@app.route("/", methods = ["GET"])
def index():
    return render_template("car_viewer.html")

@app.route("/cars", methods = ["GET"])
def get_all_cars():
    car_table = car_dao_wsaa.get_all_cars()
    return jsonify(car_table)

@app.route("/cars/<reg>", methods = ["GET"])
def get_car_by_reg(reg):
    try:
        car = car_dao_wsaa.get_car_by_reg(reg)
        if car: 
            return jsonify(car)
        else:
            return f"Error: Car with registration {reg} not found" 
    except pymysql.err.IntegrityError as e:
        return jsonify({"error": f"Car with registration {reg} not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/cars/<reg>", methods = ["DELETE"])
def delete_car(reg):
    try:
         car_dao_wsaa.delete_car(reg)
         return jsonify({"registration": reg})
    except pymysql.err.IntegrityError as e:
        return jsonify({"error": f"Car with registration {reg} not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route("/cars", methods = ["POST"])
def add_car():
    try:
         json_car = request.json
         car_dao_wsaa.add_car(json_car)
         return jsonify(json_car)
    except pymysql.err.IntegrityError as e:
        return jsonify({"error": f"Car with registration {json_car.get('registration')} already exists in database"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/cars", methods = ["PUT"])
def update_car():
    try:
         json_car = request.json
         car_dao_wsaa.update_car(json_car)
         return jsonify(json_car)
    except pymysql.err.IntegrityError as e:
        return jsonify({"error": f"Car with registration {json_car.get('registration')} not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/cars/recently_licenced_ireland", methods = ["GET"])
def cars_licenced_ireland():
    result = {
        "month": private_cars_cso_dao.month,
        "cars_licenced": private_cars_cso_dao.cars_licenced
    }
    return result



if __name__ == "__main__":
    app.run(debug=True)
