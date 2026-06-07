# השתמש בגרסה רשמית של פייתון
FROM python:3.9-slim

# הגדרת תיקיית עבודה
WORKDIR /app

# העתקת דרישות והתקנתן
COPY requirements.txt .
RUN pip install -r requirements.txt

# העתקת כל שאר הקבצים
COPY . .

# הרצת האפליקציה
CMD ["streamlit", "run", "app.py", "--server.port", "8080"]
