from flask import Response, Blueprint, render_template, request
import json


main = Blueprint("main", __name__, url_prefix="/dev/")


@main.route("/")
def hello_world():
    return '''
<pre>
 _________
< DEV ENDPOINT >
 ---------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||    
</pre>'''



@main.route("/templates/get", methods=["GET"])
def dev_template():
    variavel_nome_get = request.args.get("nome")

    return render_template("index.html", variavel=variavel_nome_get)

@main.route("/templates/post", methods=["GET", "POST"])
def dev_template_post():
    if request.method == "GET":
        return render_template("template_post.html", is_form_submited=False)
    
    # method POST
    nome = request.form.get("nome", "")
    comentario = request.form.get("comentario", "")

    return render_template("template_post.html", is_form_submited=True, nome=nome, comentario=comentario)
