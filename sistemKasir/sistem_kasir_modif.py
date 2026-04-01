class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Keranjang:
    def __init__(self, punya_member=False):
        self.daftar_barang = []
        self.punya_member = punya_member

    def tambah_produk(self, produk_baru, jumlah): 
        if produk_baru.stok >= jumlah:
            self.daftar_barang.append({
                "produk": produk_baru, 
                "jumlah": jumlah
            })
            produk_baru.stok -= jumlah 
            print(f"Berhasil menambah: {jumlah} {produk_baru.nama}")
        else:
            print(f"Gagal! Stok {produk_baru.nama} tidak cukup (Sisa: {produk_baru.stok})")

    def hapus_barang(self, nama_barang): 
        for item in self.daftar_barang:
            if item["produk"].nama == nama_barang:
                item["produk"].stok += item["jumlah"]
                self.daftar_barang.remove(item)
                print(f"Berhasil menghapus {nama_barang} dari keranjang.")
                return
        print(f"Barang {nama_barang} tidak ditemukan di keranjang.")

    def hitung_subtotal(self):
        total = 0
        for item in self.daftar_barang:
            total += item["produk"].harga * item["jumlah"]
        return total

    def cetak_struk(self):
        print("\n" + "="*35)
        print("       STRUK BELANJA DIGITAL")
        print("="*35)
        
        subtotal = self.hitung_subtotal()
        
        for item in self.daftar_barang:
            p = item["produk"]
            j = item["jumlah"]
            print(f"- {p.nama} ({j} pcs) \t: Rp{p.harga * j}")
        
        print("-" * 35)
        print(f"Subtotal \t: Rp{subtotal}")

        diskon = 0
        if self.punya_member:
            diskon = subtotal * 0.1
            print(f"Diskon Member (10%): -Rp{diskon}")

        total_sebelum_pajak = subtotal - diskon
        pajak_ppn = total_sebelum_pajak * 0.11
        print(f"PPN (11%) \t: +Rp{pajak_ppn}")
        
        total_akhir = total_sebelum_pajak + pajak_ppn
        print("-" * 35)
        print(f"TOTAL AKHIR \t: Rp{total_akhir}")
        print("="*35)
