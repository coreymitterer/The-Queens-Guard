import imaplib
import email
import quopri

user = 'thequeensguard25@gmail.com'
password = 'cgdq plxb roap mdeb'
imap_url = 'imap.gmail.com'

def get_content(msg):
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            # Extract text content (ignore attachments)
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

# Connect to Gmail
con = imaplib.IMAP4_SSL(imap_url)
con.login(user, password)
con.select('Inbox')

# Search emails from a specific sender
msgs = get_emails(5, con)

# Print cleaned email content
for msg in msgs:
    
    print(msg)
