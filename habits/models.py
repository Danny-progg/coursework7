import datetime

from django.db import models

from users.models import User, NULLABLE


class Habit(models.Model):
    PERIOD = (
        ('DAILY', 'каждый день'),
        ('WEEKLY', 'раз в неделю')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель привычки', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место', **NULLABLE)
    time = models.TimeField(verbose_name='время', **NULLABLE)
    habit_action = models.TextField(verbose_name='действие')
    pleasant_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Приятная привычка', **NULLABLE)
    is_pleasant = models.BooleanField(verbose_name='Признак приятной привычки', default=False, **NULLABLE)
    period = models.CharField(max_length=15, verbose_name='Периодичность', choices=PERIOD, default='DAILY', **NULLABLE)
    reward = models.TextField(verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.TimeField(verbose_name='Время на выполнение в секундах', default=datetime.time(minute=2),
                                        **NULLABLE)
    is_public = models.BooleanField(verbose_name='Признак публичности', default=False, **NULLABLE)

    objects = models.Manager()

    def __str__(self):
        return f"{self.habit_action}"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
