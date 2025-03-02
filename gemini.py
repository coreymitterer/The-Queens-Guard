from google import genai
from dotenv import load_dotenv
import os
from pydantic import BaseModel

def is_email_content_malicious(email: dict) -> dict:
    email_subject = email["subject"]
    email_content = email["email_body"]
    
    load_dotenv()
    GEMINI_KEY = os.getenv('GEMINI_API_KEY')

    class is_malicious(BaseModel): 
        subject_line: str
        is_email_malicious: bool
        percent_certainty: int
        is_there_a_link: bool
        included_link: str

    client = genai.Client(api_key=GEMINI_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents="After reading the following email, whould you consider this to be malicious? Also, if there is a link inside the body of the email, list that and the included link.: Subject: " + email_subject + " Email Body: " + email_content,
        config={
            'response_mime_type': 'application/json',
            'response_schema': is_malicious,
        },
    )
    #print(response.text)
    return(response.text)
