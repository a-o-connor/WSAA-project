import pymysql

conn = None 

def connect():
    global conn
    conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital",
    cursorclass=pymysql.cursors.DictCursor
)

def get_patient(ppsn):
    if conn is None:
        connect()
    query = "SELECT * FROM patient_table WHERE PPSN = %s"

    cursor = conn.cursor()
    cursor.execute(query, (ppsn,))
    result = cursor.fetchall()
    cursor.close()
    return result
    

def add_patient(ppsn, first_name, surname, address, doctorID):
    if conn is None:
        connect()
    query = "INSERT INTO patient_table(ppsn, first_name, surname, address, doctorID) VALUES (%s, %s, %s, %s, %s)"

    
    cursor = conn.cursor()
    cursor.execute(query, (ppsn, first_name, surname, address, doctorID))
    conn.commit()
    cursor.close()
    result = "Patient added successfully" 
    return result

def find_patient(surname):
    if conn is None:
        connect()
    query = "SELECT * FROM patient_table WHERE surname LIKE %s"
    like_surname = "%" + surname + "%"

    
    cursor = conn.cursor()
    cursor.execute(query, (like_surname,))
    result = cursor.fetchall()
    cursor.close()
    return result