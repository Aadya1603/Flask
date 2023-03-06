#Introduction to Flask 

#   Flask was created by Armin Ronacher in 2010 as an April Fool's joke. However,
#   it quickly gained popularity among developers and became a serious project. 
#   Flask was originally inspired by the Ruby on Rails framework, but it was designed to be more 
#   lightweight and flexible. Today, Flask is one of the most popular web application frameworks in Python.



#Architecture of Flask:

#   Flask is built using the WSGI (Web Server Gateway Interface) toolkit and follows the Model-View-Controller
#   (MVC) architectural pattern. This means that Flask separates the concerns of data, presentation,
#   and control, making it easy to manage large web applications. Flask uses Jinja2 as its templating engine, 
#   which allows developers to create dynamic HTML pages using Python code.



#Techniques used in Flask:

#Flask uses several techniques to make web development easier and more efficient.
# Some of these techniques include:

# Routing: Flask uses a routing system that maps URLs to Python functions. 
#   This allows developers to create clean, readable URLs for their web applications.
# Templates: Flask uses templates to create dynamic HTML pages. Templates allow developers to 
#   separate the presentation logic from the application logic, making it easier to manage and maintain web 
#   applications.
# Forms: Flask provides a built-in form handling system that makes it easy to create and process HTML forms.
# Extensions: Flask supports a wide range of extensions that add functionality to web applications.
#   Some popular extensions include Flask-SQLAlchemy for database management, Flask-WTF for form handling,
#   and Flask-RESTful for building RESTful APIs.




#Examples of Flask Applications:

#Flask is used to build a wide range of web applications, from simple blogs to complex e-commerce platforms.


# Here are some examples of real-world Flask applications:

#Reddit: Reddit is a popular social news aggregation website that was originally built using Python and Flask.
#Pinterest: Pinterest is a social media platform that allows users to share and discover images and videos. 
#   The platform is built using Python and Flask.
#Twilio: Twilio is a cloud communications platform that allows developers to build SMS, voice, and
#    video applications. Twilio's API is built using Python and Flask.
#Netflix: Netflix is a streaming video platform that uses Python and Flask for its microservices architecture.
#   Overall, Flask is a versatile and powerful web application framework that is widely used in the Python
#   community. Its simplicity, flexibility, and large ecosystem of extensions make it a great choice for building 
#   web applications of all sizes and complexity.




#Here's a simple example of a Flask web application that displays "Hello, World!" when the user navigates 
#   to the home page:


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()


#In this example, we first import the Flask module and create a new instance of the Flask class.
#  We then define a route for the home page ("/") using the @app.route decorator. When a user navigates
#  to the home page, Flask calls the hello function and returns the string "Hello, World!" as the response.

#Finally, we start the Flask development server using the app.run() method. When we run this code,
#  we can navigate to http://localhost:5000 in our web browser and see the "Hello, World!" message 
#  displayed on the page.