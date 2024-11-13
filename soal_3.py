while True: 
    
    jumlah_barang = int(input("Masukan Jumlah Barang :"))
    for i in range (1,jumlah_barang + 1):
        harga_barang = float(input(f"Masukan Harga Barang ke- {i} :"))


    total_harga_barang = harga_barang + harga_barang
    print(f"Jadi Totalnya adalah RP. {total_harga_barang}")

