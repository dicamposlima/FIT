import unittest
from requests import api
from pokemon_teste_base import *

verificar_online("pokeapi")

class TestPokeapi(unittest.TestCase):
    @sem_io
    def test_01a_ok(self):
        self.assertEqual(nome_do_pokemon(1), "bulbasaur")
        self.assertEqual(nome_do_pokemon(55), "golduck")
        self.assertEqual(nome_do_pokemon(25), "pikachu")
        self.assertEqual(nome_do_pokemon(700), "sylveon")
        self.assertEqual(nome_do_pokemon(807), "zeraora")

    @sem_io
    def test_02a_ok(self):
        self.assertEqual(numero_do_pokemon("marill"), 183)

    @sem_io
    def test_02b_caps(self):
        self.assertEqual(numero_do_pokemon("EEVEE"), 133)
        self.assertEqual(numero_do_pokemon("Psyduck"), 54)
        self.assertEqual(numero_do_pokemon("SkiTtY"), 300)
        self.assertEqual(numero_do_pokemon("Zeraora"), 807)

    @sem_io
    def test_02c_nao_existe(self):
        pokemon_nao_existe(lambda : numero_do_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("SpiderMan"), self)

    @sem_io
    def test_03a_ok(self):
        self.assertEqual(color_of_pokemon("marill"), "blue")
        self.assertEqual(color_of_pokemon("togekiss"), "white")
        self.assertEqual(color_of_pokemon("magneton"), "gray")

    @sem_io
    def test_03b_caps(self):
        self.assertEqual(color_of_pokemon("EEVEE"), "brown")
        self.assertEqual(color_of_pokemon("Psyduck"), "yellow")
        self.assertEqual(color_of_pokemon("SkiTtY"), "pink")
        self.assertEqual(color_of_pokemon("GASTLY"), "purple")
        self.assertEqual(color_of_pokemon("LeDyBa"), "red")
        self.assertEqual(color_of_pokemon("Torterra"), "green")
        self.assertEqual(color_of_pokemon("xurkiTree"), "black")

    @sem_io
    def test_03c_nao_existe(self):
        pokemon_nao_existe(lambda : color_of_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("batman"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("SpiderMan"), self)

    @sem_io
    def test_04a_ok(self):
        self.assertEqual(cor_do_pokemon("marill"), "azul")
        self.assertEqual(cor_do_pokemon("togekiss"), "branco")

    @sem_io
    def test_04b_caps(self):
        self.assertEqual(cor_do_pokemon("EEVEE"), "marrom")
        self.assertEqual(cor_do_pokemon("Psyduck"), "amarelo")
        self.assertEqual(cor_do_pokemon("SkiTtY"), "rosa")
        self.assertEqual(cor_do_pokemon("magneton"), "cinza")
        self.assertEqual(cor_do_pokemon("GASTLY"), "roxo")
        self.assertEqual(cor_do_pokemon("LeDyBa"), "vermelho")
        self.assertEqual(cor_do_pokemon("Torterra"), "verde")
        self.assertEqual(cor_do_pokemon("xurkiTree"), "preto")

    @sem_io
    def test_04c_nao_existe(self):
        pokemon_nao_existe(lambda : cor_do_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("SpiderMan"), self)

    @sem_io
    def test_05a_ok(self):
        assert_equals_unordered_list(["grama"], tipos_do_pokemon("chikorita"), self)
        assert_equals_unordered_list(["terra"], tipos_do_pokemon("hippowdon"), self)
        assert_equals_unordered_list(["normal", "fada"], tipos_do_pokemon("jigglypuff"), self)
        assert_equals_unordered_list(["fogo"], tipos_do_pokemon("darumaka"), self)
        assert_equals_unordered_list(["pedra", "voador"], tipos_do_pokemon("archeops"), self)

    @sem_io
    def test_05b_caps(self):
        assert_equals_unordered_list(["voador", "noturno"], tipos_do_pokemon("murKrow"), self)
        assert_equals_unordered_list(["água", "elétrico"], tipos_do_pokemon("cHinChou"), self)
        assert_equals_unordered_list(["lutador", "fantasma"], tipos_do_pokemon("MARSHADOW"), self)
        assert_equals_unordered_list(["aço"], tipos_do_pokemon("KLINK"), self)
        assert_equals_unordered_list(["lutador", "inseto"], tipos_do_pokemon("Heracross"), self)
        assert_equals_unordered_list(["veneno", "noturno"], tipos_do_pokemon("DRAPION"), self)
        assert_equals_unordered_list(["psíquico", "gelo"], tipos_do_pokemon("JYNX"), self)
        assert_equals_unordered_list(["dragão"], tipos_do_pokemon("dRaTiNi"), self)

    @sem_io
    def test_05c_nao_existe(self):
        pokemon_nao_existe(lambda : tipos_do_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("SpiderMan"), self)

    @sem_io
    def test_06a_ok(self):
        self.assertEqual(evolucao_anterior("togetic"), "togepi")

    @sem_io
    def test_06b_caps(self):
        self.assertEqual(evolucao_anterior("togeKiss"), "togetic")
        self.assertEqual(evolucao_anterior("EEleKtriK"), "tynamo")
        self.assertEqual(evolucao_anterior("EELEKTROSS"), "eelektrik")
        self.assertEqual(evolucao_anterior("Pikachu"), "pichu")
        self.assertEqual(evolucao_anterior("rAiChu"), "pikachu")

    @sem_io
    def test_06c_nao_tem(self):
        self.assertIs(evolucao_anterior("togepi"), None)
        self.assertIs(evolucao_anterior("TYNAMO"), None)
        self.assertIs(evolucao_anterior("Pichu"), None)

    @sem_io
    def test_06d_nao_existe(self):
        pokemon_nao_existe(lambda : evolucao_anterior("DOBBY"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("batman"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("SpiderMan"), self)

    @sem_io
    def test_07a_ok_evolucoes_simples(self):
        assert_equals_unordered_list(["charmeleon"], evolucoes_proximas("charmander"), self)
        assert_equals_unordered_list(["combusken"], evolucoes_proximas("torchic"), self)
        assert_equals_unordered_list(["charizard"], evolucoes_proximas("ChArMeLeON"), self)

    @sem_io
    def test_07b_ok_nao_tem_simples(self):
        assert_equals_unordered_list([], evolucoes_proximas("lugia"), self)
        assert_equals_unordered_list([], evolucoes_proximas("turtonator"), self)
        assert_equals_unordered_list([], evolucoes_proximas("CHARIZARD"), self)
        assert_equals_unordered_list([], evolucoes_proximas("gEnGar"), self)
        assert_equals_unordered_list([], evolucoes_proximas("ALAkazam"), self)

    @sem_io
    def test_07c_ok_evolucoes_complexas(self):
        assert_equals_unordered_list(["ninjask", "shedinja"], evolucoes_proximas("nincada"), self)
        assert_equals_unordered_list(["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"], evolucoes_proximas("eevee"), self)
        assert_equals_unordered_list(["hitmonlee", "hitmonchan", "hitmontop"], evolucoes_proximas("tyrogue"), self)
        assert_equals_unordered_list(["poliwhirl"], evolucoes_proximas("Poliwag"), self)
        assert_equals_unordered_list(["gloom"], evolucoes_proximas("oDDiSH"), self)
        assert_equals_unordered_list(["poliwrath", "politoed"], evolucoes_proximas("PoliWHIRL"), self)
        assert_equals_unordered_list(["vileplume", "bellossom"], evolucoes_proximas("GLOOM"), self)

    @sem_io
    def test_07d_ok_nao_tem_complexas(self):
        assert_equals_unordered_list([], evolucoes_proximas("espeon"), self)
        assert_equals_unordered_list([], evolucoes_proximas("Leafeon"), self)
        assert_equals_unordered_list([], evolucoes_proximas("POLITOED"), self)

    @sem_io
    def test_07e_nao_existe(self):
        pokemon_nao_existe(lambda : evolucoes_proximas("DOBBY"), self)
        pokemon_nao_existe(lambda : evolucoes_proximas("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : evolucoes_proximas("batman"), self)
        pokemon_nao_existe(lambda : evolucoes_proximas("SpiderMan"), self)

    @sem_io
    def test_08a_simples(self):
        self.assertEqual(nivel_do_pokemon("blastoise",   110000), 49) # 4
        self.assertEqual(nivel_do_pokemon("mewtwo",     1000000), 92) # 1
        self.assertEqual(nivel_do_pokemon("Magikarp",       900),  8) # 1
        self.assertEqual(nivel_do_pokemon("Magikarp",   1000000), 92) # 1
        self.assertEqual(nivel_do_pokemon("SLOWBRO",      65000), 40) # 2
        self.assertEqual(nivel_do_pokemon("OcTiLLeRy",   280000), 65) # 2
        self.assertEqual(nivel_do_pokemon("FRAXURE",     280000), 60) # 1
        self.assertEqual(nivel_do_pokemon("lunatone",     20000), 29) # 3
        self.assertEqual(nivel_do_pokemon("skitty",       50000), 39) # 3
        self.assertEqual(nivel_do_pokemon("torchic",      40000), 35) # 4
        self.assertEqual(nivel_do_pokemon("ODDISH",        5000), 19) # 4

    @sem_io
    def test_08b_complexos(self):
        self.assertEqual(nivel_do_pokemon("zangoose",      9000), 17) # 5
        self.assertEqual(nivel_do_pokemon("milotic",      65000), 37) # 5
        self.assertEqual(nivel_do_pokemon("Lumineon",    160000), 55) # 5
        self.assertEqual(nivel_do_pokemon("NINJASK",     300000), 72) # 5
        self.assertEqual(nivel_do_pokemon("zangoose",    580000), 97) # 5
        self.assertEqual(nivel_do_pokemon("makuhita",       600), 10) # 6
        self.assertEqual(nivel_do_pokemon("gulpin",        7000), 21) # 6
        self.assertEqual(nivel_do_pokemon("seviper",     150000), 50) # 6
        self.assertEqual(nivel_do_pokemon("drifblim",   1000000), 87) # 6

    @sem_io
    def test_08c_limites(self):
        self.assertEqual(nivel_do_pokemon("pinsir",           0),   1) # 1
        self.assertEqual(nivel_do_pokemon("bibarel",          0),   1) # 2
        self.assertEqual(nivel_do_pokemon("aipom",            0),   1) # 3
        self.assertEqual(nivel_do_pokemon("Makuhita",         0),   1) # 6
        self.assertEqual(nivel_do_pokemon("Magikarp",      1249),   9) # 1
        self.assertEqual(nivel_do_pokemon("MeTaPoD",        999),   9) # 2
        self.assertEqual(nivel_do_pokemon("Magikarp",      1250),  10) # 1
        self.assertEqual(nivel_do_pokemon("Butterfree",    1000),  10) # 2
        self.assertEqual(nivel_do_pokemon("charmeleon",   29948),  32) # 4
        self.assertEqual(nivel_do_pokemon("charmeleon",   29949),  33) # 4
        self.assertEqual(nivel_do_pokemon("hariyama",     71676),  40) # 6
        self.assertEqual(nivel_do_pokemon("hariyama",     71677),  41) # 6
        self.assertEqual(nivel_do_pokemon("togePI",      799999),  99) # 3
        self.assertEqual(nivel_do_pokemon("gengar",     1059859),  99) # 4
        self.assertEqual(nivel_do_pokemon("zangoose",    599999),  99) # 5
        self.assertEqual(nivel_do_pokemon("SWALot",     1639999),  99) # 6
        self.assertEqual(nivel_do_pokemon("sYLVEON",    1000000), 100) # 2
        self.assertEqual(nivel_do_pokemon("Jigglypuff", 1000000), 100) # 3
        self.assertEqual(nivel_do_pokemon("LEDIAN",      800000), 100) # 3
        self.assertEqual(nivel_do_pokemon("vaPorEON", 999999999), 100) # 2
        self.assertEqual(nivel_do_pokemon("VILEPLUME",  1059860), 100) # 4
        self.assertEqual(nivel_do_pokemon("zangoose",    600000), 100) # 5
        self.assertEqual(nivel_do_pokemon("SWALOT",     1640000), 100) # 6

    @sem_io
    def test_08d_nao_existe(self):
        pokemon_nao_existe(lambda : nivel_do_pokemon("DOBBY", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("Peppa-Pig", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("batman", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("SpiderMan", 1234), self)

    def test_99a_print(self):
        sem_io.test_print(self)

    def test_99b_input(self):
        sem_io.test_input(self)

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPokeapi)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)

if __name__ == '__main__':
    runTests()
