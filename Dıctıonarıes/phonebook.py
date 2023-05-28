

"""
Dictionry tanımı aşağıdaki gibi yapılabilir. listelerde biz index değerlerini kullanarak verimize ulaşırken dictionary lerde aşağıdaki gibi çalışıyoruz.
%s :::  
%d :::  
 

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)"""


"""
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
"""



phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here
phonebook["Jake"]=938273443
del phonebook["Jill"]

# testing code
if "all" in phonebook:  
    print("Jake is listed in the phonebook.")
else:
    print("all is not in the list")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  