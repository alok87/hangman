import time

class dataBase:
	db = {}

	def __init__(self):
		dataBase.db = {}

	def store(self, play):
		id = int(time.time())
		dataBase.db[id] = play
		return id

	def get(self, id):
		return dataBase.db[id]
