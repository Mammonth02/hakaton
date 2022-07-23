from rest_framework import serializers
from apps.user.models import *
from apps.vacancies.models import Vacancies



class VacanciesCreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = '__all__'