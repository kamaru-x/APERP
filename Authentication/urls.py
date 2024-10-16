from django.urls import path
from Authentication import views

urlpatterns = [
    path('sign-in',views.sign_in,name='sign-in'),
    path('sign-out',views.signout,name='sign-out'),

    path('staffs/',views.staffs,name='staffs'),
    path('staff/add/',views.add_staff,name='staff-add'),
    path('staff/edit/<int:id>/',views.edit_staff,name='staff-edit'),
    path('staff/delete/<int:id>/',views.delete_staff,name='staff-delete'),
]