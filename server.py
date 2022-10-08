from flask import Flask, Response, request
from json import dumps, loads
from src.utils import settings

# json.dumps - convert python structs to string
# json.loads - convert string to python structs
app = Flask(__name__)

examples=[]

@app.route("/example", methods=["GET"])
def example_get():
    # em métodos GET, não devemos utilizar ou aceitar corpo de requisição
    return Response(dumps(examples), status=200, headers={"Content-Type": "application/json"})

#example={"nome":"example"}

@app.route("/example", methods=["POST"])
def example_post():
    # acesso ao corpo da requisição
    # request.data - bytes
    # request.json - json or Map(dict)
    print(request.json)
    if("nome" in request.json):
        examples.append(request.json)
    return Response("post", status=204, headers={"Content-Type": "application/json"})

app.run("0.0.0.0", port=settings.PORT, debug=True)