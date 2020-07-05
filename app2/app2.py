from flask import Flask, Response, request, jsonify
from random import choice 
import requests 

app=Flask(__name__)

@app.route('/animal', methods=['GET'])
def animal():
    anm_list=['dog', 'cat', 'cow']
    anm_choice=choice(anm_list)
    return Response(anm_choice, mimetype='text/plain')

@app.route('/noise', methods=['POST'])
def noise():
    data_sent=request.data.decode('utf-8')
    if data_sent=='cow':
        noise=='moo'
    elif data_sent=='cat':
        noise='meow'
    elif data_sent=='dog':
        noise='woof'
    else:
        noise='no noise'
    return Response("This is the noise: " + data_sent, mimetype='text/plain')


if __name__=='__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')
