# Percobaan 1 : ABC PaymentMethod

from abc import ABC, abstractmethod

from core.utils import rupiah


class PembayaranGagal(Exception):
    """Dilempar saat pembayaran ditolak atau tidak valid."""


class PaymentMethod(ABC):
    """Kontrak (abstract base class) untuk semua metode pembayaran."""

    def __init__(self, nama: str):
        self.nama = nama

    @abstractmethod
    def validasi(self, jumlah: float) -> bool:
        """Periksa apakah pembayaran dapat diproses."""

    @abstractmethod
    def bayar(self, jumlah: float) -> str:
        """Proses pembayaran, lalu kembalikan ID transaksi."""

    def proses(self, jumlah: float) -> tuple[str, float, float]:
        admin = self.biaya_admin(jumlah)
        total = jumlah + admin

        if not self.validasi(total):
            raise PembayaranGagal(
                "Saldo tidak mencukupi atau batas transaksi terlampaui."
            )

        trx_id = self.bayar(total)

        return trx_id, admin, total

    @abstractmethod
    def biaya_admin(self, jumlah: float) -> float:
        """Menghitung biaya administrasi pembayaran."""
        pass

