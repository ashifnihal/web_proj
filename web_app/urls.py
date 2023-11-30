from django.urls import path, re_path
from django.conf.urls import url
from . import views
urlpatterns = [
    url('home/', views.get_cars),
    url('car_models/', views.get_carmodels),
    url('car_brands/', views.get_carbrands),
    url('car_types/', views.get_cartypes),
    url('car_input_data/', views.carInputView),
    url('car_brand_input_data/', views.add_car_brands),
    url(r'^car_overview_input_data/', views.add_car_overview),
    url('new_cars/', views.show_new_cars),
    url('pre_owned_cars', views.show_pre_owned_cars),
    re_path(r'^cars/(?P<bname>[\w-]+)/(?P<new_or_pre_owned>[\w-]+)/$', views.get_cars_by_brand),
    url(r'^car/(?P<car_model>\w+)/$', views.CarOverviewView.as_view()),
]