from flask import Flask, render_template, request
from email_gather import emails_main  # Assuming emails_main is in emails_checker.py
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        try:
            num_emails = int(request.form['num_emails'])
            results = emails_main(num_emails)  # Call phishing detection function
        except ValueError:
            results = "Invalid input. Please enter a valid number."
    return render_template('index.html', results=json.loads(json.dumps(results)))  # Ensure proper data handling


if __name__ == '__main__':
    app.run(debug=True)