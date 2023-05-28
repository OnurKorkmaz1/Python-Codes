website = "http://www.sadikturan.com"
course = "python kursu: naitan sona python programlaam rehberiniz (40 saat)"
"""
# 1- "course" karakter dizisinde kaç karakter bulunmaktadır.
result=len(course)
print(result)

# 2- "website" içinden www karakterlerini alın
print(website[7:10])

# 3- "website" içerisinden com karakterlerini alın
print(website[-3:])
#4-"course" içerisinden ilk 15 ve son 15 karakterleri alın.
print(course[0:15]+course[-1:-16])
#5- "course" kelimesindeki harfleri tersten yazdırın
result=course[::-1]
print(result)
"""
"""
name, surname, age, job ="bora", "yılmaz",32 ,"mühendis"   
#print(f"benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.")
#print("benim adım " + name + "  " + surname, "yaşım "+ str(age)+"  "+ "mesleğim "+ job)

#"Hello world" ifadesindeki w harifini W ile değiştir
s="Hello world"
s[7]="W"
print(s)
"""
#   "abc" ifadesini yanyana 3 defa yazdırın
result= "abc" * 3
print(result)
