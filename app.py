from flask import Flask, request, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return f"""
    <h1>Avaliação contínua: Aula 030</h1>
    <ul>
        <li><a href="{url_for('main')}">Home</a></li>
        <li><a href="{url_for('identificacao', nome='Cauê Weber de Souza Veras', pt='PT3032205', instituicao='IFSP')}">Identificação</a></li>
        <li><a href="{url_for('contextoreq')}">Contexto da requisição</a></li>
    </ul>
    """

@app.route("/user/<nome>/<pt>/<instituicao>")
def identificacao(nome, pt, instituicao):
    return f"""
    <h1>Avaliação contínua: Aula 03</h1>
    <h2><b>Aluno:</b> {nome}</h2>
    <h2><b>Prontuário:</b> {pt}</h2>
    <h2><b>Instituição:</b> {instituicao}</h2>
    <p><a href="{url_for('main')}">Voltar</a></p>
    """

@app.route("/contextorequisicao")
def contextoreq():
    user_agent = request.headers.get("User-Agent", "desconhecido")
    remote_ip = request.remote_addr or "desconhecido"
    host = request.host

    return f"""
    <h1>Avaliação contínua: Aula 030</h1>
    <h2><b>Seu navegador é: {user_agent}</b></h2>
    <h2><b>O IP do computador remoto é: {remote_ip}</b></h2>
    <h2><b>O host da aplicação é: {host}</b></h2>
    <p><a href="{url_for('main')}">Voltar</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True)