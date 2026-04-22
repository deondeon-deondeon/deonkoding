class AkunBank:
    def __init__(self, nomor, pemilik, saldo_awal):
     self.nomor = nomor 
     self.pemilik = pemilik
     self.saldo = saldo_awal
     self.riwayat= []
  
    def cek_saldo(self):
       print(f"Saldo {self.pemilik}: Rp{self.saldo}")
    
    def tarik_tunai(self, jumlah):
     if jumlah <= 0:
       print("Jumlah harus lebih dari 0!")
     elif jumlah <= self.saldo:
      self.saldo -= jumlah
      pesan=print(f"{self.pemilik} menarik Rp{jumlah}")
      self.riwayat.append(pesan)
      print(pesan)
     else:
      print("Saldo tidak cukup!")
  
    def transfer(self, tujuan, jumlah):
     biaya_admin = 2500
     total = jumlah + biaya_admin
     if jumlah <= 0:
       print("Jumlah harus lebih dari 0!")
     elif self.saldo >= total:
      self.saldo -= total
      tujuan.saldo += jumlah 
      pesan_kirim=f"menerima rp{jumlah} ke {tujuan.pemilik} berhasil!. Biaya admin rp.2500,saldo rp{self.saldo}"
      pesan_terima=f"menerima rp{jumlah} dari {self.pemilik}, saldo rp{tujuan.saldo}"
      self.riwayat.append(pesan_kirim)
      tujuan.riwayat.append(pesan_terima)
     else:
      print("transfer gagal : saldo tidak cukup.")
    def tampilkan_riwayat(self):
      print(f"\n riwayat transaksi {self.pemilik}:")
      for r in self.riwayat:
       print(r)