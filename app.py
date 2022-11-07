from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O porder do Amanha',
        'dataCriacao': '10-11-2002'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'datacriacao': '08-09-2001'
    },
    {
        'id': 3,
        'titulo': 'Code Clear',
        'dataCriacao': '09-07-2003'
    },
]

# Consultar(todos)
@app.route('/livros/get',methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
# Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    
    return jsonify(livros)
# Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)