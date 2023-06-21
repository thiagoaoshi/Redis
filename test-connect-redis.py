# Autor Vini Oliveira com pequenos ajuste meus Thiago Bruno
import redis
import getopt
import sys
import json
'''
Como usar o script
rodar o comando: <pipenv shell> no diretório, para que ele crie um bash e possibilite carregar os pacotes que foram instaladas no projeto.
-- Adicionar ou atualizar já uma chave no redis.
python3 client.py -s '{"foo":"bar1"}'

-- Retornar um valor de uma chave já existente
python3 cliente.py -g foo
'''
# Thiago malinando no codigo do dev  supremo
r = redis.Redis(
    host='server.localdomain',
    port=6379,
    decode_responses=True,
#   username="default", # estamos usando usuario default
    password="senha_definida_no_redis", 
    ssl=True,
    ssl_certfile="./redis.crt",
    ssl_keyfile="./redis.key",
    ssl_ca_certs="./ca.crt",
)
# Thigao terminou de malinar
 
if r.ping() == True:
  print("Conexão efetuada com sucesso! =)")
else:
  print("Ocorreu um erro na conexão")
set_arg =""
get_arg =""
argv = sys.argv[1:]

try:
    options, args = getopt.getopt(argv, "s:g:", ["set =", "get ="])
except:
    print("Error Message ")

for name, value in options:
  if name in ['-s', '--set']:
    set_arg = value
    set_arg_parsed = json.loads(set_arg)

    for key in set_arg_parsed:
      r.set(f'{key}', set_arg_parsed[key])
  elif name in ['-g', '--get']:
      get_arg = value
      print(r.get(get_arg))
