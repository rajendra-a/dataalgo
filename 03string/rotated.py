def are_rotated(s1, s2):
    if len(s1) != len(s2):
        return False

    temp = ''
    temp = s1 + s1
    return temp.find(s2) != -1

print(are_rotated('string', 'ingstr'))

