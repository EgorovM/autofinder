from django.db import models
from django.conf import settings
from django.core.mail import send_mail

from djrichtextfield.models import RichTextField

SHORT_TEXT_CHAR_AMOUNT = 172


def notify_owners(title, text):
    send_mail(title, text, settings.EMAIL_HOST_USER, settings.SENT_EMAILS_TO)


class FeedbackContact(models.Model):
    telephone = models.CharField(max_length=63)
    full_name = models.CharField(max_length=63)
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        print('saving...')
        notify_owners(
            'Вас просят связаться',
            f'Телефон: {self.telephone}\n'
            f'ФИО: {self.full_name}'
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} @{self.telephone}"

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратные связи"


class BlogArticle(models.Model):
    title = models.CharField('Заголовок', max_length=63)
    content = RichTextField('Текст')
    youtube_id = models.CharField('Идентификатор видео youtube', blank=True, max_length=1023)
    img = models.ImageField('Изображение', upload_to='blog', default='blog/default.png', null=True, blank=True)
    created = models.DateTimeField('Дата создания', auto_now=True)

    def short_content(self):
        short_word_count = self.content[:SHORT_TEXT_CHAR_AMOUNT].count(' ')
        short_text_words = self.content.split()[:short_word_count]

        return " ".join(short_text_words) + '...'

    def __str__(self):
        return f"{self.title} @{self.created.date()}"

    class Meta:
        verbose_name = "Статья блога"
        verbose_name_plural = "Статьи блога"


class WorkExample(models.Model):
    car_name = models.CharField('Название машины', max_length=63)
    year_of_issue = models.CharField('Год выпуска', max_length=15)
    saler_price = models.CharField('Цена продавца', max_length=31)
    after_price = models.CharField('Цена после торга', max_length=31)

    img = models.ImageField('Изображение', upload_to='models/work_example')
    task = models.TextField('Задача')
    result = RichTextField('Результат')

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = "Пример работы"
        verbose_name_plural = "Примеры работы"
