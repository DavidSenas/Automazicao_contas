import time
import zipfile
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Tratando_Dados_Para_Criar_Contas import extrairDados
from Siglas_Por_Estados import Pegando_Estados
from Conectar_E_Salvar_Em_BD import ConnetcDatabase



def Requisitando_Dados():
    PageUsers = requests.get("https://randomuser.me/api/?nat=us")
    dados = PageUsers.json()
    dadosdeCadastro = extrairDados(dados)
    return dadosdeCadastro


def CriandoContas():
    # DadosCadastrais = pegandodados
    while True:

        try:

            DadosCadastrais = Requisitando_Dados()
            print(DadosCadastrais[0], DadosCadastrais[1], DadosCadastrais[7])

            # Pegando Siglas do estado
            Estado = DadosCadastrais[7]
            Sigla = Pegando_Estados(Estado)

            # Pegando data atual para salvar em Banco
            dataatual = datetime.now()
            data = dataatual.strftime("%d/%m/2024")

            # Setando Proxy
            proxy_host = 'na.s3l1wmrc.lunaproxy.net'
            proxy_port = '12233'
            proxy_username = 'user-tunnelbroker-region-us'
            proxy_password = '1lw2S9WxUwFFT28'

            # Conteúdo do manifest.json
            manifest_json = """
           {
            "version": "1.0.0", 
            "manifest_version": 2,
            "name": "Proxy",
            "permissions": [
              "proxy",
              "tabs",
              "unlimitedStorage",
              "storage",
              "<all_urls>",
              "webRequest",
              "webRequestBlocking"
            ],
            "background": {
              "scripts": ["background.js"]
            }
           }
           """

            # Conteúdo do background.js
            background_js = f"""
           var config = {{
            mode: "fixed_servers",
            rules: {{
              singleProxy: {{
                scheme: "http",
                host: "{proxy_host}",
                port: parseInt({proxy_port})
              }},
              bypassList: ["localhost"]
            }}
           }};

           chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});

           function callbackFn(details) {{
            return {{
              authCredentials: {{
                username: "{proxy_username}",
                password: "{proxy_password}"
              }}
            }};
           }}

           chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {{urls: ["<all_urls>"]}},
            ['blocking']
           );
           """
            # Caminho para a extensão
            pluginfile = 'proxy_auth_plugin.zip'

            # Validando Credenciais
            with zipfile.ZipFile(pluginfile, 'w') as zp:

                zp.writestr("manifest.json", manifest_json)
                zp.writestr("background.js", background_js)

            chrome_options = Options()
            chrome_options.add_extension(pluginfile)

            # Criando Navegador e Conectando no site
            driver = webdriver.Chrome(service=Service(), options=chrome_options)
            url = ('https://tunnelbroker.net/register.php')
            driver.get(url)

            # Preechendo Campos do Site
            namecount = driver.find_element(By.ID, "user_name")
            namecount.send_keys(DadosCadastrais[0])

            password = driver.find_element(By.ID, 'password')
            password.send_keys(DadosCadastrais[1])

            password = driver.find_element(By.ID, 'password2')
            password.send_keys(DadosCadastrais[1])

            firstname = driver.find_element(By.ID, "first_name")
            firstname.send_keys(DadosCadastrais[3])

            last_name = driver.find_element(By.ID, "last_name")
            last_name.send_keys(DadosCadastrais[4])

            country = driver.find_element(By.ID, "country")
            selectCountry = Select(country)
            selectCountry.select_by_value("US")

            street = driver.find_element(By.ID, 'street')
            street.send_keys(DadosCadastrais[5])

            city = driver.find_element(By.ID, 'city')
            city.send_keys(DadosCadastrais[6])

            postal_code = driver.find_element(By.ID, 'postal_code')
            postal_code.send_keys(DadosCadastrais[8])

            phone = city = driver.find_element(By.ID, 'phone')
            phone.send_keys(DadosCadastrais[9])

            # Verificando se o elemento state está carregado e preenchedo
            try:
                wait = WebDriverWait(driver, 30)
                # Encontre o elemento <select> dentro da div com id="usstate"
                state_select = wait.until(
                    EC.presence_of_element_located((By.XPATH, '//div[@id="usstate"]//select[@name="state"]')))

                # Execute JavaScript para habilitar todas as opções do <select>
                driver.execute_script("""
                    var options = arguments[0].options;
                    for (var i = 0; i < options.length; i++) {
                        options[i].disabled = false;
                    }
                """, state_select)

                # Listar todas as opções disponíveis no <select>
                select = Select(state_select)
                options = select.options
                for option in options:

                    # Verifique se a opção está habilitada antes de selecionar
                    for option in options:
                        if option.get_attribute('value') == 'CA' and option.is_enabled():
                            select.select_by_value(Sigla)  # Selecionar Califórnia
                            break
                    break
                else:
                    print("A opção 'CA' não foi encontrada ou está desabilitada")

            except Exception as e:
                print(f"Ocorreu um erro: {e}")

            # Timeout Criado para aguardar Preencer e-mail
            time.sleep(10)

            # Pegando Email colocado no site para criação de conta
            Pegaemail = driver.find_element(By.ID, "email")
            email = Pegaemail.get_attribute("value")

            captcha = driver.find_element(By.ID, "captcha_code")
            str(input("Se o Captcha estiver preenchido, aperte qualqer tecla: "))
            CheckBox = driver.find_element(By.ID, "tos")
            CheckBox.click()

            wait.until(EC.element_to_be_clickable((By.ID, "register")))
            BottonEnter = driver.find_element(By.ID, "register")
            BottonEnter.click()

            driver.get(input("Digite Link de Confirmação: "))

            time.sleep(1)
            confirma_user = driver.find_element(By.ID, "f_user")
            confirma_user.send_keys(DadosCadastrais[0])

            confir_password = driver.find_element(By.ID, "f_pass")
            confir_password.send_keys(DadosCadastrais[1])
            enter = driver.find_element(By.CLASS_NAME, "loginButton").click()

            time.sleep(3)
            # Chamando Banco de dados e salvando dados
            ConnetcDatabase(data, email, DadosCadastrais[0], DadosCadastrais[1])
            time.sleep(2)
            driver.quit()

        except Exception as e:
            print(f"Ocorreu um o erro {e}, Tentando novamente! ")
