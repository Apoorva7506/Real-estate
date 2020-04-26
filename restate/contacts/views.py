from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.core.mail import send_mail
import os

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
        'There Has been an inquiry for '+listing+' by ' +name+" \nTheir email is: "+email+ '.\n Check it out'+"\nMessage: \n"+message,
        os.environ.get('user_email'),
        [realtor_email],
        fail_silently=False)

        return HttpResponse("<h1><center>Your request has been submitted<br>"+'<a href="/">Click to go back to Index</a></center></h1>')
        
