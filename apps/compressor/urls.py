from django.urls import path

from . import views

app_name = 'compressor'

urlpatterns = [
    path('', views.HyperlinkCreateView.as_view(), name='create'),
    path('r/<str:internal>/', views.redirect_view, name='redirect'),
    path('i/<str:internal>/', views.HyperlinkInfoView.as_view(), name='info'),
]
