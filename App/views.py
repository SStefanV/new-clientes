from django.shortcuts import render

# My Imports
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from App.models import Patient
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

# Function to render the frontend page.


def frontend(request):
    return render(request, 'frontend.html')


# ----------BACKEND SECTION--------------|


# Function to render the backend page.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def backend(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        all_patients_list = Patient.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) | Q(email__icontains=q) | Q(
                age__icontains=q) | Q(gender__icontains=q) | Q(note__icontains=q)
        ).order_by('-created_at')

    else:
        all_patients_list = Patient.objects.all().order_by('-created_at')

    paginator = Paginator(all_patients_list, 10)
    page = request.GET.get('page')
    all_patients = paginator.get_page(page)

    return render(request, 'backend.html', {"patients": all_patients})


# Function to insert new client
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def add_patient(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') or request.POST.get('note'):
            patient = Patient()
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request, "Client added successfully")
            return HttpResponseRedirect('/backend')
    else:
        return render(request, 'add.html')


# --------Function to access the client individually---------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if patient != None:
        return render(request, 'edit.html', {'patient': patient})

# --------Function to edit a client -------------------------------


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def edit_patient(request):
    if request.method == 'POST':
        patient = Patient.objects.get(id=request.POST.get('id'))
        if patient != None:
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request, "Cliente modificado con exito!!")
            return HttpResponseRedirect('/backend')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def delete_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    patient.delete()
    messages.success(request, "El cliente ha sido borrado!")
    return HttpResponseRedirect('/backend')
