import sqlite3


class JogadorNaoExisteException(Exception):
    pass


def consultar_jogador(id_j):
    # 1o passo: criar uma conexao
    connection = sqlite3.connect("rpg.db")

    # 2o passo: pegar o cursor
    cursor = connection.cursor()

    # 3o passo: cursor.execute passando uma string de sql
    # (se for passar parametros, eles aparecem como ? na
    # string, e são passados por uma LISTA (no caso [id_j],
    # uma lista com um unico elemento)
    sql = "SELECT * FROM Jogador WHERE id = (?)"
    cursor.execute(sql, [id_j])

    # 4o passo: voce nao alterou nada e não
    # precisa fazer um connection.commit() <- isso fará sentido mais pra frente!
    #                                        (não se preocupe agora)
    # em vez disso, vamos olhar o resultado!

    jogador = cursor.fetchone()

    # se o resultado for None, a busca resultou vazia
    if jogador == None:
        raise JogadorNaoExisteException

    # 5o passo: fechar a conexao
    connection.close()

    return jogador
    # talvez fosse mais esperto retornar um dicionario?
    return {'id': jogador[0], 'nome': jogador[1], 'email': jogador[2]}


def conta_jogadores():
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM Jogador"
    # agora temos uma consulta que pode retornar muitos resultados
    cursor.execute(sql)

    # para ver quantos foram, basta pegar um a um
    # ate o resultado None

    # cada vez que eu faço o comando fechone, eu pego
    # uma linha nova, e se nao houver mais linhas,
    # eu recebo None
    jogadores = 0
    while (cursor.fetchone() != None):
        jogadores += 1

    connection.close()
    return jogadores


print(f"temos {conta_jogadores()} jogadores na base de dados no momento")


def consultar_jogador_por_email(email):
    connection = sqlite3.connect("rpg.db")
    connection.row_factory = sqlite3.Row  # aqui temos
    # uma opcao que faz o sqlite retornar dicionarios (ou coisa similar)
    cursor = connection.cursor()
    sql = "SELECT * FROM Jogador WHERE email = (?)"
    cursor.execute(sql, [email])

    jogador = cursor.fetchone()

    if jogador == None:
        raise JogadorNaoExisteException

    connection.close()

    return jogador


'''
Resumindo:
    Conectar ao banco para fazer select envolve 5 passos

    #1o passo: criar uma conexao
    connection = sqlite3.connect("rpg.db")
    
    #2o passo: pegar o cursor
    cursor = connection.cursor()
    
    #3o passo: cursor.execute passando uma string de sql
    #(se for passar parametros, eles aparecem como ? na
    #string, e são passados por uma LISTA
    sql = "SELECT * FROM Jogador WHERE email = (?)"
    cursor.execute(sql, [email])



    #4o passo: 
    * Usar fetchone para pegar um dado. O fetchone retorna uma linha se
    existir (e passa pra proxima). Retorna None se não existir mais nenhuma
    linha na consulta.
    
    while (cursor.fetchone() != None):
        jogadores += 1

    O retorno do fetchone é uma lista com uma posicao por coluna. Ex:
    jogador = cursor.fetchone()
    return {'id':jogador[0],'nome':jogador[1],'email':jogador[2]}

    
    #5o passo: fechar a conexao
    connection.close()

'''
