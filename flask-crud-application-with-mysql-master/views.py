from flask import Flask, render_template, request, redirect, url_for, flash
from __init__ import app, mysql

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM aluno")
    data = cur.fetchall()
    cur.close()




    return render_template('index.html', students=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")

        nome = request.form['nome']
        sexo = request.form['sexo']
        telefone = request.form['telefone']
        email = request.form['email']
        data_nascimento = request.form['data_nascimento']
        data_matricula = request.form['data_matricula']
        turma_fk = request.form['turma_fk']
        desconto = request.form['desconto']
        cur = mysql.connection.cursor()
        cur.execute("INSERT into aluno (nome, sexo, telefone, email, data_nascimento, data_matricula, turma_fk, desconto) values (%s, %s, %s, %s, %s, %s, %s, %s)", (nome, sexo, telefone, email, data_nascimento, data_matricula, turma_fk, desconto))
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM aluno WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id = request.form['id']
        nome = request.form['nome']
        sexo = request.form['sexo']
        telefone = request.form['telefone']
        email = request.form['email']
        data_nascimento = request.form['data_nascimento']
        data_matricula = request.form['data_matricula']
        turma_fk = request.form['turma_fk']
        desconto = request.form['desconto']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE aluno
               SET  nome = %s, sexo = %s , telefone= %s, email= %s, data_nascimento= %s, data_matricula= %s, turma_fk= %s , desconto= %s
               WHERE id=%s
            """, (nome, sexo, telefone, email, data_nascimento, data_matricula, turma_fk, desconto, id))
        flash("Atualizado com sucesso!")
        mysql.connection.commit()
        return redirect(url_for('Index'))

