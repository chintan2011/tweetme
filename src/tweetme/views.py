from django.shortcuts import render

#retrieve
# GET -- templates from home.html
def home(request):
	
	return	render(request,"home.html",{})