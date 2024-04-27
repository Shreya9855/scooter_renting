from django.shortcuts import render
from .forms import registerScooterForm
from .models import Scooter,User

# Create your views here.
def register_scooter(request):
    print(request.method)
    if request.method == "POST":
        form = registerScooterForm(request.POST, request.FILES)
        for field in form:
            print("Field Error:", field.name,  field.errors)
        print(form.is_valid())
        if form.is_valid():
            model = form.cleaned_data['model']
            image = form.cleaned_data['image']
            color = form.cleaned_data['color']
            rate_per_hour = form.cleaned_data['rate_per_hour']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            vendor_id = User.objects.get(username='John123')
            scooter_details = Scooter.objects.create(
                model = model,
                image = image,
                color = color,
                rate_per_hour = rate_per_hour,
                start_time = start_time,
                end_time = end_time,
                is_active = True,
                vendor_id = vendor_id
                
            )
            print(scooter_details)
            return render(request, "scooter_register.html", {'scooter_details': scooter_details})
    else:
        form = registerScooterForm()
    return render(request, "scooter_register.html", {'form': form})

def scooter_rent(request):
    return render(request,"scooter_renting.html")