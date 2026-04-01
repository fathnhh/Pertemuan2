from sistem_kasir import Produk, Keranjang

p1 = Produk("Kopi Kenangan", 25000)
p2 = Produk("Susu UHT", 18000)
p3 = Produk("Keyboard Gaming", 250000)

# del p3

keranjang_saya = Keranjang()
keranjang_saya.tambah_produk(p1)
keranjang_saya.tambah_produk(p2)
keranjang_saya.tambah_produk(p3)

keranjang_saya.cetak_struk()