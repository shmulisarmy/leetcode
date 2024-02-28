string = '13244'


number_dealing_with = None
count = 0

ns = []


for i in string:
    if number_dealing_with != i:
        if number_dealing_with != None:
            ns.extend([str(count), str(number_dealing_with)])
        count = 1

    else:
        count += 1
    
    number_dealing_with = i

ns.extend([str(count), str(number_dealing_with)])


print(''.join(ns))
