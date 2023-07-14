from flask import Flask, render_template, request, jsonify
import operacion as o
import db

app = Flask(__name__)

db = db.db_init()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/billetera/contactos', methods=["GET"])
def get_contactos():
    args = request.args
    minumero = args.get('minumero')
    if minumero is None:
        return render_template('contactos.html',data={'ok' : False , 'msg': 'missing minumero!'})
    
    if minumero not in db.keys():
        return render_template('contactos.html',data={'ok' : False , 'msg': 'no existe la cuenta!'})
    cuenta = db[minumero]
    contactos = cuenta.contactos
    names = [db[name].nombre for name in contactos]
    data = [contactos, names]

    return render_template('contactos.html',data={'ok' : True, 'data': data}, n=len(data[0]))


@app.route('/billetera/pagar', methods=["GET"])
def transaccion():
    args = request.args
    minumero = args.get('minumero')
    numerodestino = args.get('numerodestino')
    valor = args.get('valor')
    if minumero is None:
        return render_template('pagar.html',data={'ok' : False , 'msg': 'missing minumero!'})
    if numerodestino is None:
        return render_template('pagar.html',data={'ok' : False , 'msg': 'missing numerodestino!'})
    if valor is None:
        return render_template('pagar.html',data={'ok' : False , 'msg': 'missing valor!'})
    
    if numerodestino not in db.keys():
        return render_template('pagar.html',data={'ok' : False , 'msg': 'no existe la cuenta receptora'})
    if minumero not in db.keys():
        return render_template('pagar.html',data={'ok' : False , 'msg': 'no existe la cuenta emisora'})
    
    if valor <= 0:
        return render_template('pagar.html',data={'ok' : False , 'msg': 'No puede enviar 0 soles o menos'})

    cuentae = db[minumero]
    cuentar = db[numerodestino]

    succes, fecha = cuentae.pagar(cuentar, valor)

    if not succes:
        return render_template('pagar.html',data={'ok' : False , 'msg': 'Algo salio mal en su operacion !'})

    return render_template('pagar.html',data={'ok' : True, 'data': fecha} )

@app.route('/billetera/historial', methods=["GET"])
def get_historial():
    args = request.args
    minumero = args.get('minumero')
    if minumero is None:
        return render_template('historial.html',data={'ok' : False , 'msg': 'missing minumero!'})
    
    if minumero not in db.keys():
        return render_template('historial.html',data={'ok' : False , 'msg': 'no existe la cuenta!'})
    
    cuenta = db[minumero]
    
    return render_template('historial.html',data={'ok' : True, 'operaciones': cuenta.operaciones, 'saldo': cuenta.saldo, 'nombre': cuenta.nombre } )
if __name__ == '__main__':
    app.run(debug=True, port=5000)