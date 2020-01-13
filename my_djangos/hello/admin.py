from django.contrib import admin
from .models import Hello


class HelloAdmin(admin.ModelAdmin):
    list_display = ('id', 'your_name')
    # list_display = ('id', 'your_name', 'format_published_at')
    #
    # def format_published_at(self, obj):
    #     if obj.published_at is not None:
    #         return '{0:%Y年%m月%d日 %H時%M分}'.format(obj.published_at)
    #
    # format_published_at.short_description = '公開開始日時'


admin.site.register(Hello, HelloAdmin)
