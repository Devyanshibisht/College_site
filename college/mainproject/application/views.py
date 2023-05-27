from django.shortcuts import render, redirect
from django.conf.urls.static import static
from application.models import Newstudent,Newresult,Newevent,Newnotice,Eventimg,Newfeedback,Gallery
from django.core.files.storage import FileSystemStorage
def home(request):
	return render(request,"template/index.html")
def login(request):
	return render(request,"template/login.html")
def register(request):
	return render(request,"template/register.html")
def contact(request):
	return render(request,"template/contact.html")
def about(request):
	return render(request,"template/about1.html")
def gallery(request):
	return render(request,"template/gallery.html")
def registercode(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.FILES['t5']
		f=request.POST['t6']
		g=request.POST['t7']
		h=request.POST['t8']
		i=request.POST['t9']
		j=request.POST['t10']
		data2=Newstudent.objects.filter(email=f).count()
		if data2==0:
			data=Newstudent(name=a, fname=b, mname=c, no=d, img=e, email=f, pwd=g, dob=h, class1=i, gender=j)
			data.save()
			request.session['user'] = f
			return redirect("/user/")
		else:
			user = "This Email Is All Ready Register"
			return render(request,"template/msg.html",{"msg":user})	
	else:
		redirect('/register/')
def user(request):
	if request.session.has_key('user'):
		email = request.session['user']
		data=Newstudent.objects.filter(email=email).all()
		return render(request,"template/user.html", {"usernames" : data})
	else:
		return render(request,"template/login.html")
def admin1(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		return render(request,"template/admin.html", {"usernames" : email})
	else:
		return render(request,"template/login.html")
def logout(request):
	if request.session.has_key('user'):
		del request.session['user']
	if request.session.has_key('admin'):
		del request.session['admin']
	return redirect("/login/")
def logincode(request):
	if request.method=="POST":
		email= request.POST['t1']
		pwd= request.POST['t2']
		if email == "admin@gmail.com" and pwd=="admin":
			request.session['admin'] = email
			return redirect("/admin1/")
		else:
			try:
				user = Newstudent.objects.get(email=email, pwd=pwd)
				request.session['user'] = email
				return redirect("/user/")
			except Newstudent.DoesNotExist:
				user = "Not match"
				return render(request,"template/msg.html",{"msg":user})
def showuser(request):
	data=Newstudent.objects.all()
	return render(request,"template/showuser.html",{"alldata":data})
def addresult(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.FILES['t6']
		f=request.POST['t5']
		data=Newresult(title=a, dept=b, date=c, sem=d, img=e, desc1=f)
		data.save()
		user = "This Result Is Register"
		return render(request,"template/msg.html",{"msg":user})
	else:	
		return render(request,"template/addresult.html")
def addevent(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.FILES['t6']
		f=request.POST['t5']
		data=Newevent(e_name=a, e_location=b, date=c, name=d, img=e, desc1=f)
		data.save()
		for afile in request.FILES.getlist('t7'):
			data=Eventimg(e_name= a, img= afile)
			data.save()
		user = "This Event Is Register"
		return render(request,"template/msg.html",{"msg":user})
	else:
		return render(request,"template/addevent.html")
def addgall(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		for afile in request.FILES.getlist('t3'):
			data=Gallery(location= a, date=b, img= afile)
			data.save()
		user = "This Gallery Is Register"
		return render(request,"template/msg.html",{"msg":user})
	else:
		return render(request,"template/addgall.html")
def addnotice(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		data=Newnotice(title=a, dept=b, date=c, sem=d, desc1=e)
		data.save()
		user = "This Notice Is Register"
		return render(request,"template/msg.html",{"msg":user})
	else:
		return render(request,"template/addnotice.html")
def delete_stu(request,pk):
	id=pk
	Newstudent.objects.filter(p_id=id).delete()
	return redirect("/showuser/")
def allevent(request):
	if request.session.has_key('user'):
		email = request.session['user']
		data=Newstudent.objects.filter(email=email).all()
		event=Newevent.objects.all()
		return render(request,"template/myevent.html", {"alldata" : event})
	else:
		return render(request,"template/login.html")
def allevent2(request):
	event=Newevent.objects.all()
	return render(request,"template/myevent2.html", {"alldata" : event})
def allimages(request):
	if request.session.has_key('user'):
		email = request.session['user']
		a=request.POST['t1']
		event=Eventimg.objects.filter(e_name=a).all()
		return render(request,"template/images.html", {"alldata" : event})
	else:
		return render(request,"template/login.html")
def showgall(request):
		gal=Gallery.objects.all()
		return render(request,"template/images2.html", {"alldata" : gal})
def mynotice(request):
	if request.session.has_key('user'):
		email = request.session['user']
		data=Newstudent.objects.filter(email=email).all()
		cls=data[0].class1
		notice=Newnotice.objects.filter(dept=cls).all()
		return render(request,"template/mynotice.html", {"alldata" : notice})
	else:
		return render(request,"template/login.html")
def myresult(request):
	if request.session.has_key('user'):
		email = request.session['user']
		data=Newstudent.objects.filter(email=email).all()
		cls=data[0].class1
		notice=Newresult.objects.filter(dept=cls).all()
		return render(request,"template/myresult.html", {"alldata" : notice})
	else:
		return render(request,"template/login.html")
def myprofile(request):
	if request.session.has_key('user'):
		email = request.session['user']
		data=Newstudent.objects.filter(email=email).all()
		return render(request,"template/myprofile.html", {"alldata" : data})
	else:
		return render(request,"template/login.html")
def profile(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		f=request.POST['t6']
		g=request.POST['t7']
		h=request.POST['t8']
		Newstudent.objects.filter(email=e).update(name=a,fname=b,mname=c,no=d,pwd=f,dob=g,class1=h)		
		user = "Update Profile SuccessFully"
		return render(request,"template/msg.html",{"msg":user})
	else:
		return redirect("/myprofile/")
def sendfeedback(request):
	if request.session.has_key('user'):
		email = request.session['user']
		data=Newstudent.objects.filter(email=email).all()
		return render(request,"template/sendfeedback.html", {"alldata" : data})
	else:
		return render(request,"template/login.html")
def feedback(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		data=Newfeedback(name=a, email=b, cls1=c, type1=d, msg1=e)
		data.save()
		user = "This Feedback Is Register"
		return render(request,"template/msg.html",{"msg":user})
	else:
		return render(request,"template/login.html")
def showmessage(request):
	data=Newfeedback.objects.all()
	return render(request,"template/showfeedback.html",{"alldata":data})
def showresult(request):
	data=Newresult.objects.all()
	return render(request,"template/showresult.html",{"alldata":data})
def delete_feed(request,pk):
	id=pk
	Newfeedback.objects.filter(p_id=id).delete()
	return redirect("/showmessage/")
def edit_feed(request,pk):
	id=pk
	return render(request,"template/reply.html",{"alldata":id})
def reply(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		data=Newfeedback.objects.filter(p_id=a).update(reply=b)
		user = "This Reply Is Send"
		return render(request,"template/msg.html",{"msg":user})
	else:
		return redirect("/showmessage/")
def mymsg(request):
	if request.session.has_key('user'):
		email = request.session['user']
		data=Newstudent.objects.filter(email=email).all()
		data2=Newfeedback.objects.filter(email=email).all()
		return render(request,"template/mymsg.html", {"alldata" : data2})
	else:
		return redirect("/login/")
def delete_feed2(request,pk):
	id=pk
	Newfeedback.objects.filter(p_id=id).delete()
	return redirect("/mymsg/")
def gallery(request):
		gal=Gallery.objects.all()
		return render(request,"template/gallery.html", {"alldata" : gal})
