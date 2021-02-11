# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')

ingredients = ['sodium benzoate']

toxins = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']

def check_food():
    for ingred in ingredients:
        if ingred in toxins:
            print('!!!')
            print('there is a toxin in the food!')
            print('!!!')
            make_alert_sound()
            return
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()

check_food()
