from django.urls import path, reverse_lazy#, include
from . import views

app_name='birds'
urlpatterns = [
        path('', views.BirdMain.as_view(), name='bird_main'),
        path('photos/', views.BirdPhotoView.as_view(), name='bird_photos'),
        path('photos/submit/', views.BirdPhotoSubmit.as_view(success_url=reverse_lazy('bird_main')), 
            name='bird_submit'),
        path('photos/delete/<int:pk>', views.BirdPhotoSubmit.as_view(success_url=reverse_lazy('bird_main')), 
            name='bird_submit'),

        #Adding extra tools
        #path('captcha/', include('captcha.urls')),

    ]
