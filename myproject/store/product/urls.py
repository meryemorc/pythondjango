from django.urls import path
from . import views


#http://127.0.0.1:8000/   => index
#http://127.0.0.1:8000/ürünler  => index
#http://127.0.0.1:8000/telefon    => Phone
#http://127.0.0.1:8000/bilgisayar   => Computer
#http://127.0.0.1:8000/aksesuar  => Accesory

urlpatterns = [

    path('', views.index ),
    path('<urun_id>',views.details),
    path('<int:category_id>', views.getProductByCategoryId),
    path('<str:category_name>', views.getProductByCategory, name ='product_by_category'),
    

]