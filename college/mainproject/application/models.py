from django.db import models
class Newstudent(models.Model):
	p_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	fname=models.CharField(max_length=100)
	mname=models.CharField(max_length=100)
	no=models.CharField(max_length=100)
	img= models.ImageField(upload_to = 'pictures/')
	email=models.CharField(max_length=100)
	pwd=models.CharField(max_length=100)
	dob=models.CharField(max_length=100)
	class1=models.CharField(max_length=100)
	gender=models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Newresult(models.Model):
	p_id = models.AutoField(primary_key=True)
	title=models.CharField(max_length=100)
	dept=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	sem=models.CharField(max_length=100)
	img= models.ImageField(upload_to = 'result/')
	desc1=models.TextField(max_length=500)
	def __str__(self):
		return self.title
class Newevent(models.Model):
	p_id = models.AutoField(primary_key=True)
	e_name=models.CharField(max_length=100)
	e_location=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	img= models.ImageField(upload_to = 'event/')
	desc1=models.TextField(max_length=500)
	def __str__(self):
		return self.e_name
class Eventimg(models.Model):
	p_id = models.AutoField(primary_key=True)
	e_name=models.CharField(max_length=100)
	img= models.ImageField(upload_to = 'events/')
	def __str__(self):
		return self.e_name
class Newnotice(models.Model):
	p_id = models.AutoField(primary_key=True)
	title=models.CharField(max_length=100)
	dept=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	sem=models.CharField(max_length=100)
	desc1=models.TextField(max_length=500)
	def __str__(self):
		return self.title
class Newfeedback(models.Model):
	p_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	cls1=models.CharField(max_length=100)
	type1=models.CharField(max_length=100)
	msg1=models.TextField(max_length=500)
	reply=models.TextField(max_length=500)
	def __str__(self):
		return self.name

class Gallery(models.Model):
	p_id = models.AutoField(primary_key=True)
	location=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	img= models.ImageField(upload_to = 'gallery/')
	def __str__(self):
		return self.date