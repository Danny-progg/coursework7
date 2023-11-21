from habits.models import Habit


def get_reward_or_habit():
    habits = Habit.objects.all()
    for habit in habits:
        reward = habit.reward
        pleasant = habit.pleasant_habit
        if reward:
            habit = reward
        else:
            habit = pleasant
        return habit