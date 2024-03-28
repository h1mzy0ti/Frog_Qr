from flask import Flask, render_template, request, Response ,url_for, redirect, send_file, send_from_directory
import pyqrcode 
import png 
from pyqrcode import QRCode 

app = Flask(__name__)

def gen(url):
 
        # Generate QR code 
        gurl = pyqrcode.create(url)
  
        gurl.svg("myqr.svg", scale = 8) 
  
        gurl.png('myqr.png', scale = 6) 

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        if request.form['url']:
            u_url = request.form['url']
            gen(u_url)
            return redirect(url_for('download'))
        else:
            return render_template('index.html', error='Invalid url')
    else:
        return render_template('index.html')

@app.route("/download", methods=["POST","GET"])
def download():
    if request.method == 'POST':
        if 'feedimg' in request.form:
            if request.form['feedimg'] == 'submit_button':
       
                return send_file('myqr.png', as_attachment=True)
        else:
            return "Button not found in request"
    else:
        return render_template('download.html')




if __name__ == '__main__':
    app.run(debug=True)






















def generate():
    user_inp = input("Enter")

    