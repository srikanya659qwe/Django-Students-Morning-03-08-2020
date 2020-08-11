# APSSDC-Django-Batch-4

[Click Here for syllabus](https://drive.google.com/file/d/1OnBUWHxKIa0ixTU8uKrWTGCE7HB3PbGl/view)

_____
### Day1(03-08-2020)
#### Day1 Content:
_____
- 1.Installation
  - download python exefile[for 64 bit os click here](https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe)
  - download python exefile[for 32 bit os click here](https://www.python.org/ftp/python/3.6.6/python-3.6.6.exe)
- 2.Function in pYthon 
- 3.OOP'S in Python
  - Class
  - Object
  - Constructors
  
 ____
### Day2(04-08-2020)
#### Day-2 content:
_____

- 1.inheritance with examples
- 2.Python modues with examples
- 3.Python Packages with examples

- if want to install django package
    - pip install django
- Sublime editor linke [click here](https://www.sublimetext.com/3)

 ____
### Day-3(05-08-2020)
#### Day-3 content:
_____

- 1.introdution about django
- 2.MVC, MVT,Architecture of Django
- 3.Project Creation, APP creation and use of
admin app
 - note:select project location in localmachine
  - Project creation Command is 
    - django-admin startproject projectname
    - ex:django-admin startproject demo
  - after creation of project move one step forward 
      - cd projectname
      - ex: cd demo
  - App creation
      - python manage.py startapp appname
      - ex:python manage.py startapp myapp
  - Server Running
      - python manage.py runserver
        -->http://127.0.0.1:8000/urlname or localhost:8000/urlname
        -->ex:http://127.0.0.1:8000/hello or localhost:8000/hello

_________
### Day-4(06-08-2020)
#### Day-4 content:
_________

  - 1.Displaying content by using HttpResponse
  - 2.Using html,css and javascript in HttpResponse
      - This changes can be done in single HttpResponse or else we can use it in different HttpResponses
      - html => views.py
      - ex: 
      ```python 
      def hello(request):
          return HttpResponse("<h1>Hello Welcome Users</h1>")
      ```
      - css => views.py
      - ex:
      ```python 
      def hi(request):
          return HttpResponse("<h1 style='background-color:black;color:white'>Welcome to Django Session</h1>")
      ```
      - javascript => views.py
      - ex:
      ```python 
      def wt(request):
          return HttpResponse("<script>alert("Welcome User")</script>")
      ```
  - 3.Passing 2 or more parameter values in url of a browser and displaying by using HttpResponse
      - single parameter value passing with data type
      - single parameter => urls.py
      - ex: 
      ```python 
         path("sg/<int:t>/",views.roll),
      ```
      - single parameter => views.py
      - ex: 
      ```views.py``` 
      ```python 
      def roll(request,t):
          return HttpResponse("Your roll number is: "+t) 
      ```
      - two parameters => urls.py
      - ex: 
      ```python 
         path("sg/<int:t>/<str:na>/",views.roll),
      ```
      - two parameters => views.py
      - ex: 
      ```views.py``` 
      ```python 
      def roll(request,t,na):
          return HttpResponse("Your roll number is: "+t+"<br>"+"Your name is: "+na) 
      ```
      - similarly for n parameters with different data types
      - string formatting
      - ex: 
      ```views.py```
      ```python
      def roll(request,t,na):
          return HttpResponse("Your roll number is: {}\n Your name is: {}".format(t,na))
      ```
_________
### Day-5(07-08-2020)
#### Day-5 content:
_________
  - 1.How to create Templates folder and how to access the files in templates folder
  - 2.Templates folder is created in inner of app in that we are saving all out .html files
  - 3.Useage of render method
     - ex:
     ```views.py```
     ```python
     def stu(request):
        //statements
        return render('httprequest','path of .html file',{'key':value})
    ```
  - 4.How to access the values from views to .html files
  ```html files```
  ```html
    <!DOCTYPE html>
    <html>
    <head>
  	  <title>Display Data</title>
    </head>
    <body>
      <h1>Your Username is: {{us}} </h1>
      <h3>Your email is: {{em}} </h3>
    </body>
    </html>
   ```
   ```
   DTL => Django Template Language
	  views => .html [DTL]
	  .html => hyperlink -> [DTL]
	{{variabename}}
	{% url '' %}
	{% for i in k %}
	{% endfor %}
  ```
   - 5.Brief Description of CSS with selectors like(id,tagnames,class etc.,)
      - Inline => we should use styling within a tag
      - ex:
      ```html
        <h1 style="background-color:green;color:blue">Hi Welcome</h1>
      ```
      - Internal => we should use styling within a head tag for that we need to use style tag inner of head tag
      - ex:
      ```sample example for Internal css```
      ```html
      <!DOCTYPE html>
      <html>
      <head>
          <title>Sample example for internal css</title>
          <style type="text/css">
          h1
          {
              background-color: black;
              color: white;
              margin-right: 30%;
              margin-left: 30%;
              padding:9px;
              margin-top:1px;
          }
          </style>
       </head>
       </html>
       ```
_________
### Day-6(08-08-2020)
#### Day-6 content:
_________

   - 1.Useage of External Css
    - Creating static folder in our app to access all files like .css,.js, images etc.,
   - 2.Accessing external css file that should be saved in static/css folder
      - ex: 
        appname/static/css => here css is defining to access only .css files similarly .js and images etc.  
        ```sample.css```
        ```css
        h2
        {
          background-color: cadetblue;
          color: white;
        }
        ```
   - 3.Accessing the external file in .html file.
      - For accessing the external files in .html first we need to load the static folder as ```{% load static %}```
      - After loading the static file then we need to mention in link tag for css
      - ex:
      	```sample.html```
      	```html
		{% load static %}
		<!DOCTYPE html>
		<html>
			<head>
			<title>Sample Example for External Css </title>
			<link rel="stylesheet" type="text/css" href="{% static 'css/sample.css' %}">
			</head>
			<body>
			<h2>welcome user </h2>
			</body>
		</html>
        ```
   - 4.Similar way we are accessing javascript also
   - 5.Navigation from url => views => template => views => templates
      - We need to create a url path and then views
      - ex:
        ```urls.py```
        ```python
        path('shr/',views.stu),
        ```
      - Before going to view just we need to create a form to submit the data to views
      - ex:
        ```registration.html```
        ```html
		{% load static %}
		<!DOCTYPE html>
		<html>
		<head>
		<title>Registration Form</title>
		<link rel="stylesheet" type="text/css" href="{% static 'css/sample.css' %}">
		</head>
		<body>
			<form method="POST">
			{% csrf_token %}
			<h2> User Registration </h2>
				<label>Username</label>
				<input type="text" name="uname"><br><br>
				<label>Password</label>
				<input type="password" name="pwd"><br><br>
				<label>Email</label>
				<input type="email" name="ml"><br><br>
			<button type="submit">register</button>
			</form>
		</body>
		</html>
        ```
      - In registration page we can observe forms tag in that we are passing the content from .html to views automatically when a button is clicked with method as POST 
      - For submitting the data to views we need to provide security for data so we are using ```{% csrf_token %}``` 
      - We need to create a function in views.py so the function name is stu
      - ex:
        ```views.py```
        ```python
	    def stu(request):
		if request.method == "POST":
			u = request.POST['uname']
			|         |           |
			//similarly
			d = {'us':u,.......}
			return render(request,'myApp/display.html',d) 
		return render(request,'myApp/registration.html')
        ```
      - So in views the data can be accessed from forms ie., .html with names so that names should be accessed in views.py 
      - The accessed data is formatted in the form of dictionary format with key and value pairs so just we are passing all the data in dictionary format to .html file
      - ex:
        ```display.html```
        ```html
		{% load static %}
		<!DOCTYPE html>
		<html>
		<head>
		<title>Display Data</title>
		</script>
		</head>
		<body>
		<h1>Your Username is: {{us}} </h1>
		//no of passed data from views that is gathered from .html
		</body>
		</html>
        ```
      - Here we need to access the data from views for that we need to use only key that should be in DTL language format to print the output in .html file
      
_________
### Day-7(10-08-2020)
#### Day-7 content:
_________
   - 1.Created another project to implement bootstrap tags and styling to it
   - 2.Bootstrap brief explanation, configuring in django project styling for it by using css and js
   - 3.Creation of user urls in userapp for creating the path within the app instead of admin urls
   - 4.For creating userapp urls we need to import some statements in admin app i.e., ```include()```
      - ex:
      ```admin app urls.py```
      ```python
	 from django.urls import path,include
      ```
   - 5.To include the method we need to set a particular userapp so we need to configure it first
      - ex:
      ```admin urls.py```
      ```python
	 path('',include('userappname.urls')),
      ```
   - 6.Then in userapp we can create our own urls path 
   - 7.Here we are just creating our own path and functions in views.py so just we are navigating to our .html files
   - 8.While navigating to .html here it self jusdt we are using dtl language to split scripts,navigation and body content in seperate files
      - Just we are creating scripts in header.html
      - ex:
      ```header.html```
      ```html
		{% load static %}
		<!DOCTYPE html>
		<html lang="en">
		<head>
		<title>{% block title %}{% endblock title %}</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="icon" type="text/css" href="{% static 'images/first.jpg' %}">
		<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
		<script type="text/javascript" src="{% static 'jquery/jq.js' %}"></script>
		<script src="{% static 'js/bootstrap.min.js' %}"></script>
		</head>
		<body>
		{% include 'userapp/navbar.html' %}
		{% block content %}
		{% endblock content %}
		</body>
		</html>
      ```
      - In DTL Language for accessing all the static fiels we need to load those by using ```{% load static %}``` and for title the pages will be different 
      and the names also to be changed so that we are using ```<title>{% block title %}{% endblock title %}</title>``` It automatically changes the title for each page
      - For accessing all the navbar link just we are using include to access those links so we had coded in another .html so that should be displayed so we need to acceess
      all those navbar for all pages so we had implemented in header.html file
      - To display the contents in body of each page so we are using dtl language ```{% block content %}{% endblock content %}``` within this we need to display all the 
      content of particular file
   - 9.Sample of navbar.html so here we need to use url namses to access the particualr path location to navigate so it performs some action that is written in views.py
     - ex:
     ```navbar.html```
     ```html
		{% load static %}
		<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
		<a class="navbar-brand" href="#">
	        <img src="{% static 'images/first.jpg' %}" alt="logo" style="width:40px;"></a>
		<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
		<span class="navbar-toggler-icon"></span></button>
		<div class="collapse navbar-collapse" id="collapsibleNavbar">
		<ul class="navbar-nav">
		<li class="nav-item">
		<a class="nav-link" href="{% url 'hme' %}">Home</a>
		</li>
		<li class="nav-item">
		<a class="nav-link" href="{% url 'ab' %}">Aboutus</a>
		</li>
		<li class="nav-item">
		<a class="nav-link" href="#">Contactus</a>
		</li>
		<li class="nav-item">
		<a class="nav-link" href="{% url 'rgi' %}">Register</a>
		</li>
		</ul>
		</div>
		</nav>
     ```
   - 10.In navbar for href's just we are using the names of url that should be different from the path
     - ex:
     ```python
        path('',views.home,name="hme")
     ```
   - 11.In home.html we need to extend html structure so the home.html consists with minimum number of lines of code
     - ex:
     ```home.html```	
     ```html
		{% extends 'userapp/header.html' %}
		{% load static %}
		{% block title %} Home {% endblock title %}
		{% block content %}
		<div class="container">
		<div class="jumbotron col-md-7" style="margin-top: 50px">
		<h1>My First Bootstrap Page</h1>
		<p>This is some text.</p>
		</div>
		</div>
		{% endblock content %}
     ```
   - 12.Similarly for the other files such as about,contact and etc., those files can be used in this format to reduce the number of codes of lines in particular .html
   instead of accessing all those scripts and navbar links
     - ex:
     ```aboutus.html```
     ```html
		{% extends 'userapp/header.html' %}
		{% block title %}About{% endblock title %}
		{% block content %}
		<div class="container">
		<div class="jumbotron" style="margin-top: 50px;">
		<h1>Welcome to About page</h1>
		</div>
		</div>
		{% endblock content %}
     ```
_________
### Day-8(11-08-2020)
#### Day-8 content:
_________
   - 1.Created a registration form for that we added url path in urls.py that is in userapp urls, some action in views.py and then that action to be displayed in 
   registration form
     - ex:
     ```urls.py```
     ```python
        path('reg/',views.regist,name="rg")
     ```
   - 2.In views just rendered to a file that is .html
     - ex:
     ```views.py```
     ```python
     def regist(request):
          return render(request,'userapp/register.html')
     ```
   - 3.In html file the content will be look like as shown below
     - ex:
     ```register.html```
     ```html
		{% extends 'userapp/header.html' %}
		{% block title %}Registration{% endblock title %}
		{% block content %}
		<div class="container">
		<div class="jumbotron col-md-6" style="margin: auto;margin-top:20px;">
		<h3> Register </h3>
		<form method="POST" action="#">
		<input type="text" name="uname" class="form-control col-md-10" placeholder="Enter Username"><br/>
		<input type="password" name="pwd" class="form-control col-md-10" placeholder="Enter Password"><br/>
		<input type="submit" class="btn btn-success" value="Submit">
		</form>
		</div>
		</div>
		{% endblock content %}
     ```
   - 4.So to enable a toggler then we need to use jquery for that we need to download and access in static folder way
   - 5.Description of Database,migrate and creation of superuser(i.e., Admin) logged into administration page
     - Useage of Administration page role based access in administration and how to create a users and to give permissions by using superuser(Admin)
