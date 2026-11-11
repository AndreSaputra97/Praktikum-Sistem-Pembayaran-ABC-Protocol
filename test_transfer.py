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