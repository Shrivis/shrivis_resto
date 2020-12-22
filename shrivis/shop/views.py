from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .PayTm import Checksum
from .models import UserProfile, Product, Order
from django.views.decorators.csrf import csrf_exempt
# get MERCHANT KEY from Paytm
MERCHANT_KEY = 'chnage this key'


def search_match(keyword, item):
    if keyword in item.p_desc.lower() or keyword in item.p_type or keyword in item.p_name.lower() or keyword in \
            item.p_category.lower() or keyword in item.p_subcategory.lower():
        return True
    else:
        return False


def search(request):
    keyword = request.GET.get('search').lower()
    all_product = []
    cat_products = Product.objects.values('p_category', 'p_id')
    cats = {item['p_category'] for item in cat_products}
    for cat in cats:
        prodtemp = Product.objects.filter(p_category=cat)
        prod = [item for item in prodtemp if search_match(keyword, item)]
        n = len(prod)
        all_product.append([prod, range(1, n), n])
    params = {'all_product': all_product, 'msg': ""}
    print(all_product)
    print(len(all_product))
    if len(all_product) == 0 or len(keyword) < 3:
        params = {'msg': "Pleas make sure to enter relevant search query"}
        print(params)
    return render(request, 'menu.html', params)


def about(request):
    return render(request, 'about.html')


def index(request):
    all_product = []
    cat_products = Product.objects.values('p_category', 'p_id')
    cats = {item['p_category'] for item in cat_products}
    for cat in cats:
        prod = Product.objects.filter(p_category=cat)
        n = len(prod)
        all_product.append([prod, range(1, n), n])
    params = {'all_product': all_product}
    return render(request, 'menu.html', params)


def contact(request):
    if request.method == "POST":
        messages.info(request, '******* Thanks! We will be in contact soon. *******')
        return redirect('/contact')
    else:
        return render(request, 'contact.html')


def reservation(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            messages.info(request, '******* Booking Successful *******')
            return redirect('/')
        else:
            messages.info(request, '******* Pleas login First *******')
            return redirect('/register')
    else:
        return render(request, '/')


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        add_1 = request.POST.get('address1', '')
        add_2 = request.POST.get('address2', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address_1=add_1, address_2=add_2, phone=phone, amount=amount)
        order.save()
        param_dict = {
                # get MID from Paytm
                'MID': 'chnage this key',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})

    return render(request, 'checkout.html')


@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    print(response_dict)
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            update = Order.objects.get(order_id=response_dict['ORDERID'])
            update.order_status = "Success"
            update.save()
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    print("printing order id", response_dict['ORDERID'])
    return render(request, 'paymentstatus.html', {'response': response_dict})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'No record Found!!! Pleas register first or try again.')
            return redirect('/register')
    else:
        return render(request, '/')


def register(request):
    if request.method == 'POST':
        f_name = request.POST['name']
        l_name = request.POST['l_name']
        phone = request.POST['phone']
        username = request.POST['username']
        pass_1 = request.POST['password']
        pass_2 = request.POST['password_2']
        email = request.POST['email']
        add_1 = request.POST['address']
        add_2 = request.POST['address_2']
        if pass_1 == pass_2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken!!!')
                return redirect('/register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Email Already Taken!!!')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=pass_1, first_name=f_name, last_name=l_name,
                                                email=email)
                user.save()
                other_details = UserProfile(address_1=add_1, address_2=add_2, phone=phone)
                other_details.user = user
                other_details.save()
                messages.info(request, 'Please login to Continue !!')
                return redirect('/login')
        else:
            messages.info(request, 'Password did not match!!!')
            return redirect('/register')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def order_history(request):
    all_product = []
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST['order_id']
            email = request.POST['email']
            if email == request.user.email:
                obj = Order.objects.get(order_id=id)
                param_dict = {
                    'item': obj.items_json,
                    'amount': str(obj.amount),
                    'status': obj.order_status,
                }
                return render(request, 'history.html', param_dict)
            else:
                messages.info(request, 'Email did not match. Try again!!!')
                return redirect('/contact')
    else:
        messages.info(request, 'Please Login First!!!')
        return redirect('/register')
    return render(request, 'history.html')
