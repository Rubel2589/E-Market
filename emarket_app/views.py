from django.shortcuts import render
from emarket_app.models import contact_form , brand_type_form , register_form , product_type , product_category , product_info , cart_details , order_address
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect , JsonResponse
import json
import random
from django.contrib.auth import authenticate,login,logout
from django.db.models import F
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from Paytm import checksum
# from django.shortcuts import redirect


from django import template
register = template.Library()


@register.filter(name='subtract')
def subtract(value, arg):
    return value - arg



brand_type_data = brand_type_form.objects.all().order_by('-id')
product_type_index = product_type.objects.all().order_by('-id')[:3]
pro_category = product_category.objects.all()



def navbar_page(request):
    return render(request,'navbar_footer.html',{'pro_category':pro_category})

def index(request):
    get_latest_product = product_info.objects.values().order_by('-id')[:1]
    get_all_product = product_info.objects.all().order_by('-id')[:6]
    return render(request,'index.html',{'brand_type_data':brand_type_data,'product_type':product_type_index,'latest_product':get_latest_product,'all_product_details':get_all_product,'pro_category':pro_category})

def about(request):
    return render(request,'about.html',{'pro_category':pro_category})

def contact(request):
    if 'contact_submit' in request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        contact = request.POST['contact']
        brand_type = request.POST['brand_type']
        message = request.POST['message']
        data = contact_form(first_name = first_name , last_name = last_name , email = email , contact = contact , brand_type = brand_type , subject = subject , message = message)
        data.save()
        return render(request,'index.html',{'contact_status':'Your Concern Details for brand {} is successfully stored'.format(data.brand_type)})
        # return HttpResponse(data)
    return render(request,'contact.html',{'brand_type_data':brand_type_data,'pro_category':pro_category})

def register_page(request):
    if 'signup' in request.POST:
        first_name  =request.POST['first_name']
        last_name  =request.POST['last_name']
        email  =request.POST['email']
        password  =request.POST['pass']
        userdata = User.objects.create_user(email,email,password)
        userdata.first_name = first_name
        userdata.last_name = last_name
        data = register_form( user =  userdata , first_name = first_name  , last_name = last_name , email = email , password = password)
        if 'profile_image' in request.FILES:
            pho=request.FILES['profile_image']
            data.profile_image=pho
            data.save()
        data.save()
        return render(request,'index.html',{'register_success':'Your Registertation is successfully done'})
    return render(request,'register.html',{'pro_category':pro_category})

def login_page(request):
    if 'signin' in request.POST:
        email = request.POST['email']
        password = request.POST['pass']
        user = authenticate(username = email , password = password)
        if user:
            login(request,user)
            response = HttpResponseRedirect('/')
            if 'remember-me' in request.POST:
                response.set_cookie('userid',user.id)
                response.set_cookie('useremail',user.email)
                return response
            else:
                response.set_cookie('userid',user.id)
                response.set_cookie('useremail',user.email)
                return response
        else:
            return render(request,'login.html',{'login_page_error':'Either Username Or Password Is Incorrect..Please Try Agin'})

    return render(request,'login.html',{'pro_category':pro_category})

def pro_type(request):
    if 'type' in request.GET:
        type_val = request.GET['type']
        get_product_type_data_count = product_info.objects.filter(product_type_id=type_val).count() 
        if get_product_type_data_count == 0: 
            return HttpResponseRedirect('/')
        else:
            get_product_type_data = product_info.objects.filter(product_type_id=type_val).all()
            get_product_type = product_type.objects.filter(id=type_val).all()
            # return HttpResponse(get_product_type)
            return  render(request,'single_product_type.html',{'get_product_type_data':get_product_type_data,'get_product_type':get_product_type,'pro_category':pro_category})

def single_product_detail(request):
    if 'pro_id' in request.GET:
        pro_id = request.GET['pro_id']
        single_product_data = product_info.objects.filter(id=pro_id).all()
        return render(request,'single_product_details.html',{'single_product_data':single_product_data,'pro_category':pro_category})
    return HttpResponse('dss')

def shop_page(request):
    # return HttpResponse('shop_page')
    all_product_data = product_info.objects.all().order_by('-id')
    return render(request,'shop.html',{'all_product_data':all_product_data,'pro_category':pro_category})

def product_cate(request):
    if 'pro_cat_id' in request.GET:
        pro_cat_id = request.GET['pro_cat_id']
        single_product_category_details = product_info.objects.filter(product_category_id=pro_cat_id).all()
        requested_product_category = product_category.objects.filter(id=pro_cat_id).all()
    return render(request,'single_product_category_page.html',{'single_product_category_details':single_product_category_details,'requested_product_category':requested_product_category ,'pro_category':pro_category})
    
def logout_link(request):
    logout(request)
    response=HttpResponseRedirect('/')
    response.delete_cookie('userid')
    response.delete_cookie('useremail')
    return response

def login_user_cart_data(request):
    login_user_cart_count = cart_details.objects.filter(user_email = request.COOKIES.get('useremail')).filter(status = 0).count()
    return HttpResponse(login_user_cart_count)

def add_pro_cart(request):
    if 'pro_id' in request.POST:
        pro_id = request.POST['pro_id']
        pro_name = request.POST['pro_name']
        pro_image = request.POST['pro_image']
        pro_type = request.POST['pro_type']
        pro_cat = request.POST['pro_cat']
        pro_price = request.POST['pro_price']
        pro_discount = request.POST['pro_discount']
        pro_brand = request.POST['pro_brand']
        user_email = request.COOKIES.get('useremail')
        user_id = request.COOKIES.get('userid')
        get_single_product_cart_data = cart_details.objects.filter(user_email = request.COOKIES.get('useremail') , pro_id = pro_id).all()
        search_pro_id = cart_details.objects.filter(user_email = request.COOKIES.get('useremail') , pro_id = pro_id).count()
        if search_pro_id == 0:          # New Product is adding to the cart
            add_pro_to_cart = cart_details(user_id = user_id , user_email = user_email , brand_name = pro_brand , product_type_name = pro_type , product_category_name = pro_cat , pro_id = pro_id , pro_name = pro_name , pro_image = pro_image , price = pro_price , discount = pro_discount)
            add_pro_to_cart.save()
            return HttpResponse('new_product_added')
        else:
            increment_quantity_of_added_product = cart_details.objects.filter(user_email = user_email , pro_id = pro_id).update(quantity = F('quantity') + 1) 
            # increment_quantity_of_added_product = cart_details.objects.filter(user_email = user_email , pro_id = pro_id).update(price = F('price') + get_single_product_cart_data[0].price) 
            return HttpResponse('update_cart')

def show_cart_data(request):
    get_cart_data_on_screen = list(cart_details.objects.filter(user_email = request.COOKIES.get('useremail')).filter(status = 0).values())
    return JsonResponse(get_cart_data_on_screen,safe=False)

def checkout(request):
    if 'do_payment' in request.POST:
        order_id = random.randint(1111,99999999)
        address_id = request.POST['address_id']
        update_cart_order_id_ = cart_details.objects.filter(user_email = request.COOKIES.get('useremail')).filter(status = 0).update(order_id = order_id,order_adres = address_id)
        user_email = request.COOKIES.get('useremail')
        amount = request.POST['amount']
        param_dict = {
            'MID':'wSsmEN64869628261975',
            'ORDER_ID':str(order_id),
            'TXN_AMOUNT':str(amount),
            'CUST_ID':user_email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
    	    'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest',
        }
        param_dict['CHECKSUMHASH'] =checksum.generate_checksum(param_dict, 'gVaH&G!#vttQ5h!8')
        return render(request,'paytm.html',{'param_dict':param_dict})

    get_order_address = order_address.objects.filter(user_email = request.COOKIES.get('useremail')).all()
    return render(request,'checkout.html',{'pro_category':pro_category,'get_order_address':get_order_address})

def add_order_address(request):
    if 'address_type' in request.POST:
        address_type = request.POST['address_type']
        full_name = request.POST['full_name']
        country = request.POST['country']
        address = request.POST['address']
        postcode = request.POST['postcode']
        city = request.POST['city']
        state = request.POST['state']
        phone_number = request.POST['phone_number']
        email_address = request.POST['email_address']
        user_id = request.POST['user_id']
        add_order_address_data = order_address(address_type = address_type , full_name = full_name , country = country , address = address , pin_code = postcode , city = city , state = state , contact = phone_number , user_email = email_address , user_id = user_id)
        add_order_address_data.save()
        return HttpResponse('address_added')

def dashboard(request):
    if 'set_new_password' in request.POST:
        new_password = request.POST['new_password']
        get_user_data = User.objects.get(email = request.COOKIES.get('useremail'))
        get_user_data.set_password(new_password)
        # get_user_register = register_form.objects.get(email = request.COOKIES.get('useremail'))
        # get_user_register.password = new_password
        get_user_data.save()
        # get_user_register.save()
        response=HttpResponseRedirect('/')
        response.delete_cookie('userid')
        response.delete_cookie('useremail')
        return response
    get_user_login_data = register_form.objects.filter(email = request.COOKIES.get('useremail')).all()
    get_login_user_cart_data = cart_details.objects.filter(user_email = request.COOKIES.get('useremail')).all()
    return render(request,'dashboard.html',{'pro_category':pro_category,'get_user_login_data':get_user_login_data,'get_login_user_cart_data':get_login_user_cart_data})

def check_password_url(request):
    if 'old_password' in request.GET:
        old_password = request.GET['old_password']
        get_user_data = User.objects.get(email = request.COOKIES.get('useremail'))
        if check_password(old_password,get_user_data.password):
            return HttpResponse('same')
        else:
            return HttpResponse('notsame')

def search_item_url(request):
    if 'search_item' in request.GET:
        search_item = request.GET['search_item']
        item_searched = list(product_info.objects.filter(product_name__contains = search_item).values())
        return JsonResponse(item_searched,safe=False)

@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            Checksum = form[i]
    verify =checksum.verify_checksum(response_dict,'gVaH&G!#vttQ5h!8',Checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            update_cart_order_id_ = cart_details.objects.filter(user_email = request.COOKIES.get('useremail')).filter(order_id = response_dict['ORDERID']).update(status = '1')
            print('order successfully')
        else:
            print('not success. Due to '+ response_dict['RESPMSG'])
    # return render(request,'payment_status.html',{'response':response_dict})
    return HttpResponseRedirect('dashboard')
    # patym post request
    # pass

def delete_product_url(request):
    if 'delete_product_input' in request.POST:
        delete_product_input = request.POST['delete_product_input']
        get_cart_item_to_delete = cart_details.objects.filter(id=delete_product_input)
        get_cart_item_to_delete.delete()
        return HttpResponseRedirect('dashboard')

def profile_image_change(request):
    if 'new_profile_image' in request.FILES:
        get_user = register_form.objects.get(email = request.COOKIES.get('useremail'))
        new_img = request.FILES['new_profile_image']
        # return HttpResponse(new_img)
        get_user.profile_image = new_img
        get_user.save()
        return HttpResponseRedirect('dashboard')


def check_email(request):
    if 'email' in request.GET:
        email = request.GET['email']
        get_user_email = User.objects.filter(email = email)
        if len(get_user_email):
            return HttpResponse('existing')
        else:
            return HttpResponse('new')

