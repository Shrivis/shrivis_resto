# shrivis_resto
A Django Project

get MERCHANT KEY and MID and update it in shop/views.py before running the project.

Users:
	Username: user1
	Password: 1234
	Username: user2
	Password: 1234

Potential Library Requirments
	pillow(pip install pillow)

Use the following payment details for payment
Mobile number: 77777 77777
Password: Paytm12345
OTP: 489871
Note: Do not try to make Payment with an official Paytm account or valid Debit/Credit card.

How to run
1. Open CMD, PowerShell or Terminal/CommandShell of any IDE
2. Go to the root folder where manage.py file is located
3. Run command "python manage.py runserver"
4. Open any browser and goto 127.0.0.1:8000
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
The project is in the early development stage and doesn't contain proper form validation. Please fill in all fields or it may result in an error.
Payment gateway is for development purposes and must not be used for real-world payment as of now.
Payment failure occurs very often in the development environment, to succeed, make sure you fill all required fields and try agian till it does.
for any query contact the writer.

By Vishal Srivastav
Email: vishalshrivastav52@gmail.com
Email: shrivis@hotmail.com
*************************************************************************END*************************************************************************
