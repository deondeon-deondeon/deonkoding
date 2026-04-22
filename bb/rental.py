class Mobil:
    def __init__(self, nama, harga_sewa, stok):
        self.nama = nama
        self.harga_sewa = harga_sewa
        self.stok = stok


class Rental:
    def __init__(self, member=False):
        self.daftar_sewa = []
        self.member = member

    def tambah_mobil(self, mobil, hari):
        if mobil.stok > 0:
            self.daftar_sewa.append((mobil, hari))
            mobil.stok -= 1
            print(f"Mobil {mobil.nama} berhasil disewa selama {hari} hari")
        else:
            print(f"Mobil {mobil.nama} tidak tersedia")

    def hapus_sewa(self, nama_mobil):
        for sewa in self.daftar_sewa:
            mobil, hari = sewa
            if mobil.nama == nama_mobil:
                self.daftar_sewa.remove(sewa)
                mobil.stok += 1
                print(f"Sewa mobil {nama_mobil} dibatalkan")
                return
        print("Mobil tidak tersedia")

    def hitung_total(self):
        total = 0
        for mobil, hari in self.daftar_sewa:
            total += mobil.harga_sewa * hari
        return total

    def cetak_struk(self):
        print("===Struk Rental Mobil===")
        for mobil, hari in self.daftar_sewa:
            print(f"{mobil.nama} ({hari} hari) : Rp{mobil.harga_sewa * hari}")

        total = self.hitung_total()

        if self.member:
            diskon = total * 0.05
            print(f"Diskon Member (5%) : -Rp{diskon}")
            total -= diskon

        pajak = total * 0.11
        print(f"Pajak 11% : Rp{pajak}")
        total += pajak

        print(f"Total Bayar : Rp{total}")
        return total

    def bayar(self, uang):
        total = self.cetak_struk()

        if uang >= total:
            kembalian = uang - total
            print(f"Uang dibayar : Rp{uang}")
            print(f"Kembalian : Rp{kembalian}")
        else:
            print("Uang tidak cukup!")