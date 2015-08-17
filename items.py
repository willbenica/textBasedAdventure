# items.py

# A dict of all the items in the game. First level are the item names, with sub dicts with the 'Names', 'purpose' and a 'Description'

items = {
    'Health Tonic': {
        'name': 'Health Tonic',
        'description': 'A bottle of pale green liquid. It smells rather disgusting, \nbut when has anything healthy tasted good',
        'type': 'tonic',
        'action': 'change life to a maximum'
    },
    'Death Tonic': {
        'name': 'Death Tonic',
        'description': 'A bottle of clear liquid with a pleasent aroma.',
        'type': 'tonic',
        'action': -25
    }
}
