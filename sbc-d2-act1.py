text = ('summer bootcamp')

print (text.title())
print (text.capitalize().replace("p", "P"))
print (text[-8:-4].replace("b", "L"))
print (text[-4:].replace("p", "E"))
print (f"{text[-3].upper()}{text[5].upper()}")
print (text.replace(" ", "").isalpha())