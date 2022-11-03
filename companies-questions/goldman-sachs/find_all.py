from collections import deque
def find_all(self, prefix: str) -> []:
	#Iterate through the prefix
	curr = self.trie
	for c in prefix:
		if c not in curr.children:
			return []
		curr = curr.children[c]

	listOfWords = []
	# look if the prefix itself is a word
	if curr.endOfWord:
	    listOfWords.append(prefix)

	#Form the Words
	d = deque()
	d.append((curr.children, prefix))
	while d:
		curr, pre = d.popleft()
		for key in curr.keys():
			temp = curr[key]
			if temp.endOfWord:
				listOfWords.append(pre+key)
			d.append((temp.children, pre+key))

	return listOfWords

str1 = "a aa Aaa  abca bca"
find_all(a)