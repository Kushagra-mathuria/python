# count vowels in string
s = "kushagramathuria"
vowel = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowel:
        count+=1
print("vowel: ", count)

# count consonants in string
s = "kushagramathuria"
vowel = "aeiouAEIOU"
count = 0
for ch in s:
    if ch not in vowel:
        count+=1
print("consonants: ", count)

# count uppercase in string
s = "kushagraMATHURIA"
count = 0
for ch in s:
    if ch.isupper():
        count+=1
print("uppercase: ", count)

# count lowercase in string
s = "kushagraMATHURIA"
count = 0
for ch in s:
    if ch.islower():
        count+=1
print("lowercase: ", count)

# count digit in string 
s = "kushagraMATHURIA123456"
count = 0
for ch in s:
    if ch.isdigit():
        count+=1
print("digit: ", count)

# count space in string
s = "kushagra MATHURIA"
count = 0
for ch in s:
    if ch == " ":
        count+=1
print("space: ", count)

# count special character
s = "kushagraMATHURIA@#!12"
count = 0
for ch in s:
    if not ch.isalnum():
        count+=1
print("special character: ", count)

# count total characters
s = "kushagraMATHURIA@#$12"
print("total character: ", len(s))

# count word in string
s = "kushagra MATHURIA @#$12"
words = s.split()

print("word: ", len(words))
