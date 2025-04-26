from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('match/',views.compare_image, name='match'),
    path('find/',views.find, name='find'),    

    # path('alldata/',views.alldata, name='alldata'),
    path('search/', views.search_by_field, name='search_by_field'),
    path('search-from/', views.search_form, name='search_form'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



