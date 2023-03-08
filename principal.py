from flask import Flask, render_template, request

from produto import Produto

#para instalar o flask por comando:
#1.acessar o terminal
#2.acessar venv: CD venv
#3.acessar scripts: CD scripts
#4.para visualizar arquivos: DIR
#5. .\pip install flask
#OU para instalar uma versão específica. Ex:
# .\pip install flask=2.0.2

p1 = Produto('TV LG 50"', 3999, 5)
p2 = Produto('CELULAR Samsung', 1999, 10)
p3 = Produto('Geladeira Brastemp', 1500, 3)

#         0   1   2
lista = [p1, p2, p3]
print(p1)




#criar um app do flask
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('relatorio.html', titulo='Relatório estoque', produtos=lista)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo='Cadastra Novo Produto')

@app.route('/editar')
def editar():
    return '<h1>Alteração de produto</h1>'

@app.route('/salvar', methods=['POST'])
def salvar():
    id = request.form['id']
    descricao = request.form['descricao']
    preco = request.form['preco']
    quantidade = request.form['quantidade']
    print(id, descricao, preco, quantidade)

    return '<h1>Salvando....</h1>'

if __name__ == '__main__':
    app.run(debug=True)
