from django.shortcuts import render
from .forms import DonationForm,VolunteerForm
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def causes(request):
    return render(request, 'causes.html')

def donate(request):
    return render(request, 'donate.html')

def contact(request):
    return render(request, 'contact.html')

def volunteer(request):
    return render(request, 'volunteer.html')

def result(request):
    return render(request, 'result.html')

def donate(request):
    if request.method == "POST":
        form = DonationForm(request.POST)

        if form.is_valid():
            return render(request, "result.html")
        else:
            print(form.errors)   # Check the terminal

    else:
        form = DonationForm()

    return render(request, "donate.html", {"form": form})

def volunteer(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            return render(request, "result.html")
    else:
        form = VolunteerForm()

    return render(request, "volunteer.html", {"form": form})