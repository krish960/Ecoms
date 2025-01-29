from django.db import models

# Create your models here.

class ProductType(models.Model):
	procuct_type_name=models.CharField(max_length=100)
	def __str__(self):
		return self.procuct_type_name

class Product(models.Model):
	product_name=models.CharField(max_length=100)
	product_price=models.IntegerField()
	product_image=models.ImageField(upload_to="static/upload/")
	product_color=models.CharField(max_length=100)
	product_size=models.CharField(max_length=100)
	product_details=models.TextField()
	product_type=models.ForeignKey("ProductType",on_delete=models.CASCADE)

	

class Customer(models.Model):
	customer_name=models.CharField(max_length=100)
	customer_mobile=models.CharField(max_length=15)
	customer_email=models.CharField(max_length=15)
	customer_password=models.CharField(max_length=15)


class CustomerCard(models.Model):
	customer = models.ForeignKey("Customer",on_delete=models.CASCADE)
	product = models.ForeignKey("Product",on_delete=models.CASCADE)
	qty=models.IntegerField()

	def total(self):
		return self.qty * self.product.product_price



class Order(models.Model):
	customer=models.ForeignKey("Customer",on_delete=models.CASCADE)
	delivery_fname=models.CharField(max_length=100)
	delivery_lname=models.CharField(max_length=50)
	delivery_address=models.TextField()
	delivery_apartment=models.CharField(max_length=100)
	delivery_state_country=models.CharField(max_length=100)
	delivery_postal_zip=models.CharField(max_length=100)
	delivery_email_address=models.CharField(max_length=100)
	delivery_phone=models.CharField(max_length=100)
	payment_type=models.CharField(max_length=100)
	# order_date = models.DateField()

	
class OrderProducts(models.Model):
	product=models.ForeignKey("Product",on_delete=models.CASCADE)
	customer=models.ForeignKey("Customer",on_delete=models.CASCADE)
	order=models.ForeignKey("Order",on_delete=models.CASCADE)
	qty=models.IntegerField()



class Contact(models.Model):
	c_name=models.CharField(max_length=100)
	c_lname=models.CharField(max_length=50)
	c_email=models.CharField(max_length=30)
	c_message=models.CharField(max_length=100)