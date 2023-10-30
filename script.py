import mysql.connector
import os
from random import sample
from html import escape
import zipfile

# MySQL database connection
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "ci-cd"
}

# Get the current number of exam papers in the directory
existing_papers = []
paper_number = len(existing_papers) + 1

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Add a message to indicate a successful database connection
    print("Connected to the database.")

    # Change the SQL query to select only the necessary columns
    cursor.execute("SELECT question_text, option_a, option_b, option_c, option_d, metadata FROM exam_questions ORDER BY RAND() LIMIT 5")
    questions = cursor.fetchall()

    # Assemble questions into an HTML exam paper with some basic styling
    exam_paper = """
    <html>
    <head>
        <title>Exam Paper</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 20px;
            }
            h1 {
                text-align: center;
                background-color: #333;
                color: #fff;
                padding: 10px;
            }
            p {
                background-color: #fff;
                padding: 10px;
                margin: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <h1>Exam Paper</h1>
    """

    for i, question in enumerate(questions, start=1):
        question_text, option_a, option_b, option_c, option_d, metadata = question
        options = [option_a, option_b, option_c, option_d]

        # Shuffle the order of options
        shuffled_options = sample(options, len(options))

        exam_paper += f"<p><strong>Q{i}:</strong> {escape(question_text)}<br>"

        for j, option in enumerate(shuffled_options, start=1):
            exam_paper += f"{chr(64 + j)}. {escape(option)} "

        # Find the correct answer among the shuffled options
        correct_option_index = shuffled_options.index(option_a)

        exam_paper += f"<br><strong>Correct Answer:</strong> {chr(65 + correct_option_index)}<br><em>Category: {escape(metadata)}</em></p>"

    exam_paper += "</body></html>"

    # Save the exam paper as an HTML file
    file_name = f"exam_paper{paper_number}.html"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(exam_paper)

    # Create a zip file containing the HTML
    with zipfile.ZipFile('exam_paper.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_name, file_name)

    print(f"Exam paper saved as {file_name}")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
