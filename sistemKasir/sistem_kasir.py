class Produk:
  def __init__(self, nama, harga):
    self.nama = nama
    self.harga = harga
    
class Keranjang:
  def __init__(self):
    self.daftar_barang = []
  
  def tambah_produk(self, produk_baru):
    self.daftar_barang.append(produk_baru)
    print(f"Berhasil menambah: {produk_baru.nama}")
    
  def hitung_total(self):
    total = 0
    for barang in self.daftar_barang:
      total += barang.harga
    return total
  
  def cetak_struk(self):
    print("\n=== Struk Belanja ===")
    for barang in self.daftar_barang:
      print(f"- {barang.nama} : Rp{barang.harga}")
      
    total_akhir = self.hitung_total() #293000
    if total_akhir > 100000:
      diskon = total_akhir * 0.1
      print(f"\nDiskon (10%) \t: -Rp{diskon}")
      total_akhir -= diskon
      
    print(f"Total Akhir \t: Rp{total_akhir}")