from urllib import *

page 0 urlopen("");
contents = page.read();
page.close();
print contents.split("--")[1].split
