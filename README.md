# 🏔️ Himalayan Tourism Analysis & Management System

A Python-based Tourism Analytics and Management System that combines **Data Analysis, Visualization, Database Management, and Desktop Application Development**.

This project analyzes existing Himalayan tourism data to discover useful business insights and provides a Tkinter + MySQL based application to collect and manage new tourism booking data for future analysis.

---

# 📌 Project Overview

The project contains two major modules:

## 📊 1. Tourism Data Analysis

The analysis is performed on a pre-existing Himalayan tourism dataset.

The purpose of this analysis is to understand tourism patterns, customer preferences, and business growth opportunities using data-driven techniques.

Insights generated from analysis help answer questions like:

- Should the tourism business expand?
- Which destinations attract the most tourists?
- Which months require more advertisements?
- Which adventure destinations are most popular?
- What are foreign tourist preferences?
- How can hotels and packages be planned better?

---

## 🖥️ 2. Tourism Management System

A desktop application created using Python Tkinter and MySQL.

The application helps tourism companies digitally store new customer booking information.

The newly collected data acts as a future dataset that can be used for:

- Future tourism analysis
- Customer behaviour study
- Business forecasting
- Machine Learning predictions

---

# ✨ Features

## 📈 Data Analysis Features

✔ Year-wise tourism growth analysis  
✔ Monthly tourist trend analysis  
✔ Tourist increase comparison  
✔ State-wise tourism popularity  
✔ Top adventure destination analysis  
✔ Foreign tourist preference analysis  
✔ Average stay duration analysis  
✔ Revenue insights  
✔ Hotel occupancy analysis  
✔ Customer satisfaction analysis  

---

## 🖥️ Management System Features

✔ Add customer bookings  
✔ Update booking information  
✔ Delete records  
✔ Search booking details  
✔ Display stored data  
✔ Store records permanently using MySQL  
✔ Destination based state selection  
✔ Package management  
✔ Hotel and room management  
✔ Automatic total price calculation  
✔ Generate new tourism dataset  

---

# 🛠️ Technologies Used

- Python
- Tkinter
- MySQL
- Pandas
- Matplotlib
- Jupyter Notebook
- Excel Dataset
- MySQL Connector

---

# 📂 Project Structure

```
Himalayan-Tourism-System/

│
├── main.py
│
├── dashboard_analysis.py
│
├── tourism_analysis.ipynb
│
├── Himalayan_Tourism.xlsx
│
└── README.md
```

---

# 📊 Dataset Information

The existing dataset contains tourism-related information including:

- Year
- Month
- State
- Destination
- Total tourists
- Foreign tourists
- Adventure tourists
- Revenue
- Hotel occupancy
- Satisfaction ratings
- Average stay duration

---

# 📊 Analysis Performed

## Tourism Growth Analysis

Used yearly tourist data to identify business growth trends.

---

## Monthly Trend Analysis

Identifies peak and low tourism seasons to improve advertisement planning.

---

## Destination Analysis

Finds locations receiving maximum tourist visits.

---

## Adventure Tourism Analysis

Determines popular destinations for adventure packages.

---

## Foreign Tourist Analysis

Studies destinations preferred by international tourists.

---

## Stay Duration Analysis

Helps businesses plan hotel availability and packages.

---

# 🗄️ MySQL Database Setup

The Tkinter application stores booking records inside MySQL.

Create the database:

```sql
CREATE DATABASE tourism_management;

USE tourism_management;
```

Create bookings table:

```sql
CREATE TABLE bookings
(
    booking_id INT AUTO_INCREMENT PRIMARY KEY,

    customer_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,

    destination VARCHAR(100),
    state VARCHAR(100),

    package_type VARCHAR(50),
    travellers INT,

    check_in VARCHAR(30),
    check_out VARCHAR(30),

    hotel_type VARCHAR(50),
    room_type VARCHAR(50),

    package_price DECIMAL(10,2),
    total_amount DECIMAL(10,2),

    booking_status VARCHAR(50),

    email VARCHAR(100),
    booked_by VARCHAR(100),

    remarks TEXT
);
```

---

# 🔗 Database Connection

Change MySQL credentials according to your system:

```python
mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="tourism_management"
)
```

Example:

```python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="tourism_management"
)
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Himalayan-Tourism-System.git
```

Move into project folder:

```bash
cd Himalayan-Tourism-System
```

Install required libraries:

```bash
pip install pandas matplotlib openpyxl mysql-connector-python
```

Run the application:

```bash
python main.py
```

---

# 📈 Project Workflow

```
Existing Tourism Dataset
            |
            ↓
Data Cleaning & Analysis
            |
            ↓
Data Visualization
            |
            ↓
Business Insights
            |
            ↓
Tkinter Management System
            |
            ↓
New Booking Data Collection
            |
            ↓
Future Dataset Creation
```

---

# 🚀 Future Improvements

- Machine Learning based tourist prediction
- Online booking website
- Interactive dashboard
- Customer recommendation system
- Revenue prediction model
- Cloud database integration
- Login authentication system

---

# 🎯 Purpose of Project

The main objective of this project is to combine historical tourism data analysis with a real-world data collection system.

Instead of only analyzing old data, the application creates a pipeline where new data can continuously be collected and used for future improvements.

---

# 👨‍💻 Developer

Developed as a Python Data Analytics + Database Management project.

---

# ⭐ Support

If you found this project useful, consider giving the repository a ⭐.
