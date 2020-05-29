BOT_CONFIG = {
    'intents': {
        'hello' :{
            'questions': ['Hello','Good day'],
            'answers': ['Hi', 'Nice to meet you']
        },
        'bye':{
            'questions': ['Bye','Good luck'],
            'answers': ['Bye bye', 'see you']
        },
        'whatcanyoudo':{
            'questions':['What you can', 'Tell what can you do'],
            'answers':['I can answer on questions. Just ask something']
        },
        'name':{
            'questions':['What\'s your name','Name?'],
            'answer':['My name is Bot']
        },
        'weather':{
            'questions':['What\'s the weather now'],
            'answer':['Wonderfull weather','Good for a walk']
        }
    },
    'default_answers':[
        'Don\'t understand you',
        'Sorry,repeat please',
        'Reformulate',
    ]
}
def generate_answer(text):
    return text
while True:
    text = input('Enter your question: ')
    answer = generate_answer(text)
    print(answer)
