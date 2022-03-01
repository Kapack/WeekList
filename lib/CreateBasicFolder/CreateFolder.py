import os

class CreateFolder:
	def __init__(self, path:str):
		self.path = path

	def folder(self):
		path = self.path
		if not os.path.exists(path):
			os.makedirs(path)

		return path