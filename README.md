# ETL Pipeline Using Python and PostgreSQL

## Overview

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Python and PostgreSQL.

The pipeline extracts product data from a public REST API, performs data cleaning and validation, and loads the processed data into a PostgreSQL database.

This project demonstrates fundamental data engineering concepts including data extraction, transformation, validation, database integration, logging, and modular software design.

---

## Features

* Extract data from REST API
* Clean and transform data using Pandas
* Validate data quality before loading
* Load data into PostgreSQL
* Environment variable configuration
* Logging support
* Modular ETL architecture
* Batch data loading

---

## Project Architecture

API Source

↓

Extract Layer

↓

Transform Layer

↓

Validation Layer

↓

PostgreSQL Database

---

## Technologies Used

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* Psycopg2
* Python Dotenv

---

## Project Structure

etl-project/

├── config/

├── extract/

├── transform/

├── validate/

├── load/

├── sql/

├── main.py

├── requirements.txt

└── README.md

├── screenshots/

---

## Database Schema

products

* id
* title
* price
* category

---

## Setup Instructions

### Clone Repository

git clone <repository-url>

cd etl-project

### Install Dependencies

pip install -r requirements.txt

### Configure Environment Variables

Create a .env file using .env.example.

### Create Database

CREATE DATABASE shopdb;

### Create Table

Run create_tables.sql

### Execute ETL

python main.py

---

## Sample Output

CONNECTED SUCCESSFULLY

20 rows inserted successfully

---

## Future Improvements

* Apache Airflow Scheduling
* Docker Deployment
* Incremental Loading
* Data Quality Reports
* Automated Monitoring
* CI/CD Integration

---

## Author

Diyana Kaluarachchi

Third Year Undergraduate

Sri Lanka Institute of Information Technology (SLIIT)
