import math

from pox.core import core

log = core.getLogger()

class Entropy(object):
	count = 0
	entDic = {}
	ipList = []
	dstEnt = []
	value = 1

	def statcolect(self, element):

		#print "Self values"
		#print "count is " + str(self.count)
		#print "Length of IP list is"
		#print len(self.ipList)
		#print "*********" 
		l = 0
		self.count +=1
		self.ipList.append(element)
		if self.count == 50:
			for i in self.ipList:
				l +=1
				if i not in self.entDic:
					self.entDic[i] =0
				self.entDic[i] +=1
			self.entropy(self.entDic)
			log.info(self.entDic)
			self.entDic = {}
			self.ipList = []
			l = 0
			self.count = 0

	def __init__(self):
		pass