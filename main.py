from flask import Flask, render_template, Blueprint,request, url_for, flash, redirect
from website.views import views_blueprint
#from website import views
app = Flask(__name__)
app.config['SECRET_KEY'] = 'rg@#$%RGETF43r3V34rF34tg43G$%^b44g3'

app.register_blueprint(views_blueprint)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

