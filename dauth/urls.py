from django.urls import path
from .views import UserListCreate,UserRetriveUpdateDelete,ChangePasswordView

urlpatterns = [
    path('',UserListCreate.as_view()),
    path('password/change',ChangePasswordView.as_view()),
    path('<int:pk>',UserRetriveUpdateDelete.as_view()),

]
