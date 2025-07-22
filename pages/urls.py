from django.urls import path
from pages.views import mainpage, company

urlpatterns = [
    path('', mainpage),
    path('company/', company),

]