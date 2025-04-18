import pymysql

conn = None 

def connect():
    global conn
    conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="lab1",
    cursorclass=pymysql.cursors.DictCursor
)
    
def get_all_cars():
    if conn is None:
        connect()
    query = "SELECT * FROM CAR"

    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def get_car_by_reg(registration):
    if conn is None:
        connect()
    query = "SELECT * FROM CAR WHERE registration = %s"

    cursor = conn.cursor()
    cursor.execute(query, (registration,))
    result = cursor.fetchall()
    cursor.close()
    return result
    
def add_car(car):
    if conn is None:
        connect()
    query = "INSERT INTO car(registration,make,model,colour,mileage,engineSize) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (car.get("registration"), car.get("make"),car.get("model"),car.get("colour"),car.get("mileage"),car.get("engineSize"))

    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    result = "Car added successfully" 
    return result

def update_car(car):
    if conn is None:
        connect()
    query = "UPDATE car SET make=%s, model=%s, colour=%s, mileage=%s, engineSize=%s  WHERE registration= %s"
    values = (car.get("make"),car.get("model"),car.get("colour"),car.get("mileage"),car.get("engineSize"), car.get("registration"))

    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    result = "Car updated successfully"
    cursor.close()
    return result

def delete_car(reg):
    if conn is None:
        connect()
    query = "DELETE FROM CAR WHERE registration = %s"

    cursor = conn.cursor()
    cursor.execute(query, (reg,))
    result = "Car deleted from database successfully"
    cursor.close()
    return result



