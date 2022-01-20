from flask import Flask,render_template

app=Flask(__name__)

@app.route('/', methods=['GET'] )
def paginaPrincipal():
    return "Hola Mudo!"

@app.route('/dojo',methods=['GET'])
def paginaDojo():
    return "Dojo!"

@app.route('/say/<nombre>',methods=['GET'])
def paginaNombre(nombre):
    name=str(nombre)
    print(type(nombre))
    return "Hola, " + nombre+"!"

@app.route('/repeat/<int:num>/<cadena>',methods=['GET'])
def repetirPalabra(num,cadena):
        string=str(cadena)
        print(type(num))
        print(type(cadena))
        return render_template( "index.html",  numero=num, palabra=string )


if __name__ == "__main__":
    app.run( debug=True )