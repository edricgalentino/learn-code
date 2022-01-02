print("Selamat datang! Silahkan masukkan jadwal KA:")

# List jadwal KA
daftar_jadwal = []
while True:
    jadwal = input() 
    if jadwal == "selesai":
        break
    jadwal = jadwal.split() 
    # Memasukkan info jadwal ke dictionary
    jadwal_dict = dict()
    jadwal_dict["nomor_ka"] = jadwal[0]
    jadwal_dict["tujuan_akhir"] = jadwal[1]
    jadwal_dict["jam_keberangkatan"] = int(jadwal[2])
    jadwal_dict["harga_tiket"] = int(jadwal[3])
    # Mengecek kelas dari KA berdasarkan Nomor ka
    nomor_ka = jadwal[0]
    if 100 <= int(nomor_ka) <= 199:
        kelas = "Eksekutif"
    elif 200 <= int(nomor_ka) <= 299:
        kelas = "Bisnis"
    elif 300 <= int(nomor_ka) <= 399:
        kelas = "Ekonomi"
    jadwal_dict["kelas"] = kelas

    # Memasukkan ke list penampung jadwal dict
    daftar_jadwal.append(jadwal_dict)

info_perintah = "\nPerintah yang tersedia:\n\
1. INFO_TUJUAN\n\
2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>\n\
3. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>\n\
4. EXIT"

print(info_perintah)
# Main Console
perintah = ""
while perintah != "EXIT": 
    perintah = input("\nMasukkan perintah: ") 
    jenis_perintah = perintah.split()[0] 

    perintah_valid = ["INFO_TUJUAN", "TUJUAN_KELAS", "TUJUAN_JAM", "EXIT"] 
    # Mengecek apabila perintah tidak valid
    while jenis_perintah not in perintah_valid:
        print("Perintah yang dimasukkan tidak valid")
        perintah = input("\nMasukkan perintah: ")
        jenis_perintah = perintah.split()[0]

    # Bagian INFO_TUJUAN
    if jenis_perintah == "INFO_TUJUAN":
        daftar_tujuan = set()
        for jadwal in daftar_jadwal:
            tujuan = jadwal["tujuan_akhir"]
            daftar_tujuan.add(tujuan)
        print("KA di stasiun ini memiliki tujuan akhir:")
        for tujuan in daftar_tujuan :
            print(tujuan)

    # Bagian TUJUAN_KELAS
    elif jenis_perintah == "TUJUAN_KELAS": # TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
        perintah = perintah.split()
        if len(perintah) <= 1:
            print("Perintah yang dimasukkan tidak valid")
        else:
            kelas_valid = ["Eksekutif", "Bisnis", "Ekonomi"]
            tujuan = perintah[1]
            kelas = perintah[2]
            if kelas not in kelas_valid:
                print("Perintah yang dimasukkan tidak valid")
            else:
                not_found = True # Flag jadwal tidak ditemukan
                for jadwal in daftar_jadwal:
                    if jadwal["tujuan_akhir"] == tujuan and jadwal["kelas"] == kelas:
                        not_found = False
                        nomor_ka = jadwal["nomor_ka"]
                        jam_berangkat = jadwal["jam_keberangkatan"]
                        harga_tiket = jadwal["harga_tiket"]
                        print(f"KA {nomor_ka} berangkat pukul {jam_berangkat} dengan harga tiket {harga_tiket}")
                if not_found:
                    print("Tidak ada jadwal KA yang sesuai")

    # Bagian TUJUAN_JAM
    elif jenis_perintah == "TUJUAN_JAM":
        perintah = perintah.split()
        if len(perintah) <= 1:
            print("Perintah yang dimasukkan tidak valid")
        else:
            tujuan = perintah[1]
            jam = int(perintah[2])
            not_found = True # Flag jadwal tidak ditemukan
            for jadwal in daftar_jadwal:
                if jadwal["tujuan_akhir"] == tujuan and jadwal["jam_keberangkatan"] <= jam:
                    not_found = False
                    nomor_ka = jadwal["nomor_ka"]
                    jam_berangkat = jadwal["jam_keberangkatan"]
                    harga_tiket = jadwal["harga_tiket"]
                    print(f"KA {nomor_ka} berangkat pukul {jam_berangkat} dengan harga tiket {harga_tiket}")
            if not_found:
                print("Tidak ada jadwal KA yang sesuai")
        
    
    # Bagian akhiri program
    elif jenis_perintah == "EXIT":
        print("Terima kasih sudah menggunakan program ini!")