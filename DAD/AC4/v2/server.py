'''
Esse servidor só está aqui pra gente se divertir no fim da AC, se quiser
Não faz parte da AC
'''
from flask import Flask, jsonify , request

simple_server = Flask(__name__)

@simple_server.route('/luta/<atacante>/<defensor>')
def lutar(atacante,defensor):
    return luta

luta = '''
merlin transforma harry em um flamingo, causando 8 de dano
<br>
Agora, harry tem 12 de vida
<br>
harry congela merlin, causando 7 de dano
<br>
harry solta raios contra merlin, causando 7 de dano
<br>
harry congela merlin, causando 7 de dano
<br>
harry solta raios contra merlin, causando 7 de dano
<br>
Agora, merlin tem 2 de vida
<br>
merlin solta raios contra harry, causando 8 de dano
<br>
Agora, harry tem 4 de vida
<br>
harry congela merlin, causando 7 de dano
<br>
harry congela merlin, causando 7 de dano
<br>
harry congela merlin, causando 7 de dano
<br>
harry solta raios contra merlin, causando 7 de dano
<br>
Agora, merlin tem 0 de vida
'''
#esse HTML está HORRIVEL. HORRIVEL. So pra te avisar. 
#nunca escreva HTML assim!

if __name__ == '__main__':
    simple_server.run(host = 'localhost', port = 5003, debug = True)
