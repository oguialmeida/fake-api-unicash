from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def principal():
    saudacoes = "Bem vindo! Vida longa e prospera 🖖"
    mensagem = {"Mensagem": saudacoes}
    return jsonify(mensagem)

@app.route("/user")
def getUser():
    return jsonify(
        {"id": 1, "nome": "Guilherme", "Curso": "Eng. de Software", "Saldo": 500},
        {"id": 2, "nome": "Kakashi", "Curso": "Medicina Veterinária", "Saldo": 828},
        {"id": 3, "nome": "Leonardo", "Curso": "Direito", "Saldo": 988},
        {"id": 4, "nome": "Raphael", "Curso": "Educação Física", "Saldo": 782},
        {"id": 5, "nome": "Mick", "Curso": "Gastronomia", "Saldo": 658},
        {"id": 6, "nome": "Donnie", "Curso": "Eng. de Software", "Saldo": 492},
        {"id": 7, "nome": "Splinter", "Curso": "Mestrado em ciências ambientais", "Saldo": 367},
        {"id": 8, "nome": "Robert Stark", "Curso": "Administração", "Saldo": 872},
        {"id": 9, "nome": "Shikamaru", "Curso": "Psicologia", "Saldo": 730},
        {"id": 10, "nome": "Tsunade", "Curso": "Medicina", "Saldo": 381},
        {"id": 11, "nome": "Loki", "Curso": "Eng. de Software", "Saldo": 500},
        {"id": 12, "nome": "Thor", "Curso": "Medicina Veterinária", "Saldo": 828},
        {"id": 13, "nome": "Bloom", "Curso": "Direito", "Saldo": 988},
        {"id": 14, "nome": "Flora", "Curso": "Educação Física", "Saldo": 782},
        {"id": 15, "nome": "Musa", "Curso": "Gastronomia", "Saldo": 658},
        {"id": 16, "nome": "Tecna", "Curso": "Eng. de Software", "Saldo": 492},
        {"id": 17, "nome": "Luke", "Curso": "Mestrado em ciências ambientais", "Saldo": 367},
        {"id": 18, "nome": "Leia", "Curso": "Administração", "Saldo": 872},
        {"id": 19, "nome": "Anakin", "Curso": "Psicologia", "Saldo": 730},
        {"id": 20, "nome": "Gregory House", "Curso": "Medicina", "Saldo": 381},
        {"id": 21, "nome": "Hermione Granger", "Curso": "Eng. de Software", "Saldo": 500},
        {"id": 22, "nome": "Bryan", "Curso": "Medicina Veterinária", "Saldo": 828},
        {"id": 23, "nome": "Harvey", "Curso": "Direito", "Saldo": 988},
        {"id": 24, "nome": "Leblon", "Curso": "Educação Física", "Saldo": 782},
        {"id": 25, "nome": "Soma", "Curso": "Gastronomia", "Saldo": 658},
        {"id": 26, "nome": "Spock", "Curso": "Eng. de Software", "Saldo": 492},
        {"id": 27, "nome": "Miagi", "Curso": "Mestrado em ciências ambientais", "Saldo": 367},
        {"id": 28, "nome": "Patolino", "Curso": "Administração", "Saldo": 872},
        {"id": 29, "nome": "Freud", "Curso": "Psicologia", "Saldo": 730},
        {"id": 30, "nome": "Stone", "Curso": "Medicina", "Saldo": 381},
        {"id": 31, "nome": "Gates", "Curso": "Eng. de Software", "Saldo": 500},
        {"id": 32, "nome": "Dolittle", "Curso": "Medicina Veterinária", "Saldo": 828},
        {"id": 33, "nome": "Palestrinha", "Curso": "Direito", "Saldo": 988},
        {"id": 34, "nome": "Schwarzenegger", "Curso": "Educação Física", "Saldo": 782},
        {"id": 35, "nome": "Magali", "Curso": "Gastronomia", "Saldo": 658},
        {"id": 36, "nome": "Zuckerberg", "Curso": "Eng. de Software", "Saldo": 492},
        {"id": 37, "nome": "Kami", "Curso": "Mestrado em ciências ambientais", "Saldo": 367},
        {"id": 38, "nome": "Agostinho", "Curso": "Administração", "Saldo": 872},
        {"id": 39, "nome": "Sherlock Holmes", "Curso": "Psicologia", "Saldo": 730},
        {"id": 40, "nome": "John Watson", "Curso": "Medicina", "Saldo": 381},
        {"id": 41, "nome": "Eliot", "Curso": "Eng. de Software", "Saldo": 500},
        {"id": 42, "nome": "Ace Ventura", "Curso": "Medicina Veterinária", "Saldo": 828},
        {"id": 43, "nome": "Nelson Mandela", "Curso": "Direito", "Saldo": 988},
        {"id": 44, "nome": "Neymar", "Curso": "Educação Física", "Saldo": 782},
        {"id": 45, "nome": "Salsicha Rogers", "Curso": "Gastronomia", "Saldo": 658},
        {"id": 46, "nome": "Kate Libby", "Curso": "Eng. de Software", "Saldo": 492},
        {"id": 47, "nome": "Jiraya", "Curso": "Mestrado em ciências ambientais", "Saldo": 367},
        {"id": 48, "nome": "Seu Madruga", "Curso": "Administração", "Saldo": 872},
        {"id": 49, "nome": "Paola Bracho", "Curso": "Psicologia", "Saldo": 730},
        {"id": 50, "nome": "Leornad Mccopy", "Curso": "Medicina", "Saldo": 381},
    )
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(debug=True, host='0.0.0.0', port=port)