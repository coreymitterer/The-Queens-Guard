import imaplib
import email

user = 'thequeensguard25@gmail.com'
password = 'cgdq plxb roap mdeb'
imap_url = 'imap.gmail.com'


# Gets email content if there are replies it gets all parts 
def get_content(msg):
    if msg.is_multipart():
        return get_content(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)
        

def search(key, value, con):
    result, data = con.search(None, key, "{}".format(value))
    return data

def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        type, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs

con = imaplib.IMAP4_SSL(imap_url) 

con.login(user, password) 

con.select('Inbox') 

msgs = get_emails(search('FROM', 'coreymit@udel.edu', con))

for msg in msgs[::-1]: 
    for sent in msg:
        if type(sent) is tuple: 
 
            # encoding set as utf-8
            content = str(sent[1], 'utf-8') 
            data = str(content)
 
            # Handling errors related to unicodenecode
            try: 
                indexstart = data.find("ltr")
                data2 = data[indexstart + 5: len(data)]
                indexend = data2.find("</div>")
 
                # printing the required content which we need
                # to extract from our email i.e our body
                print(data2[0: indexend])
 
            except UnicodeEncodeError as e:
                pass