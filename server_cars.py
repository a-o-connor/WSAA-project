from flask import Flask, request, jsonify
import car_dao_wsaa

app = Flask(__name__, static_url_path="", static_folder="staticpages")

@app.route("/cars", methods = ["GET"])
def getall():
    car_table = car_dao_wsaa.get_all_cars()
    return jsonify(car_table)

@app.route("/cars/<reg>", methods = ["GET"])
def get_car_by_reg(reg):
    car = car_dao_wsaa.get_car_by_reg(reg) 
    return jsonify(car)


@app.route("/cars", methods = ["POST"])
def add_a_car():
    json_car = request.json
    car_dao_wsaa.add_car(**json_car)

if __name__ == "__main__":
    app.run(debug=True)
