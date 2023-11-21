from django.urls import path

from habits.apps import HabitsConfig
from habits.views import CreateHabitAPIView, UpdateHabitAPIView, RetrieveHabitAPIView, ListHabitAPIView, \
    ListPublicHabitAPIView, DestroyHabitAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', CreateHabitAPIView.as_view(), name='create-habit'),
    path('update/', UpdateHabitAPIView.as_view(), name='update-habit'),
    path('view/<int:pk>/', RetrieveHabitAPIView.as_view(), name='view-habit'),
    path('list/', ListHabitAPIView.as_view(), name='list-habit'),
    path('list/public', ListPublicHabitAPIView.as_view(), name='list_public-habit'),
    path('delete/', DestroyHabitAPIView.as_view(), name='delete-habit'),
]