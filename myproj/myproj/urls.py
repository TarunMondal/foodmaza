"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from foodmaza import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('addadmin', views.addadmin),
    path('showadmin', views.adminshow),
    path('editadmin/<int:id>', views.adminedit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]

urlpatterns += [
    path('addcustomer', views.addcustomer),
    path('showcustomer', views.customershow),
    path('editcustomer/<int:id>', views.customeredit),
    path('custupdate/<int:id>', views.customerupdate),
    path('custdelete/<int:id>', views.customerdestroy),
]

urlpatterns += [
    path('addcategory', views.addcategory),
    path('showcategory', views.Categoryshow),
    path('editcategory/<int:C_Id>', views.Categoryedit),
    path('categoryupdate/<int:C_Id>', views.Categoryupdate),
    path('categorydelete/<int:C_Id>', views.Categorydestroy),
]

urlpatterns += [
    path('addsub_category', views.addsub_category),
    path('showsub_category', views.sub_categoryshow),
    path('editsub_category/<int:S_Id>', views.sub_categoryedit),
    path('subcategory_update/<int:S_Id>', views.sub_categoryupdate),
    path('subcategory_delete/<int:S_Id>', views.sub_categorydestroy),
]


urlpatterns += [
    path('additem', views.Itemadd),
    path('showitem', views.Itemshow),
    path('edititem/<int:Item_id>', views.Itemedit),
    path('itemupdate/<int:Item_id>', views.Itemupdate),
    path('itemdelete/<int:Item_id>', views.Itemdestroy),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Template url

urlpatterns += [
    path('home', views.home),
]

urlpatterns += [
    path('adminn', views.index),
]

urlpatterns += [
    path('calendar', views.calendar),
]

urlpatterns += [
    path('login', views.login),
]

urlpatterns += [
    path('logout', views.logout),
]

urlpatterns += [
    path('login2', views.custlogin,name="login2"),
]

urlpatterns += [
    path('signup', views.signup,name="signup"),
]

urlpatterns += [
    path('forget_pass', views.forget_pass),
]

urlpatterns += [
    path('admintable', views.admintable),
]
urlpatterns += [
    path('customertable', views.customertable),
]

urlpatterns += [
    path('cat', views.cattable),
]

urlpatterns += [
    path('sub', views.subtable),
]

urlpatterns += [
    path('item', views.itemtable),
]

