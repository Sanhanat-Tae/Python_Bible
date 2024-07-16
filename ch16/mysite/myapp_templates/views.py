from django.shortcuts import render

def my_templates(request):
    return render(request, "MyTemplates.html")
