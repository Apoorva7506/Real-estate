from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.core.mail import send_mail

def contact(request):
    if request.method=='POST':
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']

        contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)

        contact.save()

        send_mail('Property Listing Enquiry',
        'There Has been an inquiry for'+listing+'. Check it out',
        'apoorvaflame@gmail.com',
        [realtor_email,'oregairu9930@gmail.com'],
        fail_silently=False)

        return HttpResponse("Your request has been submitted")
        
