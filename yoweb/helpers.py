BASIC_ATTRS = ('rank', 'name')


def clean_stat(data):
    stats = data.split('  ')
    left_side = stats[0].split('/')
    experience = left_side[0]
    standing = {'ocean_wide': left_side[1]}
    if len(stats) == 2:
        right_side = stats[1].replace('(archipelago:\xa0', '').replace(')', '')
        standing['archipelago'] = right_side
    else:
        standing['archipelago'] = left_side[1]

    return experience, standing
