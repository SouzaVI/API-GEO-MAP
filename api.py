from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required
from auth import realizar_autenticacao  # Importa a função de autenticação do arquivo auth


app = Flask(__name__)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'S8W5W8S7D45W8D5W'
jwt = JWTManager(app)

## Dicionario de exemplo
clientes = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": { "ID": 1, "CLIENTE": "CLIENTE A", "FAZENDA": "BOA SORTE", "TALHAO": "T_1", "HA": 100.0 },
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
            [
              [-50.981826803573675, -16.214143156599999],
              [-50.977199711321049, -16.213205232494737],
              [-50.976699485131576, -16.2147371752],
              [-50.97754361682631, -16.217394626831577],
              [-50.979950955363151, -16.21861392816842],
              [-50.983296218005258, -16.21655049513684],
              [-50.981826803573675, -16.214143156599999]
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": { "ID": 2, "CLIENTE": "CLIENTA A", "FAZENDA": "BOA SORTE", "TALHAO": "T_2", "HA": 50.0 },
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
            [
              [-50.983546331099994, -16.217207042010525],
              [-50.979825898815783, -16.219520588136842],
              [-50.982014388394731, -16.221615285305262],
              [-50.98557849999473, -16.222052983221051],
              [-50.986453895826308, -16.219520588136842],
              [-50.986172518594728, -16.217425890968421],
              [-50.983546331099994, -16.217207042010525]
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": { "ID": 3, "CLIENTE": "CLIENTE B", "FAZENDA": "FELIZ", "TALHAO": "T_3", "HA": 75.0 },
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
            [
              [-51.002345678901234, -16.185432109876543],
              [-51.000987654321098, -16.184567890123457],
              [-50.998765432109876, -16.185432109876543],
              [-50.999876543210987, -16.187654321098765],
              [-51.002345678901234, -16.185432109876543]
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": { "ID": 4, "CLIENTE": "CLIENTE C", "FAZENDA": "ALEGRIA", "TALHAO": "T_4", "HA": 120.0 },
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
            [
              [-50.950123456789012, -16.250987654321098],
              [-50.947654321098765, -16.250123456789012],
              [-50.946543210987654, -16.251234567890124],
              [-50.948765432109876, -16.253456789012346],
              [-50.950123456789012, -16.250987654321098]
            ]
          ]
        ]
      }
    }
  ]
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    return realizar_autenticacao(username, password)  # Chama a função de autenticação do arquivo auth


@app.route('/clientes', methods= ['GET'])
@jwt_required()
def obter_clientes():
    return jsonify(clientes)

@app.route('/clientes/<string:cliente_nome>', methods=['GET'])
@jwt_required()
def obter_cliente(cliente_nome):
  # Assume que clientes é uma lista de dicionários onde cada dicionário representa um cliente
  cliente = next((c for c in clientes["features"] if c["properties"]["CLIENTE"] == cliente_nome), None)

  if cliente:
    return jsonify({cliente_nome +" features ": [cliente]})
  else:
    return jsonify({"mensagem": "Cliente não encontrado"}), 404

@app.route('/clientes/<string:cliente_nome>', methods=['PUT'])
@jwt_required()
def atualizar_cliente(cliente_nome):
    # Assume que clientes é um dicionário onde cada chave é um nome de cliente e o valor é um dicionário representando o cliente
    cliente = next((c for c in clientes["features"] if c["properties"]["CLIENTE"] == cliente_nome), None)

    if cliente:
        # Obtém os dados enviados na requisição
        dados_atualizados = request.json

        # Atualiza os valores do cliente com os dados fornecidos
        cliente.update(dados_atualizados)

        return jsonify({"mensagem": "Cliente atualizado com sucesso", "novo_cliente": cliente}), 200
    else:
        return jsonify({"mensagem": "Cliente não encontrado"}), 404

@app.route('/clientes', methods=['POST'])
@jwt_required()
def adicionar_cliente():
    # Obtém os dados enviados na requisição
    nova_feature = request.json

    # Adiciona a nova feature ao dicionário de clientes
    clientes["features"].append(nova_feature)

    return jsonify({"mensagem": "Feature adicionada com sucesso", "nova_feature": nova_feature}), 201

app.run(port = 5000, host = 'localhost', debug= True)