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
        {"id": 1, "nome": "Guilherme", "curso": "Eng. de Software", "saldo": 998, "img": "https://epipoca.com.br/wp-content/uploads/2021/09/Brad-Pitt.jpg"},
        {"id": 2, "nome": "Kakashi", "curso": "Medicina Veterinária", "saldo": 761, "img": "https://i.pinimg.com/736x/ee/ea/9c/eeea9c727af1372fbaa01ca2237ab055.jpg"},
        {"id": 3, "nome": "Leonardo", "curso": "Direito", "saldo": 681, "img": "https://static.wikia.nocookie.net/dublagempedia/images/c/c4/Mufasa-0.png/revision/latest?cb=20200515175716&path-prefix=pt-br"},
        {"id": 4, "nome": "Raphael", "curso": "Educação Física", "saldo": 672, "img": "https://i.pinimg.com/736x/49/27/8e/49278ebad30e84dfb484a1c126e5fac3--ninja-turtle-heroes.jpg"},
        {"id": 5, "nome": "Mick", "curso": "Gastronomia", "saldo": 658, "img": "https://upload.wikimedia.org/wikipedia/pt/e/ec/Michelangelo_%28Teenage_Mutant_Ninja_Turtles%29_2003.jpg"},
        {"id": 6, "nome": "Donnie", "curso": "Eng. de Software", "saldo": 656, "img": "https://i.pinimg.com/originals/7f/d5/2c/7fd52c68097ac33018c2e84a437e4f70.jpg"},
        {"id": 7, "nome": "Splinter", "curso": "Mestrado em ciências ambientais", "saldo": 631, "img": "https://i.pinimg.com/originals/7b/56/8e/7b568e0ece6819884e11b7d059658b75.jpg"},
        {"id": 8, "nome": "Robert Stark", "curso": "Administração", "saldo": 625, "img": "https://static1.purebreak.com.br/articles/4/11/02/74/@/500949-em-game-of-thrones-casamento-vermelho-700x700-3.jpg"},
        {"id": 9, "nome": "Shikamaru", "curso": "Psicologia", "saldo": 600, "img": "https://static.wikia.nocookie.net/naruto/images/7/7b/Shikamaru_olhando_para_as_nuvens.PNG/revision/latest/scale-to-width-down/640?cb=20131017211213&path-prefix=pt-br"},
        {"id": 10, "nome": "Tsunade", "curso": "Medicina", "saldo": 580, "img": "https://nerdhits.com.br/wp-content/uploads/2021/10/tsunade-1200x720.jpeg"},
        {"id": 11, "nome": "Loki", "curso": "Eng. de Software", "saldo": 579, "img": "https://disneyplusbrasil.com.br/wp-content/uploads/2021/06/Loki-Presidente-1024x576.jpg"},
        {"id": 12, "nome": "Thor", "curso": "Medicina Veterinária", "saldo": 555, "img": "https://cdn.mos.cms.futurecdn.net/rohSW6fcL4hcAVujAVFaxX.jpg"},
        {"id": 13, "nome": "Bloom", "curso": "Direito", "saldo": 551, "img": "https://static.wikia.nocookie.net/winx-club-br/images/9/92/BloomNick.png/revision/latest?cb=20130129034504"},
        {"id": 14, "nome": "Flora", "curso": "Educação Física", "saldo": 522, "img": "https://i.pinimg.com/originals/f8/75/2f/f8752f261933778b61d7f76d4d6a7e6f.jpg"},
        {"id": 15, "nome": "Musa", "curso": "Gastronomia", "saldo": 511, "img": "https://www.winxclub.com/sites/default/files/galleria/cover-image-musa.jpg"},
        {"id": 16, "nome": "Tecna", "curso": "Eng. de Software", "saldo": 501, "img": "https://i.pinimg.com/736x/7f/17/97/7f1797f35694244a0210effaf7e34521.jpg"},
        {"id": 17, "nome": "Luke", "curso": "Mestrado em ciências ambientais", "saldo": 479, "img": "https://classic.exame.com/wp-content/uploads/2016/09/size_960_16_9_20151020-23623-g3jah31.jpg?quality=70&strip=info&w=960"},
        {"id": 18, "nome": "Leia", "curso": "Administração", "saldo": 471, "img": "https://i.pinimg.com/474x/00/a0/0a/00a00afe3b9fd464430dd8ce4f696cd4--leia-star-wars-star-trek.jpg"},
        {"id": 19, "nome": "Anakin", "curso": "Psicologia", "saldo": 470, "img": "https://sm.ign.com/ign_br/news/a/anakin-sky/anakin-skywalker-could-have-been-in-star-wars-the_277u.jpg"},
        {"id": 20, "nome": "Gregory House", "curso": "Medicina", "saldo": 437, "img": "https://media.npr.org/assets/img/2011/11/16/house-ep723-movingon_sc40_0299_wide-bd3d16a7f8181a138dfdbe85191fdb29dcb18866-s1100-c50.jpg"},
        {"id": 21, "nome": "Hermione Granger", "curso": "Eng. de Software", "saldo": 435, "img": "https://i.pinimg.com/736x/24/b6/b0/24b6b0a6cb973bfed4c3dad35cb453aa.jpg"},
        {"id": 22, "nome": "Bryan", "curso": "Medicina Veterinária", "saldo": 420, "img": "https://i.insider.com/60d5022adf1db80018f3a208?width=700"},
        {"id": 23, "nome": "Harvey", "curso": "Direito", "saldo": 419, "img": "https://cinema10.com.br/upload/materias/materias-harveyspecter.png"},
        {"id": 24, "nome": "Leblon", "curso": "Educação Física", "saldo": 418, "img": "https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/1966.png"},
        {"id": 25, "nome": "Soma", "curso": "Gastronomia", "saldo": 417, "img": "https://i.pinimg.com/originals/41/9d/0e/419d0ec59d1b4bec84aaca3542757ba0.jpg"},
        {"id": 26, "nome": "Spock", "curso": "Eng. de Software", "saldo": 415, "img": "https://media.npr.org/assets/img/2015/02/27/spock-getty_custom-59cc0c0d026ceb215982439a3aa88d9ba5da53de.jpg"},
        {"id": 27, "nome": "Miagi", "curso": "Mestrado em ciências ambientais", "saldo": 414, "img": "https://sm.ign.com/ign_br/screenshot/default/sr-miyagi-sorriso_shkc.jpg"},
        {"id": 28, "nome": "Patolino", "curso": "Administração", "saldo": 411, "img": "https://pbs.twimg.com/media/FWCrmD0WQAQowgZ.jpg"},
        {"id": 29, "nome": "Freud", "curso": "Psicologia", "saldo": 410, "img": "https://i.imgflip.com/3x9y2c.jpg"},
        {"id": 30, "nome": "Stone", "curso": "Medicina", "saldo": 409, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8g-kreFCxdi5dO_AUpW8y6vFOtY3FwW53VCwIrMKBchWvKfPUQEw3FyTWvg66aMhKsrk&usqp=CAU"},
        {"id": 31, "nome": "Gates", "curso": "Eng. de Software", "saldo": 408, "img": "https://qph.cf2.quoracdn.net/main-qimg-020fac071c01a6321fe24013aa136e60-pjlq"},
        {"id": 32, "nome": "Dolittle", "curso": "Medicina Veterinária", "saldo": 405, "img": "https://i.discogs.com/9pantFknbeuazgSSn1PJxfi03dNQaMsDdLyhby5BD9I/rs:fit/g:sm/q:90/h:590/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTg5MDIz/MC0xMjkxNjkwMTA0/LmpwZWc.jpeg"},
        {"id": 33, "nome": "Fred", "curso": "Direito", "saldo": 399, "img": "https://static.wikia.nocookie.net/scoobydoo/images/4/47/Fred_Jones.png/revision/latest?cb=20201229021548"},
        {"id": 34, "nome": "Schwarzenegger", "curso": "Educação Física", "saldo": 388, "img": "https://i0.wp.com/www.nerdtrip.com.br/wp-content/uploads/2018/07/thumb-1920-60680.jpg?resize=560%2C600&ssl=1"},
        {"id": 35, "nome": "Hannibal", "curso": "Gastronomia", "saldo": 385, "img": "http://ci.i.uol.com.br/cinema/2012/02/15/anthony-hopkins-interpretando-o-canibal-hannibal-lecter-1329343933107_300x420.jpg"},
        {"id": 36, "nome": "Zuckerberg", "curso": "Eng. de Software", "saldo": 384, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsfaWd3MnLERLk5dAsl4ZSeWVkZKcTstPS-GyPplooW_kHG_Ge3bIExbeLyHFeK37Aj6Y&usqp=CAU"},
        {"id": 37, "nome": "Kami", "curso": "Mestrado em ciências ambientais", "saldo": 367, "img": "https://ovicio.com.br/wp-content/uploads/master-roshi-stronger_6by8kame.jpg"},
        {"id": 38, "nome": "Agostinho", "curso": "Administração", "saldo": 366, "img": "https://vejasp.abril.com.br/wp-content/uploads/2019/07/agostinho-carrara.jpg"},
        {"id": 39, "nome": "Sherlock Holmes", "curso": "Psicologia", "saldo": 301, "img": "https://uploads.jovemnerd.com.br/wp-content/uploads/2020/09/sherlock-holmes-trends-twitter.jpg"},
        {"id": 40, "nome": "John Watson", "curso": "Medicina", "saldo": 300, "img": "https://static.wikia.nocookie.net/bakerstreet/images/4/42/John-watson-season-4.jpg/revision/latest?cb=20161212231000"},
        {"id": 41, "nome": "Eliot", "curso": "Eng. de Software", "saldo": 278, "img": "https://br.web.img3.acsta.net/r_1280_720/newsv7/20/12/14/18/43/2579831.jpg"},
        {"id": 42, "nome": "Ace Ventura", "curso": "Medicina Veterinária", "saldo": 275, "img": "https://www.rbsdirect.com.br/imagesrc/26152070.jpg?w=700"},
        {"id": 43, "nome": "Nelson Mandela", "curso": "Direito", "saldo": 274, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJqqy5NK1rDaqAK0FDbv16hM6SCODXYMXKwjPsuk0vTcxBoC1GUE224qePhIGiJCXnc1w&usqp=CAU"},
        {"id": 44, "nome": "Neymar", "curso": "Educação Física", "saldo": 273, "img": "https://static.wikia.nocookie.net/villains/images/a/a9/Elipromo.jpg/revision/latest?cb=20220123083901"},
        {"id": 45, "nome": "Salsicha Rogers", "curso": "Gastronomia", "saldo": 271, "img": "https://i0.wp.com/cromossomonerd.com.br/wp-content/uploads/2019/02/Mortal-Kombat-11-Shaggy.jpg.optimal.jpg?fit=1080%2C600&ssl=1"},
        {"id": 46, "nome": "Kate Libby", "curso": "Eng. de Software", "saldo": 270, "img": "https://www.cnnbrasil.com.br/wp-content/uploads/sites/12/2021/06/24630_7E9A5B3C65889D88.jpg?w=1024"},
        {"id": 47, "nome": "Jiraya", "curso": "Mestrado em ciências ambientais", "saldo": 235, "img": "https://s.aficionados.com.br/imagens/jiraiya-frases.jpg"},
        {"id": 48, "nome": "Seu Madruga", "curso": "Administração", "saldo": 227, "img": "https://i.ytimg.com/vi/mM2rk1WzLRg/maxresdefault.jpg"},
        {"id": 49, "nome": "Paola Bracho", "curso": "Psicologia", "saldo": 217, "img": "https://coolturalblog.files.wordpress.com/2013/04/paola-bracho.jpg?w=640"},
        {"id": 50, "nome": "Leonard Mccoy", "curso": "Medicina", "saldo": 211, "img": "https://br.web.img2.acsta.net/newsv7/20/09/11/19/57/4353587.jpg"}
    )
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(debug=True, host='0.0.0.0', port=port)