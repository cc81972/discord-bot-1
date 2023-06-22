import random


def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == 'hello sam':
        return 'Hello I am the Supreme Overlord Sitaram'
    
    if p_message == 'roll':
        num_ppl = random.randint(1,10)
        return f'Sam has wrecked havoc upon {num_ppl} people today!'
    
    if p_message == '!help':
        return "`Say hello sam to get him to introduce himself\n Say roll to find out how many:)\n Say where is sam to find out what he is doing right neow`"
    
    if p_message == 'where is sam?':
        sams_actions = ['With his girlfriend', 'Working', 'Rizzing', 'Studying', 'Wrestling Practice']
        return sams_actions[random.randint(0,len(sams_actions)-1)]
    
    
    else:
        pass