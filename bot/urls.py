from django.urls import path
from .views import RegistrationAPIView , UserList, LoggedUserView

urlpatterns = [
    path('create/', RegistrationAPIView.as_view()),
    path('userlist/', UserList.as_view()),
    path('user/', LoggedUserView.as_view())
]
