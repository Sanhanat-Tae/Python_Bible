from django.shortcuts import render
from custprofile.models import CustDB
from django.contrib import messages

def index(request):
	return render(request, "index.html")

def deletecust(request):
	cust_id = request.GET.get("customer_id", None)
	del_rec = request.POST.get("del_rec", None)
	if del_rec is not None:
		delrecord = CustDB.objects.get(id=cust_id)
		delrecord.delete()
		return render(request, "searchcust.html")
	elif cust_id is not None:
		#show custdb data for 
		results = list(CustDB.objects.filter(id__contains=cust_id))
		return render(request, "deletecust.html", {"result":results[0]})
	return render(request, "deletecust.html")

def editcust(request):
	cust_id = request.GET.get("customer_id", None)
	edit_save = request.POST.get("edit_save", None)
	if edit_save is not None:
		saverecord = CustDB()
		saverecord.id = request.POST.get("customer_id")
		saverecord.firstname = request.POST.get("firstname")
		saverecord.lastname = request.POST.get("lastname")
		saverecord.age = request.POST.get("age")
		saverecord.sex = request.POST.get("sex")
		saverecord.tel = request.POST.get("tel")
		saverecord.address = request.POST.get("address")
		saverecord.save()
		messages.success(request,"แก้ไขข้อมูลลูกค้าเรียบร้อยแล้ว")
		return render(request, "editcust.html", {"result":saverecord})
	elif cust_id is not None:
		#show custdb data for edit
		results = list(CustDB.objects.filter(id__contains=cust_id))
		return render(request, "editcust.html", {"result": results[0]})
	return render(request, "editcust.html")

def searchcust(request):
	if request.method == "POST":
		query_name = request.POST.get("firstname", None)
		results = CustDB.objects.filter(firstname__contains=query_name)
		result_list = list(results)
		return render(request, "searchcust.html", {"results":result_list,"result_size":len(result_list)})
	else:
		return render(request,"searchcust.html")

def insertcust(request):
	if request.method == "POST":
		if request.POST.get("firstname") and request.POST.get("lastname") and request.POST.get("age") and request.POST.get("sex") and request.POST.get("tel") and request.POST.get("address"):
			saverecord = CustDB()
			saverecord.firstname = request.POST.get("firstname")
			saverecord.lastname = request.POST.get("lastname")
			saverecord.age = request.POST.get("age")
			saverecord.sex = request.POST.get("sex")
			saverecord.tel = request.POST.get("tel")
			saverecord.address = request.POST.get("address")
			saverecord.save()
			messages.success(request,"บันทึกข้อมูลลูกค้าสำเร็จ")
			return render(request,"insertcust.html")
		else:
			return render(request,"insertcust.html")
	else:
		return render(request,"insertcust.html")