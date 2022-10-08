# validação de entrada em python
from typing import Optional
from pydantic import StrictStr, StrictInt
from pydantic import BaseModel

class Example(BaseModel):
    nome: StrictStr
    idade: Optional[StrictInt] # campo optional

entrada = {"nome": "pedro"}
# obj = Example(nome="pedro", idade=23)
obj = Example(**entrada)
print(type(obj.nome), obj.nome, obj.idade)

def func(nome, idade):
    return nome, idade

#func(nome="nome", idade=2)
#func(idade=2, nome="nome")