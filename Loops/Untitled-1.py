defkullanici="yazilimcibebe"
defparola="1234"

while (True):
    kullanici= input("Kullanıcı Adı:")
    parola= input("parola:")
    if((kullanici == defkullanici) and (parola == defparola)):
        print("Hoşgeldiniz",kullanici)
        break
    elif((kullanici == defkullanici) and (parola != defparola)):
        print("Şifrenizi mi unuttunuz")
        print("şifreyi değiştirmek ister misiniz(E/H)")
        cevap= input()
        if (cevap=="E"):
            yeniparola=input("Yeni Parola:")
            print("lütfen bekleyin")
            defparola=yeniparola
            print("şifreniz değiştirildi")
    else:
        print("tekrar deneyiniz")



