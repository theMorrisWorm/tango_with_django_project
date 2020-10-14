# rango/urls.py

from django.urls import path
from rango import views

# Adding App name to use as namespace in URL
from rango.views import ProfileView

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    # path('rango/', views.index, name='index'),

    path('about/', views.about, name='about'),

    # For show_category
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    # For add_category form
    path('add_category/',
         views.add_category, name='add_category'),

    # For add_page form
    path('category/<category_name_slug>/add_page/',
         views.add_page, name='add_page'),
    # # For Register Page Form
    # path('register/',
    #      views.register, name='register'),
    # # For Login Page Form
    # path('login/',
    #      views.user_login, name='login'),
    # For login restricted test
    path('restricted/',
         views.restricted, name='restricted'),
    # # For logout
    # path('logout/',
    #      views.user_logout, name='logout'),

    # For AJAX like button
    path('like/', views.like_category, name='like_category'),

    # For SEARCH SUGGESTION
    path('suggest/', views.suggest_category, name='suggest_category'),

    # For Page View Count
    path("goto/", views.goto_url, name='goto'),

    # For User Profile edit
    path('profile/<username>/',ProfileView.as_view(),name='profile'),

]
