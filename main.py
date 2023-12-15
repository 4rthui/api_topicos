from typing import Optional, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/quadrados")
def squares(max: Optional[int] = 10):
    res = []
    for i in range(1, max+1, 1):
        res.append(i*i)

    return {"max": max, "quadrados": res}


@app.get("/tabuada/{num}")
def tabuada(num: int, start: Optional[int] = 1, end: Optional[int] = 10):
    res = []
    for i in range(start, end+1, 1):
        res.append(num*i)
    return {"num": num,
            "start": start,
            "end": end,
            "tabuada": res}


class PayloadBhaskara(BaseModel):
    a: int
    b: int
    c: int


def moreMinus(value):
    if value < 0:
        return " - "
    else:
        return " + "


@app.post("/bhaskara")
def tabuada(payload: PayloadBhaskara):
    a = payload.a
    b = payload.b
    c = payload.c
    delta = (b ** 2) - 4 * a * c

    if a == 0:
        return "O valor de a deve ser diferente de 0"
    elif delta < 0:
        return {
            "eq": str(a) + "x²" + moreMinus(b) + str(b).replace("-", "") + "x" + moreMinus(c) + str(c).replace("-", ""),
            "res": "Sem raízes reais"
        }
    elif delta == 0:
        return {
            "eq": a + "{a}x²" + b + "x" + "  " + c,
            "x": (-b / (2 * a))
        }
    else:
        return {
            "eq": str(a) + "x² " + moreMinus(b) + str(b).replace("-", "") + "x " + moreMinus(c) + str(c).replace("-", ""),
            "x1": (-b + delta ** (1 / 2)) / (2 * a),
            "x2": (-b - delta ** (1 / 2)) / (2 * a)
        }


class PayloadFrase(BaseModel):
    frase: str

@app.post("/conta")
def contafrase(payload: PayloadFrase):
    vogais = "aeiou"
    vogaisCount = 0
    espacosCount = 0
    outrosCount = 0

    for i in payload.frase:
        if i.lower() in vogais:
            vogaisCount += 1
        elif i == " ":
            espacosCount += 1
        else:
            outrosCount += 1

    return {
        "frase": payload.frase,
        "vogais": vogaisCount,
        "espacos": espacosCount,
        "outros": outrosCount
    }
