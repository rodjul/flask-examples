import os

# Define the application directory
APP_DIR = os.path.abspath(os.path.dirname(__file__))


# value to encrypt the session value
# SECRET_KEY = os.urandom(20)
SECRET_KEY = b'\x14]\xb2\x0c\xabe\xd9\xf2\x14\xa1\xfeJ\xf2o\x16\x8d\xf9\x10k8'


UPLOAD_FOLDER = "uploads/"