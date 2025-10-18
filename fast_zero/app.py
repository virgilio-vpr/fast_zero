from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .schemas import Message

app = FastAPI(title='Fast Zero', version='0.1.0')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'Message': 'Olá Mundo!'}


@app.get('/exercicio-html', response_class=HTMLResponse)
def exercicio_aula_02():
    return """
    <html>
        <head>
            <title>Nosso olá mundo!</title>
        </head>
        <body>
            <h1> Olá Mundo </h1>
        </body>
    </html>"""
