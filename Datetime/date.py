from datetime import datetime

time = datetime.now()
result = time.year

print(result)

#string olarak verilen bir veriyi zaman bilgisine çevirme
t = "15 april 2019 hour 10:12:30"
dt=datetime.strptime(t,"%d %B %Y hour %H:%M:%S")

print(dt)
