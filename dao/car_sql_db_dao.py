import pymysql
import config.dbconfig as config

def connect():
    return pymysql.connect(
        host=config.mysql['host'],
        user=config.mysql['user'],
        password=config.mysql['password'],
        database=config.mysql['database'],
        cursorclass=pymysql.cursors.DictCursor
        )
   
def get_all_cars():
    conn = connect()
    query = "SELECT * FROM car"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def get_car_by_reg(registration):
    conn = connect()
    query = "SELECT * FROM car WHERE registration = %s"

    cursor = conn.cursor()
    cursor.execute(query, (registration,))
    result = cursor.fetchall()
    cursor.close()
    return result
    
def add_car(car):
    conn = connect()
    query = "INSERT INTO car(registration,make,model,colour,mileage,engineSize) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (car.get("registration"), car.get("make"),car.get("model"),car.get("colour"),car.get("mileage"),car.get("engineSize"))

    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()

def update_car(car):
    conn = connect()
    query = "UPDATE car SET make=%s, model=%s, colour=%s, mileage=%s, engineSize=%s  WHERE registration= %s"
    values = (car.get("make"),car.get("model"),car.get("colour"),car.get("mileage"),car.get("engineSize"), car.get("registration"))

    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()

def delete_car(reg):
    conn = connect()
    query = "DELETE FROM car WHERE registration = %s"

    cursor = conn.cursor()
    cursor.execute(query, (reg,))
    conn.commit()
    cursor.close()


