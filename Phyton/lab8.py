print("Masukkan rantai penyebaran:")

# List nama pasien
daftar_pasien = []
while True:
    pasien = input() 
    if pasien == "selesai":
        break
    pasien = pasien.split() 
    # Memasukkan info pasien ke dictionary
    pasien_dict = dict()
    pasien_dict["nama_penular"] = pasien[0]
    pasien_dict["nama_tertular"] = pasien[1:]
    # Memasukkan ke list penampung jadwal dict
    daftar_pasien.append(pasien_dict)

info_perintah = "\nPerintah yang tersedia:\n\
1. RANTAI_PENYEBARAN <nama_penular>\n\
2. CEK_PENULARAN <nama_tertular> <nama_penular>\n\
3. EXIT"

print(info_perintah)

# Main Console
perintah = ""
while perintah != "EXIT": 
    perintah = input("\nMasukkan perintah: ") 
    jenis_perintah = perintah.split()[0] 

    perintah_valid = ["RANTAI_PENYEBARAN", "CEK_PENULARAN", "EXIT"] 
    # Mengecek apabila perintah tidak valid
    while jenis_perintah not in perintah_valid:
        print("Maaf perintah tidak dikenali. Mohon masukkan perintah yang valid.")
        perintah = input("\nMasukkan perintah: ")
        jenis_perintah = perintah.split()[0]
    # Bagian RANTAI_PENYEBARAN
    # def rantai_penyebaran(daftar_pasien):
    #     kelas_valid = ["Eksekutif", "Bisnis", "Ekonomi"]
    #         tujuan = perintah[1]
    #         kelas = perintah[2]
    #         if kelas not in kelas_valid:
    #             print("Perintah yang dimasukkan tidak valid")
    #         else:
    #             not_found = True # Flag jadwal tidak ditemukan
    #             for jadwal in daftar_jadwal:
    #                 if jadwal["tujuan_akhir"] == tujuan and jadwal["kelas"] == kelas:
    #                     not_found = False
    #                     nomor_ka = jadwal["nomor_ka"]
    #                     jam_berangkat = jadwal["jam_keberangkatan"]
    #                     harga_tiket = jadwal["harga_tiket"]
    #                     print(f"KA {nomor_ka} berangkat pukul {jam_berangkat} dengan harga tiket {harga_tiket}")
    #             if not_found:
    #                 print("Tidak ada jadwal KA yang sesuai")
    #     return rantai_penyebaran(daftar_pasien[1:])
    # # Bagian RANTAI_PENYEBARAN
    # if jenis_perintah == "RANTAI_PENYEBARAN": # RANTAI_PENYEBARAN <nama_penular>
    #     perintah = perintah.split()
    #     if len(perintah) <= 1:
    #         print("Perintah yang dimasukkan tidak valid, mohon tuliskan nama penular.")
    #     else:
    #         return rantai_penyebaran(daftar_pasien)
    # # Bagian TUJUAN_JAM
    # elif jenis_perintah == "TUJUAN_JAM":
    #     perintah = perintah.split()
    #     if len(perintah) <= 1:
    #         print("Perintah yang dimasukkan tidak valid")
    #     else:
    #         tujuan = perintah[1]
    #         jam = int(perintah[2])
    #         not_found = True # Flag jadwal tidak ditemukan
    #         for jadwal in daftar_jadwal:
    #             if jadwal["tujuan_akhir"] == tujuan and jadwal["jam_keberangkatan"] <= jam:
    #                 not_found = False
    #                 nomor_ka = jadwal["nomor_ka"]
    #                 jam_berangkat = jadwal["jam_keberangkatan"]
    #                 harga_tiket = jadwal["harga_tiket"]
    #                 print(f"KA {nomor_ka} berangkat pukul {jam_berangkat} dengan harga tiket {harga_tiket}")
    #         if not_found:
    #             print("Tidak ada jadwal KA yang sesuai")
        
    
    # # Bagian akhiri program
    # if jenis_perintah == "EXIT":
    #     print("Goodbye~ Semoga virus KOPIT cepat berakhir.")