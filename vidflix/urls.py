from django.contrib import admin
from django.urls import path, include
from api.models import MovieResource, GenreResource

movie_resource = MovieResource
genre_resource = GenreResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rental.urls')),
    path('api/', include(movie_resource.urls)),
    path('api/', include(genre_resource.urls))
]

