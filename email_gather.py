from imap_tools import MailBox
from gemini import is_email_content_malicious
from setup_env import create_dotenv
from dotenv import load_dotenv
import os
from link_detctor import check_url_status

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
            emails.append({"subject": msg.subject, "email_body": msg.text})

    #Combine the results of phishing scan into single output string
    combined = '['
    for email in emails:
        #Pass the email body to gemini, returns a dict with:
        #    subject_line: str
        #    is_email_malicious: bool
        #    percent_certainty: int
        #    is_there_a_link: bool
        #    included_link: str
        results = is_email_content_malicious(email)

        if combined == "[":
            combined = combined + results
        else:
            combined = combined + ', ' + results

        #If is_there_a_link == true, then pass the link to link_detector
        #if results["is_there_a_link"] == True:
            #url_result = check_url_status(results["included_link"])
    combined = combined + ']'

    return combined

#Testing
print(emails_main(3))