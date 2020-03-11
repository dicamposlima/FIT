import unittest
from pokemon_teste_base import *

verificar_online("offline")

class TestOffline(unittest.TestCase):
    @sem_io
    def test_01x_nao_existe(self):
        pokemon_nao_existe(lambda : nome_do_pokemon(0   ), self)
        pokemon_nao_existe(lambda : nome_do_pokemon(-1  ), self)
        pokemon_nao_existe(lambda : nome_do_pokemon(-2  ), self)
        pokemon_nao_existe(lambda : nome_do_pokemon(-666), self)
        pokemon_nao_existe(lambda : nome_do_pokemon(808 ), self)
        pokemon_nao_existe(lambda : nome_do_pokemon(999 ), self)
        pokemon_nao_existe(lambda : nome_do_pokemon(1234), self)

    @sem_io
    def test_01y_nao_existe_pegadinha(self):
        pokemon_nao_existe(lambda : nome_do_pokemon(10001), self)

    @sem_io
    def test_01z_erro_tipo(self):
        valor_errado(lambda : nome_do_pokemon(""        ), self)
        valor_errado(lambda : nome_do_pokemon("a"       ), self)
        valor_errado(lambda : nome_do_pokemon("5"       ), self)
        valor_errado(lambda : nome_do_pokemon("2-3"     ), self)
        valor_errado(lambda : nome_do_pokemon("+"       ), self)
        valor_errado(lambda : nome_do_pokemon(" "       ), self)
        valor_errado(lambda : nome_do_pokemon(5.6       ), self)
        valor_errado(lambda : nome_do_pokemon([]        ), self)
        valor_errado(lambda : nome_do_pokemon({"a": "b"}), self)
        valor_errado(lambda : nome_do_pokemon("pikachu" ), self)

    @sem_io
    def test_02z_erro_tipo(self):
        valor_errado(lambda : numero_do_pokemon(1         ), self)
        valor_errado(lambda : numero_do_pokemon(2         ), self)
        valor_errado(lambda : numero_do_pokemon([]        ), self)
        valor_errado(lambda : numero_do_pokemon({"a": "b"}), self)
        valor_errado(lambda : numero_do_pokemon(""        ), self)

    @sem_io
    def test_03z_erro_tipo(self):
        valor_errado(lambda : color_of_pokemon(1         ), self)
        valor_errado(lambda : color_of_pokemon(2         ), self)
        valor_errado(lambda : color_of_pokemon([]        ), self)
        valor_errado(lambda : color_of_pokemon({"a": "b"}), self)
        valor_errado(lambda : color_of_pokemon(""        ), self)

    @sem_io
    def test_04z_erro_tipo(self):
        valor_errado(lambda : cor_do_pokemon(1         ), self)
        valor_errado(lambda : cor_do_pokemon(2         ), self)
        valor_errado(lambda : cor_do_pokemon([]        ), self)
        valor_errado(lambda : cor_do_pokemon({"a": "b"}), self)
        valor_errado(lambda : cor_do_pokemon(""        ), self)

    @sem_io
    def test_05z_erro_tipo(self):
        valor_errado(lambda : tipos_do_pokemon(1         ), self)
        valor_errado(lambda : tipos_do_pokemon(2         ), self)
        valor_errado(lambda : tipos_do_pokemon([]        ), self)
        valor_errado(lambda : tipos_do_pokemon({"a": "b"}), self)
        valor_errado(lambda : tipos_do_pokemon(""        ), self)

    @sem_io
    def test_06z_erro_tipo(self):
        valor_errado(lambda : evolucao_anterior(1         ), self)
        valor_errado(lambda : evolucao_anterior(2         ), self)
        valor_errado(lambda : evolucao_anterior([]        ), self)
        valor_errado(lambda : evolucao_anterior({"a": "b"}), self)
        valor_errado(lambda : evolucao_anterior(""        ), self)

    @sem_io
    def test_07z_erro_tipo(self):
        valor_errado(lambda : evolucoes_proximas(1         ), self)
        valor_errado(lambda : evolucoes_proximas(2         ), self)
        valor_errado(lambda : evolucoes_proximas([]        ), self)
        valor_errado(lambda : evolucoes_proximas({"a": "b"}), self)
        valor_errado(lambda : evolucoes_proximas(""        ), self)

    @sem_io
    def test_08x_erro_tipo_1(self):
        valor_errado(lambda : nivel_do_pokemon(1         , 1234), self)
        valor_errado(lambda : nivel_do_pokemon(2         , 1234), self)
        valor_errado(lambda : nivel_do_pokemon([]        , 1234), self)
        valor_errado(lambda : nivel_do_pokemon({"a": "b"}, 1234), self)
        valor_errado(lambda : nivel_do_pokemon(""        , 1234), self)

    @sem_io
    def test_08y_erro_tipo_2(self):
        valor_errado(lambda : nivel_do_pokemon("pikachu", ""        ), self)
        valor_errado(lambda : nivel_do_pokemon("pikachu", "a"       ), self)
        valor_errado(lambda : nivel_do_pokemon("pikachu", "5"       ), self)
        valor_errado(lambda : nivel_do_pokemon("pikachu", "2-3"     ), self)
        valor_errado(lambda : nivel_do_pokemon("pikachu", "+"       ), self)
        valor_errado(lambda : nivel_do_pokemon("pikachu", " "       ), self)
        valor_errado(lambda : nivel_do_pokemon("pikachu", 5.6       ), self)
        valor_errado(lambda : nivel_do_pokemon("pikachu", []        ), self)
        valor_errado(lambda : nivel_do_pokemon("pikachu", {"a": "b"}), self)
        valor_errado(lambda : nivel_do_pokemon("pikachu", "pikachu" ), self)

    @sem_io
    def test_08z_negativo(self):
        valor_errado(lambda : nivel_do_pokemon("pikachu", -1  ), self)
        valor_errado(lambda : nivel_do_pokemon("pikachu", -2  ), self)
        valor_errado(lambda : nivel_do_pokemon("pikachu", -666), self)

    @sem_io
    def test_09z_erro_tipo(self):
        valor_errado(lambda : cadastrar_treinador(1         ), self)
        valor_errado(lambda : cadastrar_treinador(2         ), self)
        valor_errado(lambda : cadastrar_treinador([]        ), self)
        valor_errado(lambda : cadastrar_treinador({"a": "b"}), self)
        valor_errado(lambda : cadastrar_treinador(""        ), self)

    @sem_io
    def test_10v_erro_tipo_treinador(self):
        valor_errado(lambda : cadastrar_pokemon(1         , "Chapolin", "makuhita", 5000), self)
        valor_errado(lambda : cadastrar_pokemon(2         , "Chapolin", "makuhita", 5000), self)
        valor_errado(lambda : cadastrar_pokemon([]        , "Chapolin", "makuhita", 5000), self)
        valor_errado(lambda : cadastrar_pokemon({"a": "b"}, "Chapolin", "makuhita", 5000), self)
        valor_errado(lambda : cadastrar_pokemon(""        , "Chapolin", "makuhita", 5000), self)

    @sem_io
    def test_10w_erro_tipo_apelido(self):
        valor_errado(lambda : cadastrar_pokemon("Seu Madruga", 1         , "elekid", 5000), self)
        valor_errado(lambda : cadastrar_pokemon("Seu Madruga", 2         , "elekid", 5000), self)
        valor_errado(lambda : cadastrar_pokemon("Seu Madruga", []        , "elekid", 5000), self)
        valor_errado(lambda : cadastrar_pokemon("Seu Madruga", {"a": "b"}, "elekid", 5000), self)
        valor_errado(lambda : cadastrar_pokemon("Seu Madruga", ""        , "elekid", 5000), self)

    @sem_io
    def test_10x_erro_tipo_especie(self):
        valor_errado(lambda : cadastrar_pokemon("Seu Madruga", "Nhonho", 1         , 5000), self)
        valor_errado(lambda : cadastrar_pokemon("Seu Madruga", "Nhonho", 2         , 5000), self)
        valor_errado(lambda : cadastrar_pokemon("Seu Madruga", "Nhonho", []        , 5000), self)
        valor_errado(lambda : cadastrar_pokemon("Seu Madruga", "Nhonho", {"a": "b"}, 5000), self)
        valor_errado(lambda : cadastrar_pokemon("Seu Madruga", "Nhonho", ""        , 5000), self)

    @sem_io
    def test_10y_erro_tipo_experiencia(self):
        valor_errado(lambda : cadastrar_pokemon("Chaves", "Quico", "lucario", ""        ), self)
        valor_errado(lambda : cadastrar_pokemon("Chaves", "Quico", "lucario", "a"       ), self)
        valor_errado(lambda : cadastrar_pokemon("Chaves", "Quico", "lucario", "5"       ), self)
        valor_errado(lambda : cadastrar_pokemon("Chaves", "Quico", "lucario", "2-3"     ), self)
        valor_errado(lambda : cadastrar_pokemon("Chaves", "Quico", "lucario", "+"       ), self)
        valor_errado(lambda : cadastrar_pokemon("Chaves", "Quico", "lucario", " "       ), self)
        valor_errado(lambda : cadastrar_pokemon("Chaves", "Quico", "lucario", 5.6       ), self)
        valor_errado(lambda : cadastrar_pokemon("Chaves", "Quico", "lucario", []        ), self)
        valor_errado(lambda : cadastrar_pokemon("Chaves", "Quico", "lucario", {"a": "b"}), self)
        valor_errado(lambda : cadastrar_pokemon("Chaves", "Quico", "lucario", "pikachu" ), self)

    @sem_io
    def test_10z_experiencia_negativa(self):
        valor_errado(lambda : cadastrar_pokemon("Jaiminho", "Seu Barriga", "snorlax", -1  ), self)
        valor_errado(lambda : cadastrar_pokemon("Jaiminho", "Seu Barriga", "snorlax", -2  ), self)
        valor_errado(lambda : cadastrar_pokemon("Jaiminho", "Seu Barriga", "snorlax", -666), self)

    @sem_io
    def test_11w_erro_tipo_treinador(self):
        valor_errado(lambda : ganhar_experiencia(1         , "Dona Florinda", 5000), self)
        valor_errado(lambda : ganhar_experiencia(2         , "Dona Florinda", 5000), self)
        valor_errado(lambda : ganhar_experiencia([]        , "Dona Florinda", 5000), self)
        valor_errado(lambda : ganhar_experiencia({"a": "b"}, "Dona Florinda", 5000), self)
        valor_errado(lambda : ganhar_experiencia(""        , "Dona Florinda", 5000), self)

    @sem_io
    def test_11x_erro_tipo_pokemon(self):
        valor_errado(lambda : ganhar_experiencia("Girafales", 1         , 5000), self)
        valor_errado(lambda : ganhar_experiencia("Girafales", 2         , 5000), self)
        valor_errado(lambda : ganhar_experiencia("Girafales", []        , 5000), self)
        valor_errado(lambda : ganhar_experiencia("Girafales", {"a": "b"}, 5000), self)
        valor_errado(lambda : ganhar_experiencia("Girafales", ""        , 5000), self)

    @sem_io
    def test_11y_erro_tipo_experiencia(self):
        valor_errado(lambda : ganhar_experiencia("Bruxa do 71", "Satanás", ""        ), self)
        valor_errado(lambda : ganhar_experiencia("Bruxa do 71", "Satanás", "a"       ), self)
        valor_errado(lambda : ganhar_experiencia("Bruxa do 71", "Satanás", "5"       ), self)
        valor_errado(lambda : ganhar_experiencia("Bruxa do 71", "Satanás", "2-3"     ), self)
        valor_errado(lambda : ganhar_experiencia("Bruxa do 71", "Satanás", "+"       ), self)
        valor_errado(lambda : ganhar_experiencia("Bruxa do 71", "Satanás", " "       ), self)
        valor_errado(lambda : ganhar_experiencia("Bruxa do 71", "Satanás", 5.6       ), self)
        valor_errado(lambda : ganhar_experiencia("Bruxa do 71", "Satanás", []        ), self)
        valor_errado(lambda : ganhar_experiencia("Bruxa do 71", "Satanás", {"a": "b"}), self)
        valor_errado(lambda : ganhar_experiencia("Bruxa do 71", "Satanás", "pikachu" ), self)

    @sem_io
    def test_11z_erro_experiencia_negativa(self):
        valor_errado(lambda : ganhar_experiencia("Dona Florinda", "Quico", -1  ), self)
        valor_errado(lambda : ganhar_experiencia("Dona Florinda", "Quico", -2  ), self)
        valor_errado(lambda : ganhar_experiencia("Dona Florinda", "Quico", -666), self)

    @sem_io
    def test_12y_erro_tipo_nome(self):
        valor_errado(lambda : localizar_pokemon(1         , "Goku"), self)
        valor_errado(lambda : localizar_pokemon(2         , "Goku"), self)
        valor_errado(lambda : localizar_pokemon([]        , "Goku"), self)
        valor_errado(lambda : localizar_pokemon({"a": "b"}, "Goku"), self)
        valor_errado(lambda : localizar_pokemon(""        , "Goku"), self)

    @sem_io
    def test_12z_erro_tipo_apelido(self):
        valor_errado(lambda : localizar_pokemon("Vegeta", 1         ), self)
        valor_errado(lambda : localizar_pokemon("Vegeta", 2         ), self)
        valor_errado(lambda : localizar_pokemon("Vegeta", []        ), self)
        valor_errado(lambda : localizar_pokemon("Vegeta", {"a": "b"}), self)
        valor_errado(lambda : localizar_pokemon("Vegeta", ""        ), self)

    @sem_io
    def test_13z_erro_tipo(self):
        valor_errado(lambda : detalhar_treinador(1         ), self)
        valor_errado(lambda : detalhar_treinador(2         ), self)
        valor_errado(lambda : detalhar_treinador([]        ), self)
        valor_errado(lambda : detalhar_treinador({"a": "b"}), self)
        valor_errado(lambda : detalhar_treinador(""        ), self)

    def test_99a_print(self):
        sem_io.test_print(self)

    def test_99b_input(self):
        sem_io.test_input(self)

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestOffline)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)

if __name__ == '__main__':
    runTests()
