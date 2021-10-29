from flask import Response, Blueprint, render_template, request, jsonify
import json

from app.models import user


api = Blueprint("api", __name__, url_prefix="/api")


# https://flask.palletsprojects.com/en/2.0.x/quickstart/#variable-rules
@api.route("/<string:name>/json1")
def api_hello_world_json(name="World"):
    response = {
        "message": f"Hello {name}"
    }
    return response, 200


@api.route("/error")
def api_error_example():
    response = {
        "error": True,
        "message": "Requisição inválida, nenhum valor foi informado!"
    }
    return response, 400


@api.route("/error2")
def api_error_example2():
    response = {
        "error": True,
        "message": "Requisição inválida, nenhum valor foi informado!"
    }
    return Response(
        response=json.dumps(response), 
        status=400,
        headers={
            "X-Custom-Header": "Custom value"
        },
    )


@api.route("/users", methods=["GET"])
def api_list_users():
    users = user.list_users()
    response = json.dumps({
        "error": False,
        "users": users,
        "total": len(users),
    })
    return Response(
        response=response,
        status=200,
        headers={
            "Content-Type": "application/json"
        }
    )


@api.route("/users2", methods=["GET"])
def api_list_users2():
    '''
    Nesse caso, ao usar o jsonify ou json.dumps, a resposta ao client que solicitou
    essa rota, contém dados encodados de uma forma estranha, como se não tivesse
    reconhecendo como application/json.

    a rota da função api_list_users() seria o melhor jeito para não ter problemas futuros
    '''
    users = user.list_users()
    response = json.dumps({
        "error": False,
        "users": users,
        "total": len(users),
    })
    return jsonify(response), 200


@api.route("/users/<int:user_id>", methods=["GET"])
def api_get_user(user_id=0):
    # se o ID do usuário for par por exemplo, não autorizamos a 
    # visualização desse dado
    if (user_id % 2 == 0):
        return Response(
            response=json.dumps({
                "error": False,
                "message": "User not found"
            }),
            status=403,
            headers={
                "Content-Type": "application/json"
            }
        )
        
    user_data = user.get_user(user_id)
    response = json.dumps({
        "error": False,
        "data": user_data,
    })

    return Response(
        response=response,
        status=200,
        headers={
            "Content-Type": "application/json"
        }
    )