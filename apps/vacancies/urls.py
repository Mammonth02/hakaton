from django.urls import path
from apps.user.views import *


urlpatterns = [
    path('create/', UserCreatAPI.as_view()),
    # path('update/<int:pk>/', UserUpdateAPI.as_view()),
    # path('delete/<int:pk>/', UserDeleteAPI.as_view()),
    # path('detail/<int:pk>/', UserDetailAPI.as_view()),
    # path('list/', UserListAPIView.as_view()),

]