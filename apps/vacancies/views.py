
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.user.permissions import *
from apps.vacancies.models import Vacancies
from apps.vacancies.serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter




# Create your views here.

class VacanciesCreateAPI(generics.CreateAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesCreatSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()

class VacanciesDeleteAPI(generics.RetrieveDestroyAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer
    permission_classes = (DeleteProfile,)


class VacanciesDetailAPI(generics.RetrieveAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer
    permission_classes = (IsAuthenticated,)


class VacanciesUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesCreatSerializer
    permission_classes = (UpdateProfile,)



class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class VacancieslistAPI(generics.ListAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesListSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['price', 'direction', 'contract']
    search_fields = ['title', 'description']



# class VacancieslistAPICategory(generics.ListAPIView):
#     queryset = Vacancies.objects.all()
#     serializer_class = VacanciesListSerializer
#     permission_classes = (IsAuthenticated,)
#     pagination_class = Pagination

#     def get_queryset(self):



#         return super().get_queryset()


#     def get_queryset(self):
#         pk = self.kwargs.get("pk")

#         list = []

#         for i in Direction.objects.all():
#             list.append(i.id)
        
#         if pk in list:
#             direc = Direction.objects.get(id = pk)
#             return Vacancies.objects.filter(direction = direc)

#         return Vacancies.objects.all()
