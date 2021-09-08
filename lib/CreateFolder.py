import os

class CreateFolder:
	def __init__(self, path):
		self.path = path

	def folder(self):
		path = os.getcwd() + '/' + self.path + '/'
		if not os.path.exists(path):
			os.makedirs(path)

		return path