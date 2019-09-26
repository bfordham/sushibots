from dotenv import load_dotenv
load_dotenv()

import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CONSUMER_KEY = os.environ.get('CONSUMER_KEY') or 'not-set'
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET') or 'not-set'