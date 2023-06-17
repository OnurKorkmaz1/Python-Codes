def boluntuleme(liste):
    bolumler = []
    toplam = 0
    bolum = []
    
    for i in liste:
        if toplam + i> 800:
            bolumler.append(bolum)
            bolum = [i]
            toplam = i
        else:
            bolum.append(i)
            toplam += i
    
    if bolum:
        bolumler.append(bolum)
    
    return bolumler

# Örnek bir liste
liste = [100, 130, 150, 120, 180, 130, 100, 150, 200,120,200,130]

bolumler = boluntuleme(liste)

# - - - - - - - - - - - - - - - - - - - - - 

def ard_topla(listeler):
    yeni_listeler = []
    
    for liste in listeler:
        toplam = 0
        yeni_liste = []
        
        for sayi in liste:
            toplam += sayi
            yeni_liste.append(toplam)
        
        yeni_listeler.append(yeni_liste)
    
    return yeni_listeler

# Örnek listeler


yeni_listeler = ard_topla(bolumler)

# Sonuçları yazdırma
for liste in yeni_listeler:
    print(liste)


