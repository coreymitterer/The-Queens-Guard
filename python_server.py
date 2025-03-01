from flask import Flask, jsonify, request
from email_gather import emails_main
import json

app = Flask(__name__)

@app.route('/<number>', methods=['GET'])
def scan_emails(number):
    return json.loads(emails_main(int(number)))