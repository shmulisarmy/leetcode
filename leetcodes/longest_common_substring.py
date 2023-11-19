from functools import cache

first_sentence = "The sun set behind the mountains, casting a warm glow across the landscape."
second_sentence = "As dusk fell, the mountains silhouette against the fading light, creating a serene and picturesque scene."


@cache
def find_biggest_substring(string1, string2):
    if string1[0] == string2[0]:
        return (find_biggest_substring(string1[1:], string2[1:]) if len(string1) > 1 and len(string2) > 1 else '') + string1[0]

    first_sub = (find_biggest_substring(string1[1:], string2) if len(string1) > 1 else '')
    second_sub = (find_biggest_substring(string1, string2[1:]) if len(string2) > 1 else '')
    if len(first_sub) > len(second_sub):
        return first_sub
    return second_sub

print(find_biggest_substring(first_sentence, second_sentence))