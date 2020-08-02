from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def home(request):
    return render(request,'new.html')

from django.views.generic import View

class JSONCBV(View):
    def get(self,request,*args,**kwargs):
        emplpoyee_data = {'eno': 100, 'ename': "Sharad", 'esal': 60000, 'eaddr': 'Pune'}
        return JsonResponse(emplpoyee_data)
