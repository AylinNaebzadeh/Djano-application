
from django.urls import path
from . import views
from .views import SearchResultsView
urlpatterns = [
    path('' , views.first_page, name='first_page'),
    path('booksandcourses/' , views.rec_list, name='rec_list'),
    path('delete/<int:id>' , views.rec_delete, name='rec_delete'),
    path('update/<int:id>/' , views.rec_update, name='rec_update'),
    path('create/' , views.rec_create, name='rec_create'),
    path('search/' , SearchResultsView.as_view() , name='search_results'),
    path('contact/' , views.contact, name="contact"),
    path('register/' , views.register_request, name="register"),
    path('login/' , views.login_request, name="login"),
    path('logout/' , views.logout_request, name="logout"),
]