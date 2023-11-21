from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitValidator, HabitTimeValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitValidator(field1='reward', field2='pleasant_habit', field3='is_pleasant'),
                      HabitTimeValidator(fields='time_to_complete'),
                      ]