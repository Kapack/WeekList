import os
from definitions import ROOT_DIR

class CreateFolder:
	def __init__(self, path):
		self.path = path

	def folder(self):
		path = ROOT_DIR + '/' + self.path + '/'
		if not os.path.exists(path):
			os.makedirs(path)

		return path