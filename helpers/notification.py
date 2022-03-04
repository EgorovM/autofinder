import threading

import telebot
from django.conf import settings
from django.core.mail import EmailMessage


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(
            self.subject,
            self.html_content,
            settings.EMAIL_HOST_USER,
            self.recipient_list
        )
        msg.send()


class Notification:
    def notify(self, title, text):
        raise NotImplementedError()


class EmailNotification(Notification):
    def __init__(self, receipt_list=None):
        self.receipt_list = receipt_list or settings.SENT_EMAILS_TO

    def notify(self, title, text):
        EmailThread(title, text, self.receipt_list).start()


class TelegramNotification(Notification):
    def __init__(self):
        self.bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN, parse_mode="HTML")

    def notify(self, title, text):
        self.bot.send_message(
            settings.TELEGRAM_CHANNEL_NAME,
            '<b>' + title + '</b>\n' + text
        )


class WhatsappNotification(Notification):
    def __init__(self, receipt_list=None):
        self.receipt_list = receipt_list or settings.SENT_WHATSAPP_TO

NOTIFIERS_LIST = [TelegramNotification, EmailNotification]
