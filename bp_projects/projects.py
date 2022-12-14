from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/portfolio/')
def portfolio():
    return render_template("portfolio.html")

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")

@app_projects.route('/walruses/')
def walruses():
    return render_template("walruses.html")

@app_projects.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

@app_projects.route('/shirt/')
def shirt():
    return render_template("shirt.html")

@app_projects.route('/options/')
def options():
    return render_template("options.html")

@app_projects.route('/pants/')
def pants():
    return render_template("pants.html")

@app_projects.route('/co/')
def co():
    return render_template("co.html")

@app_projects.route('/jew/')
def jew():
    return render_template("jew.html")

@app_projects.route('/cart/')
def cart():
    return render_template("cart.html")

@app_projects.route('/cart2/')
def cart2():
    return render_template("cart2.html")

@app_projects.route('/cart3/')
def cart3():
    return render_template("cart3.html")

@app_projects.route('/wow/')
def wow():
    return render_template("wow.html")

@app_projects.route('/reviews/')
def reviews():
    return render_template("reviews.html")

@app_projects.route('/cart102/')
def cart102():
    return render_template("cart102.html")

@app_projects.route('/cart101/')
def cart101():
    return render_template("cart101.html")

@app_projects.route('/cart100/')
def cart100():
    return render_template("cart100.html")
    
@app_projects.route('/fakeop/')
def fakeop():
    return render_template("fakeop.html")

@app_projects.route('/welcome/')
def welcome():
    return render_template("welcome.html")