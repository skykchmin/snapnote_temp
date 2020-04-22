from django.db import models

# Create your models here.
class Snuser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    username = models.CharField(max_length=64, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='패스워드')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta: 
        db_table ='snap_user'

    