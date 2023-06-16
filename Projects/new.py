def ard_topla(liste):   # bu ardışık toplama işlemi için bir fonksiyon tanımlıyoruz.
    yeni_liste = []     # işlemin kullanacağı liste yaratıyoruz

    toplam = 0
    
    for i in range(len(liste)):
        if i == 0:
            yeni_liste.append(liste[i])
            toplam += liste[i]
        else:
            toplam += liste[i]
            if toplam > 500:
                break
            else:
                yeni_liste.append(liste[i])
    
    return yeni_liste, liste[i+1:]

# Örnek bir liste
liste = [100, 200, 150, 120, 180, 90,180,190,120]


yeni_liste, geri_kalan = ard_topla(liste)



# Sonuçları yazdırma
print(yeni_liste)
print(geri_kalan)