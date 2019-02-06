from django.db import models

# Create your models here.
class S_Question(models.Model):
	question_name = models.CharField(max_length=250)


	def __str__(self):
		return self.question_name
		
class Users(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)
	contact = models.IntegerField()
	address = models.TextField()
	question = models.ForeignKey(S_Question,on_delete=models.CASCADE,null= True,blank=True)
	answer = models.CharField(max_length=250,default='please answer',null= True,blank=True)

	def __str__(self):
		return self.first_name

