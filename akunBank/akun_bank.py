class AkunBank:
  # def __init__(self, nomor, pemilik, saldo_awal):
  #   self.nomor = nomor 
  #   self.pemilik = pemilik
  #   self.saldo = saldo_awal
  
  def cek_saldo(self):
    print(f"Saldo {self.pemilik}: Rp{self.saldo}")
    
  def tarik_tunai(self, jumlah):
    if jumlah <= self.saldo:
      self.saldo -= jumlah
      print(f"{self.pemilik} menarik Rp{jumlah}")
    else:
      print("Saldo tidak cukup!")
  
  def transfer(self, tujuan, jumlah):
    if self.saldo >= jumlah:
      self.saldo -= jumlah
      tujuan.saldo += jumlah
      print(f"Transfer Rp{jumlah} ke {tujuan.pemilik} Berhasil!")
    else:
      print("Transfer Gagal: Saldo tidak cukup.")
    
