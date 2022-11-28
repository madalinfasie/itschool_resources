from django.urls import path

from mainapp import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name="homepage"),
    path('create', views.create_titles, name="create"),
    path('movie/<int:pk>', views.MovieView.as_view(), name="details"),
    path('add', views.ContactFormView.as_view(), name='add')
]

