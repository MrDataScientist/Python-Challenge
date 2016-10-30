import string
caption = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

new_string = ""

for letter in caption: #{
	found_position = string.ascii_lowercase.find( letter );

	if ( new_string == -1 ):
		new_string += letter;
		continue;
#}
	index = found_position + 2;

	if ( index >= 26 ):
	    index -= 26;

	new_string += string.ascii_lowercase[ index ];

print (new_string);
# < >
