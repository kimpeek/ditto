from django.urls import path

from . import views

app_name = 'compressor'

urlpatterns = [
    path('', views.HyperlinkCreateView.as_view(), name='create'),
    path('<str:internal>/', views.redirect_view, name='redirect'),
    path('<str:internal>/info', views.HyperlinkInfoView.as_view(), name='info'),
]
