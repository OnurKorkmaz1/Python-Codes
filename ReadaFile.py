
# ana klasörde olmayınca çalışmıyor...

try:
    with open("File.txt") as file:
        print(file.read())

except:
    print("that files not found")
    

