from django.urls import path
from .views import HomePageView, PostDetailView, AddView


app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('info/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('post/', AddView.as_view(), name='post')
]
