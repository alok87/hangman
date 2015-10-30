from flask import render_template, request, jsonify
from app import app
from app.hangman import Play
from app import db

db_obj = db.DataBase()

@app.route('/')
def show_view():
	play  = Play()

	id = db_obj.store(play)
	return render_template("hangman.html",
			               title='Hangman',
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
