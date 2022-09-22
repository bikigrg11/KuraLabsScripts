
def permutation(string):

    out = []
    if len(string) == 1:
        return string
    else:
        for i, let in enumerate(string):
            for perm in permutation( string[:i] + string[i+1:]):
                out += [let+perm]
    return out

print(permutation("abc"))