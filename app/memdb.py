import time

class DataBase:
	memdb = {}

	def __init__(self):
		self.memdb = {}

	def store(self, play):
		id = int(time.time())
		self.memdb[id] = play
		return id

	def get(self, id):
		return self.memdb[id]
