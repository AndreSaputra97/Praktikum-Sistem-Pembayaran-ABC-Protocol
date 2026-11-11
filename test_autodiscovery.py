# Import fungsi Autodiscovery
from plugins import muat_semua_plugin

# Import Registry
from core.registry import daftar_plugin, buat_metode


# Memuat seluruh plugin secara otomatis
muat_semua_plugin()


# Menampilkan daftar plugin
print("Plugin tersedia:", daftar_plugin())


# Membuat objek Transfer Bank
bank = buat_metode(
    "transfer",
    saldo=1_000_000
)


# Membuat objek E-Wallet
ewallet = buat_metode(
    "ewallet",
    saldo=500_000,
    provider="DANA"
)


# Menampilkan informasi metode pembayaran
print("Metode 1:", bank.nama)
print("Metode 2:", ewallet.nama)