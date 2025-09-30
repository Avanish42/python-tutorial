

string = "Arificeal Intelegance"
string = string.lower()
count = 0

for i in string:
    if i in "aeiou":
        count += 1

print('Total number of vowels are ' + str(count))

