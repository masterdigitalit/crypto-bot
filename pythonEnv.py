from dotenv import load_dotenv
import os


load_dotenv()
def getFromEnv(key):
    if os.getenv(key) == 'None':
        return
    return os.getenv(key)
print(getFromEnv('TOKENs'))