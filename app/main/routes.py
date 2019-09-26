from flask import render_template, flash, redirect, url_for, request, session
from flask_login import current_user
from app.main import bp
from app.main.forms import SettingsForm
from app.models import User
from app import db

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/settings', methods=['GET', 'POST'])
def settings():
    form = SettingsForm()
    if form.validate_on_submit():
        data = {
            'frequency': form.frequency.data,
            'like_all': form.like_all.data,
            'follow_back': form.follow_back.data,
        }
        User.query.update(data)
        db.session.commit()
        flash('saved it all!')
    form = SettingsForm(obj=current_user)
    return render_template('settings.html', form=form, user=current_user)
