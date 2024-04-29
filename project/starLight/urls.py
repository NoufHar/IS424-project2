from django.urls import path
from . import views

urlpatterns = [
    path('event_list', views.event_list, name='event_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/delete/', views.event_delete, name='event_delete'),
    path('events/<int:event_id>/update/', views.event_update, name='event_update'),
    path('events/add/', views.add_event, name='add_event'),
    path("", views.index , name="index"),
    path("login", views.login_view , name="login"),
    path("logout", views.logout_view , name="logout"),
    path("account", views.account , name="account")
]
