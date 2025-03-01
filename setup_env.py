from pathlib import Path
import os
# Check for a .env file 
def env_exists() -> bool:
    env_file = Path(".env")
    if env_file.exists():
        return True
    else:
        return False

#Create a .env file
def create_dotenv() -> None:
    env = None
    #If .env does not exist, greate a .env
    if not env_exists():
        env = open(".env", "w")
        env.close()
        env = None

    #Once .env exists, open the file as read
    env = open(".env", "r")
    env_str = env.read()
    env.close()
    env = None

    env = open(".env", "a")
    #Check for Imap URL, add if not found
    if env_str.find("IMAP_URL=") == -1:
        env.write("IMAP_URL=\"imap.gmail.com\"\n")

    #Check for Gemini Key
    if env_str.find("GEMINI_API_KEY=") == -1:
        gemini = input("Please input your Gemini API key: ")
        env.write(f'GEMINI_API_KEY="{gemini}"\n')

    #Check for Email Address
    if env_str.find("EMAIL_ADDRESS=") == -1:
        email = input("Please input the full email address you wish to protect: ")
        env.write(f'EMAIL_ADDRESS="{email}"\n')

    #Check for Email Pwd, add if not found
    if env_str.find("USER_PWD=") == -1:
        pwd = input("Please input the app password of the email you with to protect: ")
        env.write(f'USER_PWD="{pwd}"\n')

    if env_str.find("VIRUSTOTAL_API=") == -1:
        total = input("Input your VirusTotal API key: ")
        env.write(f'VIRUSTOTAL_API="{total}"\n')

    env.close()
    return None

create_dotenv()