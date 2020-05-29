BOT_CONFIG = {
    'intents': {
        'Hello' :{
            'questions': ['Hello','Good day'],
            'responses': ['Hi', 'Nice to meet you']
        },
        'bye':{
            'questions': ['Bye','Good luck'],
            'responses': ['Bye bye', 'see you']
        },
        'whatcanyoudo':{
            'questions':['What you can', 'Tell what can you do'],
            'responses':['I can answer on questions. Just ask something']
        },
        'name':{
            'questions':['What\'s your name','Name?'],
            'responses':['My name is Bot']
        },
        'weather':{
            'questions':['What\'s the weather now'],
            'responses':['Wonderfull weather','Good for a walk']
        },
        'thanks':{
            'questions':['Thank you','10q','thanks'],
            'responses':['Thank you too']
        },
    },
    'failure_phrase':[
        'Don\'t understand you',
        'Sorry,repeat please',
        'Reformulate',
    ]
}

import random
def get_intent(text):
    intents = BOT_CONFIG['intents']
    for intent,value in intents.items():
        for example in value['questions']:
            if text == example:
                return intent

def get_response_by_intent(intent):
    response = BOT_CONFIG['intents'][intent]['responses']
    return random.choice(response)

def get_failure_phrase():
    phrases = BOT_CONFIG['failure_phrase']
    return random.choice(phrases)

def generate_answer(text):
    # NLU
    global answer
    intent = get_intent(text)

    # Make answer

    #by script
    if intent:
        response = get_response_by_intent(intent)
        return response
    #use generative model
    #TODO

    #use stub
    failure_phrase = get_failure_phrase()
    return failure_phrase
while True:
    text = input('Enter your question: ')
    answer = generate_answer(text)
    print(answer)
