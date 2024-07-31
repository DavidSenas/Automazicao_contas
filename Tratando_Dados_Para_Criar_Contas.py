def extrairDados(Response):

    #Response Pega Os dados coletados no site
    dadosResponse = Response

    #Percorendo Dicionário e pegando os dados necessários para criação da conta
    password = dadosResponse["results"][0]["login"]["md5"]
    email = dadosResponse["results"][0]["email"]
    firstname = dadosResponse["results"][0]["name"]["first"]
    lastname = dadosResponse["results"][0]["name"]["last"]
    namecount = firstname+lastname
    country = dadosResponse["results"][0]["location"]["state"]
    endereco = dadosResponse["results"][0]["location"]["street"]["name"]
    numeroend = dadosResponse["results"][0]["location"]["street"]["number"]
    endRua = str(numeroend) + " " + endereco
    city = dadosResponse["results"][0]['location']["city"]
    state = dadosResponse["results"][0]["location"]["state"]
    cep = dadosResponse["results"][0]["location"]["postcode"]
    phone = dadosResponse["results"][0]["phone"].replace("(", "").replace(")", "")

    #Criando uma lista apenas com os dados necessarios
    dadosParaCadastro = (namecount, password, email, firstname, lastname, endRua, city, state, cep, phone)

    return dadosParaCadastro