from flask import Flask, render_template, request, redirect, url_for
from produto import Produto
from dao import ProdutoDao



#para instalar o flask por comando:
#1.acessar o terminal
#2.acessar venv: CD venv
#3.acessar scripts: CD scripts
#4.para visualizar arquivos: DIR
#5. .\pip install flask
#OU para instalar uma versão específica. Ex:
# .\pip install flask=2.0.2


produto_dao = ProdutoDao('bancodados.db')


#criar um app do flask
app = Flask(__name__)


@app.route('/')
def index():
    produto_dao.listar()
    return render_template('relatorio.html', titulo='Relatório estoque', produtos=[])

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
    produto = Produto(descricao, preco, quantidade)
    produto_dao.salvar(produto)
    print(f'id retornado: {produto.id}')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
