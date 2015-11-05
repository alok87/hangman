from flask import render_template, request, jsonify, flash, redirect, session, url_for, request, g
from flask.ext.login import login_required, login_user, logout_user, current_user
from app import app
from app import db, models, lm, oid
from app.hangman import Play
from .forms import LoginForm
from .models import User
import operator, time, pickle

@lm.user_loader 								#Loads the function with the Flask-Login
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler 								#Tells Flask-OpenID that this our login function
def login():
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

@oid.after_login 								#This is method is called if the login is authenticated properly by the openid provider
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email, wins=0, loss=0, matches=0)
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

@app.route('/')									#This method is the route of the application /HOME
@app.route('/hangman')
@login_required
def hangman():
	user = g.user
	play  = Play()
	id = int(time.time()) 
	instance_file = 'file_'+str(id)	
	with open(instance_file, 'wb') as f:
		pickle.dump(play, f)		
	return render_template("hangman.html",
				title="Hangman",
				user=user,
				id=id,
				Play=play)


@app.route('/process', methods=["POST"])					#This handles the ajax call for processing requests
def process():
	#print "DEBUG -------------"	
	input = request.form.get('input_sent')
	input = input.upper()
	id = request.form.get('id_sent')
	instance_file = 'file_'+str(id)
	with open(instance_file, 'rb') as f:
		play = pickle.load(f)
	print play.ltrs_selectd
	input_r = play.process_input(input)
	box_r = play.show_box()
	image_r = str(play.attempts)
	game_r = play.check_result()
	answer = play.get_line()
	if game_r == "0":
		g.user.wins += 1
		g.user.matches += 1
		db.session.commit()
	elif game_r == "1":
		g.user.loss += 1
		g.user.matches += 1
		db.session.commit()
	with open(instance_file, 'wb') as f:
		pickle.dump(play, f)		

	return jsonify(game_r=str(game_r), result=str(input_r), box_r=box_r, char_input=input, image_no=str(image_r), answer=str(answer.upper()))

@app.route('/rankings')								#This shows the ranking page
@login_required
def rankings():
	my_user = g.user
	users = User.query.all()
	rank = {}
	for user in users:
		rank[user] = (user.wins * 30) - (user.loss * 5)
	sorted_rank = sorted(rank.items(), key=operator.itemgetter(1), reverse=True)
	return render_template("rankings.html",
						   title='Rankings',
						   user=my_user,
						   rank=sorted_rank)
