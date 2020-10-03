from django.shortcuts import render, redirect
from foodmaza.forms import AdminForm, CustomerForm, CategoryForm, sub_categoryForm, ItemForm
from foodmaza.models import Admin, Customer, Category, sub_category, Item
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, auth
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.impor

# Admin view--


def addadmin(request):
    if request.method == "POST":
        nm = request.POST.get("Name")
        db = request.POST.get("DOB")
        em = request.POST.get("Email")
        pas = request.POST.get("Password")
        ph = request.POST.get("Phone")
        gr = request.POST.get("Gender")

        a = Admin(Name=nm, DOB=db, Email=em, Password=pas, Phone=ph, Gender=gr)
        try:
            a.save()
            return redirect('/admintable')
        except:
            pass
    return render(request, 'adminindex.html')


def adminshow(request):
    admins = Admin.objects.all()
    return render(request, "showadmin.html", {'admins': admins})


def adminedit(request, id):
    admin = Admin.objects.get(id=id)
    return render(request, 'editadmin.html', {'admin': admin})


def update(request, id):
    admin = Admin.objects.get(id=id)
    a = AdminForm(request.POST, instance=admin)
    try:
        a.save()
        return redirect("/admintable")
    except:
        pass
    return render(request, 'editadmin.html', {'admin': admin})


def destroy(request, id):
    admin = Admin.objects.get(id=id)
    admin.delete()
    return redirect("/admintable")

    # Customer View--


def addcustomer(request):
    if request.method == "POST":
        nm = request.POST.get("Name")
        db = request.POST.get("DOB")
        em = request.POST.get("Email")
        pas = request.POST.get("Password")
        ph = request.POST.get("Phone")
        gr = request.POST.get("Gender")

        c = Customer(Name=nm, DOB=db, Email=em,
                     Password=pas, Phone=ph, Gender=gr)
        try:
            c.save()
            return redirect('/customertable')
        except:
            pass
    return render(request, 'customerindex.html')


def customershow(request):
    customers = Customer.objects.all()
    return render(request, "showcustomer.html", {'Customers': customers})


def customeredit(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'editcustomer.html', {'Customer': customer})


def customerupdate(request, id):
    cust = Customer.objects.get(id=id)
    c = CustomerForm(request.POST, instance=cust)
    try:
        c.save()
        return redirect("/customertable")
    except:
        pass
    return render(request, 'editcustomer.html', {'cust': cust})


def customerdestroy(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("/customertable")

    # Category View--


def addcategory(request):
    if request.method == "POST":
        nm = request.POST.get("Name")
        c = Category(Name=nm)
        try:
            c.save()
            return redirect('/cat')
        except:
            pass
    return render(request, 'categoryindex.html')


def Categoryshow(request):
    categorys = Category.objects.all()
    return render(request, "showcategory.html", {'Categorys': categorys})


def Categoryedit(request, C_Id):
    category = Category.objects.get(C_Id=C_Id)
    return render(request, 'editcategory.html', {'Category': category})


def Categoryupdate(request, C_Id):
    cate = Category.objects.get(C_Id=C_Id)
    c = CategoryForm(request.POST, instance=cate)
    try:
        c.save()
        return redirect("/cat")
    except:
        pass
    return render(request, 'editcategory.html', {'cate': cate})


def Categorydestroy(request, C_Id):
    category = Category.objects.get(C_Id=C_Id)
    category.delete()
    return redirect("/cat")


# sub_category--


def addsub_category(request):
    categorys = Category.objects.all()

    if request.method == "POST":
        nm = request.POST.get("Name")
        cid = request.POST["Category"]
        catid = Category.objects.get(C_Id=cid)

        s = sub_category(Name=nm, C_Id=catid)
        try:
            s.save()
            return redirect('/sub')
        except:
            pass
    return render(request, 'sub_categoryindex.html', {'categorys': categorys})


def sub_categoryshow(request):
    Sub_categorys = sub_category.objects.all()
    return render(request, "showsub_category.html", {'Sub_categorys': Sub_categorys})


def sub_categoryedit(request, S_Id):
    categorys = Category.objects.all()

    Sub_category = sub_category.objects.get(S_Id=S_Id)
    return render(request, 'editsub_category.html', {'Sub_category': Sub_category, 'categorys': categorys})


def sub_categoryupdate(request, S_Id):
    nm = request.POST.get("Name")
    cid = request.POST["Category"]
    catid = Category.objects.get(C_Id=cid)

    sab = sub_category.objects.get(S_Id=S_Id)
    sab.Name = nm
    sab.C_Id = catid
    try:
        sab.save()
        return redirect("/sub")
    except:
        pass
    categorys = Category.objects.all()
    return render(request, 'editsub_category.html', {'Sub_category': sab, 'categorys': categorys})


def sub_categorydestroy(request, S_Id):
    s_category = sub_category.objects.get(S_Id=S_Id)
    s_category.delete()
    return redirect("/sub")


# Item--


def Itemadd(request):
    sub_categorys = sub_category.objects.all()

    if request.method == "POST" and request.FILES['Item_image']:

        img = request.FILES['Item_image']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)

        nm = request.POST.get("Item_name")
        dis = request.POST.get("Discription")
        pri = request.POST.get("Item_price")
        sid = request.POST["sub_category"]
        sabid = sub_category.objects.get(S_Id=sid)

        I = Item(Item_name=nm, Item_image=uploaded_file_url,
                 Discription=dis, Item_price=pri, S_Id=sabid)
        I.save()
        return redirect('/item')
    return render(request, 'itemindex.html', {'sub_categorys': sub_categorys})


def Itemshow(request):
    items = Item.objects.all()
    return render(request, "showitem.html", {'items': items})


def Itemedit(request, Item_id):
    Sub_categorys = sub_category.objects.all()
    item = Item.objects.get(Item_id=Item_id)
    return render(request, 'edititem.html', {'item': item, 'Sub_categorys': Sub_categorys})


def Itemupdate(request, Item_id):
    if request.method == "POST" and request.FILES['Item_image']:

        img = request.FILES['Item_image']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)

        nm = request.POST.get("Item_name")
        img = request.POST.get("Item_image")
        dis = request.POST.get("Discription")
        pri = request.POST.get("Item_price")

        sid = request.POST["sub_category"]
        sabid = sub_category.objects.get(S_Id=sid)

        item = Item.objects.get(Item_id=Item_id)
        item.Item_name = nm
        item.Item_image = uploaded_file_url
        item.Discription = dis
        item.Item_price = pri
        item.S_Id = sabid
        item.save()
        return redirect("/item")

        Sub_categorys = sub_category.objects.all()
    return render(request, 'edititem.html', {'item': item, 'Sub_categorys': Sub_categorys})


def Itemdestroy(request, Item_id):
    item = Item.objects.get(Item_id=Item_id)
    item.delete()
    return redirect("/item")

# Template start


def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})


def index(request):
    return render(request, 'index.html')


def calendar(request):
    return render(request, 'calendar.html', {'calendar': calendar})


def login(request):
    em = request.POST.get("Email")
    pas = request.POST.get("Password")
    admins = Admin.objects.filter(Email=em, Password=pas)
    for admin in admins:
        request.session["Email"] = admin.Email
        return redirect('/adminn')
    return render(request, 'login.html', {'error': "Invalid Login Username OR Password"})


def logout(request):
    auth.logout(request)
    return redirect('/login')


def custlogin(request):
    em1 = request.POST.get("Email")
    pas1 = request.POST.get("Password")
    customers = Customer.objects.filter(Email=em1, Password=pas1)
    for customer in customers:
        request.session["Email"] = customer.Email
        return redirect('/home')
    return render(request, 'login2.html', {'error': "Invalid Login Username OR Password"})

    # if request.method == 'POST':
    #     # em1 = request.POST['Email']
    #     nm = request.POST['Name']
    #     pas = request.POST['Password']
    #     user = auth.authenticate(username=nm, password=pas)
    #     if user is not None:
    #         auth.login(request, user)
    #         return render(request, "home.html")
    #     else:
    #         return render(request, "login2.html", {'error': "Invalid Login Username OR Password"})
    # else:
    #     return render(request, "login2.html")


def signup(request):
    if request.method == "POST":

        nm = request.POST.get("Name")
        db = request.POST.get("DOB")
        em = request.POST.get("Email")
        pas = request.POST.get("Password")
        ph = request.POST.get("Phone")
        gn = request.POST.get("Gender")
        customer = Customer(Name=nm, DOB=db, Email=em,
                            Password=pas, Phone=ph, Gender=gn)
        customer.save()
        return render(request, 'login2.html')
    return render(request, 'signup.html')


def forget_pass(request):
    return render(request, 'forget_pass.html', {'forget_pass': forget_pass})


def admintable(request):
    admins = Admin.objects.all()
    return render(request, "admintable.html", {'admins': admins})


def customertable(request):
    customers = Customer.objects.all()
    return render(request, "customertable.html", {'Customers': customers})


def cattable(request):
    categorys = Category.objects.all()
    return render(request, "cat.html", {'Categorys': categorys})


def subtable(request):
    Sub_categorys = sub_category.objects.all()

    return render(request, 'sub.html', {'Sub_categorys': Sub_categorys})


def itemtable(request):
    items = Item.objects.all()

    return render(request, 'item.html', {'items': items})
