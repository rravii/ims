from django.urls import path
from .views import ProductGenericView,ProductRetriveUpdateDestroy

urlpatterns = [
    path('',ProductGenericView.as_view()),
    path('<int:pk>',ProductRetriveUpdateDestroy.as_view()),
]
