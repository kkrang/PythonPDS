#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2
import string

s='gfdhbobobyui'
bob = 0 #counter

for i in range(len(s)):
    if s[i:i+3] =="bob": #slicing 3 char at a time
        bob += 1
print("Number of times bob occur is: " + str(bob))