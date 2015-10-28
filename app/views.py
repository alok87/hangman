from flask import render_template, request, jsonify
from app import flaskInstance
from app.hangman import Play
from app import db

dbObj = db.dataBase()

@flaskInstance.route('/')
def showView():
	play  = Play()
	play.resetInstance()
	id = dbObj.store(play)
	return render_template("hangman.html",
			       title='Hangman',
			       Play=play,
			       id=id)

@flaskInstance.route('/process', methods=["POST"])
def process():
	input = request.form.get('input_sent')
	id = request.form.get('id_sent')
	play = dbObj.get(int(id))
	rslt = play.processInput(input)
	guessRslt = play.showGuessedBox()
	imageNumber = str(play.attempts)
	gameRslt = play.checkResult()
	ansr = play.getLine()
	return jsonify(gameResult=str(gameRslt), result=str(rslt), guessResult=guessRslt, charInput=input, hangManNo=str(imageNumber), answer=str(ansr))
