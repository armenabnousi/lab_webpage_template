from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'minglab-home'),
	path('software/', views.software, name = 'minglab-software'),
	path('publications/', views.publications, name = 'minglab-publications'),
	path('people/', views.people, name = 'minglab-people'),
	path('research/', views.research, name = 'minglab-research'),
	path('contact/', views.contact, name = 'minglab-contact'),
]
