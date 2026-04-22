class Produk:
  def __init__(self, nama, harga, stok):
    self.nama = nama
    self.harga = harga
    self.stok = stok


class Keranjang:
  def __init__(self, member=False):
    self.daftar_barang = []
    self.member = member

  def tambah_produk(self, produk_baru, jumlah):
    if jumlah <= produk_baru.stok:
      for i in range(jumlah):
        self.daftar_barang.append(produk_baru)
      produk_baru.stok -= jumlah
      print(f"Berhasil menambah {jumlah} {produk_baru.nama}")
    else:
      print("Stok tidak cukup!")

  def hapus_produk(self, nama_produk):
    for barang in self.daftar_barang:
      if barang.nama == nama_produk:
        self.daftar_barang.remove(barang)
        barang.stok += 1
        print(f"{nama_produk} dihapus dari keranjang")
        return
    print("Barang tidak ditemukan di keranjang")

  def hitung_total(self):
    total = 0
    for barang in self.daftar_barang:
      total += barang.harga
    return total

  def cetak_struk(self):
    print("\n=== Struk Belanja ===")
    for barang in self.daftar_barang:
      print(f"- {barang.nama} : Rp{barang.harga}")

    total = self.hitung_total()

    if self.member:
      diskon = total * 0.05
      print(f"Diskon Member (5%) : -Rp{diskon}")
      total -= diskon

    ppn = total * 0.11
    print(f"PPN 11% : Rp{ppn}")
    total += ppn

    print(f"Total Bayar : Rp{total}")
    return total

  def bayar(self, uang_diterima):
    total = self.cetak_struk()

    if uang_diterima >= total:
      kembalian = uang_diterima - total
      print(f"Uang diterima : Rp{uang_diterima}")
      print(f"Kembalian : Rp{kembalian}")
    else:
      print("Uang tidak cukup!")