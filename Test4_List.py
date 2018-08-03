print "Available fruits: apple, mango, banana."

Fruits = ["apple", "mango", "banana"]

name = raw_input('Enter fruit name: ')

found = False

for fruit in Fruits:
    if fruit == name:
        found = True

if found == True:
    print "Fruit present in list"
else:
    print "Fruit not present in list"
