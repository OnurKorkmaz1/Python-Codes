def yeni_liste_olustur(liste):
    yeni_liste = []
    toplam = 0
    
    for i in range(len(liste)):
        toplam += liste[i]
        if toplam > 500:
            print("Toplam:", toplam)
            break
        else:
            yeni_liste.append(liste[i])
    
    geri_kalan = liste[i+1:]
    
    while True:
        toplam = sum(geri_kalan)
        if toplam > 500:
            break
        
        if len(geri_kalan) == 0:
            break
        
        yeni_liste.append(geri_kalan[0])
        geri_kalan = geri_kalan[1:]
    
    return yeni_liste

# Örnek bir liste
liste = [100, 200, 150, 120, 180, 90, 150, 150,80]

yeni_liste = yeni_liste_olustur(liste)

# Sonucu yazdırma
print("Yeni Liste:", yeni_liste)