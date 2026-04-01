class AkunBank:
    def __init__(self, nomor, pemilik, saldo_awal):
        self.nomor = nomor 
        self.pemilik = pemilik
        self.saldo = saldo_awal
        self.riwayat = [] 

    def tarik_tunai(self, jumlah):
        if jumlah <= 0:
            print("Jumlah tarikan harus lebih dari 0!")
        elif jumlah <= self.saldo:
            self.saldo -= jumlah
            self.riwayat.append(f"Tarik Tunai: Rp{jumlah}")
            print(f"{self.pemilik} menarik Rp{jumlah} BERHASIL")
        else:
            print("Saldo tidak cukup!")

    def transfer(self, tujuan, jumlah):
        biaya_admin = 2500
        total_potong = jumlah + biaya_admin

        if self.saldo >= total_potong:
            self.saldo -= total_potong
            tujuan.saldo += jumlah
            self.riwayat.append(f"Transfer ke {tujuan.pemilik}: Rp{jumlah}")
            print(f"Transfer ke {tujuan.pemilik} Berhasil! (Admin: Rp2.500)")
        else:
            print("Transfer Gagal: Saldo tidak cukup untuk transfer + admin.")

    def cetak_mutasi(self):
        print(f"\n=== Riwayat Transaksi {self.pemilik} ===")
        for aksi in self.riwayat:
            print(f"- {aksi}")
        print(f"Saldo Akhir: Rp{self.saldo}")