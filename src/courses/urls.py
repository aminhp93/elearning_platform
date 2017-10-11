from django.conf.urls import url, include

from . import views

urlpatterns = [
	
	# COURSE
	url(r'^$', views.CourseListView.as_view(), name='course_list'),
	url(r'^create/$', views.CourseCreateView.as_view(), name='course_create'),
	url(r'^(?P<slug>[\w-]+)/$', views.CourseDetailView.as_view(), name='course_detail'),
	url(r'^(?P<slug>[\w-]+)/update/$', views.CourseUpdateView.as_view(), name='course_update'),
	url(r'^(?P<slug>[\w-]+)/delete/$', views.CourseDeleteView.as_view(), name='course_delete'),


]

