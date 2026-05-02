import datetime
import os

class SistemTol:
    def __init__(self):
        # Data tarif tol dan persentase diskon
        # 0.1 artinya diskon, 0.50 artinya 50%
        self.tarif_dasar = {
            "1": {"tipe": "Mobil Pribadi/Sedan", "harga": 50000, "diskon": 0.50},
            "2": {"tipe": "Bus/Truk Kecil", "harga": 100000, "diskon": 0.30},
            "3": {"tipe": "Truk Besar/Gandar", "harga": 150000, "diskon": 0.25}
        }
        self.log_transaksi = []

    def bersihkan_layar(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def cetak_struk(self, golongan, bayar, sisa, gerbang, harga_asli, besar_diskon):
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "="*35)
        print("        STRUK PEMBAYARAN TOL       ")
        print("="*35)
        print(f"Gerbang      : {gerbang}")
        print(f"Waktu        : {waktu}")
        print(f"Gol          : {self.tarif_dasar[golongan]['tipe']}")
        print(f"Harga Normal : Rp{harga_asli:,}")
        print(f"Diskon       : Rp{besar_diskon:,}")
        print(f"Total Bayar  : Rp{(harga_asli - besar_diskon):,}")
        print("-" * 35)
        print(f"Uang Dibayar : Rp{bayar:,}")
        print(f"Kembalian    : Rp{sisa:,}")
        print("="*35)
        print("     TERIMA KASIH, HATI-HATI!    \n")

    def mulai_simulasi(self):
        self.bersihkan_layar()
        print("--- SISTEM MANAJEMEN JALAN TOL (PROMO) ---")
        lokasi = input("Masukkan Nama Gerbang: ")
        
        while True:
            print(f"\n[ MENU GERBANG: {lokasi.upper()} ]")
            print("1. Masuk Kendaraan")
            print("2. Lihat Laporan Pendapatan")
            print("3. Bersihkan Layar")
            print("4. Keluar Program")
            
            pilihan = input("Pilih menu (1/2/3/4): ")

            if pilihan == "1":
                print("\n--- DAFTAR TARIF & DISKON ---")
                for k, v in self.tarif_dasar.items():
                    info_diskon = f"(Diskon {int(v['diskon']*100)}%)" if v['diskon'] > 0 else ""
                    print(f"{k}. {v['tipe']} - Rp{v['harga']:,} {info_diskon}")
                
                gol = input("Pilih Golongan Kendaraan: ")
                
                if gol in self.tarif_dasar:
                    harga_asli = self.tarif_dasar[gol]['harga']
                    potongan = int(harga_asli * self.tarif_dasar[gol]['diskon'])
                    harga_akhir = harga_asli - potongan
                    
                    try:
                        print(f"\nTarif Akhir: Rp{harga_akhir:,}")
                        saldo = int(input("Masukkan jumlah uang/saldo: Rp"))

                        if saldo >= harga_akhir:
                            sisa = saldo - harga_akhir
                            self.log_transaksi.append(harga_akhir)
                            self.cetak_struk(gol, saldo, sisa, lokasi, harga_asli, potongan)
                        else:
                            print(f"\n[!] Saldo kurang Rp{harga_akhir - saldo:,}")
                    except ValueError:
                        print("\n[!] Masukkan angka nominal yang valid!")
                else:
                    print("\n[!] Golongan tidak valid!")

            elif pilihan == "2":
                total = sum(self.log_transaksi)
                print("\n" + "-"*30)
                print(f"LAPORAN PENDAPATAN {lokasi.upper()}")
                print(f"Total Kendaraan : {len(self.log_transaksi)}")
                print(f"Total Uang      : Rp{total:,}")
                print("-"*30)

            elif pilihan == "3":
                self.bersihkan_layar()

            elif pilihan == "4":
                print("Sistem mati. Selamat istirahat!")
                break

if __name__ == "__main__":
    app = SistemTol()
    app.mulai_simulasi()