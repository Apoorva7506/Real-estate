from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index,name='index'),
    path("realtors/<int:r_id>", views.realtors, name='realtors'),
    path("browse/", views.browse, name='browse'),
    path('<int:h_id>', views.infoh, name='infoh'),
    path('search/', views.search, name='search'),
    path('about/',views.about,name='about'),
   


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
