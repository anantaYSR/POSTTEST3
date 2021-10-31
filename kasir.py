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
        harga=(4000*jumlahpesan)
        if jumlahpesan >= 3:
            diskon = int(harga*5/100)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "b":
        listnama= "Es Teh"
        harga = (3000*jumlahpesan)
        if jumlahpesan >= 3:
            diskon = int(harga * 5/100)
            totalharga =int(harga-diskon)
        else:
            diskon =(0)
            totalharga =int(harga)
    elif pesan == "c":
        listnama= "Es Josu"
        harga=int(5000*jumlahpesan)
        if jumlahpesan >= 3:
            diskon = int(harga*10/100)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "d":
        listnama= "Nasi Padang"
        harga=int(14000*jumlahpesan)
        if jumlahpesan >= 2:
            diskon = int(harga*10/100)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    elif pesan == "e":
        listnama= "Nasi campur"
        harga=int(13000*jumlahpesan)
        if jumlahpesan >= 2:
            diskon = int(harga*10/100)
            totalharga=int(harga-diskon)
        else:
            diskon =(0)
            totalharga=int(harga)
    else:
        listnama = "-"
        harga = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali y/t =")
 
    print("--------------------------")
    print("waroeng ananta")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali y/t =")
