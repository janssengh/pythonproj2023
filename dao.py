#dao = Data Acess Objetct ou Objeto de Acesso a Dados
#módulo responsável pelo acesso ao banco de dados
import sqlite3

SQL_PREPARA_BANCO = 'create table if not exists produto (' \
                       'descricao varchar(60) not null,' \
                       'preco double not null,' \
                       'quantidade integer not null' \
                      ');'

SQL_SALVA_PRODUTO = 'insert into produto values (?, ?, ?)'
SQL_LISTA_PRODUTOS = 'SELECT DESCRICAO, PRECO, QUANTIDADE, ROWID FROM PRODUTO'
SQL_PRODUTO_POR_ID = 'SELECT DESCRICAO, PRECO, QUANTIDADE, ROWID FROM PRODUTO WHERE rowid=?'
SQL_ATUALIZA_PRODUTO = 'update produto set descicao=?, preco=?, quantidade=? where rowid=?'
SQL_DELETA_PRODUTO = 'delete from produto where rowid=?'

class ProdutoDao:

    def __init__(self, nome_banco):
        self.__nome_banco = nome_banco
        self.prepara_banco()

    def prepara_banco(self):
        print('Conectando com o banco de dados...', end='')
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_PREPARA_BANCO)
        #comitando senão nada terá efeito
        conexao.commit()
        print('OK')

    def salvar(self, produto):
        print('Salvando produto...', end='')
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_SALVA_PRODUTO, (produto.descricao, produto.preco, produto.quantidade))
        produto.id = cursor.lastrowid
        conexao.commit()
        print('OK')
        return produto #devolve o mesmo produto, porém agora com o id

    def listar(self):
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_LISTA_PRODUTOS)
        #converte a lista de dados em lista de objetos tipo Produto
        produtos = traduz_produtos(cursor.fetchall())
        return  produtos

def traduz_produtos(self, produtos):
    pass

