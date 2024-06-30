from django.urls import path
from . import views
from calMoves.views import *

urlpatterns = [
    path('chess/queen', views.findValidMoves),
    path('chess/knight', views.findValidMoves),
    path('chess/bishop', views.findValidMoves),
    path('chess/rook', views.findValidMoves),
]