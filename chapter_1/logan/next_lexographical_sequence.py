def next_lexicographical_sequence(s: str) -> str:
    s_list = list(s)
    first = len(s_list) - 2

    while first >= 0:
        if s_list[first] < s_list[first + 1]:
            # char on left i.e 'b' is less than char on right i.e 'c'
            # found break, search for min letter to right of first that is greater than letter at first
            second = first + 1
            to_swap = second
            second += 1
            while second < len(s_list):
                if s_list[second] > s_list[first] and s_list[second] <= s_list[to_swap]:
                    to_swap = second
                second += 1
            # swap    
            temp = s_list[first]
            s_list[first] = s_list[to_swap]
            s_list[to_swap] = temp
            # rev to the right of first
            return ''.join(s_list[:first + 1]) + ''.join(reversed(s_list[first + 1:]))
        first -= 1    

    # if everything in string was in descending order (no breaks) just reverse string
    return s[::-1]
    
next_lexicographical_sequence('abcedda')