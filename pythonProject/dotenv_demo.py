import os
from dotenv import load_dotenv


load_dotenv()  # USER is inbuit in system environment hence it is giving value which is present in system environment.
# To override .env variables to system environment load_dotenv(override=True)

API_KEY = os.getenv("API_KEY")
USER = os.getenv("USERNAME")

print(API_KEY)
print(USER)
