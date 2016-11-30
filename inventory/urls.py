from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^add_product$', views.add_producttype, name='add_product'),
    url(r'^add_product_model$', views.add_productmodel, name='add_product_model'),
    url(r'^add_product_supplier$', views.add_supplier, name='add_supplier'),
    url(r'^add_inventory$', views.add_inventory, name='add_inventory'),

]
