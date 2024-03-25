# Automação de Cadastro de Produtos

Este projeto consiste em uma automação desenvolvida em Python para facilitar o processo de cadastro de produtos em um sistema empresarial.

## Passo a Passo do Projeto

### Passo 1: Entrar no Sistema da Empresa
- Utilizamos a biblioteca `pyautogui` para realizar automação de interface de usuário.
- Abrimos o navegador e navegamos até o sistema da empresa.

### Passo 2: Fazer Login
- Inserimos as credenciais de login e clicamos no botão para acessar o sistema.

### Passo 3: Importar a Base de Dados
- Utilizamos a biblioteca `pandas` para importar os dados dos produtos de um arquivo CSV.

### Passo 4: Cadastrar o Produto
- Iteramos sobre cada linha da tabela de produtos.
- Preenchemos os campos necessários para cada produto, como código, marca, tipo, categoria, preço, custo e observação.
- Finalizamos o cadastro do produto.

## Instalação de Dependências
Para executar este projeto, você precisa instalar as seguintes bibliotecas Python:

```bash
pip install pyautogui pandas numpy openpyxl
```

Certifique-se de que seu ambiente Python esteja configurado corretamente antes de executar o código.

## Observações
- Este projeto é apenas um exemplo básico de automação de cadastro de produtos e pode precisar de ajustes para se adequar ao seu sistema específico.
- É importante entender as políticas e termos de uso do sistema em que a automação será aplicada para garantir conformidade e evitar problemas legais.

Esperamos que este projeto seja útil para simplificar suas tarefas de cadastro de produtos. Sinta-se à vontade para contribuir e melhorar este projeto conforme necessário.
