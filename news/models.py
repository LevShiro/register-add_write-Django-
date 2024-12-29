from django.db import models

from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Articles(models.Model):
    title = models.CharField('Название',max_length=50,default="Дэфолт название")
    anons = models.CharField('Анонс',max_length=50,default="Дэфолт анонс")
    full_text = models.TextField('Статья',max_length=250,default="Дэфолт что-то интересное")
    autor = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,default=None)
    date = models.DateTimeField("Дата публикации",auto_now_add=True)

    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    
    def __str__(self):
        return self.title