from django.urls import path
from Core import views

urlpatterns = [
    path('leads/',views.leads,name='leads'),
    path('lead/add/',views.add_lead,name='add-lead'),
    path('lead/view/<int:lid>/',views.view_lead,name='view-lead'),
    path('lead/edit/<int:lid>/',views.edit_lead,name='edit-lead'),
    path('lead/delete/<int:lid>/',views.delete_lead,name='delete-lead'),

    path('followup/add/<int:lid>/',views.add_followup,name='add-followup'),
    path('followup/delete/<int:fid>/',views.delete_followup,name='delete-followup'),
]