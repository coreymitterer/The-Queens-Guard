import imaplib
import email
import quopri
from gemini import is_email_content_malicious
from setup_env import create_dotenv
from dotenv import load_dotenv
import os
from link_detctor import check_url_status

#Create and Import the .env
create_dotenv()
load_dotenv()

#Get the Environment Variables from .env
user = os.getenv('EMAIL_ADDRESS')
password = os.getenv('USER_PWD')
imap_url = os.getenv('IMAP_URL')
virus_total = os.getenv('VIRUSTOTAL_API')

def get_content(msg):
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            if "attachment" not in content_disposition and content_type in ["text/plain", "text/html"]:
                payload = part.get_payload(decode=True)
                return payload.decode("utf-8", errors="ignore")
    else:
        return msg.get_payload(decode=True).decode("utf-8", errors="ignore")

def search(key, value, con):
    result, data = con.search(None, key, f'"{value}"')
    return data

def get_emails(n, con):
    # Fetch all emails
    result, data = con.search(None, 'ALL')
    email_ids = data[0].split()
    
    # Get the last n emails
    last_n_ids = email_ids[-n:]  # Fetch the last 'n' email IDs
    msgs = []
    for email_id in last_n_ids:
        typ, data = con.fetch(email_id, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                msgs.append(get_content(msg))
    return msgs


con = imaplib.IMAP4_SSL(imap_url)
con.login(user, password)
con.select('Inbox')

msgs = get_emails(1, con)

for msg in msgs:
    #Pass the email body to gemini, returns a dict with:
    #    is_email_malicious: bool
    #    percent_certainty: int
    #    is_there_a_link: bool
    #    included_link: str
    results = is_email_content_malicious(msg)
    print(msg)
    print()

    #If is_there_a_link == true, then pass the link to link_detector
    if results["is_there_a_link"] == True:
        url_result = check_url_status(results["included_link"])

    #TODO: Save results and url_results in some way
