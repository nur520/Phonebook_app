import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))

class Config():
    '''
    set config variables for the flask app
    using enviromment variables where available
    otherwise creat the config variable if not done already.
    '''

    #for the computer accese or read path
    FLASK_APP = os.getenv('FLASK_APP')  
    FLASK_DEBUG =os.getenv('FLASK_DEBUG')

    FLASK_ENV = os.getenv('FLASK_ENV')  
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'anyone will never get access to my CSS' 
     #for the datebaser accese or read path
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICAITONS = False
    STRIPE_API_KEY = os.getenv('STRIPE_API_KEY')