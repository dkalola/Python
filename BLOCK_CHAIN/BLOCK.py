import hashlib
import datetime
import json
from progress.spinner import PixelSpinner
from tqdm import tqdm

class Block():

	def __init__(self, data, timestamp=str(datetime.datetime.now())):
		"""

		:param data: block data
		:param index: block index
		:param previous_hash: previous block hash
		:param timestamp: block time stamp
		"""
		self.data = data
		self.index = 0
		self.timestamp = timestamp
		self.previous_hash = 0
		self.nonce = 0
		self.hash = self.calculateHash()

	def mineBlock(self,difficulty):
		self.nonce = 0
		with tqdm(total = 100) as pbar:
			while not (self.hash.startswith('0' * difficulty)):
				self.nonce += 1
				self.hash = self.calculateHash()
				pbar.update(10)

		print(f'Block {self.index} mined : {self.hash} nonce: {self.nonce}')
		print()


	def calculateHash(self):
       
		return hashlib.sha256(str.encode(json.dumps(self.data) + str(self.index)+ str(self.timestamp)+str(self.nonce)+str(self.previous_hash))).hexdigest()
	def setIndex(self, index):
		self.index = index

	def getData(self):
		return self.data

	def getBlockTime(self):
		return self.timestamp

	def getBlockHash(self):
		return self.hash



