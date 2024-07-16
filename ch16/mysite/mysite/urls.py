from django.contrib import admin
from django.urls import include,path
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path("myapp/", include("myapp.urls")),
    path("myapp_templates/",include("myapp_templates.urls")),
    path("myapp_templates2/",include("myapp_templates2.urls")),
    path("myapp_testmodel/",include("myapp_testmodel.urls")),
    path("myapp_testmodel2/",include("myapp_testmodel.urls")),
    path("products/",include("products.urls")),
]

