nama = input("masukkan nama: ")
n= 0
for i in range(len(nama)):
    print(nama[0:n+1])
    n+=1

for i in range (len(nama)-1):
    print(nama[0:n-1])
    n-=1


