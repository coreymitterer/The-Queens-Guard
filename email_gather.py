from imap_tools import MailBox
from gemini import is_email_content_malicious
from setup_env import create_dotenv
from dotenv import load_dotenv
import os
from link_detctor import check_url_status
import json

def emails_main(num: int):
    #Initialize .env
    create_dotenv()
    load_dotenv()
    user = os.getenv('EMAIL_ADDRESS')
    password = os.getenv('USER_PWD')
    imap_url = os.getenv('IMAP_URL')
    virus_total = os.getenv('VIRUSTOTAL_API')

    #Get first num emails from mailbox
    emails = []
    with MailBox('imap.gmail.com').login('thequeensguard25@gmail.com', 'hwjs uvap zdqz xzfx') as mailbox:
        for msg in mailbox.fetch(limit=num, reverse=True):
            emails.append({"subject": msg.subject, "email_body": msg.text, "email_uid": msg.uid})

    #Combine the results of phishing scan into single output dictionary
    combined = []
    for email in emails:
        #Pass the email body to gemini, returns a dict with:
        # 'subject_line': 'IRS - Taxes', 
        # 'is_email_malicious': True, 
        # 'percent_certainty': 95, 
        # 'is_there_a_link': True, 
        # 'included_link': 'https://grabify.org/27CB2'
        # 'is_link_malicious': True

        #Make Gemini call
        results = is_email_content_malicious(email)
        jsond = json.loads(results)
        
        combined.append(jsond)
    return combined

#Testing
print(emails_main(1))