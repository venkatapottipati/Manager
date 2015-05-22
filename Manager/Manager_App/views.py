from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response

from Manager_App.models import Contact_List

def AddContact(request):
    if request.method == "POST":
    	name = request.POST.get("Name")
    	PhoneNumber= request.POST.get("Phone")
    	emailAddress = request.POST.get("email")
    	
    	Contact_List.objects.create(
                                Fullname=name, PhoneNumber=PhoneNumber, emailAddress=emailAddress
			      )
    	return HttpResponseRedirect("/list/")
    else:
 	return render_to_response("add_form.html", {}, RequestContext(request))

def Listing(request):
    data = Contact_List.objects.all()
    return render_to_response("list.html", {"data":data}, RequestContext(request))


def Delete(request, pid):
    Contact_List.objects.get(id=pid).delete()
    return HttpResponseRedirect("/list/")





