from django.shortcuts import render, redirect
from .models import Device
from .forms import DeviceForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User



def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email')
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'home/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'home/register.html')

        user = User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')

    return render(request, 'home/register.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.GET.get('next', 'home')  # Default to 'home'

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'home/login.html')


def home_view(request):
    return render(request, 'home/home.html')


def add_device(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        device_type = request.POST.get('device_type', 'Other')
        if name:
            Device.objects.create(name=name, device_type=device_type)
        return redirect('dashboard')
    return render(request, 'add_device.html') 

def about_view(request):
    return render(request, 'home/about.html')


def dashboard_view(request):
    # Pass any necessary context to the template if needed
    devices = Device.objects.all()  # Example if you're using the 'Device' model
    return render(request, 'home/dashboard.html', {'devices': devices})

    if request.method == 'POST':
        device_id = request.POST.get('device_id')
        device = get_object_or_404(Device, id=device_id)
        device.is_on = not device.is_on
        device.save()
        return redirect('dashboard')

    return render(request, 'dashboard.html', {'devices': devices})


def toggle_device(request, device_id):
    device = Device.objects.get(id=device_id)
    device.is_on = not device.is_on   # ✅ Use the correct field name
    device.save()
    return redirect('dashboard')


def delete_device(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    device.delete()
    return redirect('dashboard')



def dashboard(request):
    devices = Device.objects.all()

    if request.method == "POST":
        device_id = request.POST.get("device_id")
        device = Device.objects.get(id=device_id)
        device.is_on = not device.is_on
        device.save()
        return redirect('dashboard')

    return render(request, 'home/dashboard.html', {'devices': devices})

def add_device(request):
    form = DeviceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'home/add_device.html', {'form': form})
