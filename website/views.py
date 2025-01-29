from django.shortcuts import render
from website import models
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def home(req):
	# print(req.session['customer_id'])
	data=models.Product.objects.all()
	obj={"produts":data}
	return render(req,"index.html",obj)

def shop(req):
	data=models.Product.objects.all()
	obj={"produts":data}
	return render(req,"shop.html",obj)

def product_details(req):
	info=models.Product.objects.get(id= req.GET['id'])
	obj={"info":info}
	return render(req,"product_details.html",obj)

def signup(req):
	return render(req,"signup.html")

def create_account(req):
	customer = models.Customer(
		customer_name=req.POST['customer_name'],
		customer_mobile=req.POST['customer_mobile'],
		customer_email=req.POST['customer_email'],
		customer_password=req.POST['customer_password']
	)
	customer.save()
	return redirect("/login")

def login(req):
	return render(req,"login.html")

def login_process(req):
	customer = models.Customer.objects.filter(customer_mobile= req.POST['customer_mobile'],customer_password=req.POST['customer_password']).values()
	customer =list(customer)
	
	if len(customer)==0:
		return render(req,"login_Failed.html")
	else:
		req.session['customer_id'] = customer[0]['id']
		return redirect("/")

def add_to_cart(req):
    customer_id = req.session.get('customer_id')  
    product_id = req.GET.get('id') 
    
    if not customer_id or not product_id:
        return redirect("/error/") 
    
    try:
        customer = models.Customer.objects.get(id=customer_id)
        product = models.Product.objects.get(id=product_id)
    except models.Customer.DoesNotExist:
        return redirect("/error/")  
    except models.Product.DoesNotExist:
        return redirect("/error/") 
    
    qty = 1 
    
    cart = models.CustomerCard(
        customer=customer,
        product=product,
        qty=qty
    )
    cart.save()
    
    return redirect("/cart/")
def cart(req):
    customer_id = req.session.get('customer_id')
    
    if not customer_id:
        return redirect("/login/")  
    
    carts = models.CustomerCard.objects.filter(customer=customer_id)
    obj = {"carts": carts}
    return render(req, "cart.html", obj)


def increaese_cart_qty(req):
	qty = req.GET['qty']
	id = req.GET['cart_id']

	qty =int(qty) + 1;
	cart=models.CustomerCard.objects.get(id = id)
	cart.qty=qty
	cart.save()
	return HttpResponse(qty)

def checkout(req):
	carts=models.CustomerCard.objects.filter(customer = req.session['customer_id'])
	obj={"carts":carts}
	return render(req,"checkout.html",obj)

def place_order(req):
	print(req.POST)
	order=models.Order(
			customer = models.Customer.objects.get(id = req.session['customer_id']),
			delivery_fname=req.POST['delivery_fname'],
			delivery_lname=req.POST['delivery_lname'],
			delivery_address=req.POST['delivery_address'],
			delivery_apartment=req.POST['delivery_apartment'],
			delivery_state_country=req.POST['delivery_state_country'],
			delivery_postal_zip=req.POST['delivery_postal_zip'],
			delivery_email_address=req.POST['delivery_email_address'],
			delivery_phone=req.POST['delivery_phone'],
			payment_type=req.POST['payment_type'],
			# order_date=req.POST['order_date']
	)
	order.save()

	# carts=models.CustomerCard.objects.filter(customer =req.session['customer_id']).values()
	# for i in carts:
	# 	order_product=models.OrderProducts(
	# 		product=models.Product.objects.get(id = product_id),
	# 		customer=models.Customer.objects.get(id = req.session['customer_id']),
	# 		order=models.Order.objects.latest('id'),			
	# 		qty= i.qty
	# 	)
	# 	order_product.save()

	return redirect("/checkout")

def Qr_code(req):
	return render(req,"Qr_code.html")


def about(req):
	return render(req,"about.html")


def services(req):
	data=models.Product.objects.all()
	obj={"produts":data}
	return render(req,"services.html",obj)

def blog(req):
	return render(req,"blog.html")


def contact(req):
	return render(req,"contact.html")

def save_contact(req):
	data=models.Contact(
		c_name=req.POST['c_name'],
		c_lname=req.POST['c_lname'],
		c_email=req.POST['c_email'],
		c_message=req.POST['c_message'],
	)
	data.save()
	return redirect("/contact")

def delete_product(req):
    order_id=req.GET['id']
    models.CustomerCard.objects.get(id = order_id).delete()
    return redirect("/cart")

