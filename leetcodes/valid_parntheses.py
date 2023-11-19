s = "()[]{}"

list_of_parantheses = []

for i in s:
    if i in list_of_parantheses:
        list_of_parantheses.pop(list_of_parantheses.index(i))
    else:
        list_of_parantheses.append(i)

print(list_of_parantheses)