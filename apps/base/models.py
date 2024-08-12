from django.db.models import * 

# Create your models here.
class Index(Model):
    title = CharField(
        max_length=255,
        verbose_name='Заголовок сайта (на главной странице)'
    )
    description = TextField(
        verbose_name="Описание сайта ()"
    )
    logo = ImageField(
        upload_to='image/',
        verbose_name='Логотип'
    )
    banner = ImageField(
        upload_to='image/'
    )
    twitter = URLField(
        verbose_name='Укжите ссылку на twitter'
    )
    facebook = URLField(
        verbose_name='Укжите ссылку на facebook'
    )
    github = URLField(
        verbose_name='Укжите ссылку на github'
    )
    gmail = URLField(
        verbose_name='Укжите ссылку на почту'
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки главной страницы'