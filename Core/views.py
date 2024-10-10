from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Core.models import Department, Lead, FollowUp

# Create your views here.

@login_required
def leads(request):
    leads = Lead.objects.all()
    pending_leads = Lead.objects.filter(status='pending')

    context = {
        'main' : 'leads',
        'leads' : leads,
        'pending_leads' : pending_leads
    }
    return render(request,'leads/leads.html',context)

@login_required
def add_lead(request):
    departments = Department.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        type = request.POST.get('type')
        district = request.POST.get('district')
        sub_district = request.POST.get('sub_district')
        departments = request.POST.getlist('departments[]')
        students = request.POST.get('students')
        teachers = request.POST.get('teachers')
        contact = request.POST.get('contact')
        number = request.POST.get('number')
        info = request.POST.get('info')

        try:
            lead = Lead.objects.create(
                name=name,location=location,type=type,district=district,sub_district=sub_district,
                students=students,teachers=teachers,info=info,contact_name=contact,contact_number=number
            )

            lead.departments.set(departments)

            messages.success(request, 'New lead created successfully ... !')
            return redirect('leads')

        except Exception as exception:
            messages.warning(request,str(exception))
            return redirect('add-lead')

    context = {
        'main' : 'leads',
        'departments' : departments
    }

    return render(request,'leads/lead-add.html',context)

@login_required
def view_lead(request,lid):
    departments = Department.objects.all()
    lead = Lead.objects.get(id=lid)
    followups = FollowUp.objects.filter(lead=lead).order_by('-id')
    context = {
        'main' : 'leads',
        'departments' : departments,
        'lead' : lead,
        'followups' : followups
    }
    return render(request,'leads/lead-view.html',context)

@login_required
def edit_lead(request,lid):
    departments = Department.objects.all()
    lead = Lead.objects.get(id=lid)

    if request.method == 'POST':
        deps = request.POST.getlist('departments[]')
        lead.name = request.POST.get('name')
        lead.location = request.POST.get('location')
        lead.type = request.POST.get('type')
        lead.district = request.POST.get('district')
        lead.sub_district = request.POST.get('sub_district')
        lead.students = request.POST.get('students')
        lead.teachers = request.POST.get('teachers')
        lead.contact_name = request.POST.get('contact')
        lead.contact_number = request.POST.get('number')
        lead.info = request.POST.get('info')

        lead.departments.set(deps)

        try:
            lead.save()
            messages.success(request,'Lead details edited successfully ... !')
            return redirect('leads')
        except Exception as exception:
            messages.warning(request,str(exception))
            return redirect('edit-lead',lid=lead.id)


    context = {
        'main' : 'leads',
        'departments' : departments,
        'lead' : lead
    }
    return render(request,'leads/lead-edit.html',context)

@login_required
def delete_lead(request,lid):
    lead = Lead.objects.get(id=lid)
    lead.delete()
    messages.warning(request ,'Lead deleted successfully ... !')
    return redirect('leads')

@login_required
def add_followup(request,lid):
    lead = Lead.objects.get(id=lid)

    if request.method == 'POST':
        title = request.POST.get('title')
        details = request.POST.get('details')

        try:
            FollowUp.objects.create(lead=lead,title=title,details=details)
            messages.success(request,'follow up added successfully ... !')

        except Exception as exception:
            messages.warning(request,str(exception))

    return redirect('view-lead',lid=lead.id)

@login_required
def delete_followup(request,fid):
    followup = FollowUp.objects.get(id=fid)
    lead = followup.lead
    followup.delete()
    return redirect('view-lead',lid=lead.id)