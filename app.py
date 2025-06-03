from flask import Flask, render_template, request, redirect
import sqlite3
import os

banco=sqlite3.connect('BancoSite.db')
cursor = banco.cursor()

app = Flask(__name__,static_folder='static')

@app.route('/cadastro')
def cadastro ():
    return render_template("cadastro.html")

@app.route('/exclusao')
def exclusao ():
    return render_template("excluiprato.html")

@app.route('/admin', methods=['POST','GET'])
def admin ():
    params = request.form
    id=params.get('id')
    dia=params.get('dia')
    prato1=params.get('prato1')
    descrição1=params.get('descrição1')
    valor1=params.get('valor1')
    prato2=params.get('prato2')
    descrição2=params.get('descrição2')
    valor2=params.get('valor2')
    sobremesa=params.get('sobremesa')
    descriçãosobremesa=params.get('descriçãosobremesa')
    valorsobremesa=params.get('valorsobremesa')
    bebida=params.get('bebida')
    descriçãobebida=params.get('descriçãobebida')
    valorbebida=params.get('valorbebida')
    sql=f"insert into pratos values ({id},'{dia}','{prato1}','{descrição1}',{valor1},'{prato2}','{descrição2}',{valor2},'{sobremesa}','{descriçãosobremesa}',{valorsobremesa},'{bebida}','{descriçãobebida}',{valorbebida})"
    con=sqlite3.connect("BancoSite.db")
    cur=con.cursor()
    cur.execute(sql)
    con.commit()
    return "Cadastrado com sucesso <br> <a href='http://127.0.0.1:5000/index'>Ok</a>"

@app.route('/excluir', methods=['POST','GET'])
def apagarprato():
    id=request.form.get('id')
    sql="delete from pratos where id="+id; 
    con=sqlite3.connect("BancoSite.db")
    cur=con.cursor()
    cur.execute(sql)
    con.commit()
    return "Excluido com sucesso <br> <a href='http://127.0.0.1:5000/index'>Ok</a>"

@app.route('/consulta')
def consulta():
    con=sqlite3.connect("BancoSite.db")
    cur=con.cursor()
    cur.execute("select * from pratos")
    dados=cur.fetchall()
    x=str()
    for p in dados:
        x=(str(p) + "<br>") + x
    return '{}'.format(x) + "<br><a href='.'><p>voltar<p><a>"

@app.route('/')
@app.route('/index') 
def index():
    return render_template("index.html")


@app.route('/patri')
def patriocinadores():
    return render_template("patri.html") 

@app.route('/login')
def login():
    return render_template("index_login.html")

@app.route('/cadastrar')
def cadastrar():
    return render_template("index_cadastro.html")

@app.route('/port_guilherme')
def portguilherme():
    return render_template("port.html")

@app.route('/port_luigi')
def portluigi():
    return render_template("port_luigi.html")

@app.route('/port_luis')
def portluis():
    return render_template("port_luis.html")

@app.route('/port_nonas')
def portnonas():
    return render_template("vini.html")


@app.route('/exibir')
def exibir ():
    return render_template("exibir.html")



if __name__ == "__main__":
 app.run(debug=True)
