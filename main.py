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
        {"id": 1, "nome": "Guilherme", "curso": "Eng. de Software", "saldo": 500},
        {"id": 2, "nome": "Kakashi", "curso": "Medicina Veterinária", "saldo": 828},
        {"id": 3, "nome": "Leonardo", "curso": "Direito", "saldo": 988},
        {"id": 4, "nome": "Raphael", "curso": "Educação Física", "saldo": 782},
        {"id": 5, "nome": "Mick", "curso": "Gastronomia", "saldo": 658},
        {"id": 6, "nome": "Donnie", "curso": "Eng. de Software", "saldo": 492},
        {"id": 7, "nome": "Splinter", "curso": "Mestrado em ciências ambientais", "saldo": 367},
        {"id": 8, "nome": "Robert Stark", "curso": "Administração", "saldo": 872},
        {"id": 9, "nome": "Shikamaru", "curso": "Psicologia", "saldo": 730},
        {"id": 10, "nome": "Tsunade", "curso": "Medicina", "saldo": 381},
        {"id": 11, "nome": "Loki", "curso": "Eng. de Software", "saldo": 500},
        {"id": 12, "nome": "Thor", "curso": "Medicina Veterinária", "saldo": 828},
        {"id": 13, "nome": "Bloom", "curso": "Direito", "saldo": 988},
        {"id": 14, "nome": "Flora", "curso": "Educação Física", "saldo": 782},
        {"id": 15, "nome": "Musa", "curso": "Gastronomia", "saldo": 658},
        {"id": 16, "nome": "Tecna", "curso": "Eng. de Software", "saldo": 492},
        {"id": 17, "nome": "Luke", "curso": "Mestrado em ciências ambientais", "saldo": 367},
        {"id": 18, "nome": "Leia", "curso": "Administração", "saldo": 872},
        {"id": 19, "nome": "Anakin", "curso": "Psicologia", "saldo": 730},
        {"id": 20, "nome": "Gregory House", "curso": "Medicina", "saldo": 381},
        {"id": 21, "nome": "Hermione Granger", "curso": "Eng. de Software", "saldo": 500},
        {"id": 22, "nome": "Bryan", "curso": "Medicina Veterinária", "saldo": 828},
        {"id": 23, "nome": "Harvey", "curso": "Direito", "saldo": 988},
        {"id": 24, "nome": "Leblon", "curso": "Educação Física", "saldo": 782},
        {"id": 25, "nome": "Soma", "curso": "Gastronomia", "saldo": 658},
        {"id": 26, "nome": "Spock", "curso": "Eng. de Software", "saldo": 492},
        {"id": 27, "nome": "Miagi", "curso": "Mestrado em ciências ambientais", "saldo": 367},
        {"id": 28, "nome": "Patolino", "curso": "Administração", "saldo": 872},
        {"id": 29, "nome": "Freud", "curso": "Psicologia", "saldo": 730},
        {"id": 30, "nome": "Stone", "curso": "Medicina", "saldo": 381},
        {"id": 31, "nome": "Gates", "curso": "Eng. de Software", "saldo": 500},
        {"id": 32, "nome": "Dolittle", "curso": "Medicina Veterinária", "saldo": 828},
        {"id": 33, "nome": "Palestrinha", "curso": "Direito", "saldo": 988},
        {"id": 34, "nome": "Schwarzenegger", "curso": "Educação Física", "saldo": 782},
        {"id": 35, "nome": "Magali", "curso": "Gastronomia", "saldo": 658},
        {"id": 36, "nome": "Zuckerberg", "curso": "Eng. de Software", "saldo": 492},
        {"id": 37, "nome": "Kami", "curso": "Mestrado em ciências ambientais", "saldo": 367},
        {"id": 38, "nome": "Agostinho", "curso": "Administração", "saldo": 872},
        {"id": 39, "nome": "Sherlock Holmes", "curso": "Psicologia", "saldo": 730},
        {"id": 40, "nome": "John Watson", "curso": "Medicina", "saldo": 381},
        {"id": 41, "nome": "Eliot", "curso": "Eng. de Software", "saldo": 500},
        {"id": 42, "nome": "Ace Ventura", "curso": "Medicina Veterinária", "saldo": 828},
        {"id": 43, "nome": "Nelson Mandela", "curso": "Direito", "saldo": 988},
        {"id": 44, "nome": "Neymar", "curso": "Educação Física", "saldo": 782},
        {"id": 45, "nome": "Salsicha Rogers", "curso": "Gastronomia", "saldo": 658},
        {"id": 46, "nome": "Kate Libby", "curso": "Eng. de Software", "saldo": 492},
        {"id": 47, "nome": "Jiraya", "curso": "Mestrado em ciências ambientais", "saldo": 367},
        {"id": 48, "nome": "Seu Madruga", "curso": "Administração", "saldo": 872},
        {"id": 49, "nome": "Paola Bracho", "curso": "Psicologia", "saldo": 730},
        {"id": 50, "nome": "Leornad Mccopy", "curso": "Medicina", "saldo": 381},
    )
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(debug=True, host='0.0.0.0', port=port)