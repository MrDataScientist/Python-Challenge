fileObject = open('C:\Users\Administrator\Desktop\sample.txt', 'r') 
string = fileObject.read() s = "" 
for z in string: 
  if ord(z)<=90 and ord(z)>=65 or ord(z)<=122 and ord(z)>=97: 
    s+=z 
    print(s);
