from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.vacancies.models import Vacancies
from apps.vacancies.serializers import VacanciesCreatSerializer


# Create your views here.

class VacanciesCreateAPI(generics.CreateAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesCreatSerializer
    permission_classes = (IsAuthenticated,)
    