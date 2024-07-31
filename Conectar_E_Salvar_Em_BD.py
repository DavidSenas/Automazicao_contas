import mysql.connector
def ConnetcDatabase(datacriacao, email, namecount, password):
    data = datacriacao
    email = email
    namecount = namecount
    password = password

    # Criando as Credenciais do Banco de dados
    credenciais = {
        "user": "root",
        "password": "david123",
        "host": "localhost",
        "database": "contas_tunel",
        "raise_on_warnings": True
    }

    #Variantes para salvar os dados no banco de dados
    Insert = f"INSERT INTO usuarios (datacriacao, email, namecount, password) VALUES ('{data}', '{email}', '{namecount}',' {password}')"
    Values = (data, email, namecount, password)

    #Conectando ao banco de dados
    try:
        ConnectDatabase = mysql.connector.connect(**credenciais)
        if ConnectDatabase.is_connected():

            # Criando Cursor para executar os comandos no banco de dados
            cursor = ConnectDatabase.cursor()
            cursor.execute(Insert)
            ConnectDatabase.commit()
            print("Dados Salvos com sucesso")

    except Exception as e:
        print(f"Não conectado {e}")

