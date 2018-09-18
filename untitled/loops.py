#x=int(input("Input Any Number:"))
#for i in range (1,x+1):
   # print("*"*i)
string = ""
baris = 1

x = int(input("Masukkan angka :"))

# Looping Baris
while baris <= x:
    kolom = baris

    # Looping Kolom
    while kolom > 0:
        string = string + "*"
        kolom = kolom - 1

    string = string + "\n"
    baris = baris + 1
print(string)

string = ""
bar = 1

x = int(input("Masukkan angka :"))

# Looping Baris
while bar <= x:
    # Looping Kolom Spasi Kosong
    kol = bar
    while kol > 1:
        string = string+"   "
        kol = kol - 1

    # Looping Kolom Bintang
    kanan = 0
    while kanan <= (x - bar):
        string = string + " * "
        kanan = kanan + 1

    string = string + "\n"
    bar = bar + 1
print(string)