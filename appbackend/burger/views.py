from django.http import JsonResponse
import json
from . import models
from django.db.models import Q
import time

# Create your views here.
def index(requests):


    if requests.method == "POST":
        # Do validation stuff here
        body_unicode = requests.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        try: 
            o = models.Order(username=body['username'], salad=body['salad'], slices=body['slices'], cutlets=body['cutlets'],cost=body['cost'],buns=body['buns'])
            o.save()
            return JsonResponse({'statusCode':201, 'data':body  })
        except Exception as e:
            return JsonResponse({'statusCode':400, 'message':str(e)  })
        
    else:
        
        user_filter = {
        "username" : requests.GET.getlist('username') if requests.GET.__contains__('username') else False,
        }     

        q_objects = Q() 
        if user_filter["username"]:
            q_objects &= Q(username=user_filter["username"][0])    
        
        try:
            orders = models.Order.objects.filter(q_objects)
            data =  list(orders.values("id","username","salad","buns","slices","cutlets","cost","timestamp"))
            totalcost= 0
            for order in data:
                totalcost+=order["cost"]

            if len(data):                                
                return JsonResponse({'statusCode':200, 'data':data, 'totalcost':totalcost  })
            else:
                return JsonResponse({'statusCode':404, 'data':"No data found for your request"  })
        except Exception as e:
            return JsonResponse({'statusCode':400, 'message':str(e)  })


def orderdetails(requests,order_id):
    try:
        order = models.Order.objects.filter(pk=order_id)
        data = list(order.values("id","username","salad","buns","slices","cutlets","cost","timestamp"))
       
        return JsonResponse({'statusCode':200, 'data':data[0]})
    
    except Exception as identifier:
            
        return JsonResponse({'statusCode':404, 'data':"No data found for your request"})