from django.urls import path
from Core import views

urlpatterns = [
    path('leads/',views.leads,name='leads'),
    path('lead/add/',views.add_lead,name='add-lead'),
    path('lead/view/<int:lid>/',views.view_lead,name='view-lead'),
    path('lead/edit/<int:lid>/',views.edit_lead,name='edit-lead'),
    path('lead/delete/<int:lid>/',views.delete_lead,name='delete-lead'),
    path('lead/cancel/<int:lid>/',views.cancel_lead,name='cancel-lead'),

    path('followup/add/<int:lid>/',views.add_followup,name='add-followup'),
    path('followup/delete/<int:fid>/',views.delete_followup,name='delete-followup'),

    path('bookings/',views.bookings,name='bookings'),
    path('booking/add/<int:lid>/',views.add_booking,name='add-booking'),
    path('booking/edit/<int:bid>/',views.edit_booking,name='edit-booking'),
]