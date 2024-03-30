def reverse(s, b, e):
    while (b < e):
        s[b], s[e] = s[e], s[b]
        b += 1
        e -= 1

def reverse_words(s):
    n = len(s)
    b = 0
    for e in range(n):
        if (s[e] == ' '):
            reverse(s, b, e-1)
            b = e+1
    reverse(s, b, e-1)
    reverse(s, 0, n-1)

print(reverse_words('Narayana'))