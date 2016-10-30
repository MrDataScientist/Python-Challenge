fileObject = open('C:\Users\Administrator\Desktop\sample.txt', 'r') 
string = fileObject.read() s = "" 
for z in string: 
  if ord(z)<=90 and ord(z)>=65 or ord(z)<=122 and ord(z)>=97: 
    s+=z 
    print(s);

    
    
    #----------------------
#in python 3 : from urllib.request
import urllib.request

req = urllib.request.Request("http://www.pythonchallenge.com/pc/def/ocr.html")
req.add_header('Referer', 'http://www.python.org/')
# Customize the default User-Agent header value:
req.add_header('User-Agent', 'urllib-example/0.1 (Contact: . . .)')
page = urllib.request.urlopen(req)

#page = opener.open("http://www.pythonchallenge.com/pc/def/ocr.html");
contents = page.read();
page.close();
mess = contents.split("<!--")[1].split("-->\n")[1]

items = {};

for  item in mess:
	if item in items:
		items[item] = items[item] +1;
	else:
		items[item] = 1;
