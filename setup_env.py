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
    print(env_exists())
    #If .env does not exist, greate a .env
    if not env_exists():
        env = open(".env", "w")
        env.write("IMAP_URL='imap.gmail.com'")
        env.close()

    #Once .env exists, ask for any relevant info
    env = open(".env", "r")

    #Check for Gemini Key
    if env.read().find("GEMINI_API_KEY=") == -1:
        gemini = input("Please input your Gemini API key: ")
        env.close()
        env = open(".env", "a")
        env.write(f'GEMINI_API_KEY="{gemini}"\n')
        env.close()
        env = open(".env", "r")
        
    #Check for Email User, add if not found
    if env.read().find("USER_EMAIL=") == -1:
        user = input("Please input the FULL email address that you wish to protect: ")
        env.close()
        env = open(".env", "a")
        env.write(f'USER_EMAIL="{user}"\n')
        env.close()
        env = open(".env", "r")

    #Check for Email Pwd, add if not found
    if env.read().find("USER_PWD=") == -1:
        pwd = input("Please input the app password of the email you with to protect: ")
        env.close()
        env = open(".env", "a")
        env.write(f'USER_PWD="{pwd}"\n')
        env.close()
        env = open(".env", "r")

    #Check for Imap URL, add if not found
    if env.read().find("IMAP_URL=") == -1:
        env.close()
        env = open(".env", "a")
        env.write("IMAP_URL='imap.gmail.com'")
        env.close()
        env = open(".env", "r")

    env.close()
    return None

create_dotenv()