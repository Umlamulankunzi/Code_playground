def disemvowel(word):
	#variables
	vowels =["a","e","i","o","u","A","E","I","O","U"]
	nw_lst =[]
	
	#for loop
	for ltr in word:
		if ltr in vowels:
			continue
		else:
			nw_lst.append(ltr)
	
	return ''.join(nw_lst)
	
print(disemvowel("MuZInda"))

class disemvowel(object):
	def __init__(self, word):
		self.word = word
		self.vowels = ["a","e","i","o","u","A","E","I","O","U"]
		self.nw_lst = []
		
		for ltr in self.word:
			if ltr in self.vowels:
				continue
			else:
				self.nw_lst.append(ltr)
				
		print( ''.join(self.nw_lst))
		
x =disemvowel("MuzInda")