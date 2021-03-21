def most_frequent(string):
    d=dict()
    for k in string:
        if k not in d:
            d[k]=1
        else:
            d[k]+=1
    return d
print(most_frequent('Mississippi'))
