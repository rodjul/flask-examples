# Exemplos de CURL


Enviar um arquivo no /upload
```bash
$ curl localhost:5000/upload -F "file=@arquivo.txt" -i

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 36
Server: Werkzeug/2.0.2 Python/3.6.14
Date: Fri, 29 Oct 2021 00:58:48 GMT

file arquivo.txt upload with successr

```

Ver os usuários
```bash
$ curl localhost:5000/api/users -i

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 899
Server: Werkzeug/2.0.2 Python/3.6.14
Date: Fri, 29 Oct 2021 00:59:23 GMT

{
    "error": false, 
    "users": [{"id": 1, "email": "george.bluth@reqres.in", "first_name": "George", "last_name": "Bluth", "avatar": "https://reqres.in/img/faces/1-image.jpg"}, {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver", "avatar": "https://reqres.in/img/faces/2-image.jpg"}, {"id": 3, "email": "emma.wong@reqres.in", "first_name": "Emma", "last_name": "Wong", "avatar": "https://reqres.in/img/faces/3-image.jpg"}, {"id": 4, "email": "eve.holt@reqres.in", "first_name": "Eve", "last_name": "Holt", "avatar": "https://reqres.in/img/faces/4-image.jpg"}, {"id": 5, "email": "charles.morris@reqres.in", "first_name": "Charles", "last_name": "Morris", "avatar": "https://reqres.in/img/faces/5-image.jpg"}, {"id": 6, "email": "tracey.ramos@reqres.in", "first_name": "Tracey", "last_name": "Ramos", "avatar": "https://reqres.in/img/faces/6-image.jpg"}], 
    "total": 6
}
```

Ver 1 usuário
```bash
$ curl localhost:5000/api/users/1 -i

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 199
Server: Werkzeug/2.0.2 Python/3.6.14
Date: Fri, 29 Oct 2021 01:00:34 GMT

{
  "error": false,
  "data": {
    "id": 1,
    "email": "george.bluth@reqres.in",
    "first_name": "George",
    "last_name": "Bluth",
    "avatar": "https://reqres.in/img/faces/1-image.jpg"
  }
}
```
