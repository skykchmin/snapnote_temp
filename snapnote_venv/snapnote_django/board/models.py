from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')

class File(models.Model):
    title = models.CharField(max_length=128, verbose_name='파일제목')
    pdf = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.title