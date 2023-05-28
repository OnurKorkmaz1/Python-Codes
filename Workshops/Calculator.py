
def topla(sayi1,sayi2):
    return sayi1 + sayi2

def çıkar(sayi1,sayi2):
    return sayi1-sayi2

def çarp(sayi1,sayi2):
    return sayi1*sayi2

def böl(sayi1,sayi2):
    return sayi1/sayi2

print("Hangi operasyonu yapmak istediğinizi seçin")
print("1:topla")
print("2:çıkar")
print("3:çarp")
print("4:böl")


secenek = input("operasyon seçiniz:")


sayi1 = int(input("ilk sayıyı giriniz:"))
sayi2 = int(input("ikinci sayıyı giriniz:"))

if secenek == "1":
    print("Toplam:" +str(topla(sayi1,sayi2)))
elif secenek == "2":
    print("çıkarma:" +str(çıkar(sayi1,sayi2)))
    
elif secenek == "3":
    print("çarpma:" +str(çarp(sayi1,sayi2)))

elif secenek == "4":
    print("bölme:" +str(böl(sayi1,sayi2)))