from flask import Flask, redirect, url_for, request, render_template, session, send_from_directory, jsonify, make_response
from time import gmtime, strftime, sleep
import bcrypt
import os

application = Flask(__name__)

@application.route('/')
def root():
    return render_template("index.html")

@application.route('/shop')
def shop():
    return render_template("shop.html")

@application.route('/product/<name>')
def product(name):
    return render_template(str(name)+'.html')




















##ignore it's bad i know
@application.route('/shop.min.css')
def shopImg():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                                'shop.min.css')

@application.route('/VIP.webp')
def vip():
   return send_from_directory(os.path.join(application.root_path, 'static'),
                               'VIP.webp') 

@application.route('/script.min.js')
def script():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'script.min.js')

@application.route('/intro-bg.webp')
def introbg():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'intro-bg.webp')

@application.route('/downloads-bg.webp')
def downloadsbg():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'downloads-bg.webp')

@application.route('/bootstrap.min.css')
def bootstrap():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'bootstrap.min.css')

@application.route('/Product-Details.css')
def productDetails():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'Product-Details.css')

@application.route('/Animated-Pretty-Product-List-v12.css')
def PrettyProduct():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                               'Animated-Pretty-Product-List-v12.css')

if __name__ == '__main__': ##Starts server
    application.run(host='0.0.0.0', port=5000, debug=True)
