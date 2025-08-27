def inputm(m):
    print(f"Masukkan elemen matrix {m} (3x3): ")
    M = []
    for i in range(3):
        baris=[]
        for j in range(3):
            elemen = int(input(f"Elemen [{i+1}][{j+1}]: "))
            baris.append(elemen)
        M.append(baris)
    return M

def printm(M):
    for baris in M:
        print(" ".join(f"{elemen:4}" for elemen in baris))
    print()

A = inputm("A")
B = inputm("B")

#Opsi penjumlahan matriks
def plus(A,B):
    return [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]
#Opsi pengurangan matriks
def minus(A,B):
    return [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]
#Opsi perkalian matriks
def kali(A,B):
    hasil = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                hasil[i][j]+=A[i][k]*B[k][j]
    return hasil
#Opsi untuk memeriksa apakah kedua matriks adalah satuan atau tidak
def satuan(M):
    for i in range(3):
        for j in range(3):
            if M[i][j] not in (0,1):
                return False
    return True

print("Pilih menu:"
      "\npilihan 1 untuk operasi penjumlahan kedua matriks"
      "\npilihan 2 untuk operasi pengurangan matriks A dengan matriks B"
      "\npilihan 3 adalah operasi perkalian matriks A dengan matriks B"
      "\npilihan 4 adalah operasi untuk memeriksa apakah kedua matriks adalah matriks satuan atau tidak")
pilihan = int(input("Masukkan pilihan: "))

if pilihan == 1:
    print("\nHasil Penjumlahan Matriks A + B:")
    printm(plus(A,B))
elif pilihan == 2:
    print("\nHasil Pengurangan Matriks A - B:")
    printm(minus(A,B))
elif pilihan == 3:
    print("\nHasil Perkalian Matriks A * B:")
    printm(kali(A,B))
elif pilihan == 4:
    print("\nPemeriksaan Matriks Satuan:")
    print("Matriks A", "adalah matriks satuan" if satuan(A) else "bukan matriks satuan")
    print("Matriks B", "adalah matriks satuan" if satuan(B) else "bukan matriks satuan")
else:
    print("\nBukan pilihan yang benar")
