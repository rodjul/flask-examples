# flask-examples
## Introdução

Esse projeto contém uma estrutura básica de projeto e exemplos de como criar uma API, rotas, responder requisições com status diferentes, e entre outros.

## Iniciando o projeto

Para iniciar o projeto, execute os seguintes comandos:

Criar um ambiente virtual
```bash
$ python3 -m virtualenv env
```

Instalar as depêndencias
```bash
(env) $ pip3 install -r requirements.txt
```

Iniciar o projeto
```bash
(env) $ flask run --debugger --reload --host 0.0.0.0
```


## Colocando em produção o projeto

Para colocar o projeto em produção, não é recomendado utilizar o próprio webserver do FLASK por conta de perda de performance.

Para isso, precisamos utilizar um WSGI (Web Server Gateway Interface) que nos permite chamar nossas rotas do projeto com uma boa performance, e será o Gunicorn.

Execute o seguinte comando para iniciar o projeto, onde utiliza o wsgi.py para obter as referências:
```bash
$ gunicorn -b 0.0.0.0:8080 -w 4 wsgi:app --log-level=debug
```

## Alguns exemplos de comando CURL

- 


## Referências

- [Comandos do FLASK](https://flask.palletsprojects.com/en/2.0.x/cli/)

- [Exemplos de WSGI compatíveis com FLASK](https://flask.palletsprojects.com/en/2.0.x/eploying/)
- [Gunicorn](https://flask.palletsprojects.com/en/2.0.x/deploying/wsgi-standalone/)

- [Criando um projeto mínimo, pronto para produção](https://mark.douthwaite.io/getting-production-ready-a-minimal-flask-app/)