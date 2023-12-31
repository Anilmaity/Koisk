from django.contrib import admin
from django.urls import path
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('<str:PromptInput>', views.chatgptprompt, name='Chatgpt'),
                  path('', views.chatgpthtml, name='Chatgpt'),
                  path('Cost', views.usage, name='Chatgpt'),
                  path('/imgtotxt/<str:PromptInput>', views.dall_e, name='Chatgpt'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)