string = 'abcdea'
lst = []
max_so_far = 0
for letter in string:
	if letter in lst:
		max_so_far = max(max_so_far, len(lst))
		lst = lst[lst.index(letter)+1:]
	lst.append(letter)
max_so_far = max(max_so_far, len(lst))
print(max_so_far)
