from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Определение выборов для поля gender
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    # Определение выборов для поля user_type
    USER_TYPE_CHOICES = [
        ('customer', 'Исполнитель'),
        ('executor', 'Заказчик'),
    ]
    text = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True, verbose_name="Пол")
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='customer', verbose_name="Тип аккаунта")

    def __str__(self):
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[(
        'new', 'New'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='projects')


class Application(models.Model):
    text = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[(
        'new', 'New'), ('rejected', 'Rejected'), ('accepted', 'Accepted')])
    executor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='applications')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='applications')


class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='reviews')


class Specialization(models.Model):
    name = models.CharField(max_length=100)
    executors = models.ManyToManyField(
        User, related_name='specializations')
