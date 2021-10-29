# flask-examples
## Introdução

Esse projeto contém uma estrutura básica de projeto e exemplos de como criar uma API, rotas, responder requisições com status diferentes, e entre outros.

## Estrutura

Para esse projeto, a estrutura do projeto é:
- *app/* - diretório onde contém a implementação da aplicação
- *app/api* - contém a rota /api/ do projeto
- *app/models* - contém manipulação de dados específicos da sua aplicação, como gerenciar usuários
- *app/templates* - contém os HTML com códigos de jinja2, para exibir ao usuário
- *examples/* - alguns exemplos de comando de CURL 
- *tests/* - testes unitários / integração para o projeto
- *uploads/* - diretório da aplicação para armazenar os arquivos que foram submetidos pelo o usuário

## Iniciando o projeto

Para iniciar o projeto, execute os seguintes comandos:

Criar um ambiente virtual
```bash
$ python3 -m virtualenv env
```

Iniciando o ambiente virtual (linux)
```bash
$ source env/bin/activate 
```
Iniciando o ambiente virtual (windows)
```
$ .\env\bin\activate.cmd
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

[Visualizar](./examples/curl_commands.md)


## Executando testes unitários / integração no projeto

Execute o seguinte comando para validar os testes, para esse projeto o output será:
```bash
$ python3 -m unittest tests/test_app.py

Finished
.Finished
F
======================================================================
FAIL: test_get_index (tests.test_app.FlaskTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "~/rodjul/flask-examples/tests/test_app.py", line 32, in test_get_index
    self.assertEqual(home.get_data(as_text=True), "<p>Hello World!</p>", "O valor do index, deveria ser <p>Hello, World!</p>")
AssertionError: '<p>Hello, World!</p>' != '<p>Hello World!</p>'
- <p>Hello, World!</p>
?         -
+ <p>Hello World!</p>
 : O valor do index, deveria ser <p>Hello, World!</p>

----------------------------------------------------------------------
Ran 2 tests in 0.018s

FAILED (failures=1)
```

## Referências

- [Curso de flask para mais informações](https://www.youtube.com/watch?v=r40pC9kyoj0)
- [Comandos do FLASK](https://flask.palletsprojects.com/en/2.0.x/cli/)
- [Exemplos de WSGI compatíveis com FLASK](https://flask.palletsprojects.com/en/2.0.x/deploying/)
- [Gunicorn](https://flask.palletsprojects.com/en/2.0.x/deploying/wsgi-standalone/)

- [Criando um projeto mínimo, pronto para produção](https://mark.douthwaite.io/getting-production-ready-a-minimal-flask-app/)