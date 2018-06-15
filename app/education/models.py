from django.db import models

from django.db import models
from django.utils import timezone


class School(models.Model):
    name = models.CharField(max_length=200)  # 길이 제한 있는 text
    description = models.TextField(blank=True)  # 길이가 무한인 text
    created_date = models.DateTimeField(default=timezone.now)  # date와 time을 저장해놓은 필드
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  # 객체를 문자열로 정의하고 싶을 때 사용
        return self.name


class Student(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)  # 길이 제한 있는 text
    created_date = models.DateTimeField(default=timezone.now)  # date와 time을 저장해놓은 필드
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  # 객체를 문자열로 정의하고 싶을 때 사용
        return self.name
