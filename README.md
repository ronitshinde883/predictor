# MHT CET College Predictor (Pune)

This is a web application that predicts possible engineering colleges for students based on their **MHT CET percentile, category, and preferred branch**.

The project is built using Python and Django and currently supports **engineering colleges in Pune**. The system compares the student's percentile with previous cutoff data stored in the database and displays colleges that the student may get.

---

## Features

- Predict colleges using **MHT CET percentile**
- Filter predictions based on:
  - Category
  - Preferred branch
- Uses **previous year cutoff data**
- Simple and user-friendly interface
- Backend logic implemented in Django
- PostgreSQL database for storing cutoff data

---

## Tech Stack

Backend  
- Python  
- Django  

Frontend  
- HTML  
- CSS  
- JavaScript  

Database  
- PostgreSQL  

---

## Project Structure

```
PREDICT/
│
├── predictorbase/        # Django project settings
│
├── predictorapp/         # Main application
│   ├── migrations/
│   ├── views/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── signal.py
│   ├── tests.py
│   ├── urls.py
│
├── templates/            # HTML templates
│
├── manage.py             # Django project manager
│
├── .gitignore
│
└── venv/                 # Virtual environment
```

---

## How the Predictor Works

1. The user enters:
   - MHT CET percentile
   - Category
   - Preferred branch

2. The system checks the cutoff database.

3. Colleges whose cutoff percentile is **less than or equal to the user's percentile** are displayed as predicted colleges.

---

## Installation

Clone the repository

```
git clone https://github.com/ronitshinde883/predictor
```

Move to the project folder

```
cd mhtcet-predictor
```

Install dependencies

```
pip install -r requirements.txt
```

Run migrations

```
python manage.py migrate
```

Start the server

```
python manage.py runserver
```

Open in browser

```
http://127.0.0.1:8000/
```

---

## Current Limitations

- Only **Pune colleges supported**
- Limited cutoff dataset
- Predictions based on previous year trends

---

## Future Improvements

- Add colleges from all Maharashtra
- Add multiple years cutoff data
- Improve prediction accuracy
- Add login system
- Add college comparison
- Allow users to save predicted colleges

---

## Author

Developed as a project to help students estimate possible college admissions after MHT CET results.