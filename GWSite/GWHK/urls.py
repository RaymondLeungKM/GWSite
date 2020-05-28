from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('companyInfo', views.companyInfo, name='companyInfo'),
    path('visionValues', views.visionValues, name='visionValues'),
    path('companyCulture', views.companyCulture, name='companyCulture'),
    path('companyNews/<int:pk>/', views.companyNewsDetail.as_view(), name='companyNewsDetail'),
    path('companyNews', views.companyNewsList.as_view(), name='companyNewsList'),
    path('pressRelease', views.pressReleaseList.as_view(), name='pressReleaseList'),
    path('pressRelease/<int:pk>/', views.pressReleaseDetail.as_view(), name='pressReleaseDetail'),    
    path('jobOpenings', views.jobOpeningsList.as_view(), name='jobOpeningsList'),
    path('contactus', views.contactUs, name='contactUs'),
    path('stockInvest', views.stockInvest, name='stockInvest'),
    path('assetMgt', views.assetMgt, name='assetMgt'),     
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
