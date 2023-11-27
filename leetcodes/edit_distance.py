def brea_problem_down(word1, word2, quickest_so_far, this_paths_distance_so_far):
    if word1 == word2:
        return 0
    if len(word1) == 0:
        return len(word2)
    if len(word2) == 0:
        return len(word1)
    
    replace = brea_problem_down(word1[1:], word2[1:]) + 1
    if replace <= 2:
        return replace
    min_of_replace_and_remove = min(brea_problem_down(word1[1:], word2, replace) + 1, replace)
    if min_of_replace_and_remove <= 2:
        return min_of_replace_and_remove
    min_of_all = min(min_of_replace_and_remove, brea_problem_down([word2[0]].extend(word1), word2, min_of_replace_and_remove) + 1)

    return min_of_all

word1 = 'ab'
word2 = 'ba'
brea_problem_down(word1, word2, max(len(word1), len(word2)), 0)