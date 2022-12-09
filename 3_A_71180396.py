batas = int(input("Masukkan Pembatas: "))
forbidden = int(input("Masukkan Angka yang dilarang: "))

for i in range (0,batas):
    if i == forbidden:
        continue 
    print(i , end = " ")
    