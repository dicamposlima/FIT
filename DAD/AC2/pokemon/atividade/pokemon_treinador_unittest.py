import unittest
from requests import api
from pokemon_teste_base import *

verificar_online("pokeapi+treinador")

class TestTreinador(unittest.TestCase):

    def reset(self):
        resposta = api.post(f"{site_treinador}/reset")
        self.assertEqual(resposta.status_code, 200)

    @sem_io
    def test_09a_ok(self):
        self.reset()

        treinador_nao_cadastrado(lambda : detalhar_treinador("Ash Ketchum"), self)
        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        self.assertEqual(detalhar_treinador("Ash Ketchum"), {})

        treinador_nao_cadastrado(lambda : detalhar_treinador("Misty"), self)
        self.assertTrue(cadastrar_treinador("Misty"))
        self.assertEqual(detalhar_treinador("Misty"), {})

        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
            "Misty": {"nome": "Misty", "pokemons": {}}
        })

    @sem_io
    def test_09b_limpeza(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Jessie"))
        self.assertTrue(cadastrar_treinador("James"))
        self.reset()
        treinador_nao_cadastrado(lambda : detalhar_treinador("Jessie"), self)
        treinador_nao_cadastrado(lambda : detalhar_treinador("James"), self)

    @sem_io
    def test_09c_repetido(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Jessie"))
        self.assertFalse(cadastrar_treinador("Jessie"))
        self.assertEqual(detalhar_treinador("Jessie"), {})
        cadastrar_pokemon("Jessie", "A", "ARBOK", 20000)
        cadastrar_pokemon("Jessie", "B", "wobbuffet", 2000)
        cadastrar_pokemon("Jessie", "C", "Lickitung", 2500)
        self.assertFalse(cadastrar_treinador("Jessie"))

        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Jessie": {
                "nome": "Jessie",
                "pokemons": {
                    "A": {"apelido": "A", "tipo": "arbok", "experiencia": 20000},
                    "B": {"apelido": "B", "tipo": "wobbuffet", "experiencia": 2000},
                    "C": {"apelido": "C", "tipo": "lickitung", "experiencia": 2500}
                }
            }
        })

    @sem_io
    def test_10a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "Pikachu", 50000)
        self.assertTrue(cadastrar_treinador("Misty"))
        cadastrar_pokemon("Misty", "A", "STARYU", 10000)
        cadastrar_pokemon("Misty", "B", "sTaRyU", 12000)
        self.assertTrue(cadastrar_treinador("Brock"))
        cadastrar_pokemon("Brock", "O", "onix", 8000)
        cadastrar_pokemon("Brock", "G", "Geodude", 20000)
        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "A", "KOFFING", 5000)
        cadastrar_pokemon("James", "B", "MeowTH", 20000)

        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {"P": {"apelido": "P", "tipo": "pikachu", "experiencia": 50000}}},
            "Misty": {"nome": "Misty", "pokemons": {"A": {"apelido": "A", "tipo": "staryu", "experiencia": 10000}, "B": {"apelido": "B", "tipo": "staryu", "experiencia": 12000}}},
            "Brock": {"nome": "Brock", "pokemons": {"O": {"apelido": "O", "tipo": "onix", "experiencia": 8000}, "G": {"apelido": "G", "tipo": "geodude", "experiencia": 20000}}},
            "James": {
                "nome": "James",
                "pokemons": {
                    "A": {"apelido": "A", "tipo": "koffing", "experiencia": 5000},
                    "B": {"apelido": "B", "tipo": "meowth", "experiencia": 20000}
                }
            }
        })

    @sem_io
    def test_10b_treinador_nao_existe(self):
        self.reset()
        treinador_nao_cadastrado(lambda : cadastrar_pokemon("Max", "D", "lapras", 40000), self)
        self.assertEqual(api.get(f"{site_treinador}/treinador").json(), {})

    @sem_io
    def test_10c_pokemon_nao_existe(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Iris"))
        pokemon_nao_existe(lambda : cadastrar_pokemon("Iris", "D", "homer", 40000), self)
        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Iris": {"nome": "Iris", "pokemons": {}}
        })

    @sem_io
    def test_10d_pokemon_ja_existe(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Misty"))
        cadastrar_pokemon("Misty", "estrela", "STARMIE", 40000)
        pokemon_ja_cadastrado(lambda : cadastrar_pokemon("Misty", "estrela", "staryu", 1000), self)

        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Misty": {"nome": "Misty", "pokemons": {"estrela": {"apelido": "estrela", "tipo": "starmie", "experiencia": 40000}}}
        })

    @sem_io
    def test_10e_treinador_errado(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        treinador_nao_cadastrado(lambda : cadastrar_pokemon("Gary", "pi", "pikachu", 40000), self)
        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}}
        })

    @sem_io
    def test_11a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)
        ganhar_experiencia("Ash Ketchum", "P", 1500)

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "VictREeBEL", 12000)
        ganhar_experiencia("James", "P", 2500)

        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {"P": {"apelido": "P", "tipo": "pikachu", "experiencia": 51500}}},
            "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 12500}, "Q": {"apelido": "Q", "tipo": "victreebel", "experiencia": 12000}}}
        })

    @sem_io
    def test_11b_treinador_nao_existe(self):
        self.reset()
        treinador_nao_cadastrado(lambda : ganhar_experiencia("Cilan", "bob-esponja", 10000), self)
        self.assertEqual(api.get(f"{site_treinador}/treinador").json(), {})

    @sem_io
    def test_11c_pokemon_nao_existe(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Bonnie"))
        pokemon_nao_cadastrado(lambda : ganhar_experiencia("Bonnie", "bob-esponja", 40000), self)

        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Bonnie": {"nome": "Bonnie", "pokemons": {}}
        })

    @sem_io
    def test_11d_treinador_errado(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Serena"))
        self.assertTrue(cadastrar_treinador("Dawn"))
        cadastrar_pokemon("Serena", "fen", "fennekin", 5000)
        pokemon_nao_cadastrado(lambda : ganhar_experiencia("Dawn", "fen", 100), self)

        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Serena": {"nome": "Serena", "pokemons": {"fen": {"apelido": "fen", "tipo": "fennekin", "experiencia": 5000}}},
            "Dawn": {"nome": "Dawn", "pokemons": {}}
        })

    @sem_io
    def test_12a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "Gloom", 12000)

        pikachu = localizar_pokemon("Ash Ketchum", "P")
        weezing = localizar_pokemon("James", "P")
        gloom = localizar_pokemon("James", "Q")

        self.assertIs(type(pikachu), Pokemon)
        self.assertEqual(pikachu.nome_treinador, "Ash Ketchum")
        self.assertEqual(pikachu.apelido, "P")
        self.assertEqual(pikachu.tipo, "pikachu")
        self.assertEqual(pikachu.experiencia, 50000)
        self.assertEqual(pikachu.nivel, 36)
        self.assertEqual(pikachu.cor, "amarelo")
        self.assertEqual(pikachu.evoluiu_de, "pichu")
        assert_equals_unordered_list(["raichu"], pikachu.evolui_para, self)

        self.assertIs(type(weezing), Pokemon)
        self.assertEqual(weezing.nome_treinador, "James")
        self.assertEqual(weezing.apelido, "P")
        self.assertEqual(weezing.tipo, "weezing")
        self.assertEqual(weezing.experiencia, 10000)
        self.assertEqual(weezing.nivel, 21)
        self.assertEqual(weezing.cor, "roxo")
        self.assertEqual(weezing.evoluiu_de, "koffing")
        assert_equals_unordered_list([], weezing.evolui_para, self)

        self.assertIs(type(gloom), Pokemon)
        self.assertEqual(gloom.nome_treinador, "James")
        self.assertEqual(gloom.apelido, "Q")
        self.assertEqual(gloom.tipo, "gloom")
        self.assertEqual(gloom.experiencia, 12000)
        self.assertEqual(gloom.nivel, 25)
        self.assertEqual(gloom.cor, "azul")
        self.assertEqual(gloom.evoluiu_de, "oddish")
        assert_equals_unordered_list(["vileplume", "bellossom"], gloom.evolui_para, self)

    @sem_io
    def test_12b_treinador_nao_existe(self):
        self.reset()
        treinador_nao_cadastrado(lambda : localizar_pokemon("Cilan", "bob-esponja"), self)
        self.assertEqual(api.get(f"{site_treinador}/treinador").json(), {})

    @sem_io
    def test_12c_pokemon_nao_existe(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Bonnie"))
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Bonnie", "bob-esponja"), self)

        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Bonnie": {"nome": "Bonnie", "pokemons": {}}
        })

    @sem_io
    def test_12d_treinador_errado(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Serena"))
        self.assertTrue(cadastrar_treinador("Dawn"))
        cadastrar_pokemon("Serena", "fen", "fennekin", 5000)
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Dawn", "fen"), self)

        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Serena": {"nome": "Serena", "pokemons": {"fen": {"apelido": "fen", "tipo": "fennekin", "experiencia": 5000}}},
            "Dawn": {"nome": "Dawn", "pokemons": {}}
        })

    @sem_io
    def test_13a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "WeepinBElL", 12000)

        ash = detalhar_treinador("Ash Ketchum")
        james = detalhar_treinador("James")

        self.assertEqual(ash, {"P": "pikachu"})
        self.assertEqual(james, {"P": "weezing", "Q": "weepinbell"})

    @sem_io
    def test_13b_treinador_nao_existe(self):
        self.reset()
        treinador_nao_cadastrado(lambda : detalhar_treinador("Cilan"), self)
        self.assertEqual(api.get(f"{site_treinador}/treinador").json(), {})

    @sem_io
    def test_14a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

        self.assertTrue(cadastrar_treinador("Prof. Carvalho"))

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "WeepinBElL", 12000)

        excluir_treinador("Ash Ketchum")

        resposta1 = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta1.json(), {
            "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 10000}, "Q": {"apelido": "Q", "tipo": "weepinbell", "experiencia": 12000}}},
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        treinador_nao_cadastrado(lambda : detalhar_treinador("Ash Ketchum"), self)
        treinador_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"), self)

        excluir_treinador("James")

        resposta2 = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta2.json(), {
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        treinador_nao_cadastrado(lambda : detalhar_treinador("James"), self)
        treinador_nao_cadastrado(lambda : localizar_pokemon("James", "P"), self)
        treinador_nao_cadastrado(lambda : localizar_pokemon("James", "Q"), self)

        excluir_treinador("Prof. Carvalho")

        resposta3 = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta3.json(), {})
        treinador_nao_cadastrado(lambda : detalhar_treinador("Prof. Carvalho"), self)

    @sem_io
    def test_14b_treinador_nao_existe(self):
        self.reset()

        treinador_nao_cadastrado(lambda : excluir_treinador("Kiawe"), self)
        self.assertEqual(api.get(f"{site_treinador}/treinador").json(), {})

        self.assertTrue(cadastrar_treinador("Kiawe"))
        cadastrar_pokemon("Kiawe", "c", "charizard", 50000)
        treinador_nao_cadastrado(lambda : excluir_treinador("Lillie"), self)
        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

        excluir_treinador("Kiawe")
        self.assertEqual(api.get(f"{site_treinador}/treinador").json(), {})

    @sem_io
    def test_15a_ok(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Ash Ketchum"))
        cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)

        self.assertTrue(cadastrar_treinador("Prof. Carvalho"))

        self.assertTrue(cadastrar_treinador("James"))
        cadastrar_pokemon("James", "P", "WEEZING", 10000)
        cadastrar_pokemon("James", "Q", "WeepinBElL", 12000)

        excluir_pokemon("Ash Ketchum", "P")

        resposta1 = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta1.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
            "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 10000}, "Q": {"apelido": "Q", "tipo": "weepinbell", "experiencia": 12000}}},
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"), self)
        localizar_pokemon("James", "P")
        localizar_pokemon("James", "Q")

        excluir_pokemon("James", "Q")

        resposta2 = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta2.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
            "James": {"nome": "James", "pokemons": {"P": {"apelido": "P", "tipo": "weezing", "experiencia": 10000}}},
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"), self)
        localizar_pokemon("James", "P")
        pokemon_nao_cadastrado(lambda : localizar_pokemon("James", "Q"), self)

        excluir_pokemon("James", "P")

        resposta3 = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta3.json(), {
            "Ash Ketchum": {"nome": "Ash Ketchum", "pokemons": {}},
            "James": {"nome": "James", "pokemons": {}},
            "Prof. Carvalho": {"nome": "Prof. Carvalho", "pokemons": {}}
        })
        pokemon_nao_cadastrado(lambda : localizar_pokemon("Ash Ketchum", "P"), self)
        pokemon_nao_cadastrado(lambda : localizar_pokemon("James", "P"), self)
        pokemon_nao_cadastrado(lambda : localizar_pokemon("James", "Q"), self)

    @sem_io
    def test_15b_treinador_nao_existe(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Kiawe"))
        cadastrar_pokemon("Kiawe", "c", "charizard", 50000)
        treinador_nao_cadastrado(lambda : excluir_pokemon("Lillie", "c"), self)
        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

        localizar_pokemon("Kiawe", "c")
        self.assertEqual(api.get(f"{site_treinador}/treinador").json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

    @sem_io
    def test_15c_pokemon_nao_existe(self):
        self.reset()

        self.assertTrue(cadastrar_treinador("Kiawe"))
        cadastrar_pokemon("Kiawe", "c", "charizard", 50000)
        pokemon_nao_cadastrado(lambda : excluir_pokemon("Kiawe", "d"), self)
        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

        localizar_pokemon("Kiawe", "c")
        self.assertEqual(api.get(f"{site_treinador}/treinador").json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {"c": {"apelido": "c", "tipo": "charizard", "experiencia": 50000}}}
        })

        excluir_pokemon("Kiawe", "c")
        self.assertEqual(api.get(f"{site_treinador}/treinador").json(), {
            "Kiawe": {"nome": "Kiawe", "pokemons": {}}
        })

    @sem_io
    def test_98a_limpeza(self):
        self.reset()
        self.assertTrue(cadastrar_treinador("Tracey"))
        cadastrar_pokemon("Tracey", "m", "MARILL", 40000)

        self.reset()
        treinador_nao_cadastrado(lambda : detalhar_treinador("Tracey"), self)
        treinador_nao_cadastrado(lambda : localizar_pokemon("Tracey", "m"), self)
        treinador_nao_cadastrado(lambda : ganhar_experiencia("Tracey", "m", 4000), self)
        treinador_nao_cadastrado(lambda : cadastrar_pokemon("Tracey", "t", "togepi", 500), self)
        treinador_nao_cadastrado(lambda : excluir_pokemon("Tracey", "t"), self)
        treinador_nao_cadastrado(lambda : excluir_treinador("Tracey"), self)

        resposta = api.get(f"{site_treinador}/treinador")
        self.assertEqual(resposta.json(), {})

    def test_99a_print(self):
        sem_io.test_print(self)

    def test_99b_input(self):
        sem_io.test_input(self)

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTreinador)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)

if __name__ == '__main__':
    runTests()
