from django.urls import path
from . import views

urlpatterns = [
    path('info_items/', views.info_items),
    path('info_locations/', views.info_locations),
    path('info_lore/', views.info_lore),
    path('info_moby/', views.info_moby),
    path('info_player/', views.info_player),
    path('info_value/', views.info_value),
    path('', views.info),
    
    
    
]