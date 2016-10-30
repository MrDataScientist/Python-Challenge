import string

original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc " \
    "dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq " \
    "rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu " \
    "ynnjw ml rfc spj."

table = string.maketrans(
    "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
)

print original.translate(table)


#new_string = ""
#for letter in caption: #{
#	if ( letter == "k" ):
#		new_string += "m"
#	elif ( letter == "o" ):
#		new_string += "q"
#	elif ( letter == "e" ):
#		new_string += "g"
#	else:
#		new_string += letter;
#}

#print (new_string);
