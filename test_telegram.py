from core.notifiers import TelegramNotifier
from core.protocols import Notifier
from core.processor import PaymentProcessor

telegram = TelegramNotifier("TOKEN-12345")

pemroses = PaymentProcessor(telegram)

print("TelegramNotifier berhasil digunakan!")




'''
telegram = TelegramNotifier()

print(isinstance(telegram, Notifier))
'''
