Documentação do Código
Sistema de Simulação de Aluguel
Este código é um sistema de simulação de aluguel desenvolvido em Python usando a biblioteca Tkinter para criar a interface gráfica do usuário (GUI). O sistema permite que os usuários simulem um contrato de aluguel, gerem um contrato com base nos dados inseridos e efetuem login na interface.

Visão Geral
O sistema é composto por várias funcionalidades principais:

Login de Usuário: Os usuários podem fazer login no sistema fornecendo um nome de usuário e senha. O login é necessário para acessar a funcionalidade de simulação de aluguel.

Simulação de Aluguel: Após o login, os usuários podem inserir informações, como o valor do aluguel, o número de meses e a data de início do contrato. O sistema calculará o valor total do aluguel e exibirá os resultados na interface.

Geração de Contrato: Com base nas informações fornecidas na simulação de aluguel, o sistema permite que os usuários gerem um contrato em formato DOCX. O contrato é preenchido automaticamente com os detalhes do aluguel.

Tipos de Pessoa: O sistema oferece suporte a dois tipos de pessoa: física e jurídica. Os campos exibidos na interface variam de acordo com o tipo selecionado.

Funções Principais
calcular_data_saida(data_inicial, meses)
Esta função calcula a data de saída com base na data inicial e no número de meses fornecidos como entrada. Ela utiliza a biblioteca datetime para realizar os cálculos.

gerar_contrato(valor, meses, data_inicial)
Esta função gera um contrato em formato DOCX com base nas informações fornecidas na simulação de aluguel. O contrato é preenchido automaticamente com detalhes como nome do locatário, valor do aluguel, data de início, data de saída, etc.

fazer_login()
Esta função é chamada quando os usuários tentam fazer login no sistema. Ela verifica se o nome de usuário e a senha correspondem aos dados de login armazenados no código.

mostrar_campos_pessoa_fisica() e mostrar_campos_pessoa_juridica()
Essas funções alternam entre os campos exibidos na interface, dependendo se o tipo de pessoa selecionado é física ou jurídica. Elas ajudam a personalizar a entrada de dados com base no tipo escolhido.

simular_aluguel(valor, meses, data_inicial)
Esta função realiza a simulação de aluguel com base nas informações fornecidas pelos usuários. Ela calcula o valor total do aluguel com base no valor mensal, no número de meses e na data de início.

Como Usar o Sistema
Login: O usuário deve fazer login no sistema com um nome de usuário e senha válidos. O usuário padrão é "admin" e a senha é "admin".

Selecionar Tipo de Pessoa: Após fazer login, o usuário deve selecionar se é uma pessoa física ou jurídica. Isso determinará quais campos serão exibidos na tela.

Preencher Dados: Insira as informações necessárias na tela, incluindo o valor do aluguel, o número de meses e a data de início do contrato. Os campos específicos variam dependendo do tipo de pessoa.

Simular Aluguel: Clique no botão "Simular" para calcular os detalhes do aluguel com base nas informações inseridas. Os resultados serão exibidos na tela.

Gerar Contrato: Se desejar gerar um contrato com base na simulação, clique no botão "Gerar Contrato". O contrato gerado será salvo em formato DOCX na pasta de downloads do usuário.

Logout: O usuário pode fazer logout a qualquer momento clicando em "Logout" na tela principal.

Notas Adicionais
O código possui campos para dados pessoais de pessoas físicas e jurídicas, como nome, CPF, CNPJ, endereço, etc.
Os campos de cidade e estado são preenchidos manualmente, e é possível personalizar as listas de estados e cidades conforme necessário.
Espero que esta documentação ajude a entender e utilizar o sistema de simulação de aluguel. Se você tiver alguma dúvida ou precisar de assistência adicional, sinta-se à vontade para entrar em contato.

Esta documentação fornece uma visão geral do código e das principais funcionalidades do sistema. Certifique-se de personalizar ainda mais a documentação conforme necessário e adicionar informações específicas sobre como configurar o ambiente de execução do código e quaisquer requisitos adicionais.
