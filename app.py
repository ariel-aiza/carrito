from flask import Flask, render_template,request,session,redirect,url_for

app=Flask(__name__)
#necesario cuando se usa session
app.secret_key = 'unaclavesecreta'

@app.route("/")
def carrito():
    #verificando si lista esta en la sesion
    if 'lista' not in session:
        #inicializar la lista
        session['lista'] = []
    return render_template('index.html',lista = session['lista'])

@app.route("/procesa",methods=['GET','POST'])
def procesa():
    producto=request.form.get("producto")
    if 'lista' in session and producto:
        #producto adicionado en la lista
        session['lista'].append(producto)
        #aseguramos q la sesion a sido modificada
        session.modified=True
    return redirect(url_for("carrito"))

@app.route("/vaciar",methods=["GET"])
def vaciar():
    #elimina de sesion lista
    session.pop("lista",None)
    return redirect(url_for("carrito"))
if __name__ == "__main__":
    app.run(debug=True)

