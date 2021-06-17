import sqlite3

words = [
    ("exp.", ""),
    ("vp", "" ),
    ("s", "" ),
    ("", "" ),
    ("chic", "" ),
    ("tp", "" ),
    ("est", "" ),
    ("rdu", "" ),
    ("pet", "" ),
    ("ed", "" ),
    ("tq", "" ),
    ("-", "" ),
    ("pp", "" ),
    ("atp", "" ),
    ("cd", "" ),
    ("qa", "" ),
    ("un", "" ),
    ("uni", "" ),
    ("kg", "" ),
    ("k", "" ),
    ("*", "" ),
    ("@", "" ),
    ("vh", "Vinho" ),
    ("ling", "Linguiça" ), 
    ("vpj", "VPJ"),
    ("nat.", "NAT."),
    ("92", "92"),
    ("bov.", "Bovina" ),
    ("bov", "Bovina" ),
    ("porc.", "Porcionados"),
    ("de", "de"),
    ("em", "em"),
    ("c/", "com"),
    ("s/", "sem"),
    ("p/", "para"),
    ("481", "481"),
    ("ext.", "Extra"   ),
    ("t.borthwick", "T.Borthwick" ),
    ("temp.", "Temperada"),
    ("temp", "Temperado"),
    ("bov.", "Bovino"),
    ("resf.", "Resfriado"),
    ("cong.", "Congelada"),
    ("cong", "Congelado"),
    ("prem.", "Premium"),
    ("pc", "Peça"),
    ("osso", "Osso"),
    ("cabeça", "Cabeça"),
    ("da", "da"),
    ("do", "do"),
    ("dos", "dos"),
    ("com", "com"),
    ("sem", "sem"),
    ("fgo", "Frango"),
    ("frg", "Frango"),
    ("frgo", "Frango"),
    ("qjo", "Queijo"),
    ("qj", "Queijo"),
    ("sanduiche", "Sanduíche"),
    ("sand", "Sanduíche"),
    ("1kg(cada),", " - 1kg(cada),"),
    ("500ml(cada),", " - 500ml(cada),"),
    ("tp", "tipo" ),
    ("beaujolais-villages", "Beaujolais-Villages"),
    ("branaire-ducru", "Branaire-Ducr"),
    ("c", "com"),
    ("erv", "Ervas"),
    ("carr´s", "Carr´S"),
    ("e", "e"),
    ("cor.ação", "Coração"),
    ("coracao", "Coração"),
    ("cor.ação", "Coração"),
    ("aaa", "AAA"),
    ("aa", "AA"   ),
    ("for/me", "For/Me" ),
    ("6und", "6 unidade"       ),
    ("uht", "UHT" ),
    ("bd", "Bandeja" ),
    ("cabernet-carmenere", "Cabernet-Carmenere" ),
    ("pimenta-do-reino", "Pimenta-do-Reino " ),
    ("pimenta-da-jamaica", "Pimenta-da-Jamaica"     ),
    ("e", "e"    ),
    ("lt", "Lata"    ),
    ("lta", "Lata" ),
    ("pmg", "PMG"  ),
    ("sem", "sem" ),
    ("org", "Orgânica" ),
    ("hig", "Higienizada" ),
    ("ao", "ao" ),
    ("para", "para" ),
    ("witor", "Witor's" ),
    ("ita", "Integral" ),
    ("desiam", "deSIAM" ),
    ("frutt`oro", "Frutt`Oro" ),
    ("cada", "cada" ),
    ("x","x" ),
    ("organica", "Orgânica" ),
    ("bdj", "Bandeja" ),
    ("pedaco", "Pedaço" ),
    ("pedacos", "Pedaços" ),
    ("und", "Unidade"),
    ("emb", "Embalada"),
    ("acucar", "Açúcar"),
    ("ag", "Água"),
    ("miner", "Mineral"),
    ("miner", "Mineral"),
    ("c/gas", "com gás"),
    ("agriao", "Agrião"),
    ("hidroponico", "Hidropônico"),
    ("hidroponica", "Hidropônica"),
    ("agua", "Água"),
    ("coco", "Cocô"),
    ("un", "Unidade"),
    ("desf", "Desfolhada"),
    ("pct", "Pacote"   ),
    ("st.n.vinhedo", "St. N. Vinhedo"),
    ("alface-americana", "Alface Americana"),
    ("alface-crespa", "Alface Crespa"),
    ("alface-roxa", "Alface Roxa"  ),
    ("pt", "Pote" ),
    ("s/sal", "sem Sal" ),
    ("poro", "Poró" ),
    ("alho-poró", "Alho Poró" ),
    ("cne/cer/lte", "Carne, Cereais e Leite" ),
    ("ameix", "Ameixa" ),
    ("cob", "com Cobertura" ),
    ("choc", "Chocolate" ),
    ("amarg", "Amargo" ),
    ("croc", "Crocante" ),
    ("c/c", "Com Casca" ),
    ("amendoimgraudo", "Amendoim Graudo" ),
    ("t1", "Tipo 1" ),
    ("int", "Integral" ),
    ("tp1", "Tipo 1" ),
    ("t-1", "Tipo 1" ),
    ("parb", "Parboilizado" ),
    ("resf", "Resfriado" ),
    ("vde", "Verde" ),
    ("c/caroço", "Com Caroço" ),
    ("90g/100g", " - 90g/100g" ),
    ("banana-passa", "Banana Passa" ),
    ("gfao", "Garrafão" ),
    ("emgelgelálcool", "em Gel Gelalcool"),
    ("choc/ameixa", "Chocolate e Ameixa"),
    ("choc/coco", "Chocolate e Cocô"),
    ("choc/damasco", "Chocolate e Damasco"),
    ("choc/nozes", "Chocolate e Nozes"),
    ("choc/trad", "Chocolate Tradicional"),
    ("batata-doce", "Batata Doce"),
    ("batata-inglesa", "Batata Inglesa"),
    ("beb", "Bebida"),
    ("lac", "Láctea"),
    ("fer", "Fermentada"),
    ("mam", "Mamão"),
    ("mamao", "Mamão"),
    ("mae", "Mãe"),
    ("mor", "Morango"),
    ("à", "à"),
    ("a", "a"),
    ("uht", "UHT"),
    ("hig.", "Higienizada"),
    ("bisc", "Biscoito"),
    ("bisc.", "Biscoito"),
    ("amant", "Amanteigado"),
    ("amat", "Amanteigado"),
    ("7graos", "7 grãos"),
    ("linhaca", "Linhaça"),
    ("limao", "Limão"),
    ("mant", "Manteigado"),
    ("rech", "Recheado"  ),
    ("c/mor", "com Morango"),
    ("recheadogufs", "Recheado Gufs"),
    ("pasc", "de Páscoa"),
    ("dce", "Doce"),
    ("pascoa", "Páscoa"),
    ("emb", "Embalada"),
    ("brocolis", "Brócolis"),
    ("broc", "Brócolis"),
    ("bja", "Bandeja"),
    ("feijao", "Feijão"),
    ("-garrafa", "Garrafa" ),
    ("cachorro-quente", "Cachorro Quente" ),
    ("cafe", "Café" ),
    ("nescafe", "Nescafé" ),
    ("manha", "Manhã" ),
    ("pao", "Pão"),
    ("coracões", "Corações"),
    ("coracoes", "Corações"),
    ("ceu", "Céu"),
    ("cast", "Castanha"),
    ("moida", "Moída"),
    ("moido", "Moído"),
    ("excelencia", "Excelência"),
    ("tor/sal", "Torrada com Sal" ),
    ("s/sal", "sem sal"),
    ("castanha-de-caju", "Castanha de Caju"),
    ("castanha-do-pará", "Castanha do Pará"),
    ("pcte", "Pacote"),
    ("hidrop", "Hidropônica"),
    ("hidroponica", "Hidropônica"),
    ("nac", "Nacional"),
    ("cer", "Cereal" ),
    ("c/acucar", "com Açúcar"),
    ("cab", "CAB"),
    ("peq", "Pequena"),
    ("gde", "Grande"),
    ("cha", "Chá"),
    ("spfc", "SPFC"),
    ("adocada", "Adoçada" ),
    ("adocado", "Adoçado" ),
    ("coco-verde", "Coco Verde"),
    ("fat", "Fatiado"),
    ("pt", "Preto"),
    ("int", "Inteiro"),
    ("organico", "Orgânico"),
    ("organicos", "Orgânicos"),
    ("cao", "Cão"),
    ("clar", "Claro"),
    ("nat", "Natural"),
    ("colo", "Coloração" ),
    ("comgotas", "com Gotas" ),
    ("pao/mateiga/suco", "Pão, Manteiga e Suco"),
    ("laran", "Laranja"),
    ("caramel", "Caramelo"),
    ("plast", "Plástico"),
    ("plastico", "Plástico"),
    ("jfc", "JFC"),
    ("c/sob", "com Sobrecoxa"),
    ("s/pele", "sem Pele"),
    ("lte", "Leite"),
    ("cr", "Creme"),
    ("crisantemo", "Crisântemo"),
    ("sanitario", "Sanitário"),
    ("sanitaria", "Sanitária"),
    ("feijao", "feijão"),
    ("lider", "Líder"),
    ("feijão-carioca", "Feijão Carioca"),
    ("feijao-carioca", "Feijão Carioca"),
    ("feijão-fradinho", "Feijão Fradinho"),
    ("caldobom", "Caldo Bom"),
    ("fgogre", "Frango Grelhado"),
    ("file", "Filé"),
    ("sob/cox", "Sobrecoxa/coxa"),
    ("orquidea", "Orquídea" ),
    ("pós-sol", "Pós-Sol" ),
    ("pass", "Passarinho" ),
    ("friboignel", "Friboi Granel" ),
    ("abobora", "Abóbora" ),
    ("desc", "Descascada" ),
    ("vac", "a Vácuo" ),
    ("vacuo", "Vácuo" ),
    ("hortela", "Hortelã" ),
    ("salmao", "Salmão" ),
    ("iog", "Iogurte" ),
    ("pessego", "Pêssego" ),
    ("liq", "Líquido"  ),
    ("liquido", "Líquido"  ),
    ("liquida", "Líquida" ),
    ("norte-americano", "Norte-Americano" ),
    ("pascoa", "Páscoa" ),
    ("refrig", "Refrigerante"  ),
    ("nutriçao", "Nutrição"),
    ("nutricao", "Nutrição"),
    ("nutricão", "Nutrição"),
    ("laranja-baía", "Laranja Baía"),
    ("laranja-lima", "Laranja Lima"),
    ("laranja-pera", "Laranja Pêra"),
    ("laranja-pêra", "Laranja Pêra"),
    ("pera", "Pêra"),
    ("parmesao", "Parmesão"),
    ("lava-louças", "Lava Louças"),
    ("loucas", "Louças"),
    ("louca", "Louça"),
    ("longa-vida", "Longa Vida"),
    ("past", "Pasteriorizado"),
    ("suina", "Suína"),
    ("suino", "Suíno"),
    ("peca", "Peça" ),
    ("m&m's", "M&M's" ),
    ("d.p.a", "D.P.A" ),
    ("maca", "Maçã" ),
    ("tragrani", "Tra Gani"),
    ("maco", "Maço"),
    ("manjericao", "Manjericão"),
    ("c/sal", "com Sal"),
    ("pos", "Pós"),
    ("quimica", "Química"),
    ("mascara", "Máscara"),
    ("mc", "Maço"),
    ("avela", "Avelã"),
    ("po", "Pó"),
    ("prestigio", "Prestígio"),
    ("milho-verde", "Milho Verde"),
    ("minipao", "Mini Pão"),
    ("minipizza", "Mini Pizza" ),
    ("minissuculentas", "Mini Suculenta"),
    ("cheiro-verde", "Cheiro Verde"),
    ("balsamico", "Balsâmico"),
    ("vinagr", "Vinagre"),
    ("maracuja", "Maracujá"),
    ("camarao", "Camarão"),
    ("oleo", "Óleo"),
    ("graos", "Grãos"),
    ("grao", "Grão"),
    ("nestle", "Nestlé"),
    ("classico", "Clássico" ),
    ("páscoagaroto", "Páscoa Garoto" ),
    ("medio", "Médio" ),
    ("media", "Média" ),
    ("tipogrande", "Tipo Grande" ),
    ("omega", "Ômega" ),
    ("oral-b", "Oral-B" ),
    ("tres", "Três" ),
    ("frances", "Francês" ),
    ("hamburguer", "Hambúrguer"  ),
    ("sirio", "Sírio"  ),
    ("japones", "Japonês"  ),
    ("pure", "Purê"  ),
    ("guarana", "Guaraná"  ),
    ("bufala", "Búfala"  ),
    ("bufalo", "Búfalo"  ),
    ("rucula", "Rúcula"  ),
    ("agriao", "Agrião"),
    ("salsao", "Salsão"  ),
    ("tamara", "Tâmara" ),
    ("acai", "Açaí"),
    ("açai", "Açaí"),
    ("acaí", "Açaí"),
    ("italia", "Itália"),
    ("monica", "Mônica"),
    ("delicia", "Delícia"),
    ("q.delicia", "Q Delícia"),
    ("portugues", "Português"),
    ("terranova", "TerraNova"),
    ("b&g", "B&G"),
    ("sulafricano", "Sul-africano"),
    ("ype", "Ypê"),
    ("achoc", "Achocolatado"),
    ("excel", "Excelência"),
    ("uniao", "União"),
    ("amendoa", "Amêndoa"),
    ("amendoas", "Amêndoas"),
    ("avela", "Avelã"),
    ("bcaa", "BCAA"),
    ("betania", "Betânia"),
    ("cx", "Caixa"),
    ("sitio", "Sítio"),
    ("camarao", "Camarão"),
    ("sache", "Sachê"),
    ("empadao", "Empadão"),
    ("cp", "Copo"),
    ("mamae", "Mamãe"),
    ("feijão-carioca", "Feijão Carioca"),
    ("feijao-carioca", "Feijão Carioca"),
    ("figado", "Fígado" ),
    ("tilapia", "Tilápia"),
    ("geleia", "Geléia"),
    ("sao", "São" ),
    ("acafrao", "Açafrão"),
    ("tonica", "Tônica"),
    ("laranja-baía", "Laranja Baía"),
    ("laranja-lima", "Laranja Lima"),
    ("laranja-Pera", "Laranja Pera"),
    ("ling", "Linguiça"),
    ("linguica", "Linguiça"),
    ("trad", "Tradicional"),
    ("lactea", "Láctea" ),
    ("instantaneo", "Instantâneo"),
    ("alcool", "Álcool"),
    ("sensacao", "Sensação"),
    ("sensacoes", "Sensações"),
    ("oreo", "Óreo"),
    ("panet", "Panetone"),
    ("rustica", "Rústica"),
    ("rustico", "Rústico"),
    ("moca", "Moça"),
    ("pimentao", "Pimentão"),
    ("caja", "Cajá"),
    ("paraiso", "Paraíso"),
    ("qualita", "Qualitá"),
    ("perdigao", "Perdigão"),
    ("pe", "Pé"),
    ("melao", "Melão"),
    ("requeijao", "Requeijão"),
    ("proteina", "Proteína"),
    ("oregano", "Orégano" ),
    ("tm", "Torrado e Moído" ),
    ("pacoca", "Paçoca" ),
    ("fuba", "Fubá" ),
    ("piraque", "Piraquê" ),
    ("pizzaquê", "Pizzaquê" ),
    ("sodio", "Sódio" ),
    ("almeirao", "Almeirão" ),
    ("almondega", "Almôndega" ),
    ("capsula", "Cápsula" ),
    ("semola", "Sêmola" ),
    ("macarrao", "Macarrão" ),
    ("perola", "Pérola"),
    ("imp", "Importada" ),
    ("gnel", "a Granel" ),
    ("1953", "1953" ),
    ("1953", "1953" ),
    ("contrafile", "Contra Filé" ),
    ("contrafilé", "Contra Filé" ),
    ("coxao", "Coxão" ),
    ("file", "Filé" ),
    ("caja", "Cajá" ),
    ("pedaco", "Pedaço" ),
    ("jilo", "Jiló"),
    ("holandes", "Holandês"  ),
    ("lingüiça", "Linguiça" ),
    ("medalhao", "Medalhão" ),
    ("musculo", "Músculo"),
    ("pêra", "Pera"),
    ("facil", "Fácil"),
    ("esferico", "Esférico"),
    ("purissimo", "Puríssimo"),
    ("padrao", "Padrão"),
    ("muss", "Mussarela"),
    ("formâ", "Forma"),
    ("tabua", "Tábua"),
    ("ii", "II"),
    ("mucarela", "Muçarela"      ),
    ("lingua", "Língua"  ),
    ("medalhoes", "Medalhões"     ),
    ("asiatica", "Asiática"           ),
    ("macadamia", "Macadâmia"    ),
    ("nivea", "Nívea"    ),
    ("3m", "3M"  ),
    ("51", "51"  ),
    ("algodao", "Algodão"  ),
    ("piraque", "Piraquê"  ),
    ("retornavel", "Retornável" ),
    ("posicoes", "Posições"   ),
    ("aluminio", "Alumínio" ),
    ("cartao", "Cartão"    ),
    ("memoria", "Memória" ),
    ("cerv", "Cerveja" ),
    ("antuerpia", "Antuérpia" ),
    ("therezopolis", "Therezópolis" ),
    ("leao", "Leão" ),
    ("chicle", "Chiclete" ),
    ("classicos", "Clássicos" ),
    ("chin", "Sandália" ),
    ("hav", "Havaianas"),
    ("ipa", "Ipanema"),
    ("ipan", "Ipanema"),
    ("class", "Clássica"),
    ("classica", "Clássica"),
    ("masc", "Masculina"),
    ("fem", "Feminina"),
    ("inf,", "Infantil"),
    ("cjt,", "Conjunto"),
    ("tacas", "Taças"),
    ("taca", "Taça"),
    ("bastao", "Bastão"),
    ("fosforo", "Fósforo"),
    ("tonica", "Tônica"),
    ("gas", "Gás"),
    ("atelie", "Ateliê"),
    ("ype", "Ypê"),
    ("sabao", "Sabão" ),
    ("reconstrucao", "Reconstrução"),
    ("energetico", "Energético"),
    ("higienica", "Higiênica"),
    ("antisseptica", "Antisséptica"),
    ("higienico", "Higiênico"),
    ("carvao", "Carvão"),
    ("mediterraneo", "Mediterrâneo"),
    ("quimico", "Químico"),
    ("lacteo", "Lácteo" ),
    ("gluten", "Glúten" ),
    ("açucar", "Açúcar"),
    ("acem", "Acém" ),
    ("ingles", "Inglês"),
    ("xicara", "Xícara"),
    ("aco", "Aço"),
    ("flexivel", "Flexível"),
    ("biogradavel", "Biogradável" ),
    ("impermeavel", "Impermeável"),
    ("alcas", "Alças"),
    ("alca", "Alça"),
    ("eletrica", "Elétrica"),
    ("extensao", "Extensão"),
    ("aniversario", "Aniversário"),
    ("parana", "Paraná"),
    ("utensilio", "Utensílio"),
    ("pecas", "Peças"),
    ("lampada", "Lâmpada"),
    ("ge", "GE"),
    ("nene", "Nenê"),
    ("descartavel", "Descartável"),
    ("elastico", "Elástico"),
    ("reutilizavel", "Reutilizável"),
    ("chao", "Chão"),
    ("economico", "Econômico"),
    ("pinca", "Pinça"),
    ("acrilico", "Acrílico" ),
    ("valvula", "Válvula"),
    ("ceramica", "Cerâmica"),
    ("ceramico", "Cerâmico"),
    ("mao", "Mão"),
    ("sta", "Santa"),
    ("pescoco", "Pescoço"),
    ("grauda", "Graúda"),
    ("india", "Índia"),
    ("comestivel", "Comestível"),
    ("tamara", "Tâmara"),
    ("vitoria", "Vitória"),
    ("racao", "Ração"),
    ("raca", "Raça"),
    ("racas", "Raças"),
    ("cachaca", "Cachaça"),
    ("joao", "João"),
    ("balsamo", "Bálsamo"),
    ("soluvel", "Solúvel"),
    ("salpicao", "Salpicão"),
    ("multigraos", "Multigrãos"),
    ("aviacao", "Aviação"),
    ("reliquia", "Relíquia"),
    ("caroco", "Caroço"),
    ("transgenico", "Transgênico")
]

con = sqlite3.connect("app.db")

con.execute('BEGIN TRANSACTION')
con.execute("delete from words")
for i in words:
    print(i)
    con.execute("insert into words(word_from, word_to) values (?,?)", i)

con.execute('COMMIT')