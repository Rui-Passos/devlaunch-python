import json
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Funções para carregar e guardar dados em JSON
def carregar_dados():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return [] # Retorna lista vazia se o ficheiro não exitir
    
# Guardar dados no ficheiro JSON
def guardar_dados():
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    erro = None
    if request.method == 'POST':
        #1. Obter dados do formulario e "limpar" espaços em branco com .strip()
        titulo = request.form.get('titulo', '').strip()
        descricao = request.form.get('descricao', '').strip()
        imagem = request.form.get('imagem', '').strip()

        #2. Validar se algum campo está vazio
        if not titulo or not descricao or not imagem:
            erro = "Por favor, preenche todos os campos antes de gravar!"
        else:
            novo_projecto = {
                "id": len(carregar_dados()) + 1,
                "titulo": request.form.get('titulo'),
                "descricao": request.form.get('descricao'),
                "imagem": request.form.get('imagem')
            }
    
            #2. Ler dados actuais, adicionar o novo e guardar
            dados = carregar_dados()
            dados.append(novo_projecto)
            guardar_dados(dados)

            #3. Redirecionar para a página inicial
            return redirect(url_for('home'))
        
    # Passamos a variável 'error' para o html
    return render_template('admin.html', mensagem_error=erro)


@app.route('/')
def home():
    trabalhos = carregar_dados()
    return render_template('index.html', trabalhos=trabalhos)

if __name__ == '__main__':
    app.run(debug=True)

# Lista de projetos - Atenção às vírgulas e chavetas
projetos_restauro = [
    {
        "titulo": "Pintura a Óleo - Séc. XVIII",
        "descricao": "Limpeza de vernizes oxidados e reintegração cromática.",
        "imagem": "https://via.placeholder.com/400x300/e9e4d9/8b795e?text=Restauro+Pintura"
    },
    {
        "titulo": "Talha Dourada - Altar-Mor",
        "descricao": "Consolidação do suporte e aplicação de folha de ouro.",
        "imagem": "https://via.placeholder.com/400x300/e9e4d9/8b795e?text=Restauro+Talha"
    },
    {
        "titulo": "Escultura Policromada",
        "descricao": "Fixação de camada pictórica em peça de madeira.",
        "imagem": "https://via.placeholder.com/400x300/e9e4d9/8b795e?text=Escultura"
    }
]

@app.route('/')
def home():
    # Passamos a lista 'projetos_restauro' para a variável 'trabalhos' no HTML
    return render_template('index.html', trabalhos=projetos_restauro)

if __name__ == '__main__':
    app.run(debug=True)