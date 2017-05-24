from __future__ import unicode_literals
from django.db import models
from ..loginReg.models import User
from datetime import datetime, date

# Create your models here.
class TravelManager(models.Manager):
    def createTravel(request, data):
        error=[]
        if not len(data['destination']):
            error.append("Please enter a destination")
        if not len(data['description']):
            error.append("Please enter a description")
        if not len(data['date_from']):
            error.append("Please enter a Travel Date From")
        if not len(data['date_to']):
            error.append("Please enter a Travel Date To")

        print "DATE TYPE", type(data['date_from'])
        date_from = datetime.strptime(data['date_from'], "%Y-%m-%d")
        print "DATE TYPE2", type(date_from)
        now = datetime.today()
        date_to = datetime.strptime(data['date_to'], "%Y-%m-%d")

        print "NOW", now
        print "DATE FROM", data['date_from']
        if not(date_from>now):
            error.append("please enter future date")
        if (date_from>date_to):
            error.append("Date From cannot be after Date To")

        if error:
            return (False, error, False)

        print "USER ID=", data['user_id']

        # try:
        #     item_exist = Item.objects.get(item_name=data['item_name'])
        #     if item_exist:
        #         error.append("Item already exists")
        #         return (False, error, False)
        # except:
        #     print "It is indeed a new item"
        #     pass

        #Get/create user and item instances
        user_info = User.objects.get(id=data['user_id'])
        user_info.travel_of_user.create(destination=data['destination'], description = data['description'], date_from = data['date_from'], date_to = data['date_to'], creator=user_info)
        user_info.save()

        return (True, "Succesful registration to Wish List!", user_info)

    def join(request, user_id, travel_id):
        user_info = User.objects.get(id=user_id)
        curr_travel = Travel.objects.get(id = travel_id)

        user_info.travel_of_user.add(curr_travel)
        user_info.save()
        return "Succesfully joined a trip!"

    def delete(request, user_id, travel_id):
        # user_info = User.objects.get(id=user_id)
        travel = Travel.objects.get(id = travel_id).delete()
        print 'removed trip!'
        # user_info.travel_of_user.remove(curr_travel)
        # travel.save()
        return "Succesfully removed a trip!"



class Travel(models.Model):
    destination = models.CharField(max_length =45)
    description = models.TextField()
    date_from = models.DateField(auto_now=False)
    date_to = models.DateField(auto_now=False)
    user_of_travel = models.ManyToManyField(User, default=0, related_name = 'travel_of_user')
    creator = models.ForeignKey(User, related_name="travel_of_creator")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TravelManager()
