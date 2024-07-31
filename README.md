# Automazicao_contas
Projeto criado para automatizar criação de contas e validação.
Não foi realizada uma automatização completa do processo devido a procedimentos internos.

# Passo a passo
* 1 - É configurado um Proxy
* 2 - Sistema entra em um site para gerar Dados cadastrais de usuários aleatórios.
* 3 - O Sistema faz uma raspagem e salva apenas os dados necessários para  criaçao da conta e salva em uma List
* 4 - O Sistema Acessa o site de criação de contas e cadastra um novo usuário, confirma conta.
* 5 - O Sistema segue o fluxo, conecta a um banco de dados MySQL e salva os dados e contas que foiram criadas

# Ferramentas Utilizadas

* Python
* Selenium
* MySQL
