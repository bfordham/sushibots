from flask import render_template, flash, redirect, url_for, request, session, current_app
import tweepy
from flask_login import current_user, login_user
from app.models import User
from app import db, twitter_auth
from app.connect import bp

@bp.route('/')
@bp.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    auth = twitter_auth()
    redirect_url = auth.get_authorization_url()
    session['oauth_token'] = auth.request_token['oauth_token']

    return render_template('connect/index.html', title='Connect Account', auth_url=redirect_url)

@bp.route('/callback')
def callback():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    token = request.args.get("oauth_token")
    verifier = request.args.get("oauth_verifier")

    auth = twitter_auth()
    
    auth.request_token = { 'oauth_token' : token, 'oauth_token_secret' : verifier }

    #try:
    auth.get_access_token(verifier)
    username = auth.get_username()
    api = tweepy.API(auth)
    user_info = api.get_user(username)
    twitter_id = user_info.id

    # If we can find user, great!
    user = User.query.filter_by(twitter_id=twitter_id).first()
    if not user:
        user = User(username=username, twitter_id=twitter_id, access_token=auth.access_token, access_token_secret=auth.access_token_secret)
        db.session.add(user)
        db.session.commit()
    
    login_user(user, remember=True)
    return redirect(url_for('main.index'))
    #except tweepy.TweepError:
    #    return 'Error! Failed to get access token.'