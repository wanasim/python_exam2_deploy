from django.shortcuts import render, redirect
from .models import Travel
from django.contrib import messages
from ..loginReg.models import User

# Create your views here.
def index(request):
    if 'id' in request.session:
        name = User.objects.get(id=request.session['id'])
        current_user = Travel.objects.filter(user_of_travel__id=request.session['id'])
        not_user = Travel.objects.exclude(user_of_travel__id=request.session['id'])
        travels = Travel.objects.all()

        context={
            "items": travels,
            "current_user": current_user,
            "not_user":not_user,
            "name": name,
        }
        return render(request, 'belt_app/index.html', context)
    return redirect('loginReg:index')

def addTravel(request): #routes to addItem html page
    if 'id' in request.session:
        return render(request, 'belt_app/addTravel.html')
    return redirect('loginReg:index')


def createTravel(request): #creates item
    #check for user session
    if 'id' in request.session:
        valid, response, info = Travel.objects.createTravel(request.POST)

        if not valid:
            for error in response:
                messages.error(request, error)
            return redirect('beltapp:addTravel')
        return redirect('beltapp:index')
    return redirect('loginReg:index')

def travelInfo(request, id):
    if 'id' in request.session:
        travel_info = Travel.objects.get(id=id)

        context = {
            "travel_info" : travel_info,
        }
        return render(request, 'belt_app/travelInfo.html', context)
    return redirect('loginReg:index')

def join(request, id):
    if 'id' in request.session:
        user_id = request.session['id']
        add_travel = Travel.objects.join(user_id, id)

        return redirect('beltapp:index')
    return redirect('loginReg:index')

def delete(request, id):
    if 'id' in request.session:
        user_id = request.session['id']
        delete_travel = Travel.objects.delete(user_id, id)

        return redirect('beltapp:index')
    return redirect('loginReg:index')
