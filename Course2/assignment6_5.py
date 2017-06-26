#Write code using find() and string slicing to extract the number at the end of
#the line below. Convert the extracted value to a floaring point number and
#pint it out.

text = "X-DSPAM-Confidence:    0.8475";
init = text.find('0')
sub = text[init:]
value = float(sub)
print(value)
