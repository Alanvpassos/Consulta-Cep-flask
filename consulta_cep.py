from flask import Flask
from flask import render_template
from flask import request
import requests
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/consulta-cep', methods=['POST'])
def consulta_cep():
    cep = request.form['cep']
    response = requests.get('http://viacep.com.br/ws/'+cep+'/json').json()
    
    data = {'CEP':response['cep'],'Bairro':response['bairro'],'UF':response['uf'],'Código IBGE':response['ibge'] }
    return render_template('response.html',result=data)

if __name__ == '__main__':
    app.run()