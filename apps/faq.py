import json

from database import faq

def get_faq():
    request = faq.select()
    resultados = []

    for fila in request:
        modelo = {
            'id': fila.id,
            'ask': fila.ask,
            'answer': fila.answer
        }
        resultados.append(modelo)

    json_result = json.dumps({'faq': resultados})
    data = json.loads(json_result)

    return data
