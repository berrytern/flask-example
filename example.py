# validação de entrada em python
from typing import Optional
from pydantic import StrictStr, StrictInt
from pydantic import BaseModel

class Example(BaseModel):
    # não faz conversão de tipos(Strict...)
    nome: StrictStr # campo optional
    # nome: str # faz conversão para string
    idade: Optional[StrictInt] # campo optional
    # nome: int # faz conversão para inteiro

entrada = {"nome": "pedro"}
# obj = Example(nome="pedro", idade=23)
obj = Example(**entrada)
print(type(obj.nome), obj.nome, obj.idade)

def func(nome, idade):
    return nome, idade

#func(nome="nome", idade=2)
#func(idade=2, nome="nome")