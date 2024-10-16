from django.shortcuts import render,redirect
from Authentication.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Authentication.models import Group

# Create your views here.

#------------------------------------------------- SIGN IN ---------------------------------------------------#

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'incorrect username or password')
            return redirect('.')
    return render(request,'auth/sign-in.html')

#----------------------------------------------CHANGE PASSWORD -----------------------------------------------#

@login_required
def changepassword(request):
    user = request.user
    if request.method == 'POST':
        currentPassword = request.POST.get('currentPassword')
        newPassword = request.POST.get('newPassword')
        confirmPassword = request.POST.get('confirmPassword')

        if not user.check_password(currentPassword):
            messages.error(request, 'Incorrect current password')
            return redirect('change-password')
        elif newPassword != confirmPassword:
            messages.error(request,'Password and confirm password does not match try again')
            return redirect('change-password')
        else:
            user.set_password(confirmPassword)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request,'Password changed login again')
            return redirect('dashboard')

    return render(request,'auth/change-password.html')

#------------------------------------------------- SIGN OUT --------------------------------------------------#

@login_required
def signout(request):
    logout(request)
    return redirect('sign-in')

#------------------------------------------------- STAFFS --------------------------------------------------#

@login_required
def staffs(request):
    staffs = User.objects.exclude(is_superuser=True)
    context = {
        'main' : 'staffs',
        'staffs' : staffs
    }
    return render(request,'staffs/staffs.html',context)

@login_required
def add_staff(request):
    groups = Group.objects.all()

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        group = request.POST.get('group')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            group = Group.objects.get(id=group)
            user = User.objects.create(
                username=username,first_name=first_name,last_name=last_name,mobile=mobile,email=email,group=group
            )
            user.set_password(password)

            messages.success(request,'Staff created successfully ... !')
            return redirect('staffs')

        except Exception as exception:
            messages.warning(request,str(exception))
            return redirect('staffs')

    context = {
        'main' : 'staffs',
        'groups' : groups
    }
    return render(request,'staffs/staff-add.html',context)

@login_required
def edit_staff(request,id):
    groups = Group.objects.all()
    staff = User.objects.get(id=id)

    if request.method == 'POST':
        group = request.POST.get('group')
        staff.first_name = request.POST.get('first_name')
        staff.last_name = request.POST.get('last_name')
        staff.mobile = request.POST.get('mobile')
        staff.email = request.POST.get('email')

        try:
            group = Group.objects.get(id=group)
            staff.save()

            messages.success(request,'Staff details changed successfully ... !')
            return redirect('staffs')

        except Exception as exception:
            messages.warning(request,str(exception))
            return redirect('staff-edit',id=staff.id)

    context = {
        'main' : 'staffs',
        'groups' : groups,
        'staff' : staff
    }
    return render(request,'staffs/staff-edit.html',context)

@login_required
def delete_staff(request,id):
    staff = User.objects.get(id=id)
    staff.is_active = False
    staff.save()

    messages.error(request,'Staff deleted successfully ... !')
    return redirect('staffs')