import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')

# Load the dotenv file
load_dotenv(dotenv_path)

# get the os environment to get secret dropbox key
DROPBOX_KEY = os.environ.get("SECRET_DROPBOX_KEY")
