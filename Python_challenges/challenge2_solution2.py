from urllib import *

page = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html");
contents = page.read();
page.close();
print contents.split("<!--")[1].split("-->\n")[1]
