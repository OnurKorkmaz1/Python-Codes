import re

#Return a list containing every occurrence of "ai":

str= "Python Regular expression module cours - ,regex"

result = re.findall("..thon",str)

"""         
# [] köşeli parantezler arasına yazılan bütün karakterler aranır.

    [abc] --> a   : 1 match
              ac  : 2 match
              Python : No matches
    [a-e]  --> [abcde]
    [1-5] --> [12345]
    [0-39] --> [01239]

    [^abc]  --> abc disindaki karakterler.
    [^0-9]  --> rakam olmayan karakterler

    . --> herhangi bir tek karakteri ifade eder.

        .. -->  a      : No match
                ab     : 1 match
                abc    : 1 match
                abcd   : 2 match
# Belirtilen karakterler başlıyor mu ? (^)

        ^a  -->  a   : 1 match
                 abc : 1 match
                 bac : No match    

# belirtilern karakterle bitiyor mu ($)

        a$  -->   a : 1 match
                  lamba : 1 match
                  Python : no match

# * - bir karakterin sifir ya da daha fazla sayida olmasini kontrol eder

      ma*n  --> mn       : 1match
                man      : 1match
                maaan    : 1match
                main     :    no match (a nin arkasindan n gelmiyor)  

#  {} - -> karakter sayisini kontrol eder.

      al{2}    -- > a karakterinin arkasina l 2 kez tekrarlanmalı
      al{2,3}  -->  a karakterinin arkasina l karakteri en az 2 en fazla 3 kez gelmeli
      [0-9]{en az 2 en çok 4 basamakli sayilar}

#  | - alternatif seceneklerden birinin gerçekleşmesi gerekit.
        a|b  --> a yada b
            ade  --> 1 match
            acdbea --> 3 match

"""
#---------------------------------------------------
# karakter aramasında kullanılan ifadelerde var ezberlemeye gerek yok bakarak yazabilir.



result = re.findall("[abc]",str)   # bulduğu bütün abc karakterllerini bize verir
result = re.findall("Py..on",str)























print(result)

