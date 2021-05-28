# shrivis_resto
A Django Project

get MERCHANT KEY and MID from paytm and update it in shop/views.py before running the project.

Users:<br/>
	Username: user1<br/>
	Password: 1234<br/>
	Username: user2<br/>
	Password: 1234<br/>
Admin:
Username: shrivis<br/>
Password: pi314159<br/>

Potential Library Requirments<br/>
	pillow(pip install pillow)

Use the following payment details for payment<br/>
Mobile number: 77777 77777<br/>
Password: Paytm12345<br/>
OTP: 489871<br/>
Note: Do not try to make Payment with an official Paytm account or valid Debit/Credit card as of now.<br/>

How to run
1. Open CMD, PowerShell or Terminal/CommandShell of any IDE
2. Go to the root folder where manage.py file is located
3. Run command "python manage.py runserver"
4. Open any browser and go to 127.0.0.1:8000
5. You should be able to see the homepage

View Admin Panel
1. Run server
2. Open browser and visit 127.0.0.1:8000/admin
3. Login with provided username and password

Adding new menu items
1. Login as admin
2. Go to products
3. Click Add products and provide valid details of new product
4. To confirm visit homepage and look for added product

Changing Admin Password
1. Go to root folder
2. Run following command "python manage.py changepassword <user_name>"
3. Provide new password

Points to keep in mind
The payment gateway is for development purposes and must not be used for real-world payment as of now.
Payment failure occurs very often in the development environment, to succeed, make sure you fill all required fields and try again till it does.
for any query contact the writer.

By Vishal Srivastav aka Shrivis<br/>
Email:<br/>
vishalshrivastav52@gmail.com<br/>
shrivis@hotmail.com
