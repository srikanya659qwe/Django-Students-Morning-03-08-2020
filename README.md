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
  - 1.How to create Templates folder and ahow to access the files in templates folder
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
      - Internal => we should use styling within a head tag then it consists of style tag
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
   - 2.Accessing external css file that is tored in static folder
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
