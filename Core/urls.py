from django.urls import path
from Core import views

urlpatterns = [
    path('source/',views.sources,name='source'),
    path('source/add/',views.add_source,name='source-add'),
    path('source/edit/<int:id>/',views.edit_source,name='source-edit'),
    path('source/delete/<int:id>/',views.delete_source,name='source-delete'),

    path('groups/',views.groups,name='groups'),
    path('group/add/',views.add_group,name='group-add'),
    path('group/edit/<int:id>/',views.edit_group,name='group-edit'),
    path('group/delete/<int:id>/',views.delete_group,name='group-delete'),

    path('leads/',views.leads,name='leads'),
    path('lead/add/',views.add_lead,name='add-lead'),
    path('lead/view/<int:id>/',views.view_lead,name='view-lead'),
    path('lead/edit/<int:id>/',views.edit_lead,name='edit-lead'),
    path('lead/delete/<int:id>/',views.delete_lead,name='delete-lead'),
    path('lead/cancel/<int:id>/',views.cancel_lead,name='cancel-lead'),

    path('followup/add/<int:id>/',views.add_followup,name='add-followup'),
    path('followup/delete/<int:id>/',views.delete_followup,name='delete-followup'),

    path('bookings/',views.bookings,name='bookings'),
    path('booking/add/<int:id>/',views.add_booking,name='add-booking'),
    path('booking/edit/<int:id>/',views.edit_booking,name='edit-booking'),
]