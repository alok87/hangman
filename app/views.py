from flask import render_template, request, jsonify, flash, redirect, session, url_for, request, g
from flask.ext.login import login_required, login_user, logout_user, current_user
from app import app
from app import db, models, lm, oid
from app.hangman import Play
from app import memdb
from .forms import LoginForm
from .models import User

db_obj = memdb.DataBase()

@lm.user_loader 		#Loads the function with the Flask-Login
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler 		#Tells Flask-OpenID that this our login function
def login():
	print "auth auth"
	print g.user.is_authenticated
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('hangman'))
	form = LoginForm()

	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
	return render_template('login.html',
							title='Login',
							form=form,
							providers=app.config['OPENID_PROVIDERS'])

@oid.after_login 		# This is method is called if the login is authenticated properly by the openid provider
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(url_for('hangman'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('hangman'))

@app.route('/hangman')
@login_required
def hangman():
	user = g.user
	play  = Play()
	id = db_obj.store(play)
	return render_template("hangman.html",
			               title='Hangman',
						   user=user,
			               Play=play,
			               id=id)

@app.route('/process', methods=["POST"])
def process():
	input = request.form.get('input_sent')
	id = request.form.get('id_sent')
	play = db_obj.get(int(id))
	input_r = play.process_input(input)
	box_r = play.show_box()
	image_r = str(play.attempts)
	game_r = play.check_result()
	answer = play.get_line()
	return jsonify(game_r=str(game_r), result=str(input_r), box_r=box_r, char_input=input, image_no=str(image_r), answer=str(answer))
