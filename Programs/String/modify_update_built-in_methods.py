# replace(): replace string with another string
a = "kushagra mathuria"
print(a.replace("mathuria", "gupta"))

# strip(): remove whitespace
a = "               kushagra          mathuria    "
print(a.strip())

# lstrip(): remove left whitespace
a = "     kushagra mathuria"
print(a.lstrip())

# rstrip(): remove right whitespace
a = "kushagra mathuria         "
print(a.rstrip())

# split(): splits the string from the left (beginning).
a = "kushagra mathuria"
print(a.split())

# rsplit(): splits the string from the right (end).
a = "kushagra mathuria"
print(a.rsplit(","))

# join(): join the elements of an iterable to the end of string.
a = "avani sharma"
w="#".join(a)

print(w)
