from flask import Flask, render_template, request, session

app= Flask('__name__')
app.secret_key = '12345'

@app.errorhandler(404)
def err_handler(e):
    return render_template('404.html')

@app.route('/', defaults={'nom': 'Usuario'})

@app.route('/<nom>')
def index(nom):
    usuario={}
    
    if 'user' in session:
        usuario= session['user']
    
    
    
    nombre = nom
    nombres= ['andi' , 'johan']
    dic = {
        'names':['johan','maria','juan'],
        'ages': [25,22,21]
    }
    return render_template('index.html', name=nombre, names=nombres, values=dic, usuario=usuario)

@app.route('/clientes', defaults={'cli': 'cliente 1', 'pro': 'producto 1'})

@app.route('/clientes/<cli>/<pro>')
def clientes(cli,pro):
    clientes=cli
    producto=pro 
    return render_template('clientes.html', client=clientes, product=producto)

@app.route('/register', methods=['GET', 'POST'])
def register():
    user= {
        'name': '',
        'email': ''          
    }
    if request.args:
        user['name']= request.args['nombre']
        user['email']= request.args['correo']
        
        
    if request.method =='POST':
        user['name']= request.form['nombre']
        user['email']= request.form['correo']
        
    session['user'] = user
        
    return render_template('register.html', usuario=user)

if __name__=='__main__':
    app.run()