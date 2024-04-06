import json
import sqlite3
import csv

# Read data from the JSON file
with open('LT_Python/DB/questionDoctorQAs.json', 'r') as file:
    data = json.load(file)

# Create a SQLite database and connect to it
conn = sqlite3.connect('LT_Python/DB/qa.db')
cursor = conn.cursor()

# Create a table to store the questions, answers, and doctors
cursor.execute('''CREATE TABLE IF NOT EXISTS qa (
                    question TEXT,
                    answer TEXT,
                    doctor TEXT
                )''')

# Insert data into the table
for item in data:
    question = item['question']
    answer = item['answer']
    doctor = item['answer_author']
    cursor.execute("INSERT INTO qa VALUES (?, ?, ?)", (question, answer, doctor))

# Commit the changes and close the connection
conn.commit()
conn.close()
print()

# Export data to CSV file
with open('LT_Python/DB/QA_doctor.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(['STT', 'Question', 'Answer', 'Doctor'])
    conn = sqlite3.connect('LT_Python/DB/qa.db')
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer, doctor FROM qa")
    rows = cursor.fetchall()
    for index, row in enumerate(rows, start=1):
        writer.writerow([index] + list(row))
    conn.close()

# Generate statistics
conn = sqlite3.connect('LT_Python/DB/qa.db')
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM qa")
total_qa = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(DISTINCT doctor) FROM qa")
total_doctors = cursor.fetchone()[0]
conn.close()

# Write statistics to a text file
with open('LT_Python/DB/Stat.txt', 'w', encoding='utf-8') as file:
    file.write(f"Total questions-answers: {total_qa}\n")
    file.write(f"Total doctors: {total_doctors}\n")