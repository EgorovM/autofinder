import re

from django.db import models
from djrichtextfield.models import RichTextField

from helpers.notification import NOTIFIERS_LIST

SHORT_TEXT_CHAR_AMOUNT = 172


def notify_owners(title, text):
    for notifier_class in NOTIFIERS_LIST:
        notifier = notifier_class()
        notifier.notify(title, text)


class FeedbackContact(models.Model):
    telephone = models.CharField(max_length=63)
    full_name = models.CharField(max_length=63)
    details = models.TextField(default='Обратная связь')
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        notify_owners(
            'Вас просят связаться',
            f'Телефон: {self.telephone}\n'
            f'ФИО: {self.full_name}\n'
            f'Детали: {self.details}'
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
        content_without_tag = re.sub('<[^>]*>', ' ', self.content)
        short_word_count = content_without_tag.count(' ')
        short_text_words = content_without_tag.split()[:short_word_count]

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

    img = models.ImageField('Изображение', upload_to='media/work_example')
    task = models.TextField('Задача')
    result = RichTextField('Результат')

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = "Пример работы"
        verbose_name_plural = "Примеры работы"


class Service(models.Model):
    title = models.CharField('Название услуги', max_length=63)
    description = models.TextField('Описание услуги')
    price_from = models.CharField('Цены от', max_length=15)
    service_include = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class CompanyInfo(models.Model):
    info = RichTextField()

    def __str__(self):
        return f'Информация @{self.id}'

    class Meta:
        verbose_name = "Информация о компании"
        verbose_name_plural = "Информация о компании"


class FAQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = RichTextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Часто задаваемый вопрос"
        verbose_name_plural = "Часто задаваемые вопросы"
