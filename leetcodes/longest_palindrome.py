

def find_longest_palindrome(string):
    length = len(string)
    biggest = 0
    for i in range(length):
        cur_palindrome_length = 1
        for j in range(1, length):
            if (-1 < i-j and i+j < length) and string[i-j] == string[i+j]:
                cur_palindrome_length += 2
            else:
                biggest = max(cur_palindrome_length, biggest)
                break

    return biggest

        





print(find_longest_palindrome('aa'))


