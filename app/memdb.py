import time

class DataBase:
	memdb = {}

	def __init__(self):
		DataBase.memdb = {}

	def store(self, play):
		id = int(time.time())
		DataBase.memdb[id] = play
		return id

	def get(self, id):
		return DataBase.memdb[id]
