from core.notifiers import ConsoleNotifier, EmailNotifier
from core.processor import PaymentProcessor

from plugins.ewallet import EWallet
from plugins.transfer_bank import TransferBank


# Identitas pelanggan
email = "andi@utr.ac.id"


# 1. Inisialisasi PaymentProcessor
pemroses = PaymentProcessor(ConsoleNotifier())


# 2. Pengujian pembayaran Transfer Bank
pemroses.checkout(
    TransferBank(saldo=1_000_000),
    250_000,
    email
)


# 3. Pengujian pembayaran E-Wallet
pemroses.checkout(
    EWallet(saldo=100_000),
    150_000,
    email
)


# 4. Mengganti kanal notifikasi
# Tanpa mengubah kode PaymentProcessor
pemroses.notifier = EmailNotifier()

dana = EWallet(
    saldo=500_000,
    provider="DANA"
)

pemroses.checkout(
    dana,
    300_000,
    email
)


# 5. Pengujian Notifier tidak valid
try:
    PaymentProcessor(notifier="bukan notifier")

except TypeError as e:
    print("Error:", e)