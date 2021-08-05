def menu():
    import os
    os.system("Cls")
    print("Daftar menu")
    print("1. Tambah data")
    print("2. Tampilkan semua data")
    pilih=int(input("Masukan pilihan : "))
    pilihmenu(pilih)

def pilihmenu(p):
    if p==1:
        tambahdata()
    elif p==2:
        tampildata()

def tampildata():
    print("Menampilkan semua data")
    f=open("Data.txt")
    isi=f.readlines()
    isi.sort()
    if len(isi)==0:
        print("Data masih kosong")
    else:
        i=1;
        for x in isi:
            pecah=x.split(",")
            if(len(pecah)==1):
                print(str(i)+". ",end="")
                print(pecah[0],end="")
                i+=1
    print("tekan enter untuk melanjutkan")
    f.close()
    input()
    menu()

def tambahdata():
    print("Masukan data")
    n=input("Data : ")
    f=open("Data.txt","a")
    f.writelines([n+"\n"])
    f.close()
    input()
    menu()
    
        
