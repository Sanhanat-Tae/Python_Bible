from django.shortcuts import render

def test_templates1(request):
    templates_var = {
                       "name" : "มานี",
                       "surname" : "ใจกล้า",
                       "tel" : "0819548686"
                    }
    return render(request, "MyTemplatesVar.html", templates_var)

def test_templates2(request):
    templates_var2 = {
                        "sports" : ["Basketball", "Tennis", "Table Tennis", "Volleyball"],
                        "subjects" : {"Math" : 98, "English" : 80, "Science" : 79}
                      }
    return render(request, "MyTemplatesVar2.html", templates_var2)