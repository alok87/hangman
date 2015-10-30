import time

class DataBase:
	db = {}

	def __init__(self):
		DataBase.db = {}

	def store(self, play):
		id = int(time.time())
		DataBase.db[id] = play
		return id

	def get(self, id):
		return DataBase.db[id]
