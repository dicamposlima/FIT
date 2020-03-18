from requests import api
from dataclasses import dataclass

"""
Instruções para TODOS os exercícios/funções abaixo:
1. Veja as instruções de como instalar e executar o PokeAPI, o treinador e os testes no documento entregue junto com este arquivo.
2. Se um determinado parâmetro de uma função deve ser inteiro, então esta função deve rejeitar valores não-numéricos ou numerais não-inteiros nesse parâmetro.
3. Da mesma forma, se um parâmetro de uma função deve ser uma string, então esta função deve rejeitar valores que não sejam do tipo string nesse parâmetro.
4. Strings em branco são sempre consideradas inválidas.
5. Se algum dos parâmetros ser inválido, uma ValueError deve ser lançada. Recomenda-se usar as funções check_int e check_str acima para ajudar na validação.
6. Se algum parâmetro puder ser determinado como inválido antes que alguma chamada a um servidor externo seja realizada, então ele deve ser detectado como tal sem que o servidor seja contactado, mesmo se ele estiver off-line.
7. Em todos os casos onde procura-se algum tipo de pokémon pelo nome ou pelo número e o mesmo não existir, uma exceção PokemonNaoExisteException deve ser lançada.
8. Em todos os casos onde procura-se algum treinador cadastrado e o mesmo não existir, uma exceção TreinadorNaoCadastradoException deve ser lançada.
9. Em todos os casos onde procura-se algum pokémon cadastrado e o mesmo não existir, uma exceção PokemonNaoCadastradoException deve ser lançada.
10. Em todos os casos onde tenta-se cadastrar um pokémon e o mesmo já exista, uma exceção PokemonJaCadastradoException deve ser lançada.
11. Todos os nomes de pokémons que aparecerem como parâmetros devem ser aceitos em minúsculas, MAIÚSCULAS ou até mesmo MiStUrAdO. Lembre-se dos métodos lower() e upper() da classe string.
12. Todos os nomes de pokémons, cores, jogos, movimentos, etc. recebidos e devolvidos pela PokeAPI estão em letras minúsculas e assim devem ser mantidas.
13. Não faça conexões com as URLs externas (https://pokeapi.co). O motivo disso é que eles irão bloquear IPs que fizerem um número muito grande de requisições.

Alguns exemplos de URLs que podem servir de inspiração:
http://localhost:8000/api/v2/
http://localhost:8000/api/v2/pokemon/39/
http://localhost:8000/api/v2/pokemon/jigglypuff/
http://localhost:8000/api/v2/pokemon-species/39/
http://localhost:8000/api/v2/pokemon-species/jigglypuff/
http://localhost:8000/api/v2/evolution-chain/11/
http://localhost:8000/api/v2/growth-rate/1/
http://localhost:8000/api/v2/pokemon-color/2/
"""

"""
Não altere estas URLs. Elas são utilizadas para conectar no treinador e no PokeAPI, respectivamente.
"""
site_treinador = "http://127.0.0.1:9000"
site_pokeapi = "http://127.0.0.1:8000"

"""
Vamos precisar destas quatro exceções personalizadas.
"""
class PokemonNaoExisteException(Exception):
    pass

class PokemonNaoCadastradoException(Exception):
    pass

class TreinadorNaoCadastradoException(Exception):
    pass

class PokemonJaCadastradoException(Exception):
    pass

"""
Esta função certifica-se de que seu parâmetro é um número inteiro e lança uma ValueError se não for.
"""
def check_int(a):
    if type(a) is not int:
        raise ValueError()

"""
Esta função certifica-se de que seu parâmetro é uma string e que não está vazia e lança uma ValueError se não for.
"""
def check_str(a):
    if type(a) is not str or a == "":
        raise ValueError()

"""
Esta classe será utilizada no exercício 12 abaixo.
"""
@dataclass(frozen = True)
class Pokemon:
    nome_treinador: str
    apelido: str
    tipo: str
    experiencia: int
    nivel: int
    cor: str
    evoluiu_de: str
    evolui_para: list

"""
1. Dado o número de um pokémon, qual é o nome dele?
"""
def nome_do_pokemon(numero):
    check_int(numero)
    pokemon = api.get(f"{site_pokeapi}/api/v2/pokemon/{numero}/")
    if pokemon.status_code == 404:
        raise PokemonNaoExisteException()
    else:
        return pokemon.json()['name']

"""
2. Dado o nome de um pokémon, qual é o número dele?
"""
def numero_do_pokemon(nome):
    check_str(nome)
    nome = nome.lower()
    pokemon = api.get(f"{site_pokeapi}/api/v2/pokemon/{nome}/")
    if pokemon.status_code == 404:
        raise PokemonNaoExisteException()
    else:
        return pokemon.json()['id']

"""
3. Dado o nome ou número de um pokémon, qual é o nome da cor (em inglês) predominante dele?
"""
def color_of_pokemon(nome):    
    if type(nome) == str:
        check_str(nome)
        id = numero_do_pokemon(nome)
    else:
        check_int(nome)
        id = nome
    pokemon = api.get(f"{site_pokeapi}/api/v2/pokemon-species/{id}/")
    if pokemon.status_code == 404:
        raise PokemonNaoExisteException()
    else:
        return pokemon.json()["color"]['name']

"""
4. Dado o nome ou número de um pokémon, qual é o nome da cor (em português) predominante dele?
Os nomes de cores possíveis em português são "marrom", "amarelo", "azul", "rosa", "cinza", "roxo", "vermelho", "branco", "verde" e "preto".
No entanto, a pokeapi ainda não foi traduzida para o português! Como você pode dar um jeito nisso?
"""
def cor_do_pokemon(nome):
    check_str(nome)
    color = color_of_pokemon(nome)
    color_portugues = {'blue':'azul','brown':'marrom','yellow':'amarelo','pink':'rosa','gray':'cinza','purple':'roxo','red':'vermelho','white':'branco','green':'verde','black':'preto'}
    return color_portugues[color]
"""
5. Dado o nome de um pokémon, quais são os tipos no qual ele se enquadra?
Os nomes dos tipos de pokémons em português são "normal", "lutador", "voador", "veneno", "terra", "pedra", "inseto", "fantasma", "aço", "fogo", "água", "grama", "elétrico", "psíquico", "gelo", "dragão", "noturno" e "fada".
Todo pokémon pode pertencer a um ou a dois tipos diferentes. Retorne uma lista contendo os tipos, mesmo que haja somente um.
Se houver dois tipos, a ordem não é importante.
"""
def tipos_do_pokemon(nome):
    check_str(nome)
    nome = nome.lower()
    pokemon = api.get(f"{site_pokeapi}/api/v2/pokemon/{nome}/")
    if pokemon.status_code == 404:
        raise PokemonNaoExisteException()
    else:
        types = []
        translation = {"normal":"normal","fighting":"lutador","flying":"voador","poison":"veneno","ground":"terra","rock":"pedra","bug":"inseto","ghost":"fantasma","steel":"aço","fire":"fogo","water":"água","grass":"grama","electric":"elétrico","psychic":"psíquico","ice":"gelo","dragon":"dragão","dark":"noturno","fairy":"fada"}
        for type_ in pokemon.json()['types']:
            types.append(translation[type_['type']['name']])
        return types

"""
6. Dado o nome de um pokémon, liste de qual pokémon ele evoluiu.
Por exemplo, evolucao_anterior('venusaur') == 'ivysaur'
Retorne None se o pokémon não tem evolução anterior. Por exemplo, evolucao_anterior('bulbasaur') == None
"""
def evolucao_anterior(nome):
    check_str(nome)
    id = numero_do_pokemon(nome)
    pokemon = api.get(f"{site_pokeapi}/api/v2/pokemon-species/{id}/")
    result = pokemon.json()
    if "evolves_from_species" in result and result["evolves_from_species"]:
        return result["evolves_from_species"]['name']
    return None

"""
7. Dado o nome de um pokémon, liste para quais pokémons ele pode evoluiur.
Por exemplo, evolucoes_proximas('ivysaur') == ['venusaur'].
A maioria dos pokémons que podem evoluir, só podem evoluir para um único tipo de pokémon próximo. No entanto, há alguns que podem evoluir para dois ou mais tipos diferentes de pokémons.
Se houver múltiplas possibilidades de evoluções, a ordem delas não importa. Por exemplo:
evolucoes_proximas('poliwhirl') == ['poliwrath', 'politoed']
Note que esta função dá como resultado somente o próximo passo evoluitivo. Assim sendo, evolucoes_proximas('poliwag') == ['poliwhirl']
Se o pokémon não evolui, retorne uma lista vazia. Por exemplo, evolucoes_proximas('celebi') == []
"""
def evolucoes_proximas(nome):
    check_str(nome)
    id = numero_do_pokemon(nome)
    pokemon = api.get(f"{site_pokeapi}/api/v2/pokemon-species/{id}/")
    pokemon = pokemon.json()
    if "url" not in pokemon["evolution_chain"]:
        return []
    evolution_chain = api.get(pokemon["evolution_chain"]["url"])
    evolution_chain = evolution_chain.json()
    if len(evolution_chain["chain"]["evolves_to"]) <= 0:
        return []
    
    evolves = []
    if evolution_chain["chain"]["species"]["name"] == nome.lower():
        evolves = evolution_chain["chain"]["evolves_to"]
    else:
        for chain in evolution_chain["chain"]["evolves_to"]:
            if chain["species"]["name"] == nome.lower():
                evolves = chain["evolves_to"]
    if len(evolves) <= 0:
        return []

    types = []
    for type_ in evolves:
        types.append(type_["species"]['name'])
    return types

"""
8. A medida que ganham pontos de experiência, os pokémons sobem de nível.
É possível determinar o nível (1 a 100) em que um pokémon se encontra com base na quantidade de pontos de experiência que ele tem.
Entretanto, cada tipo de pokémon adota uma curva de level-up diferente (na verdade, existem apenas 6 curvas de level-up diferentes).
Assim sendo, dado um nome de pokémon e uma quantidade de pontos de experiência, retorne o nível em que este pokémon está.
Valores negativos de experiência devem ser considerados inválidos.
"""
def nivel_do_pokemon(nome, experiencia):
    check_str(nome)
    check_int(experiencia)
    id = numero_do_pokemon(nome)
    pokemon = api.get(f"{site_pokeapi}/api/v2/pokemon-species/{id}/")
    pokemon = pokemon.json()
    if "url" not in pokemon["growth_rate"]:
        return 0
    growth_rate = api.get(pokemon["growth_rate"]["url"])
    growth_rate = growth_rate.json()
    if len(growth_rate["levels"]) <= 0:
        return 0
    
    rate = -1
    i = 0
    growth_rate_len = len(growth_rate["levels"])
    while experiencia >= rate:
        if i == growth_rate_len:
            break
        rate = growth_rate["levels"][i]["experience"]
        if rate <= experiencia:
            i = i + 1

    return growth_rate["levels"][i-1]["level"]

"""
9. Dado um nome de treinador, cadastre-o na API de treinador.
Retorne True se um treinador com esse nome foi criado e False em caso contrário (já existia).
"""
def cadastrar_treinador(nome):
    check_str(nome)

    treinador = api.get(f"{site_treinador}/treinador/{nome}")
    if treinador.status_code == 200:
        return False

    treinador = api.put(f"{site_treinador}/treinador/{nome}")
    if treinador.status_code == 202:
        return True
    else:
        return False
"""
10. Imagine que você capturou dois pokémons do mesmo tipo. Para diferenciá-los, você dá nomes diferentes (apelidos) para eles.
Logo, um treinador pode ter mais do que um pokémon de um determinado tipo, mas não pode ter dois pokémons diferentes com o mesmo apelido.
Assim sendo, dado um nome de treinador, um apelido de pokémon, um tipo de pokémon e uma quantidade de experiência,
cadastre o pokémon com o tipo correspondente ao treinador dado na API do treinador.
Certifique-se de que todos os dados são válidos.
"""
def cadastrar_pokemon(nome_treinador, apelido_pokemon, tipo_pokemon, experiencia):
    check_str(nome_treinador)
    treinador = api.get(f"{site_treinador}/treinador/{nome_treinador}")
    if treinador.status_code == 404:
        raise TreinadorNaoCadastradoException()

    check_str(apelido_pokemon)
    check_str(tipo_pokemon)
    numero_do_pokemon(tipo_pokemon)

    check_int(experiencia)
    tipo_pokemon = tipo_pokemon.lower()
    pokemon = api.get(f"{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}")
    if pokemon.status_code == 200:
        raise PokemonJaCadastradoException()
    payload = {"tipo": tipo_pokemon, "experiencia": experiencia}
    api.put(f"{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}", json=payload)


"""
11. Dado um nome de treinador, um apelido de pokémon e uma quantidade de experiência, localize esse pokémon e acrescente-lhe a experiência ganha.
"""
def ganhar_experiencia(nome_treinador, apelido_pokemon, experiencia):
    check_str(nome_treinador)
    treinador = api.get(f"{site_treinador}/treinador/{nome_treinador}")
    if treinador.status_code == 404:
        raise TreinadorNaoCadastradoException()
    
    check_str(apelido_pokemon)
    pokemon = api.get(f"{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}")
    if pokemon.status_code != 200:
        raise PokemonNaoCadastradoException()

    check_int(experiencia)
    pokemon = pokemon.json()
    api.post(f"{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}/exp", json={'experiencia': experiencia})


"""
12. Dado um nome de treinador e um apelido de pokémon, localize esse pokémon na API do treinador e retorne um objeto da classe Pokemon mostrando:
Qual é a sua espécie, a sua quantidade de experiência e em que nível ele está.
"""
#from pokemon import Pokemon
def localizar_pokemon(nome_treinador, apelido_pokemon):
    check_str(nome_treinador)
    treinador = api.get(f"{site_treinador}/treinador/{nome_treinador}")
    if treinador.status_code == 404:
        raise TreinadorNaoCadastradoException()
    
    check_str(apelido_pokemon)
    pokemon = api.get(f"{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}")
    if pokemon.status_code == 200:
        pokemon = pokemon.json()
        tipo = pokemon["tipo"]
        experiencia = pokemon["experiencia"]
        nivel = nivel_do_pokemon(pokemon["tipo"], pokemon["experiencia"])
        cor = cor_do_pokemon(pokemon["tipo"])        
        evoluiu_de = evolucao_anterior(pokemon["tipo"])
        evolui_para = evolucoes_proximas(pokemon["tipo"])
        p = Pokemon(nome_treinador, apelido_pokemon, tipo, experiencia, nivel, cor, evoluiu_de, evolui_para)
        return p
    raise PokemonNaoCadastradoException()

"""
13. Dado o nome de um treinador, localize-o na API do treinador e retorne um dicionário contendo como chaves,
os apelidos de seus pokémons e como valores os tipos deles.
"""
def detalhar_treinador(nome_treinador):
    check_str(nome_treinador)

    treinador = api.get(f"{site_treinador}/treinador/{nome_treinador}")
    if treinador.status_code != 200:
        raise TreinadorNaoCadastradoException()
    else:
        treinador = treinador.json()
        if len(treinador["pokemons"]) > 0:
            pokemons = {}
            for pokemon in treinador["pokemons"]:
                pokemons[pokemon] = (treinador["pokemons"][pokemon]["tipo"])
            return pokemons
        else:
            return {}

"""
14. Dado o nome de um treinador, localize-o na API do treinador e exclua-o, juntamente com todos os seus pokémons.
"""
def excluir_treinador(nome_treinador):
    check_str(nome_treinador)
    treinador = api.get(f"{site_treinador}/treinador/{nome_treinador}")
    if treinador.status_code != 200:
        raise TreinadorNaoCadastradoException()
    pokemons = detalhar_treinador(nome_treinador)
    if len(pokemons) > 0:
        for apelido_pokemon in pokemons:
            excluir_pokemon(nome_treinador, apelido_pokemon)
            #api.delete(f"{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}")
    api.delete(f"{site_treinador}/treinador/{nome_treinador}")

"""
15. Dado o nome de um treinador e o apelido de um de seus pokémons, localize o pokémon na API do treinador e exclua-o.
"""
def excluir_pokemon(nome_treinador, apelido_pokemon):
    check_str(nome_treinador)
    treinador = api.get(f"{site_treinador}/treinador/{nome_treinador}")
    if treinador.status_code != 200:
        raise TreinadorNaoCadastradoException()

    check_str(apelido_pokemon)
    pokemon = api.get(f"{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}")
    if pokemon.status_code != 200:
        raise PokemonNaoCadastradoException()

    api.delete(f"{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}")