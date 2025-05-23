# WSAA Coursework
## Web Services and Applications
**By A. O'Connor**
*********
<p align="center">
  <img src="https://tse3.mm.bing.net/th?id=OIP.t1Tj83H0YrBBMicwWmAU2QHaKF&cb=iwc2&pid=Api" alt="Flask Logo" />
</p>

*********

## Introduction
This Git repository contains a Flask app written for the *Web Services and Applications* module, part of my Higher Diploma in Computer Science and Data Analytics at ATU. Details of the contents of each folder in this repository are provided in the **Contents** section below. 

## Contents

### 1. Config 
   - **Files**: `dbconfig.py`,
   - **Description**: A file containing config details for connecting to the Database containing the cars. Currently the config details saved in this file access the database via Python Anywhere. If running the app locally, change these comfig details accordingy. 

### 2. dao
   - **Files**: `car_sql_db_dao.py`, `private_cars_cso_dao.py` 
   - **Description**: A script that accessses car data from a sql databases, and a script that retrieves the dataset for the **Private Cars Licenced in Ireland** from a public RESTful API supplied by the CSO. 
   - **Libraries/Modules**: `requests`, `json`, `pymysql`

### 3. templates 
   - **File**: `car_viewer.html`  
   - **Description**: The HTML page that retrieves the data from the different endpoints of the server using AJax, and displays the data in a table. The page allows users to update, create and delete cars in the database.
   - **Libraries/Modules**: `requests`, `json`, `config`, `github` 

