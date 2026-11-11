'''
from plugins.transfer_bank import TransferBank
from core.base import PembayaranGagal
from core.utils import rupiah


# Membuat objek TransferBank
transfer = TransferBank(saldo=1000000, bank="BCA")

print("Nama Bank:", transfer.nama)
print("Saldo Awal:", rupiah(transfer.saldo))

try:
    # Melakukan pembayaran
    transaksi = transfer.proses(250000)
    # transaksi = transfer.proses(1500000) / Test Gagal

    print("ID Transaksi:", transaksi)
    print("Saldo Akhir:", rupiah(transfer.saldo))

except PembayaranGagal as e:
    print("Pembayaran Gagal:", e)
'''

# Import plugin agar otomatis terdaftar
import plugins.transfer_bank
import plugins.ewallet

from core.registry import daftar_plugin, buat_metode


# Menampilkan plugin yang tersedia
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


# Menampilkan nama metode pembayaran
print("Nama metode:", bank.nama)
print("Nama metode:", ewallet.nama)