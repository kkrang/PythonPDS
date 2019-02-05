#Assume s is a string of lower case characters.

#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

#Longest substring in alphabetical order is: abc

s="azcbobobegghakl"
longest = s[0]
current = s[0]
result = []
final = []

for letters in s:
    result = result + [letters]
    if result == sorted(result) and len(result)>= len(final):
        final = result
    elif result != sorted(result):
        result = [result[len(result)-1]]
for i in s[1:]:
    if i >= current[-1]:
        if len(current) > len(longest):
            longest = current
    else:
        current = i

print("Longest substring in alphabetical order is: " + longest)