from requests import api, exceptions
from pokemon import *

def verificar_online(desejado):

    def pokeapi_online():
        try:
            resposta1 = api.get(f"{site_pokeapi}/api/v2/")
            if resposta1.status_code == 200 and resposta1.json()['pokemon'] == f'{site_pokeapi}/api/v2/pokemon/':
                return "online"
            return "zumbi"
        except exceptions.ConnectionError as x:
            return "offline"
        except:
            return "zumbi"

    def treinador_online():
        try:
            resposta2 = api.get(f"{site_treinador}/hello")
            if resposta2.status_code == 200 and resposta2.text == 'Pikachu, eu escolho você!':
                return "online"
            return "zumbi"
        except exceptions.ConnectionError as x:
            return "offline"
        except:
            return "zumbi"

    if site_treinador != "http://127.0.0.1:9000" or site_pokeapi != "http://127.0.0.1:8000": raise Exception("As URLs para as APIs estão incorretas.")
    y = pokeapi_online()
    z = treinador_online()

    if desejado == "pokeapi":
        if y == "zumbi" or z == "zumbi": raise Exception("Os servidores aparentemente não estão em funcionamento. Estes testes só devem ser executados com o pokeapi on-line e o treinador off-line.")
        if y == "offline" and z == "offline": raise Exception("O pokeapi está off-line. Estes testes só devem ser executados com o pokeapi on-line.")
        if y == "online" and z == "online": raise Exception("O treinador está on-line. Estes testes só devem ser executados com o treinador off-line.")
        if y == "offline" and z == "online": raise Exception("O pokeapi está off-line e o treinador on-line. Estes testes só devem ser executados com o pokeapi on-line e o treinador off-line.")
        assert y == "online" and z == "offline"
    elif desejado == "pokeapi+treinador":
        if y == "zumbi" or z == "zumbi": raise Exception("Os servidores aparentemente não estão em funcionamento. Estes testes só devem ser executados com ambos os servidores on-line.")
        if y == "offline" and z == "offline": raise Exception("Os servidores estão off-line. Estes testes só devem ser executados com ambos os servidores on-line.")
        if y == "online" and z == "offline": raise Exception("O treinador está off-line. Estes testes só devem ser executados com ambos os servidores on-line.")
        if y == "offline" and z == "online": raise Exception("O pokeapi está off-line. Estes testes só devem ser executados com ambos os servidores on-line.")
        assert y == "online" and z == "online"
    elif desejado == "offline":
        if y == "zumbi" or z == "zumbi": raise Exception("Há alguma coisa em execução nas portas dos servidores. Estes testes só devem ser executados com ambos os servidores off-line.")
        if y == "online" and z == "online": raise Exception("Os servidores estão on-line. Estes testes só devem ser executados com ambos os servidores off-line.")
        if y == "online" and z == "offline": raise Exception("O pokeapi está on-line. Estes testes só devem ser executados com ambos os servidores off-line.")
        if y == "offline" and z == "online": raise Exception("O treinador está on-line. Estes testes só devem ser executados com ambos os servidores off-line.")
        assert y == "offline" and z == "offline"
    else:
        assert False, "O teste deveria ser pokeapi, pokeapi+treinador ou offline."

def verificar_erro(interno, tipo_erro, tests = None):
    if tests is None:
        try:
            interno()
        except Exception as x:
            assert type(x) is tipo_erro, f"Esperava-se que um erro do tipo {tipo_erro.__name__}, mas obteve-se uma do tipo {x.__class__.__name__}."
        else:
            assert False, f"Esperava-se que um erro do tipo {tipo_erro.__name__} fosse produzido, mas não foi."
    else:
        try:
            interno()
        except Exception as x:
            tests.assertIs(type(x), tipo_erro, f"Esperava-se que um erro do tipo {tipo_erro.__name__}, mas obteve-se uma do tipo {x.__class__.__name__}.")
        else:
            tests.fail(f"Esperava-se que um erro do tipo {tipo_erro.__name__} fosse produzido, mas não foi.")

def pokemon_nao_existe(interno, tests = None):
    verificar_erro(interno, PokemonNaoExisteException, tests)

def pokemon_nao_cadastrado(interno, tests = None):
    verificar_erro(interno, PokemonNaoCadastradoException, tests)

def treinador_nao_cadastrado(interno, tests = None):
    verificar_erro(interno, TreinadorNaoCadastradoException, tests)

def pokemon_ja_cadastrado(interno, tests = None):
    verificar_erro(interno, PokemonJaCadastradoException, tests)

def valor_errado(interno, tests = None):
    verificar_erro(interno, ValueError, tests)

def assert_equals_unordered_list(esperada, obtida, tests = None):
    if tests is None:
        assert len(esperada) == len(obtida), f"Esperava-se que o resultado fosse {obtida}, mas foi {esperada}."
        for item in esperada:
            assert item in obtida, f"Esperava-se que o resultado fosse {obtida}, mas foi {esperada}."
    else:
        tests.assertEqual(len(esperada), len(obtida), f"Esperava-se que o resultado fosse {obtida}, mas foi {esperada}.")
        for item in esperada:
            tests.assertIn(item, obtida, f"Esperava-se que o resultado fosse {obtida}, mas foi {esperada}.")

class NoStdIO:
    def __init__(self):
        import sys
        self.__oout = sys.stdout
        self.__oin = sys.stdin
        self.__usou_print = False
        self.__usou_input = False

    def __enter__(self):
        import sys
        self.__oout = sys.stdout
        self.__oin = sys.stdin
        sys.stdout = self
        sys.stdin = self

    def __exit__(self, a, b, c):
        import sys
        sys.stdout = self.__oout
        sys.stdin = self.__oin

    def write(self, str):
        self.__usou_print = True
        return self.__oout.write(str)

    def readline(self):
        self.__usou_input = True
        return self.__oin.readline()

    def flush(self):
        pass

    @property
    def usou_print(self):
        return self.__usou_print

    @property
    def usou_input(self):
        return self.__usou_input

    def __call__(self, delegate):
        from functools import wraps
        @wraps(delegate)
        def sem_input(*args, **kwargs):
            with self:
                return delegate(*args, **kwargs)
        return sem_input

    def test_print(self, tests = None):
        if tests is None:
            assert self.usou_print == False, "Você não deveria utilizar a função print neste exercício."
        else:
            tests.assertFalse(self.usou_print, "Você não deveria utilizar a função print neste exercício.")

    def test_input(self, tests = None):
        if tests is None:
            assert self.usou_input == False, "Você não deveria utilizar a função input neste exercício."
        else:
            tests.assertFalse(self.usou_input, "Você não deveria utilizar a função print neste exercício.")

sem_io = NoStdIO()