from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'labapp-home'),
	path('software/', views.software, name = 'labapp-software'),
	path('publications/', views.publications, name = 'labapp-publications'),
	path('people/', views.people, name = 'labapp-people'),
	path('research/', views.research, name = 'labapp-research'),
	path('contact/', views.contact, name = 'labapp-contact'),
]
