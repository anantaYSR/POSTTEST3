users = {} 
users['ananta'] = '123'

def garis():
    print("==============Daftar Akun===============")
    print.format("No", "Nama", "Password")

def login():
    count = 0
    while count < 3 :    
        username = input('Masukkan username : ')
        if username in users:
            password = input("masukan password    : ")
            if users[username] == password:
                print('Berhasil Login')
                print('Selamat Datang')
                break
            else:
                print('Gagal Login, Coba Lagi')
                count += 1
        else:
            print("Username Tidak Valid")
    print()

def akun_baru():
    username = input("Masukkan Username : ")
    password = input('Masukkan Password : ')
    users[username] = password

loop = True
while loop :
    print("Portal Login")
    print("[1] login \n[2] Buat Akun Baru \n[3] Exit")
    pilihan = int(input("Masukkan Pilihan = "))
    if pilihan == 1:
        login()
        print()
    elif pilihan == 2:
        akun_baru()
        print()
    elif pilihan == 3:
        print("Terima Kasih")
        loop = False
    else:
        print("Input Salah, Masukkan ulang")
