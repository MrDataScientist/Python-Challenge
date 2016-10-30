def challenge2():
    import collections

    import urllib

    u = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
    thestring = u.read()
    u.close()

    thestring = thestring.split('\n')
    thestring = thestring[38:1257]
    thestring = "".join(thestring)

    print thestring

    d = collections.defaultdict(int)
    for c in thestring:
        d[c] += 1
    
    for c in sorted(d, key=d.get, reverse=True):
print '%s %6d' % (c, d[c])
