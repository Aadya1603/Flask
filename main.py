from flask import Flask , redirect, url_for, render_template

### WSGI Application 
app=Flask(__name__)

@app.route('/')
def welcome():
    return"Welcome to my youtube channel"

@app.route('/success/<int:score>')
def success(score):
    return"<html><body><h1>The Result is passed </h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return"the person has failed and marks is" + str(score)


#result checker
@app.route('/results/<int:marks>')
def results(marks):
    results=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result , score= marks))

if __name__=='__main__':
    app.run(debug=True)


