# For challenge 3

def challenge3():
    import re
    import urllib

    u = urllib.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
    thestring = u.read()
    u.close()

    thestring = thestring.split('\n')
    thestring = thestring[22:1271]
    thestring = "".join(thestring)

    # print thestring

    # p = re.compile(r'(\w)\1{2}[a-z](\w)\2{2}')
    #print p.search('the is a good boy the the tt UUUiYYYAAAaTYW KKKjOPS OSHzRTQQ').group()
    #'the the'
    print re.findall(r'[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]', thestring)
# print p.search(thestring).group()
