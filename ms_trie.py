# Michael Solimano 2020
# Practice implementing a trie

class trieNode():
	# create trie nodes with characters and lists to hold children nodes

	def __init__(self, char=None):

		self.char = char
		self.children = {
			'a' : None,
			'b' : None,
			'c' : None,
			'd' : None,
			'e' : None,
			'f' : None,
			'g' : None,
			'h' : None,
			'i' : None,
			'j' : None,
			'k' : None,
			'l' : None,
			'm' : None,
			'n' : None,
			'o' : None,
			'p' : None,
			'q' : None,
			'r' : None,
			's' : None,
			't' : None,
			'u' : None,
			'v' : None,
			'w' : None,
			'x' : None,
			'y' : None,
			'z' : None,
		}
		self.end_of_word = False

class Trie():
	#Create a trie that handles the lower_case alphabet

	def __init__(self):

		self.root = trieNode()


	def add_trie(self, string):
		#add a string onto the trie

		string_length = len(string)
		mover = self.root

		for letter in string:
			if mover.children[letter] != None:
				mover = mover.children[letter]
				print(f"{letter} already here.")
			else:
				char = trieNode(letter)
				mover.children[letter] = char
				mover = mover.children[letter]
				print(f"Adding {letter}.")
		mover.end_of_word = True

	def search_prefix(self, word):
		#search for a word in the trie.
		#In this method, the word can be a prefix of a larger word.

		tracing_node = self.root

		for letter in word:
			if tracing_node.children[letter] != None:
				tracing_node = tracing_node.children[letter]
			else:
				print(f"{word} isn't a valid prefix.")
				return
		print(f"{word} is here!")




new = Trie()
new.add_trie("testing")
new.add_trie("test")
new.search_prefix("testr")




			



