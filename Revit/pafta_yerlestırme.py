def yeni_liste_olustur(liste):
    yeni_liste = []
    
    for i in range(len(liste)):
        if i == 0:
            yeni_liste.append(liste[i])
        else:
            yeni_liste.append(liste[i] + liste[i-1])
    
    return yeni_liste

# Örnek bir liste
liste = [60, 120, 120, 120, 120,150,150]

while True:
    yeni_liste = yeni_liste_olustur(liste)
    max_deger = max(yeni_liste)
    
    if max_deger > 500:
        print("paftaya olmuyor") # pafta genişliği 500 civarı diye düşünerek kısıtladık. 500 ü geçerlerse yeni listeler oluşturulacak

    else:
        break
    
    liste = yeni_liste
