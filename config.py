import os

basedir = os.path.abspath(os.path.dirname(__file__)) 

# Give's access to the project in ANY OS we find oursleves in
# Allows outside files /folder to be added to the project from the base directory


class Config:
    """
    Sets configuration variables for our Flask app here
    Eventually will use hidden variable items - but for now, we'll leave them exposed in config
    """
    SECRET_KEY= "You will never guess..."
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Decreases unnecessary output in terminal

    #SQLALCHEMY_DATABASE_URI