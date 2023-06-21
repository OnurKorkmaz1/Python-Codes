import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


#--------------------------------------------------------------------------------------


# A Python program to demonstrate working of
# findall()
# A sample text string where regular expression is searched.

string = """Hello my Number 500 is 123456789 and
           my friend's number is 987654321"""
 
# A sample regular expression to find digits.
regex = '\d+'
 
match = re.findall(regex, string)
print(match)


#--------------------------------------------------------------------------------------

txt = "The rain in Spain"
x = re.search("\s", txt)              # \s : Returns a match where the string contains a white space character

print("position:", x.start())