perguntas = [
    {
        'Question': 'Quanto é 2+2?',
        'Options': ['1', '3', '4', '5'],
        'Response': '4',
    },
    {
        'Question': 'Quanto é 5*5?',
        'Options': ['25', '55', '10', '51'],
        'Response': '25',
    },
    {
        'Question': 'Quanto é 10/2?',
        'Options': ['4', '5', '2', '1'],
        'Response': '5',
    },
]

acertou = 0
errou = 0

for question in perguntas:
    print('Pergunta: ', question['Question'])        

    for i, alternative in enumerate(question['Options']):        
        print(i, ') ', alternative)

    answer = int(input('Digite sua resposta _> '))

    if question['Options'][answer] == question['Response']:
        print()
        print('Acertou ✔')
        acertou += 1
        print()
    else:
        print()
        print('Errou ❌')        
        errou += 1
        print()

if acertou > 0:
    print(f'Total de acertos: {acertou}')
if errou > 0: 
    print(f'Total de erros: {errou}')