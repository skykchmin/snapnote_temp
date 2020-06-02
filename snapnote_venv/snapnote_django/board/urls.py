from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('list/', views.board_list),
    path('upload/', views.upload),
    path('files/', views.file_list, name='file_list'),
    path('files/upload/', views.upload_file, name='upload_file'),
    # path('fileupload/', views.FileFieldView.as_view(), name='file_upload'),
    # path('files/upload/', views.UploadView.as_view(), name='upload_file'),
    # path('files/basic-upload/', views.BasicUploadView.as_view(), name='basic_upload'),
    # path('index/', views.FileFieldView.as_view()),
    url(r'/$', views.UploadView.as_view()),
    # path('form/', views.UploadView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)