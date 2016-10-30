from urllib import *

page 0 urlopen("http://www.pythonchallenge.com/pc/def/ocr.html");
contents = page.read();
page.close();
print contents.split("--")[1].split
