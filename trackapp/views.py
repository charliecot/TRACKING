from django.shortcuts import render, get_object_or_404,redirect
from .models import Package,Subscriber,Contact
from .forms import TrackingForm
from django.contrib import messages


# Create your views here.

def home(request):
    package = None
    form = TrackingForm(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            tracking_id = form.cleaned_data['tracking_id']
            try:
                package =Package.objects.get(tracking_id=tracking_id)
            except Package.DoesNotExist:
                 messages.error(request, "Tracking ID not found. Please check and try again.")    
            return render(request, 'index.html', {
                'tracking_info': package,
                'form': form  # keep the form visible
            })
    else:
        form = TrackingForm() 

    return render(request, 'index.html', {'form': form})       


def track(request):
    package=None
    form = TrackingForm(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            tracking_id = form.cleaned_data['tracking_id']
            try:
                package =Package.objects.get(tracking_id=tracking_id)
            except Package.DoesNotExist:
                messages.error(request, "Tracking ID not found. Please check and try again.")
                  
            return render(request, 'track.html', {
                'tracking_info': package,
                'form': form  #  keep the form visible
            })
    else:
        form = TrackingForm() 

    return render(request, 'track.html', {'form': form}) 




def subscribe(request):
    form = TrackingForm()  # always create the form
    if request.method == "POST":
        email = request.POST.get("email")
        if Subscriber.objects.filter(email=email).exists():
            messages.warning(request, "This email is already subscribed.")
        else:
            Subscriber.objects.create(email=email)
            messages.success(request, "You have successfully subscribed!")

    return render(request, "index.html", {"form": form})





def Contact_view(request):
    form = TrackingForm()  # always create the form
    if request.method == "POST":
      first_name= request.POST.get("firstname")  
      last_name= request.POST.get("lastname") 
      email = request.POST.get("email")
      message= request.POST.get("message")
      
      if Contact.objects.filter(email=email).exists():
            messages.warning(request, "This email already exits.")
      else:
            Contact.objects.create(first_name=first_name, last_name=last_name,email=email,message=message)
            messages.success(request, "Your message has sent successfull!")   
            
    return render(request, "index.html", {"form": form})