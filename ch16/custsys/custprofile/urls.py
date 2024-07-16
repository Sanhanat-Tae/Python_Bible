from django.urls import path
from . import views

urlpatterns = [
	path("",views.index,name="index"),
	path("insertcust/",views.insertcust,name="addcust"),
	path("searchcust/",views.searchcust,name="selectcust"),
	path("editcust/",views.editcust,name="updatecust"),
	path("deletecust/",views.deletecust,name="delcust")
]