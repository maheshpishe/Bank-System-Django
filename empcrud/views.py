from django.shortcuts import render,redirect
from .models import Employee,Transaction,History
from .forms import Userform,Transactform
from . import models
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime


# Create your views here.
def home(request):
	accounts=Employee.objects.all()
	context={'accounts':accounts}
	return render(request,'home.html',context
		)
def transview(request):
	
	form=Transactform()
	
	return render(request,'transact.html',{'form1':form})
	

def trans(request):
	form=Transactform()
	# history=History.objects.all()
	fromacnt=request.POST['from_acnt']
	toacnt=request.POST['to_acnt']
	bal=float(request.POST['amount'])
	up=Employee.objects.filter(id=fromacnt)[0]
	up1=Employee.objects.filter(id=toacnt)[0]
	if bal>up.balance:
		
		msg=messages.error(request, 'Oops!! Insufficient Balance')
		return render(request,'transact.html',{'message':msg,'form1':form})
	else:
		x=datetime.now()
		obj=History.objects.create(frm=up.name,to=up1.name,money=bal,date=x)
		obj.save()
		up.balance-=bal
		up1.balance+=bal
		up.save()
		up1.save()
		msg=messages.success(request, 'Transaction Successful!')
		return render(request,'transact.html',{'message':msg,'form1':form})
def accnt(request):
	form=Userform()
	if request.method=='GET':
		
		return render(request,'acc.html',{'form':form})
	else:
		form=Userform(request.POST)
		if form.is_valid():
			form.save()
		msg=messages.success(request, 'Account Added Succesfully!')
		return render(request,'acc.html',{'form':Userform(),'msg':msg})

def history(request):
	data=History.objects.all()
	context={'data':data}
	return render(request,'history.html',context)