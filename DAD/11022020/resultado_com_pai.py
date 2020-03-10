import unittest

# 50% em cada prova PAI. Nota do PAI vai para 6.
# 58% em cada prova PAI. Nota do PAI vai para 6.
# 60% em cada prova PAI. Nota do PAI vai para 8.
# 74% em cada prova PAI. Nota do PAI vai para 8.
# 76% em cada prova PAI. Nota do PAI vai para 10.
# Nota do PAI seria 7.4, que é jogado para 8, mas como está acima do percentil80, vai para 10.
# Nota do PAI seria 7.4, que é jogado para 8, mas como está igual ao percentil80, vai para 10.
# Nota do PAI seria 4, mas como está acima do percentil80, vai para 10.
# Nota do PAI seria 4, mas como está igual ao percentil80, vai para 10.
# Nota do PAI seria 4, mas como está entre o percentil60 é o percentil80, vai para 8.
# Nota do PAI seria 4, mas como é igual ao percentil60, vai para 8.
# Nota do PAI seria 4, mas como está entre o percentil40 é o percentil60, vai para 6.
# Nota do PAI seria 4, mas como é igual ao percentil40, vai para 6.
# Nota do PAI é 4, que assim fica por ser menor que o percentil40.


def caulcula_pai_pontos(total_pontos, percentil40, percentil60, percentil80):
    pontos = 10*total_pontos/50
    porcentagem = 100*total_pontos/50
    pontos = 6 if porcentagem >= 50 and porcentagem < 60 else pontos
    pontos = 8 if porcentagem >= 60 and porcentagem < 76 else pontos
    pontos = 10 if porcentagem >= 76 else pontos
    pontos = 10 if pontos >= percentil80 else pontos
    pontos = 8 if pontos >= percentil60 and pontos < percentil80 else pontos
    pontos = 6 if pontos >= percentil40 and pontos < percentil60 else pontos
    return pontos

# O retorno deverá ser uma tupla onde o primeiro valor é a nota
# final e o segundo uma string que pode ser:
# 'AP' para aprovado;
# 'RF' para reprovado por falta;
# 'RM' para reprovado por média;
# 'RMF' para reprovado por média e falta.


def resultado_com_pai(frequencia, ac1, ac2, ac3, ac4, ac5, prova, sub, pai1, pai2, pai3, percentil40, percentil60, percentil80):
    # Atividades
    acs = [ac1, ac2, ac3, ac4, ac5]
    acs.sort(reverse=True)
    acs.pop()  # somente para descartar o último valor
    mac = 0.3 * sum(acs)/4

    # Provas
    prova = prova if prova > sub else sub
    mprova = 0.4 * prova

    # PAI
    mpai = [pai1, pai2, pai3]
    mpai.sort(reverse=True)
    mpai.pop()  # somente para descartar o último valor

    mpai1_pontos = caulcula_pai_pontos(
        mpai.pop(), percentil40, percentil60, percentil80)
    mpai2_pontos = caulcula_pai_pontos(
        mpai.pop(), percentil40, percentil60, percentil80)

    mpai = 0.3 * sum([mpai1_pontos, mpai2_pontos])/2

    nota_final = round(sum([mac, mprova, mpai]), 2)

    # print(f"frequencia: {frequencia}, ac1: {ac1}, ac2: {ac2}, ac3: {ac3}, ac4: {ac4}, ac5: {ac5}, prova: {prova}, sub: {sub}, pai1: {pai1}, pai2: {pai2}, pai3: {pai3}, percentil40: {percentil40}, percentil60: {percentil60}, percentil8: {percentil80}, mac: {mac}, mprova: {mprova}, mpai: {mpai}, nota_final: {nota_final}")

    if frequencia <= 0.75:
        return (nota_final, 'RMF') if nota_final < 6 else (nota_final, 'RF')
    return (nota_final, 'RM') if nota_final < 6 else (nota_final, 'AP')


class TestNota(unittest.TestCase):

    # Testes que calculam um aluno que só vez AV.
    # verificam se a menor AC é descartada.

    def test_01a_media_acs_descarta_menor(self):
        r = resultado_com_pai(0.9, 10, 10, 10, 1, 10,
                              0, 0, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (3, 'RM'))

    def test_01b_media_acs_descarta_menor(self):
        r = resultado_com_pai(0.9, 5.5, 4, 1, 6, 4.5,
                              0, 0, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (1.5, 'RM'))

    def test_01c_media_acs_descarta_menor(self):
        r = resultado_com_pai(0.9, 7, 2, 7, 7, 7, 0, 0, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (2.1, 'RM'))

    # Testes que verificam o calculo da nota
    # apenas considerando a prova.
    # Lembrando: apenas a melhor prova é considerada.
    # (se quiser arredondar a nota, pode fazer round(nota,2)
    # para pegar 2 casas decimais)

    def test_02a_escolhe_melhor_prova(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (1.6, 'RM'))

    def test_02b_escolhe_melhor_prova(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 6, 4, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (2.4, 'RM'))

    # Testes que verificam o calculo do PAI.
    # Lembrando: cada variável é um número de acertos
    # (de 0 a 50), que deve ser transformada em uma nota de 0 a 10,
    # e a menor nota do PAI é descartada.

    def test_03a_media_pai_descarta_menor(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 9, 18, 22, 10, 10, 10)
        self.assertEqual(r, (1.2, 'RM'))

    def test_03b_media_pai_descarta_menor(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 16, 2, 20, 10, 10, 10)
        self.assertEqual(r, (1.08, 'RM'))

    # Lembrando (vide regulamento) que alunos que tiram mais de
    # 50% tem bonificações na nota do PAI

    def test_04a_media_pai_porcentagem_acertos(self):
        # 44% em cada prova PAI.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 22, 22, 22, 10, 10, 10)
        self.assertEqual(r, (1.32, 'RM'))

    def test_04b_media_pai_porcentagem_acertos(self):
        # 46% em cada prova PAI.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 23, 23, 23, 10, 10, 10)
        self.assertEqual(r, (1.38, 'RM'))

    def test_04c_media_pai_porcentagem_acertos(self):
        # 48% em cada prova PAI.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 24, 24, 24, 10, 10, 10)
        self.assertEqual(r, (1.44, 'RM'))

    def test_04d_media_pai_porcentagem_acertos(self):
        # 50% em cada prova PAI. Nota do PAI vai para 6.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 25, 25, 25, 10, 10, 10)
        self.assertEqual(r, (1.8, 'RM'))

    def test_04e_media_pai_porcentagem_acertos(self):
        # 58% em cada prova PAI. Nota do PAI vai para 6.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 29, 29, 29, 10, 10, 10)
        self.assertEqual(r, (1.8, 'RM'))

    def test_04f_media_pai_porcentagem_acertos(self):
        # 60% em cada prova PAI. Nota do PAI vai para 8.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 30, 30, 30, 10, 10, 10)
        self.assertEqual(r, (2.4, 'RM'))

    def test_04g_media_pai_porcentagem_acertos(self):
        # 74% em cada prova PAI. Nota do PAI vai para 8.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 37, 37, 37, 10, 10, 10)
        self.assertEqual(r, (2.4, 'RM'))

    def test_04h_media_pai_porcentagem_acertos(self):
        # 76% em cada prova PAI. Nota do PAI vai para 10.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 38, 38, 38, 10, 10, 10)
        self.assertEqual(r, (3, 'RM'))

    def test_04i_media_pai_porcentagem_acertos(self):
        # 100% em cada prova PAI.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 10, 10, 10)
        self.assertEqual(r, (3, 'RM'))

    # Testes que verificam como se dá o ajuste das notas do PAI de acordo com os percentis de acertos.

    def test_05a_media_pai_percentis(self):
        # Nota do PAI seria 7.4, que é jogado para 8, mas como está acima do percentil80, vai para 10.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 37, 37, 37, 1, 1, 7)
        self.assertEqual(r, (3, 'RM'))

    def test_05b_media_pai_percentis(self):
        # Nota do PAI seria 7.4, que é jogado para 8, mas como está igual ao percentil80, vai para 10.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 37, 37, 37, 1, 1, 8)
        self.assertEqual(r, (3, 'RM'))

    def test_05c_media_pai_percentis(self):
        # Nota do PAI seria 4, mas como está acima do percentil80, vai para 10.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 1, 2, 3)
        self.assertEqual(r, (3, 'RM'))

    def test_05d_media_pai_percentis(self):
        # Nota do PAI seria 4, mas como está igual ao percentil80, vai para 10.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 1, 2, 4)
        self.assertEqual(r, (3, 'RM'))

    def test_05e_media_pai_percentis(self):
        # Nota do PAI seria 4, mas como está entre o percentil60 é o percentil80, vai para 8.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 1, 2, 9)
        self.assertEqual(r, (2.4, 'RM'))

    def test_05f_media_pai_percentis(self):
        # Nota do PAI seria 4, mas como é igual ao percentil60, vai para 8.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 1, 4, 9)
        self.assertEqual(r, (2.4, 'RM'))

    def test_05g_media_pai_percentis(self):
        # Nota do PAI seria 4, mas como está entre o percentil40 é o percentil60, vai para 6.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 1, 5, 9)
        self.assertEqual(r, (1.8, 'RM'))

    def test_05h_media_pai_percentis(self):
        # Nota do PAI seria 4, mas como é igual ao percentil40, vai para 6.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 4, 5, 9)
        self.assertEqual(r, (1.8, 'RM'))

    def test_05i_media_pai_percentis(self):
        # Nota do PAI é 4, que assim fica por ser menor que o percentil40.
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 5, 7, 9)
        self.assertEqual(r, (1.2, 'RM'))

    # Testes que verificam como as faltas afetam o conceito.

    def test_06a_faltas(self):
        r = resultado_com_pai(0.9, 2, 2, 2, 2, 2, 2, 2, 10, 10, 10, 10, 10, 10)
        self.assertEqual(r, (2, 'RM'))

    def test_06b_faltas(self):
        r = resultado_com_pai(0.2, 2, 2, 2, 2, 2, 2, 2, 10, 10, 10, 10, 10, 10)
        self.assertEqual(r, (2, 'RMF'))

    def test_06c_faltas(self):
        r = resultado_com_pai(0.2, 10, 10, 10, 10, 10,
                              10, 10, 50, 50, 50, 1, 2, 3)
        self.assertEqual(r, (10, 'RF'))

    def test_06d_faltas(self):
        r = resultado_com_pai(0.9, 10, 10, 10, 10, 10,
                              10, 10, 50, 50, 50, 1, 2, 3)
        self.assertEqual(r, (10, 'AP'))

    # Testes que verificam como a nota é composta.

    def test_07a_composicao_das_notas(self):
        r = resultado_com_pai(0.9, 10, 10, 10, 10, 10,
                              0, 0, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (3, 'RM'))

    def test_07b_composicao_das_notas(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (4, 'RM'))

    def test_07c_composicao_das_notas(self):
        r = resultado_com_pai(0.9, 0, 0, 0, 0, 0, 0, 0, 10, 50, 50, 10, 10, 10)
        self.assertEqual(r, (3, 'RM'))

    def test_07d_composicao_das_notas(self):
        r = resultado_com_pai(0.9, 8, 8, 8, 8, 8, 0, 8, 12, 12, 12, 10, 10, 10)
        self.assertEqual(r, (6.32, 'AP'))

    # Testes que verificam a nota mínima para a aprovação.

    def test_08a_arredondamento_das_notas(self):
        # Média sem arredondamento é 5.24.
        r = resultado_com_pai(0.9, 10, 10, 10, 10, 10,
                              2.24 / 0.4, 0, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (5.24, 'RM'))

    def test_08b_arredondamento_das_notas(self):
        # Média sem arredondamento é 5.25.
        r = resultado_com_pai(0.9, 10, 10, 10, 10, 10,
                              2.25 / 0.4, 0, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (5.25, 'RM'))

    def test_08c_arredondamento_das_notas(self):
        # Média sem arredondamento é 5.74.
        r = resultado_com_pai(0.9, 10, 10, 10, 10, 10,
                              2.74 / 0.4, 0, 0, 0, 0, 10, 10, 10)
        self.assertEqual(r, (5.74, 'RM'))


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestNota)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    runTests()
