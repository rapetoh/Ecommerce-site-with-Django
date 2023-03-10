from django.urls import path, include
from app import views
from .views import CategoryView
from ec import settings
from django.conf.urls.static import static



urlpatterns=[
    path('main/',views.indexx),
    path('home/',views.home),
    path('category/<slug:val>',views.CategoryView.as_view(),name='ctg'),
    path('productDet/',views.ProductDetail.as_view(),name='pdt')
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

