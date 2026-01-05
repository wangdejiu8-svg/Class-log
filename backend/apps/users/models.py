from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('student', '学生'),
        ('teacher', '老师'),
    ]

    name = models.CharField('真实姓名', max_length=50)
    user_type = models.CharField('用户类型', max_length=10, choices=USER_TYPE_CHOICES, default='student')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
