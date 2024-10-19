from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Authentication.models import Source, Group, User
from Core.models import Department, Lead, FollowUp, Booking
from django.http import JsonResponse
from datetime import datetime
today = datetime.now().date()

# Create your views here.

@login_required
def sources(request):
    sources = Source.objects.all()
    context = {
        'main' : 'source',
        'sources' : sources
    }
    return render(request,'source/source.html',context)

@login_required
def add_source(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Source.objects.create(name=name)
        messages.success(request,'Source created successfully ... !')
        return redirect('source')
    context = {
        'main' : 'source',
    }
    return render(request,'source/source-add.html',context)

@login_required
def edit_source(request,id):
    source = Source.objects.get(id=id)

    if request.method == 'POST':
        source.name = request.POST.get('name')
        source.save()
        messages.success(request,'Source edited successfully ... !')
        return redirect('source')

    context = {
        'main' : 'source',
        'source' : source
    }
    return render(request,'source/source-edit.html',context)

@login_required
def delete_source(request,id):
    source = Source.objects.get(id=id)
    source.delete()

    messages.warning(request,'Source deleted successfully ... !')

    return redirect('source')

@login_required
def groups(request):
    groups = Group.objects.all()
    context = {
        'main' : 'groups',
        'groups' : groups
    }
    return render(request,'group/groups.html',context)

@login_required
def add_group(request):
    if request.method == 'POST':
        source = Source.objects.first()
        name = request.POST.get('name')
        Group.objects.create(name=name,source=source)
        messages.success(request,'Group created successfully ... !')
        return redirect('groups')
    context = {
        'main' : 'groups',
    }
    return render(request,'group/group-add.html',context)

@login_required
def edit_group(request,id):
    group = Group.objects.get(id=id)

    if request.method == 'POST':
        group.name = request.POST.get('name')
        group.save()
        messages.success(request,'Group edited successfully ... !')
        return redirect('groups')

    context = {
        'main' : 'groups',
        'group' : group
    }
    return render(request,'group/group-edit.html',context)

@login_required
def delete_group(request,id):
    group = Group.objects.get(id=id)
    group.delete()

    messages.warning(request,'Group deleted successfully ... !')

    return redirect('groups')

@login_required
def leads(request):
    leads = Lead.objects.all().order_by('-id')
    pending_leads = Lead.objects.filter(status='pending')
    converted_leads = Lead.objects.filter(status='converted')
    failed_leads = Lead.objects.filter(status='failed')

    context = {
        'main' : 'leads',
        'leads' : leads,
        'pending_leads' : pending_leads,
        'converted_leads' : converted_leads,
        'failed_leads' : failed_leads
    }
    return render(request,'leads/leads.html',context)

@login_required
def add_lead(request):
    departments = Department.objects.all()
    sources = Source.objects.all()
    groups = Group.objects.all()
    staffs = User.objects.exclude(is_superuser=True)

    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        type = request.POST.get('type')
        district = request.POST.get('district')
        sub_district = request.POST.get('sub_district')
        departments = request.POST.getlist('departments[]')
        students = request.POST.get('students')
        teachers = request.POST.get('teachers')
        primary_name = request.POST.get('primary_name')
        primary_number = request.POST.get('primary_number')
        secondary_name = request.POST.get('secondary_name')
        secondary_number = request.POST.get('secondary_number')
        source = request.POST.get('source')
        group = request.POST.get('group')
        staff = request.POST.get('staff')
        info = request.POST.get('info')

        try:
            if source:
                source = Source.objects.get(id=source)
            else:
                source = None

            if group:
                group = Group.objects.get(id=group)
            else:
                group = None

            if staff:
                staff = User.objects.get(id=staff)
            else:
                staff = None

            lead = Lead.objects.create(
                name=name,location=location,type=type,district=district,sub_district=sub_district,
                students=students,teachers=teachers,info=info,primary_name=primary_name,primary_number=primary_number,
                secondary_name=secondary_name,secondary_number=secondary_number,source=source,group=group,staff=staff
            )

            lead.departments.set(departments)

            messages.success(request, 'New lead created successfully ... !')
            return redirect('leads')

        except Exception as exception:
            messages.warning(request,str(exception))
            return redirect('add-lead')

    context = {
        'main' : 'leads',
        'departments' : departments,
        'sources' : sources,
        'groups' : groups,
        'staffs' : staffs
    }

    return render(request,'leads/lead-add.html',context)

@login_required
def view_lead(request,id):
    departments = Department.objects.all()
    lead = Lead.objects.get(id=id)
    followups = FollowUp.objects.filter(lead=lead).order_by('-id')
    followup = FollowUp.objects.filter(lead=lead).order_by('id').last()
    context = {
        'main' : 'leads',
        'departments' : departments,
        'lead' : lead,
        'followups' : followups,
        'followup' : followup
    }
    return render(request,'leads/lead-view.html',context)

@login_required
def edit_lead(request,id):
    departments = Department.objects.all()
    lead = Lead.objects.get(id=id)
    sources = Source.objects.all()
    groups = Group.objects.all()
    staffs = User.objects.exclude(is_superuser=True)

    if request.method == 'POST':
        deps = request.POST.getlist('departments[]')
        lead.name = request.POST.get('name')
        lead.location = request.POST.get('location')
        lead.type = request.POST.get('type')
        lead.district = request.POST.get('district')
        lead.sub_district = request.POST.get('sub_district')
        lead.students = request.POST.get('students')
        lead.teachers = request.POST.get('teachers')
        lead.primary_name = request.POST.get('primary_name')
        lead.primary_number = request.POST.get('primary_number')
        lead.secondary_name = request.POST.get('secondary_name')
        lead.secondary_number = request.POST.get('secondary_number')
        lead.info = request.POST.get('info')

        source = request.POST.get('source')
        group = request.POST.get('group')
        staff = request.POST.get('staff')

        lead.departments.set(deps)

        try:
            if source:
                source = Source.objects.get(id=source)
            else:
                source = None

            if group:
                group = Group.objects.get(id=group)
            else:
                group = None

            if staff:
                staff = User.objects.get(id=staff)
            else:
                staff = None

            lead.source = source

            if source.id == 1:
                lead.group = group
                lead.staff = staff
            else:
                lead.group = None
                lead.staff = None

            lead.save()
            messages.success(request,'Lead details edited successfully ... !')
            return redirect('leads')
        except Exception as exception:
            messages.warning(request,str(exception))
            return redirect('edit-lead',id=lead.id)


    context = {
        'main' : 'leads',
        'departments' : departments,
        'lead' : lead,
        'sources' : sources,
        'groups' : groups,
        'staffs' : staffs
    }
    return render(request,'leads/lead-edit.html',context)

@login_required
def delete_lead(request,id):
    lead = Lead.objects.get(id=id)
    lead.delete()
    messages.warning(request ,'Lead deleted successfully ... !')
    return redirect('leads')

@login_required
def cancel_lead(request,id):
    lead = Lead.objects.get(id=id)
    lead.status = 'FAILED'
    lead.save()
    messages.warning(request,'Marked lead as failed lead ... !')
    return redirect('leads')

def update_lead_type(request,id):
    if request.method == 'POST':
        lead_type = request.POST.get('lead_type')

        lead = Lead.objects.get(id=id)
        lead.lead_type = lead_type
        lead.save()

        return JsonResponse({'status': 'success', 'lead_type': lead_type})

    return JsonResponse({'status': 'warning'}, status=400)

@login_required
def add_followup(request,id):
    lead = Lead.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        details = request.POST.get('details')
        next_date = request.POST.get('next-date')

        try:
            FollowUp.objects.create(lead=lead,title=title,details=details,next_date=next_date)
            messages.success(request,'follow up added successfully ... !')

        except Exception as exception:
            messages.warning(request,str(exception))

    return redirect('view-lead',id=lead.id)

@login_required
def delete_followup(request,id):
    followup = FollowUp.objects.get(id=id)
    lead = followup.lead
    followup.delete()
    return redirect('view-lead',id=lead.id)

@login_required
def bookings(request):
    today_bookings = Booking.objects.filter(date=today)
    other_bookings = Booking.objects.exclude(date=today).order_by('date')
    context = {
        'main' : 'booking',
        'today_bookings' : today_bookings,
        'other_bookings' : other_bookings
    }
    return render(request,'booking/bookings.html',context)

@login_required
def add_booking(request,id):
    lead = Lead.objects.get(id=id)

    if request.method == 'POST':
        students = request.POST.get('students')
        teachers = request.POST.get('teachers')
        date = request.POST.get('date')
        arrival = request.POST.get('arrival')
        leaving = request.POST.get('leaving')
        food = request.POST.get('food')
        info = request.POST.get('info')

        lead.status = 'CONVERTED'
        lead.save()

        try:
            Booking.objects.create(
                lead=lead,students=students,teachers=teachers,visit_date=date,time_arrival=arrival,
                time_leave=leaving,food=food,info=info
            )
            messages.success(request,'New booking added ... !')
            return redirect('bookings')

        except Exception as exception:
            messages.warning(request,str(exception))
            return redirect('view-lead',id=lead.id)

@login_required
def edit_booking(request,id):
    booking = Booking.objects.get(id=id)

    if request.method == 'POST':
        booking.students = request.POST.get('students')
        booking.teachers = request.POST.get('teachers')
        booking.date = request.POST.get('date')
        booking.time_arrival = request.POST.get('arrival')
        booking.time_leave = request.POST.get('leaving')
        booking.food = request.POST.get('food')
        booking.info = request.POST.get('info')

        try:
            booking.save()
            messages.success(request,'Booking Details Edited')
            return redirect('bookings')
        except Exception as exception:
            messages.warning(request,str(exception))
            return redirect('edit-booking',id=booking.id)

    context = {
        'main' : 'booking',
        'booking' : booking
    }
    return render(request,'booking/booking-edit.html',context)

def filter_staff(request):
    group_id = request.GET.get('group_id')

    if group_id:
        staff_list = User.objects.filter(group_id=group_id)
    else:
        staff_list = User.objects.none()

    staff_data = [
        {'id': staff.id, 'name': f"{staff.first_name} {staff.last_name}"}
        for staff in staff_list
    ]

    return JsonResponse({'staff': staff_data})

@login_required
def booking_details(request,id):
    booking = Booking.objects.get(id=id)
    context = {
        'main' : 'booking',
        'booking' : booking
    }
    return render(request,'booking/booking-details.html',context)

@login_required
def print_booking(request):
    bookings = Booking.objects.filter(date=today)
    context = {
        'bookings' : bookings,
        'today' : today
    }
    return render(request,'booking/booking-print.html',context)