from django.urls import path
from .  import views 

urlpatterns = [
    path('',views.index,name='index') ,
    path('<int:number>',views.calc_tax,name='calculate_tax'),
    path('tax_rate',views.tax_rate,name='tax')

]
