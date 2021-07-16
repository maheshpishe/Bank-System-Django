from django.db import models
from django.db.models import IntegerField

# Create your models here.
# class Position(models.Model):
# 	"""docstring for Position"""
# 	pos=models.CharField(max_length=10)
# 	def __str__(self):
# 		return self.pos

class Employee(models.Model):
	name=models.CharField(max_length=20,default=None)
	acntnumber=models.IntegerField(blank=False,null=False,default=None)
	email=models.EmailField(max_length=20,default=None)
	MobNumber=models.CharField(max_length=10,default=None)
	balance=models.FloatField(null=True, blank=True, default=0.0)
	# position=models.ForeignKey(Position,on_delete=models.CASCADE)
	"""docstring for Position"""
	def __str__(self):	
		return self.name


class Transaction(models.Model):
	"""docstring for ClassName"""
	from_acnt = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="fromuser",default=None)
	to_acnt=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="touser",default=None)
	amount = models.DecimalField(max_digits=100, decimal_places=2,default=0.00)
	# enter_your_user_name = models.CharField(max_length = 150, default = None)
	# enter_the_destination_account_number = models.IntegerField(default = None)
	# enter_the_amount_to_be_transferred_in_INR = models.IntegerField(default = None,null=True,blank=True)
		
class History(models.Model):
	frm=models.CharField(max_length=20,default=None)
	to=models.CharField(max_length=20,default=None)
	money=models.DecimalField(max_digits=100, decimal_places=2,default=None)
	date=models.CharField(max_length=20,default=None)
	"""docstring for ClassName"""
	def __str__(self):
		
		return self.frm
