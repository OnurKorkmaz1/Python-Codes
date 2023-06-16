# --- < Opening Files in Python >---

#genel klasörde olunca okumuyor , dosya yolunu denemek gerekiyor.

#open file in current directory
file_library = open("File.txt","r")

"""
file1 = open("test.txt")      # equivalent to 'r' or 'rt'
file1 = open("test.txt",'w')  # write in text mode
file1 = open("img.bmp",'r+b') # read and write in binary mode
"""

#Reading Files in Python
read_content = file_library.read()
print(read_content)

# close the file
file_library.close()


