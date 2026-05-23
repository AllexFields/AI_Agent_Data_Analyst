# AI Data Analyst

An interactive AI-powered data analysis web application built using Python, Streamlit, Pandas, and Plotly.

This project allows users to upload CSV datasets, automatically inspect the data, generate KPIs, and create interactive visualizations — all through a modern dashboard interface.

---

# Features

## CSV Upload System

* Upload CSV datasets directly from the browser
* Automatic file reading with encoding handling
* Responsive dataset preview

## Automatic Dataset Analysis

The application automatically detects:

* Number of rows and columns
* Column data types
* Missing values
* Duplicate rows
* Numeric columns
* Summary statistics

## KPI Dashboard

Automatically generated KPI cards including:

* Total Rows
* Total Columns
* Missing Values
* Duplicate Rows
* Numeric Columns

## Automatic Visualizations

Interactive charts generated dynamically using Plotly:

* Histogram
* Bar Chart
* Pie Chart

## Modern UI

* Dark theme dashboard
* Hero banner section
* Responsive layout
* Interactive visualizations

---

# Tech Stack

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Core programming language    |
| Streamlit  | Web application framework    |
| Pandas     | Data analysis and processing |
| Plotly     | Interactive visualizations   |
| Openpyxl   | Excel file support           |

---

# Project Structure

```text
AI_Data_Analyst/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── banner.jpg
│
└── .streamlit/
    └── config.toml
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/AI_Data_Analyst.git
```

## Move Into Project Folder

```bash
cd AI_Data_Analyst
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run The Application

```bash
streamlit run app.py
```

---

# Streamlit Cloud Deployment

This project can be deployed easily using Streamlit Community Cloud.

## Deployment Steps

1. Push project to GitHub
2. Login to Streamlit Cloud
3. Connect GitHub repository
4. Select `app.py`
5. Deploy application

---

# Current Functionalities

* CSV Upload
* Data Preview
* Dataset Inspection
* KPI Dashboard
* Interactive Charts
* Responsive UI

---

# Future Improvements

Planned features for future versions:

* AI-generated business insights
* Natural language queries
* Chat-based analytics assistant
* Advanced filtering system
* Downloadable reports
* Automated chart recommendations
* Machine learning integration
* API-based AI integration
* Multi-file support

---

# Learning Goals Behind This Project

This project is designed to improve skills in:

* Python programming
* Data analysis
* Dashboard development
* Streamlit application building
* Data visualization
* Business intelligence concepts
* AI-powered analytics systems

---

# Author

Shivam Thakur

# 📬 Connect With Me

- 💼 LinkedIn: https://www.linkedin.com/in/shivam-thakur-55b167406/
- 📧 Email: dataanalyst.shivamthakur@gmail.com
---

# License

This project is open-source and available for learning and educational purposes.
