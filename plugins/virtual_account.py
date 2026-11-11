from datetime import datetime, timedelta

from core.base import PaymentMethod
from core.registry import register_plugin
from core.utils import buat_id


@register_plugin("va")
class VirtualAccount(PaymentMethod):

    def __init__(
        self,
        merchant: str = "Kantin Kampus",
        batas_menit: int = 30
    ):
        super().__init__(f"Virtual Account {merchant}")

        self.batas_waktu = datetime.now() + timedelta(
            minutes=batas_menit
        )

        self.status = "menunggu"

    def validasi(self, jumlah: float) -> bool:
        return (
            jumlah > 0
            and datetime.now() <= self.batas_waktu
        )

    def biaya_admin(self, jumlah: float) -> float:
        return 0.0

    def bayar(self, jumlah: float) -> str:
        self.status = "menunggu"
        return buat_id("VA")