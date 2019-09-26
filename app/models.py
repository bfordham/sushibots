import os
import markovify
import tweepy
from app import db, login, twitter_auth
from flask_login import UserMixin
from config import BASEDIR

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    twitter_id = db.Column(db.Integer)
    access_token = db.Column(db.String(128))
    access_token_secret = db.Column(db.String(128))
    frequency = db.Column(db.String(128))
    like_all = db.Column(db.Boolean)
    like_timestamp = db.Column(db.Integer)
    follow_back = db.Column(db.Boolean)
    follow_timestamp = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_tweet(self):
        return self.get_text_model().make_short_sentence(280)

    def tweet(self, text=None):
        if not text:
            text = self.get_tweet()
        
        self.get_twitter_api().update_status(text)

    def get_text_model(self):
        if not hasattr(self, '_text_model'):
            path = os.path.join(BASEDIR, "data", "{}.json".format(self.id))
            with open(path) as f:
                self._text_model = markovify.Text.from_json(f.read())
        return self._text_model

    def get_twitter_api(self):
        if not hasattr(self, '_api'):
            auth = twitter_auth()
            auth.set_access_token(self.access_token, self.access_token_secret)
            self._api = tweepy.API(auth)
        return self._api

@login.user_loader
def load_user(id):
    return User.query.get(int(id))