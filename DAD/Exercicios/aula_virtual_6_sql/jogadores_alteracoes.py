import sqlite3


#1o passo: criar uma conexao
connection = sqlite3.connect("rpg.db")


#2o passo: pegar o cursor
cursor = connection.cursor()


#3o passo: cursor.execute passando uma string de sql
create_sql = """
CREATE TABLE IF NOT EXISTS Jogador (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
"""
cursor.execute(create_sql)


#4o passo: fazer o commit (se for uma query que altera o banco)
connection.commit()


#5o passo: fechar a conexao
connection.close()

def criar_jogador(nome,email):

    #1o passo: criar uma conexao
    connection = sqlite3.connect("rpg.db")
    
    #2o passo: pegar o cursor
    cursor = connection.cursor()
    try:
        #3o passo: cursor.execute passando uma string de sql
        #(se for passar parametros, eles aparecem como ? na
        #string, e são passados por uma LISTA
        #no caso a lista [nome,email]
        sql_criar = "INSERT INTO Jogador (nome,email) VALUES (?, ?)"
        cursor.execute(sql_criar, [nome,email])

        # Repare que a minha query nao especificou uma coluna: a ID do usuário
        # o sqlite está preenchendo essa coluna sozinho
        
        
        #4o passo: se voce alterou alguma coisa
        #precisa fazer um connection.commit()
        connection.commit()

    except sqlite3.IntegrityError as e:
        print('o sql está reclamando que o jogador ja foi criado')
        print('o email em questão: '+email)
    #5o passo: fechar a conexao
    connection.close()


from jogadores_select import consultar_jogador
def alterar_jogador(id_j,novos_dados):
    #antes de mais nada eu faço um localizar, pra garantir 
    #que o usuario realmente existe
    #se nao existir, o localizar faz o exception pra mim
    #e aborta a execução da funcao
    consultar_jogador(id_j)
    connection = sqlite3.connect("rpg.db")
    #1o passo: criar uma conexao
    cursor = connection.cursor()
    #2o passo: pegar o cursor
    sql = "UPDATE Jogador SET nome=?, email=? WHERE id = ?"
    cursor.execute(sql, [novos_dados['nome'],novos_dados['email'],id_j])
    #3o passo: cursor.execute passando uma string de sql
    #(se for passar parametros, eles aparecem como ? na
    #string, e são passados por uma LISTA

    #4o passo: se vc alterou alguma coisa
    #precisa fazer um connection.commit()
    connection.commit()
    #TAE AC2 (brasileirao), AC3 (omdb)
    #AC8 será TAE (lms com sistemas distribuidos)
    #AC9 será TAE (lms2 com sistemas distribuidos)

    
    connection.close()
    #5o passo: fechar a conexao


def remover_jogador(id_j):
    #antes de mais nada eu faço um localizar, pra garantir 
    #que o usuario realmente existe
    #se nao existir, o deletar faz o exception pra mim
    #e aborta a execução da funcao
    consultar_jogador(id_j)
    connection = sqlite3.connect("rpg.db")
    #1o passo: criar uma conexao
    cursor = connection.cursor()
    #2o passo: pegar o cursor
    sql = "DELETE FROM Jogador WHERE id = ?"
    cursor.execute(sql, [id_j])
    #3o passo: cursor.execute passando uma string de sql
    #(se for passar parametros, eles aparecem como ? na
    #string, e são passados por uma LISTA

    #4o passo: se vc alterou alguma coisa
    #precisa fazer um connection.commit()
    connection.commit()

    
    connection.close()
    #5o passo: fechar a conexao






'''
Resumindo:
    * conectar ao banco para fazer um delete, update ou insert envolve 5 passos

    connection = sqlite3.connect("rpg.db")
    #1o passo: criar uma conexao
    
    cursor = connection.cursor()
    #2o passo: pegar o cursor
    
    sql = "DELETE FROM Jogador WHERE id = ?"
    cursor.execute(sql, [id_j])
    #3o passo: cursor.execute passando uma string de sql
    #(se for passar parametros, eles aparecem como ? na
    #string, e são passados por uma LISTA

    #4o passo: se vc alterou alguma coisa (fez delete, update ou insert)
    #precisa fazer um connection.commit()
    connection.commit()

    
    connection.close()
    #5o passo: fechar a conexao

    * se for fazer um select, o passo 4 muda. Em vez de fazer commit,
    fará fetchone para pegar um dado. O fetchone retorna uma linha se
    existir (e passa pra proxima). Retorna None se não existir mais nenhuma
    linha na consulta.
    
    while (cursor.fetchone() != None):
        jogadores += 1

    O retorno do fetchone é uma lista com uma posicao por coluna. Ex:
    jogador = cursor.fetchone()
    return {'id':jogador[0],'nome':jogador[1],'email':jogador[2]}
'''

'''
Sobre a arquitetura:
    a arquitetura desses arquivos jogador está sem sentido
    ninguém separaria a parte dos selects da parte das alteraçoes.

    normalmente se coloca todos os acessos de banco da mesma entidade
    num mesmo arquivo, usando uma classe (padrao de projeto DAO)

    Por motivos didaticos, nao fizemos isso aqui
'''
