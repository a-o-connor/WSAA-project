# WSAA Coursework
## Web Services and Applications
**By A. O'Connor**
*********
<p align="center">
  <img src="https://tse3.mm.bing.net/th?id=OIP.t1Tj83H0YrBBMicwWmAU2QHaKF&cb=iwc2&pid=Api" alt="Flask Logo" />
</p>

*********

## Introduction
This Git repository contains a Flask app written for the *Web Services and Applications* module, part of my Higher Diploma in Computer Science and Data Analytics at ATU. The app is hosted at Python Anywhere, at the following link: https://ailsa.pythonanywhere.com/

The app links to a SQL database that contains details (registration, make, model, colour, mileage, and engine size) about various cars. On the main page of the app, users can view a table displaying these car records. Buttons allow a user to create, update or delete a car. Any changes made are pushed back to the SQL database and updated the app table. The user can also create a new car and add this to the database. 

The app also links into a publicly available API provided by the CSO. This API reports the number of cars licenced per month across Irish counties. The app pulls the most recent dataset available and displays the cars registered in that month in Ireland, by county. This API is available at the following address: [Private cars licenced - CSO API](https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/DOTM05/JSON-stat/2.0/en). 
 

## Repository Structure

### 1. Config Folder 
   - **Files**: `dbconfig.py`, `car_database.sql`
   - **Description**: A file containing config details for connecting to the Database containing the cars. Currently the config details saved in this file access the database via Python Anywhere. If running the app locally, a sample SQL database `car_database.sql`, is also available in this folder. Import this file onto your local SQL and change the connection detalis in the `dbconfig.py` file accordingly. 

### 2. DAO Folder
   - **Files**: `car_sql_db_dao.py`, `private_cars_cso_dao.py` 
   - **Description**: Scripts to access the two data sources. One script interacts with the local SQL database and the other accesses the car registration data from the CSO public API. 
   - **Libraries/Modules**: `requests`, `json`, `pymysql`

### 3. Templates Folder
   - **File**: `car_viewer.html`  
   - **Description**: The HTML page that communicates with both databases using AJAX functions.
   - **Libraries/Modules**: `HTML`, `AJAX`, `JavaScript`

### 4. Main
   - **File**: `server_cars.py`  
   - **Description**: This file is the Flask server that defines the endpoints that handle the HTTP methods `GET`, `PUT`, `POST` and `DELETE`. The main app links to the HTML page in the template folder for viewing the data. 
   - **Libraries/Modules**: `requests`, `json`, `config`, `github`

### Dependencies
- The required Python dependencies are listed in `requirements.txt`.
- Install dependencies using:
    ````bash
    pip install -r requirements.txt
    ````




