Answers to Assignment 4: 

# Conditional exercises

1. 
```
response = input("input 1 or 2\n")

if response == '1' or response == '2':
    print("OK")
elif response == '':
    print("subject did not respond")
else:
    print("Subject pressed the wrong key")
```

2. 
```response = input("input 1 or 2\n")

if response == '1' or response == '2':
    if response == '1':
        print("Correct!")
    elif response == '2':
        print("Incorrect!")
    #print("OK"
elif response == '':
    print("subject did not respond")
else:
    print("Subject pressed the wrong key")
```

3. Yes, it returns the expected output 

# For loop exercises

1. 
```
first_name = "Jahratul"
for letter in first_name:
    print(letter)
```
2. 
```first_name = "Jahratul"
count = -1
for letter in first_name:
    count +=1
    print(letter)
    print("This letter has an index of %i" %count)
```
3. 
```
names = ["Amy","Rory","River"]

for name in names:
    for letter in name: 
        print(letter)
```
4. 
```
names = ["Amy","Rory","River"]
for name in names:
    count = -1
    for letter in name: 
        count += 1 
        print(letter)
        print("This letter has an index of %s" %count)
```

# While loop exercises
1. 
```
iteration = 0
while iteration <=20:
    iteration +=1
    if iteration <=10:
        print("%i image1.png" %iteration)
    elif iteration >10 and iteration <=20:
        print("%i image2.png" %iteration)
```
2. 
```
import random 

response = False 
while not response:
    print("Showing an image")
    image = random.randint(0,10)
    if image == 1 or image == 2:
        response = True
```
 
