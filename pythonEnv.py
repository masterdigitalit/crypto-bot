from dotenv import load_dotenv
import os


load_dotenv()
def getKeyFromEnv(key):
    if os.getenv(key) == 'None':
        return
    return os.getenv(key)
