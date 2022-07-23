from rest_framework import serializers
from apps.user.models import *
from apps.vacancies.models import Vacancies



class VacanciesCreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = ['title', 'description', 'price', 'company', 'contract', 'direction']


class VacanciesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = ['title',  'price', 'company', 'contract', 'direction', 'user']


class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = '__all__'