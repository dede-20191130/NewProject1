from django.db import models


class Posting(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='名前',
        help_text='<b>あなたの名前を入力してください</b>',
    )
    message = models.CharField(
        max_length=255,
        verbose_name='メッセージ',
        help_text='<u>メッセージを入力してください</u>',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='登録日時',
    )
