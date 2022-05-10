# Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão, chame este dicionário de 
# glossário.

# a. Pense em cinco palavras relacionada à programação que você conheceu nesta disciplina. Use estas palavras como chaves em seu 
# glossário e armazene seus significados como valores.

# b. Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante. Por exemplo: você pode exibir a 
# palavra seguida de dois-pontos e depois o seu significado, ou apresentar a palavra em uma linha e então exibir seu significado 
# identado em uma segunda linha. Utilize o caractere de quebra de linha (\n) para inserir uma linha em branco entre cada par 
# palavra-significado em sua saída.

# c. Sugestões de termos: Algoritmos, Python, Webscraping, Lógica de Programação, Google Colab, Visual Studio Code.

glossario = {
    'Variavel' : 'Uma variável é um nome que se refere a um valor. Um comando de atribuição cria uma nova variável e lhe dá um valor. Variáveis são usadas para guardarmos valores que serão usados mais tarde no programa.',
    'Webscraping' : 'também conhecido como extração de dados da web, é o nome dado ao processo de coleta de dados estruturados da web de maneira automatizada.',
    'Strings' : 'são conjuntos de caracteres de texto que podem ser compreendidos como representações de informações escritas dentro de um código.',
    'Teste de mesa' : 'É uma técnica usada para testar algoritmos ou programas de computador, com o intuito de checar se há algum erro na logica durante a execução do algoritmo ou programa. Ele também simula o fluxo de execução de uma parte de um programa ou o programa todo.',
    'Biblioteca' : 'As bibliotecas Python são um conjunto de módulos e funções úteis que reduzem o uso de código no programa. São mais de 137 mil bibliotecas Python que facilitam a programação dos desenvolvedores, com diversas finalidades. Por meio delas, é possível fazer tratamento de dados Python.',
    }

for i in glossario:
        print('=' * 148)
        print(f'O significado de {i} é:')
        print('\n')
        print(glossario[i])
        print('-' * 148)
        print('\n')