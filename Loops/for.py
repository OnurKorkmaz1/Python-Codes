#true kullanmamızın amacı döngünün sürekli devam etmesi için ypaıyoruz.
faktöriyel=1

while True:
    sayi=int(input("lütfen negatif olmayan bir sayı giriniz:"))
    if(sayi <= 0):
        print("lütfen negatif olmayan bir sayı giriniz")
    else:
        for i in range(1,sayi+1):
            faktöriyel *= i
        print("faktöriyel",faktöriyel)
        break

       




