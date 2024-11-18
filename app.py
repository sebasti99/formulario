from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
import pymysql.cursors

app = Flask(__name__)



def connect_to_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='proveedores',
        cursorclass=pymysql.cursors.DictCursor,
        ssl_disabled=True
    )

@app.route('/')
def index():
        
    return render_template('index.html')


@app.route('/agregar',methods=["GET","POST"])
def ingreso():
    if request.method=="POST":
        codigo=request.form["codigo"]
        Nombre=request.form["Nombre"]
        try:
            conn = connect_to_db()
            cur = conn.cursor() 
            cur.execute("INSERT INTO categoria (codigo,Nombre) VALUES (%s, %s)",
                        (codigo,Nombre))
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('consulta'))
        except Exception:
            return redirect(url_for('index'))
    return render_template('formu.html')
      
@app.route('/consulta')
def consulta():
    try:
        conn = connect_to_db()
        cur = conn.cursor() 
        cur.execute("SELECT * FROM categoria ")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('reporte.html', categorias=data)
    except Exception:
        return render_template('reporte.html', categorias=[])
        
@app.route('/ingresa',methods=["GET","POST"])
def ingresa():
    if request.method=="POST":
        codigo=request.form["codigo"]
        Direccion=request.form["Direccion"]
        Ciudad=request.form["Ciudad"]
        Provincia=request.form["Provincia"]
        try:
            conn = connect_to_db()
            cur = conn.cursor() 
            cur.execute("INSERT INTO proveedor (codigo,Direccion,Piudad,Provincia) VALUES (%s, %s, %s, %s)",
                        (codigo,Direccion,Ciudad,Provincia))
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('index'))
        except Exception:
            return redirect(url_for('index'))
    return render_template('formu2.html')
      
@app.route('/consultar')
def consultar():
    try:
        conn = connect_to_db()
        cur = conn.cursor() 
        cur.execute("SELECT * FROM proveedor ")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('reporte2.html', proveedores=data)
    except Exception:
        return render_template('reporte2.html', proveedores=[])

if __name__ == '__main__':
    app.run(debug=True)