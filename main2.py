from SistemKasir import Produk, Keranjang
p1 = Produk("Kopi Kenangan", 25000, 10)
p2 = Produk("Susu UHT", 18000, 5)
p3 = Produk("keyboard gaming", 250000, 3)

keranjang_saya = Keranjang(member=True)

keranjang_saya.tambah_produk(p1, 2)
keranjang_saya.tambah_produk(p2, 1)
keranjang_saya.tambah_produk(p3, 3)


keranjang_saya.hapus_produk("Kopi Kenangan")

keranjang_saya.bayar(1000000)