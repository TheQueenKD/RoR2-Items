ITEMS = {
    'Hopoo Feather': 'Gain +1 (+1 per stack) maximum jump count.',
    'Focus Crystal': 'Increase damage to enemies within 13m by 20% (+20% per stack).',
    'Frost Relic': 'Killing an enemy surrounds you with an ice storm that deals 1200% '
                   'damage per second and slows enemies by 80% for 1.5s. '
                   'The storm grows with every kill, increasing its radius by 2m. '
                   'Stacks up to 18m (+12m per stack).',
}


def print_item_list_or_description(item_choice):
    if item_choice == '':
        print('Item List:')
        for item in sorted(ITEMS):
            print(item)
    else:
        print(f'{item_choice}:\t{ITEMS.get(item_choice, "Item not in list")}')
