# -*- coding: utf-8 -*-
"""Archivo principal para el echobot. Main File for the echobot"""
from flask import Flask, request
import ImageToMusic

app = Flask(__name__)

@app.route('/')
def hello_world():
    """La página principal del servidor. The server main page."""
    return 'Inicio del servidor'


@app.route('/soultempo', methods=['GET', 'POST'])
def st():
    data = None
    if request.method == 'POST':  # if the message is a POST, we handle it with message_handler. Si el mensaje es POST, se maneja con el message_handler
        main = ImageToMusic(JSON.request)

        img = request.args.get('base64img')
        audio = request.args.get('base64audio')
        mail = request.args.get('mail')
        imagename = request.args.get('imagename')

        data = main.processData()
    return data



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)
