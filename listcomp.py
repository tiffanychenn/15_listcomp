import string

def requirements(password):
	upper = any(x.isupper() for x in password) 
	lower = any(x.islower() for x in password)
	num = any(x.isdigit() for x in password)
	return upper & lower & num

print requirements("")
print requirements("abc123")
print requirements("ABSVJHBSKJNa")
print requirements("A6b")

def rate(password):
	special_chars = string.punctuation
	chars = 0
	if any(x.isupper() for x in password):
		chars += 1
	if any(x.islower() for x in password):
		chars += 1
	if any(x.isdigit() for x in password):
		chars += 1
	if any(x in special_chars for x in password):
		chars += 1
	lent = len(password) / 3
	if lent > 6:
		lent = 6
	return chars + lent

print rate("")
print rate("abc123")
print rate("a5!Q")
print rate("1234567890A!a1356952891947")