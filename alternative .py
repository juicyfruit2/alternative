
# Created a program that reads the alternative of hello world 

# created 2 variables, used a loop and if statements, upper and lower functions 
string = "Hello World"
New = " " 
string_len = len(string)
for i in range (string_len):
    if i % 2 == 0 :
      New += string[i].upper()
    else:
        New += string[i].lower()
print(New)

# created 3 variables, used a loop and if statements, upper and lower functions 
x = "Hello World "
space  = " "
new = x.split()

for i in range (len(new)):
    if i % 2 == 0:
     space = space + new [i].lower()+" "
    else:
        space = space + new [i].upper()+" "
print(space)
    

