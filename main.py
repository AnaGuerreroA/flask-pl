from  flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    ip_usuario = request.remote_addr
    response = make_response(redirect('/welcome'))
    response.set_cookie('user_ip', user_ip)
    response.set_cookie('usuario_ip', ip_usuario)

    return response


@app.route('/home')
def hello():
    user_ip = request.cookies.get('user_ip')
    return render_template('hello.html', user_ip=user_ip)

@app.route('/welcome')
def welcome():
    ip_usuario = request.cookies.get('usuario_ip')

    return render_template('welcome.html', usuario_ip=ip_usuario)
    #return 'Hola hola maquinola, tu ip es {}'.format(ip_usuario)