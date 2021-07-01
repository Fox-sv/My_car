from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('add_date_oil/', views.add_date_oil, name='add_date_oil'),
    path('add_date_insurance/', views.add_date_insurance, name='add_date_insurance'),
    path('add_date_inspection/', views.add_date_inspection, name='add_date_inspection'),
    path('all_date_oil/', views.all_date_oil, name='all_date_oil'),
    path('all_date_insurance/', views.all_date_insurance, name='all_date_insurance'),
    path('all_date_inspection/', views.all_date_inspection, name='all_date_inspection'),
    path('delete_date_oil/<int:oil_id>', views.delete_date_oil, name='delete_date_oil'),
    path('update_date_oil/<int:oil_id>/', views.update_date_oil, name='update_date_oil'),
    path('delete_date_inspection/<int:inspection_id>', views.delete_date_inspection, name='delete_date_inspection'),
    path('update_date_inspection/<int:inspection_id>/', views.update_date_inspection, name='update_date_inspection'),
    path('delete_date_insurance/<int:insurance_id>', views.delete_date_insurance, name='delete_date_insurance'),
    path('update_date_insurance/<int:insurance_id>/', views.update_date_insurance, name='update_date_insurance'),
    path('about_car/', views.about_car, name='about_car'),
    path('all_expenses/', views.expenses_car, name='expenses_car'),
    path('expenses/<int:expenses_id>', views.expenses_details, name='expenses_details'),
    path('delete/<int:expenses_id>', views.delete_expenses, name='expenses_delete'),
    path('expenses/<int:expenses_id>/', views.update_expenses, name='update_expenses'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
