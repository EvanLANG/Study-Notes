def lengthOfLongestSubstring(s):
	"""
	:type s: str
	:rtype: int
	"""
	dic = dict()
	maxlen=start=0
	for i,c in enumerate(s):
		#print([i,c])
		if c in dic and start <= dic[c]:
			start = dic[c]+1
			
			print([start,dic[c]])
		else:	
			maxlen = max(maxlen, i-start+1)
		dic[c] = i
		#print(i,c)
		print(maxlen)
	return maxlen

def length(s):
    start = maxLength = 0
    usedChar = {}
    
    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i
    print(maxLength)
    return maxLength
if __name__ == '__main__':
	lengthOfLongestSubstring("tmmzuxt")
	length("tmmzuxt")