from flask import jsonify
from flask_jwt_extended import create_access_token

def realizar_autenticacao(username, password):
    # Adicione sua lógica de autenticação aqui (por exemplo, verificar credenciais em um banco de dados)
    if username == 'igor_souza' and password == '12345':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"mensagem": "Credenciais inválidas"}), 401
