from rental import Mobil, Rental
m1 = Mobil("Estillo", 300000, 4)
m2 = Mobil("Bugatti", 2500000, 2)
m3 = Mobil("Grandmax", 800000, 7)

rental_saya = Rental(member=True) 

rental_saya.tambah_mobil(m1, 3)
rental_saya.tambah_mobil(m2, 1)
rental_saya.tambah_mobil(m3, 3)

rental_saya.hapus_sewa("Grandmax")

rental_saya.bayar(10000000)