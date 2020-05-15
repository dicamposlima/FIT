"""Model"""
import random
import shutil
import unittest
from math import floor
from typing import Tuple, List

import herois
import itens
import itens_do_heroi
from herois import HeroiNaoExisteException
from itens import ItemNaoExisteException


class OverpowerException(Exception):
    """Se o heroi for poderoso demais
    (a soma dos 3 atributos for maior que 20)"""
    pass


class HeroiJaUsaEsseTipoDeItemException(Exception):
    """ Se tentarmos colocar_item_em_uso em um chapeu quando o heroi já tem um
    chapeu em uso"""
    pass


def heroi_pronto_por_nome(nome_heroi: str) -> List:
    """
    recebe um nome de heroi e retorna
    um dicionario com todos os dados do heroi
    (por exemplo, a chave 'nome' conterá o valor
    da coluna 'nome' associada a essa id).

    se receber uma id invalida, a funcao levanta
    uma HeroiNaoExisteException (que voce deverá
    criar)
    Os dados do dicionario incluem os itens em uso.
    Se o heroi está usando um item que aumenta
    suas habilidades, as habilidades que aparecem no dicionario serão
    as do heroi, aumentadas de acordo com o item

    Por exemplo, considere um heroi com agilidade 2 e usando
    um item de agilidade 3. Para ele, o dicionario devera
    reportar agilidade 5
    repare, porem, que o item tem que ser do heroi e estar
    em uso para fazer efeito
    :param nome_heroi: nome do heroí a ser retornado
    :return: list com os dados do herói
    """
    heroi = herois.consultar_heroi_por_nome(nome_heroi)
    heroi['vida'] = heroi['fisico'] * 10
    itens_em_uso = lista_itens_em_uso_do_heroi(heroi['id'])
    if len(itens_em_uso) > 0:
        for item in itens_em_uso:
            heroi['fisico'] = heroi['fisico'] + item['fisico']
            heroi['magia'] = heroi['magia'] + item['magia']
            heroi['agilidade'] = heroi['agilidade'] + item['agilidade']
    return heroi


def atacar_com_fisico(atacante: dict, defensor: dict) -> Tuple:
    """
    A função atacar_com_fisico recebe dois dicionarios, de dois herois.
    (esses dicionarios sao os gerados pela funcao heroi_pronto_por_nome)
    O primeiro heroi é o atacante e o segundo é o defensor
    O defensor perde vida. A perda é igual ao atributo fisico do atacante.
    Se o atacante for muito mais rápido que o defensor,
    poderá atacar duas vezes
    Para isso, divida agilidade do atacante pela agilidade do defensor,
    arredondando para baixo.
    Se der algum número maior que 1, esse é o número de ataques
    que o atacante vai conseguir fazer.
    Se der 1 ou menos, o atacante conseguirá fazer exatamente 1 ataque.
    :param atacante: dicinário com os dados do atacante
    :param defensor: dicinário com os dados do defensor
    :return: um tupla com os dados do atacante e defensor alterados
    """
    ataques = floor(atacante['agilidade'] / defensor['agilidade'])
    if ataques <= 0:
        defensor['vida'] = defensor['vida'] - atacante['fisico']
    else:
        defensor['vida'] = defensor['vida'] - (atacante['fisico'] * ataques)
    if defensor['vida'] <= 0:
        defensor['vida'] = 0
    mensagem_de_ataque_fisico(defensor['vida'],
                              defensor['nome'],
                              atacante['nome'])
    return atacante, defensor


def atacar_com_magia(atacante: dict, defensor: dict) -> Tuple:
    """
    A função atacar_com_magia recebe dois dicionarios, de dois herois.
    (esses dicionarios sao os gerados pela funcao heroi_pronto_por_nome)
    O primeiro heroi é o atacante e o segundo é o defensor
    O defensor perde vida. A perda é igual ao atributo magia do atacante.
    Se o atacante for muito mais rápido que o defensor,
     poderá atacar duas vezes
    Para isso, divida agilidade do atacante pela agilidade do defensor,
    arredondando para baixo.
    Se der algum número maior que 1, esse é o número de ataques
    que o atacante vai conseguir fazer.
    Se der 1 ou menos, o atacante conseguirá fazer exatamente 1 ataque.
    :param atacante:
    :param defensor:
    :return: um tupla com os dados do atacante e defensor alterados
    """
    ataques = floor(atacante['agilidade'] / defensor['agilidade'])
    if ataques <= 0:
        defensor['vida'] = defensor['vida'] - atacante['magia']
    else:
        defensor['vida'] = defensor['vida'] - (atacante['magia'] * ataques)

    if defensor['vida'] <= 0:
        defensor['vida'] = 0
    mensagem_de_ataque_magico(defensor['vida'],
                              defensor['nome'],
                              atacante['nome'])
    return atacante, defensor


def lista_itens_do_heroi(id_heroi: int) -> List:
    """
    recebe uma id de heroi e retorna uma lista de todas as linhas
    da tabela ItemDoHeroi em que a id do heroi (coluna idHeroi)
    é igual à recebida.
    O retorno deve ser uma lista, com as linhas da tabela ItemDoHeroi,
    cada uma das linhas representada por um dicionario, com as chaves
    id, idHeroi e idItem
    :param id_heroi: o id do herói que terao os itens retornados
    :return: lista com os itens do herói
    """
    heroi = herois.consultar_heroi(id_heroi)
    herois_lista = []
    itens_dos_herois = itens_do_heroi.consulta_itens_por_heroi(id_heroi)
    if len(itens_dos_herois) <= 0:
        return herois_lista
    for item in itens_dos_herois:
        heroi_item = itens.consultar_item(item['idItem'])
        herois_lista.append(heroi_item)
    return herois_lista


def lista_itens_em_uso_do_heroi(id_heroi: int) -> List:
    """
    Um item está em uso quando o valor da coluna emUso é 1.
    Se for 0, o heroi tem o item mas não está usando.
    :param id_heroi: o id do herói que terao os itens retornados
    :return: lista com os itens em uso do herói
    """
    herois_itens = lista_itens_do_heroi(id_heroi)
    return [heroi_item
            for heroi_item in herois_itens
            if heroi_item['emUso']]


def criar_heroi(nome: str, agilidade: int, fisico: int, magia: int) -> None:
    """
    Recebe o nome e os atributos:
    Ela deve criar um heroi no banco de dados, com os atributos
    dados.
    Se o heroi for poderoso
    demais (a soma dos 3 atributos for maior que 20) nossa funcao
    criar_heroi devera lançar uma OverpowerException
    :param nome: nome do herói
    :param agilidade: agilidade do herói
    :param fisico: fisico do herói
    :param magia: magia do herói
    """
    if agilidade + fisico + magia > 20:
        raise OverpowerException
    herois.criar_heroi(nome, agilidade, fisico, magia)


def criar_item(tipo: str,
               nome: str, fisico: int, agilidade: int, magia: int) -> None:
    """
    Recebe um nome de item e devolve a id numerica correspondente
    :param tipo: tipo do item
    :param nome: nome do item
    :param fisico: fisico do item
    :param agilidade: agilidade do item
    :param magia: magia do item
    """
    itens.criar_item(tipo, nome, fisico, agilidade, magia)


def dar_item_para_heroi(heroi: dict, item: dict) -> None:
    """
    Faz com que o heroi se
    torne o dono (ou dona) do item. Ela recebe dois dicionarios:
    um do heroi e um do item.
    No itens_do_heroi, você adicionará uma linha nova,
    marcando que o item pertence ao heroi.
    :param heroi: dados do herói
    :param item: dados do item
    """
    itens_do_heroi.dar_item_para_heroi(heroi, item)


def colocar_item_em_uso(heroi: dict, item: dict) -> None:
    """
    Recebe o dicionario do heroi e o dicionario do item,
    e faz com que o item fique emUso.
    Um item só pode ficar em
    uso se o heroi nao está usando outro item do mesmo tipo
    Se tentarmos colocar_item_em_uso em um chapeu quando o heroi já
    tem um chapeu em uso, a funcao deve lancar
    o erro HeroiJaUsaEsseTipoDeItemException
    :param heroi: dados do herói
    :param item: dados do item
    """
    itens_em_uso = lista_itens_em_uso_do_heroi(heroi['id'])
    if len(itens_em_uso) > 0:
        if any([item_em_uso['tipo'] == item['tipo']
                for item_em_uso in itens_em_uso]):
            raise HeroiJaUsaEsseTipoDeItemException

        # for item_em_uso in itens_em_uso:
        # if item_em_uso['tipo'] == item['tipo']:
        # raise HeroiJaUsaEsseTipoDeItemException
        # break
    itens.colocar_item_em_uso(item)


'''
Voce terminou a atividade!

Agora, pode fazer tres coisas:
    * primeiro, experimentar os prints abaixo
    * depois, fazer o server.py receber dois nomes de lutadores
    e colocar eles pra brigar de verdade
    * terceiro: criar uma nova tabela,de ataques personalizados
    por exemplo "merlin sufoca harry com a sua barba" e
    "hulk esmaga conan". um heroi poderá ter um ou mais
    ataques personalizados, e deverá usar eles em vez/misturados
    com os genericos (como você preferir, porque isso nao
    será testado)
'''

'''
O uso das funcoes a seguir é opcional
'''


def mensagem_de_ataque_fisico(dano, nome_atacante, nome_defensor):
    """

    :param dano:
    :param nome_atacante:
    :param nome_defensor:
    """
    msgs = [f'{nome_atacante} dá um soco em {nome_defensor},'
            f'causando {dano} de dano',
            f'{nome_atacante} dá um chute em {nome_defensor},'
            f'causando {dano} de dano',
            f'{nome_atacante} ataca {nome_defensor} covardemente,'
            f'causando {dano} de dano']
    msg = msgs[random.randrange(0, len(msgs) - 1)]
    print(msg)


def mensagem_de_ataque_magico(dano, nome_atacante, nome_defensor):
    """

    :param dano:
    :param nome_atacante:
    :param nome_defensor:
    """
    msgs = [f'{nome_atacante} solta raios contra {nome_defensor},'
            f'causando {dano} de dano',
            f'{nome_atacante} congela {nome_defensor},'
            f'causando {dano} de dano',
            f'{nome_atacante} transforma {nome_defensor} em um flamingo,'
            f'causando {dano} de dano']
    msg = msgs[random.randrange(0, len(msgs) - 1)]
    print(msg)


def luta(atacante, defensor):
    """

    :param atacante:
    :param defensor:
    """
    while atacante['vida'] != 0 and defensor['vida'] != 0:
        if atacante['magia'] > atacante['fisico']:
            atacar_com_magia(atacante, defensor)
        else:
            atacar_com_fisico(atacante, defensor)
        print(f'Agora, {defensor["nome"]} tem {defensor["vida"]} de vida')
        atacante, defensor = defensor, atacante  # inverte


def merlin_versus_harry():
    merlin = heroi_pronto_por_nome('merlin')
    harry = heroi_pronto_por_nome('harry')
    luta(merlin, harry)


'''
Fim das funcoes de uso opcional

Inicio dos testes
'''


class TestStringMethods(unittest.TestCase):

    def test_02_pega_heroi(self):
        self.assertEqual(herois.consultar_heroi(1)['nome'], 'conan')
        self.assertEqual(herois.consultar_heroi(2)['nome'], 'merlin')
        self.assertEqual(herois.consultar_heroi(3)['nome'], 'harry')
        self.assertRaises(HeroiNaoExisteException,
                          herois.consultar_heroi, 50329)

    def test_03_pega_item(self):
        self.assertEqual(itens.consultar_item(1)['nome'], 'forca do gigante')
        self.assertEqual(itens.consultar_item(1)['tipo'], 'cinto')
        self.assertEqual(itens.consultar_item(2)['nome'], 'de alladin')
        self.assertEqual(itens.consultar_item(2)['tipo'], 'lampada')
        self.assertRaises(ItemNaoExisteException, itens.consultar_item, 329)

    def test_04_status_do_heroi(self):
        self.assertEqual(heroi_pronto_por_nome('conan')['fisico'], 3)
        self.assertEqual(heroi_pronto_por_nome('conan')['magia'], 2)
        self.assertEqual(heroi_pronto_por_nome('conan')['agilidade'], 5)
        self.assertEqual(heroi_pronto_por_nome('merlin')['fisico'], 3)
        self.assertEqual(heroi_pronto_por_nome('merlin')['agilidade'], 1)
        self.assertEqual(heroi_pronto_por_nome('merlin')['magia'], 8)

    def test_05_vida_do_heroi(self):
        self.assertEqual(heroi_pronto_por_nome('conan')['vida'], 30)
        self.assertEqual(heroi_pronto_por_nome('merlin')['vida'], 30)

    def test_06_ataque_fisico(self):
        conan = heroi_pronto_por_nome('conan')
        harry = heroi_pronto_por_nome('harry')
        self.assertEqual(harry['vida'], 20)
        atacar_com_fisico(atacante=conan, defensor=harry)
        self.assertEqual(harry['vida'], 17)
        atacar_com_fisico(atacante=conan, defensor=harry)
        self.assertEqual(harry['vida'], 14)
        atacar_com_fisico(defensor=conan, atacante=harry)
        self.assertEqual(conan['vida'], 28)

    def test_07_ataque_magico(self):
        merlin = heroi_pronto_por_nome('merlin')
        harry = heroi_pronto_por_nome('harry')
        self.assertEqual(harry['vida'], 20)
        atacar_com_magia(atacante=merlin, defensor=harry)
        self.assertEqual(harry['vida'], 12)
        atacar_com_magia(atacante=merlin, defensor=harry)
        self.assertEqual(harry['vida'], 4)
        atacar_com_magia(atacante=merlin, defensor=harry)
        self.assertEqual(harry['vida'], 0)

    def test_14_itens_do_heroi(self):
        self.assertEqual(len(itens_do_heroi.consulta_itens_por_heroi(1)), 2)
        self.assertEqual(len(itens_do_heroi.consulta_itens_por_heroi(3)), 1)
        self.assertEqual(len(itens_do_heroi.consulta_itens_por_heroi(2)), 0)
        item = itens_do_heroi.consulta_itens_por_heroi(3)
        item_do_3 = itens.consultar_item(item[0]['idItem'])
        self.assertEqual(item_do_3['tipo'], 'varinha')

    def test_15_lista_itens_do_heroi(self):
        self.assertEqual(len(lista_itens_do_heroi(1)), 2)
        self.assertEqual(len(lista_itens_do_heroi(3)), 1)
        self.assertEqual(len(lista_itens_do_heroi(2)), 0)
        self.assertRaises(HeroiNaoExisteException, lista_itens_do_heroi, 9999)
        item = lista_itens_do_heroi(1)
        lista_tipos = [item[0]['tipo'], item[1]['tipo']]
        self.assertIn('cinto', lista_tipos)
        self.assertIn('lampada', lista_tipos)

    def test_16_itens_que_heroi_esta_usando(self):
        self.assertEqual(len(lista_itens_em_uso_do_heroi(1)), 0)
        self.assertEqual(len(lista_itens_em_uso_do_heroi(3)), 1)
        self.assertEqual(len(lista_itens_em_uso_do_heroi(2)), 0)
        item = lista_itens_em_uso_do_heroi(3)
        item_do_3 = item[0]
        self.assertEqual(item_do_3['tipo'], 'varinha')

    def test_17_status_alterado_por_itens(self):
        self.assertEqual(heroi_pronto_por_nome('conan')['fisico'], 3)
        self.assertEqual(heroi_pronto_por_nome('conan')['magia'], 2)
        self.assertEqual(heroi_pronto_por_nome('conan')['agilidade'], 5)
        self.assertEqual(heroi_pronto_por_nome('harry')['fisico'], 2)
        self.assertEqual(heroi_pronto_por_nome('harry')['agilidade'], 4)
        self.assertEqual(heroi_pronto_por_nome('harry')['magia'], 7)
        self.assertEqual(heroi_pronto_por_nome('merlin')['fisico'], 3)
        self.assertEqual(heroi_pronto_por_nome('merlin')['agilidade'], 1)
        self.assertEqual(heroi_pronto_por_nome('merlin')['magia'], 8)

    def test_18_vida_do_heroi_alterado_por_itens(self):
        self.assertEqual(heroi_pronto_por_nome('conan')['vida'], 30)
        self.assertEqual(heroi_pronto_por_nome('merlin')['vida'], 30)
        self.assertEqual(heroi_pronto_por_nome('harry')['vida'], 20)

    def test_19_ataque_repetido_gracas_a_agilidade(self):
        merlin = heroi_pronto_por_nome('merlin')
        harry = heroi_pronto_por_nome('harry')
        self.assertEqual(merlin['vida'], 30)
        atacar_com_magia(atacante=harry, defensor=merlin)
        self.assertEqual(merlin['vida'], 2)
        atacar_com_magia(atacante=harry, defensor=merlin)
        self.assertEqual(merlin['vida'], 0)

    def test_21_criar_heroi(self):
        criar_heroi('van damma', agilidade=5, fisico=7, magia=0)
        dama = heroi_pronto_por_nome('van damma')
        self.assertEqual(dama['agilidade'], 5)
        self.assertEqual(dama['fisico'], 7)
        harry = heroi_pronto_por_nome('harry')
        atacar_com_magia(atacante=harry, defensor=dama)
        self.assertEqual(dama['vida'], 63)

    def test_22_criar_overpower(self):
        self.assertRaises(OverpowerException, criar_heroi,
                          'freeza', 10, 10, 10)
        self.assertRaises(OverpowerException, criar_heroi, 'legolas', 20, 2, 2)

    def test_23_nome_para_id_item(self):
        idDuelo = itens.nome_para_id_item('de duelo')
        duelo = itens.consultar_item(idDuelo)
        self.assertEqual(duelo['nome'], 'de duelo')
        idConfortavel = itens.nome_para_id_item('confortavel')
        confortavel = itens.consultar_item(idConfortavel)
        self.assertEqual(confortavel['nome'], 'confortavel')

    def test_24_criar_item(self):
        itens.criar_item(tipo='varinha', nome='mestra',
                         fisico=0, agilidade=0, magia=8)
        idMestra = itens.nome_para_id_item('mestra')
        mestra = itens.consultar_item(idMestra)
        self.assertEqual(mestra['nome'], 'mestra')
        self.assertEqual(mestra['id'], idMestra)
        self.assertEqual(mestra['magia'], 8)

    def test_25_dar_item_para_heroi(self):
        itens.criar_item(tipo='espada', nome='celestial',
                         fisico=3, agilidade=3, magia=3)
        dama = heroi_pronto_por_nome('van damma')
        idCelestial = itens.nome_para_id_item('celestial')
        celestial = itens.consultar_item(idCelestial)
        dar_item_para_heroi(heroi=dama, item=celestial)
        dama = heroi_pronto_por_nome('van damma')
        self.assertEqual(dama['agilidade'], 5)  # agilidade ainda nao mudou
        colocar_item_em_uso(dama, celestial)
        self.assertEqual(dama['agilidade'], 5)  # agilidade ainda nao mudou,
        # pois ainda nao fizemos uma nova consulta
        dama = heroi_pronto_por_nome('van damma')
        self.assertEqual(dama['agilidade'], 8)  # agilidade mudou
        # dama está usando o item e tb fizemos a nova consulta
        print('hey')

    def test_26_heroi_nao_pode_usar_dois_itens_do_mesmo_tipo(self):
        itens.criar_item(tipo='espada', nome='vorpal',
                         fisico=10, agilidade=2, magia=0)
        dama = heroi_pronto_por_nome('van damma')
        idVorpal = itens.nome_para_id_item('vorpal')
        vorpal = itens.consultar_item(idVorpal)
        dar_item_para_heroi(heroi=dama, item=vorpal)  # roda sem problemas
        # o que nao pode eh ela usar o item, porque ela ja tem outra varinha
        self.assertRaises(HeroiJaUsaEsseTipoDeItemException,
                          colocar_item_em_uso, dama, vorpal)


def runTests():
    shutil.copyfile('rpg.original.db', 'rpg.db')
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

if __name__ == '__main__':
    runTests()
