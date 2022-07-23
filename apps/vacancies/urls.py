from django.urls import path
from apps.vacancies.views import *


urlpatterns = [
    path('create/', VacanciesCreateAPI.as_view()),
    path('update/<int:pk>/', VacanciesUpdateAPI.as_view()),
    path('delete/<int:pk>/', VacanciesDeleteAPI.as_view()),
    path('detail/<int:pk>/', VacanciesDetailAPI.as_view()),
    path('list/', VacancieslistAPI.as_view()),
    # path('list/cat/<int:pk>/', VacancieslistAPICategory.as_view()),

]