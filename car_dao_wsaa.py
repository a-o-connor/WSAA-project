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
    
def add_car(registration,make,model,colour,mileage,engineSize):
    if conn is None:
        connect()
    query = "INSERT INTO car(registration,make,model,colour,mileage,engineSize) VALUES (%s, %s, %s, %s, %s, %s)"

    
    cursor = conn.cursor()
    cursor.execute(query, (registration,make,model,colour, mileage, engineSize,))
    conn.commit()
    cursor.close()
    result = "Car added successfully" 
    return result


