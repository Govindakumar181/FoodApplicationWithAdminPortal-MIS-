from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
# import json
# import datetime
from datetime import datetime
# from datetime import date
# from datetime import timedelta 
from store.models import * 
# from .utils import cookieCart, cartData, guestOrder
# from django.contrib.auth.models import User

# ---------------------------------------------------------------------
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
#-----------------------------------------------------------------------
from store.forms import * 
from store.views import * 

def portal(request):
    try:
        profile = Customer.objects.get(user=request.user)
        if profile.user.username == "rameez": 
            customers = Customer.objects.all()
            products = Product.objects.all()
            orders = Order.objects.filter(complete=True)
            reviews = Reviews.objects.all()
            
            lencustomers = len(customers)
            lenproducts = len(products)
            lenorders = len(orders)
            lenreviews = len(reviews)

            customers = customers
            products = products
            orders = orders
            reviews = reviews

            todaysorder = 0
            # print(orders.posting_date)
            for i in orders:
                # print(i.posting_date.date())
                if datetime.now().date() == i.posting_date.date():
                    todaysorder += 1
            # print(todaysorder)

            context={
                'profile':profile,
                'lencustomers':lencustomers,'lenproducts':lenproducts,'lenorders':lenorders,'lenreviews':lenreviews,
                'customers':customers,'products':products,'orders':orders,'reviews':reviews,
                'todaysorder':todaysorder,
                }
            return render(request, 'index.html',context)
        else:
            return render(request, 'store/signin.html')
    except:
        return render(request, 'store/signin.html')
