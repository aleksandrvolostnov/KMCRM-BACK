from rest_framework import serializers
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    start_date = models.DateField()  # Добавьте это поле для даты начала
    end_date = models.DateField()  # Добавьте это поле для даты завершения
    status = models.CharField(max_length=100)  # Добавьте это поле для статуса
    responsible = models.CharField(max_length=200)  # Добавьте это поле для ответственного
    customer = models.CharField(max_length=100)  # Добавьте это поле для заказчика
    report_text = models.TextField(blank=True, null=True)  # Текстовый отчет
    report_file = models.FileField(upload_to='report_files/', blank=True, null=True)  # Файл отчета


    def __str__(self):
        return self.title
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

from django.db import models
from .models import Task
class ReportFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='reportfile_set')
    file = models.FileField(upload_to='report_files/')

class TaskFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to='task_files/', default = None, null=True)

    def __str__(self):
        return self.file.name  # Вернуть имя файла как строковое представление
