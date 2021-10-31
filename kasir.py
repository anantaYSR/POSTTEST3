import datetime
pilihan="y"
while pilihan=="y":
    print("""
    ==============================
          waroeng ananta
            List Menu 
    ==============================
    A. Es Jeruk      : Rp 4.000
    B. Es Teh        : Rp 3.000
    C. Es Jous       : Rp 5.000
    D. Nasi Padang   : Rp 14.000
    E. Nasi campur   : Rp.13.000
    ==============================
    """)
    pesan=str(input("masukkan list abjad menu ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "a":
        listnama= "Es Jeruk"
        harga = 4000
        diskon = 10 if jumlahpesan >= 3 else 0
        totalharga = (harga*jumlahpesan)
    elif pesan == "b":
        listnama= "Es Teh"
        harga = 3000
        diskon = 10 if jumlahpesan >= 3 else 0
        totalharga = (harga*jumlahpesan)
    elif pesan == "c":
        listnama= "Es Teh"
        harga = 5000
        diskon = 10 if jumlahpesan >= 3 else 0
        totalharga = (harga*jumlahpesan)
    elif pesan == "d":
        listnama= "Nasi Padang"
        harga = 14000
        diskon = 5 if jumlahpesan >= 2 else 0
        totalharga = (harga*jumlahpesan)
    elif pesan == "e":
        listnama= "Nasi campur"
        harga = 13000
        diskon = 5 if jumlahpesan >= 2 else 0
        totalharga = (harga*jumlahpesan)
    else:
        listnama = "-"
        harga = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali y/t =")
    metodepembayaran = input("Apa anda ingin membayar dengan E-money? (y/n)")
    diskonpembayaran = 5 if metodepembayaran == "y" else 0
    diskonhari = 10 if datetime.datetime.today().weekday() < 5 else 5
    totaldiskon = diskon + diskonpembayaran + diskonpembayaran
    totalbayar = totalharga - (totaldiskon * totalharga / 100)
    print("--------------------------")
    print("waroeng ananta")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", totaldiskon,"%")
    print("--------------------------")
    print("Jumlah Bayar :", totalbayar)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali y/t =")
