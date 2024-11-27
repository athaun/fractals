import Functions as fl

def generate_state(tile):
    state = ""

    # Next
    if tile.next == None: state += "*."
    else:
        for neighbor in tile.next: 
            state += neighbor
        state += '.'

    # Previous
    if tile.previous == None: state += "*."
    else:
        for neighbor in tile.previous: 
            state += neighbor
        state += '.'

    # Copy direction
    if tile.copy_direction == None: state += "*."
    else: state += tile.copy_direction + '.'

    # Caps
    if len(tile.caps) == 0: state += "*."
    else:
        for c in tile.caps: 
            state += c
        state += '.'

    # Status
    if tile.status == None: state += "*."
    else: state += tile.status + '.'

    # If there exists a tile in each direction
    if tile.tile_to_N == None: state += "*"
    else: state += 'Y'

    if tile.tile_to_E == None: state += "*"
    else: state += 'Y'

    if tile.tile_to_W == None: state += "*"
    else: state += 'Y'

    if tile.tile_to_S == None: state += "*."
    else: state += 'Y.'

    # Whether new key tile or not
    if tile.new_kt_N: state += 'T'
    else: state += 'F'

    if tile.new_kt_E: state += 'T'
    else: state += 'F'

    if tile.new_kt_W: state += 'T'
    else: state += 'F'

    if tile.new_kt_S: state += 'T.'
    else: state += 'F.'

    # Breadcrumb trail
    if tile.N == None: state += '*'
    else: state += tile.N

    if tile.E == None: state += '*'
    else: state += tile.E

    if tile.W == None: state += '*'
    else: state += tile.W

    if tile.S == None: state += '*.'
    else: state += tile.S + '.'

    # Temp
    if tile.temp == None: state += '*.'
    else: state += tile.temp + '.'

    # Transfer
    if tile.transfer == None: state += '*.'
    else: state += tile.transfer + '.'

    # Pseudo seed
    if tile.pseudo_seed: state += 'T.'
    else: state += 'F.'

    # Original seed
    if tile.original_seed: state += 'T.'
    else: state += 'F.'

    # Wall
    if tile.wall: state += 'T.'
    else: state += 'F.'

    # Key tile directions
    if tile.key_tile_N == None: state += '*'
    else: state += tile.key_tile_N[0]

    if tile.key_tile_E == None: state += '*'
    else: state += tile.key_tile_E[0]

    if tile.key_tile_W == None: state += '*'
    else: state += tile.key_tile_W[0]

    if tile.key_tile_S == None: state += '*.'
    else: state += tile.key_tile_S[0]

    # Copied
    if tile.copied: state += 'T.'
    else: state += 'F.'

    # Terminal
    if tile.terminal: state += 'T.'
    else: state += 'F.'

    # Number of times copied
    state += str(tile.num_times_copied)

    return state


def generate_xml_file(states, transitions, affinities, seed): 
    uniq = []
    for i in states:
        if not i in uniq:
            uniq.append(i)
    states = uniq 

    uniq = []
    for i in transitions:
        if not i in uniq:
            uniq.append(i)
    transitions = uniq

    # uniq = []
    # for i in affinities:
    #     if not i in uniq:
    #         uniq.append(i)
    # affinities = uniq

    vertical_transitions, horizontal_transitions, vertical_affinities, horizontal_affinities = [], [], [], []
    for a in affinities: 
        if len(a) == 0:
            continue
        if a[2] == 'V': vertical_affinities.append(a)
        elif a[2] == 'H': horizontal_affinities.append(a)

    for t in transitions: 
        if len(t) == 0:
            continue
        if t[4] == 'V': vertical_transitions.append(t)
        elif t[4] == 'H': horizontal_transitions.append(t)

    path = r"Output/Output.xml"
    
    # Open and write to this file
    f = open(path, 'w')
    f.write('<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<System Temp="1"><AllStates>')
    for s in states: 
        # color = get_state_color(s)
        f.write('<State Label="%s" Color="ffffff" DisplayLabel="%s" DisplayLabelFont="Fira Code Regular Nerd Font Complete Mono" DisplayLabelColor="ffffff" />' % (s, s))
    f.write('</AllStates><InitialStates>')
    for s in states:  
        # color = get_state_color(s)
        f.write('<State Label="%s" Color="ffffff" DisplayLabel="%s" DisplayLabelFont="Fira Code Regular Nerd Font Complete Mono" DisplayLabelColor="ffffff" />' % (s, s))
    f.write('</InitialStates><SeedStates>')

    stack = [seed]
    visited_tiles = []
    while len(stack) > 0:
        cur_tile = stack.pop()
        f.write('<State Label="%s" Color="ffffff" DisplayLabel="%s" DisplayLabelFont="Fira Code Regular Nerd Font Complete Mono" DisplayLabelColor="ffffff" />' % (generate_state(cur_tile), generate_state(cur_tile)))

        if cur_tile.next != None:
            for neighbor in cur_tile.next:
                if fl.retrieve_tile(cur_tile, neighbor) not in visited_tiles: stack.append(fl.retrieve_tile(cur_tile, neighbor))

        if cur_tile.previous != None:
            for neighbor in cur_tile.previous:
                if fl.retrieve_tile(cur_tile, neighbor) not in visited_tiles: stack.append(fl.retrieve_tile(cur_tile, neighbor))

        visited_tiles.append(cur_tile)
    
    f.write('</SeedStates><Tiles>')

    stack = [[seed, 0, 0]]
    visited_tiles = []
    while len(stack) > 0:
        [cur_tile, x, y] = stack.pop()
        f.write('<Tile Label="%s" Color="ffffff" x="%i" y="%i" DisplayLabel="%s" DisplayLabelFont="ffffff" DisplayLabelColor="ffffff" />' % (generate_state(cur_tile), x, y, generate_state(cur_tile)))

        if cur_tile.next != None:
            for neighbor in cur_tile.next:
                if fl.retrieve_tile(cur_tile, neighbor) not in visited_tiles: 
                    if neighbor == 'N': stack.append([fl.retrieve_tile(cur_tile, neighbor), x, y+1])
                    if neighbor == 'E': stack.append([fl.retrieve_tile(cur_tile, neighbor), x+1, y])
                    if neighbor == 'W': stack.append([fl.retrieve_tile(cur_tile, neighbor), x-1, y])
                    if neighbor == 'S': stack.append([fl.retrieve_tile(cur_tile, neighbor), x, y-1])

        if cur_tile.previous != None:
            for neighbor in cur_tile.previous:
                if fl.retrieve_tile(cur_tile, neighbor) not in visited_tiles: 
                    if neighbor == 'N': stack.append([fl.retrieve_tile(cur_tile, neighbor), x, y+1])
                    if neighbor == 'E': stack.append([fl.retrieve_tile(cur_tile, neighbor), x+1, y])
                    if neighbor == 'W': stack.append([fl.retrieve_tile(cur_tile, neighbor), x-1, y])
                    if neighbor == 'S': stack.append([fl.retrieve_tile(cur_tile, neighbor), x, y-1])

        visited_tiles.append(cur_tile)

    f.write('</Tiles><VerticalTransitions>')
    for [t1, t2, t1_transition, t2_transition, _] in vertical_transitions: 
        f.write('<Rule Label1="%s" Label2="%s" Label1Final="%s" Label2Final="%s" />' % (t1, t2, t1_transition, t2_transition))

    f.write('</VerticalTransitions><HorizontalTransitions>')
    for [t1, t2, t1_transition, t2_transition, _] in horizontal_transitions: 
        f.write('<Rule Label1="%s" Label2="%s" Label1Final="%s" Label2Final="%s" />' % (t1, t2, t1_transition, t2_transition))

    f.write('</HorizontalTransitions><VerticalAffinities>')
    for [t1, t2, _, _] in vertical_affinities: 
        f.write('<Rule Label1="%s" Label2="%s" Strength="1" />' % (t1, t2))

    f.write('</VerticalAffinities><HorizontalAffinities>')
    for [t1, t2, _, _] in horizontal_affinities: 
        f.write('<Rule Label1="%s" Label2="%s" Strength="1" />' % (t1, t2))

    f.write('</HorizontalAffinities></System>')

# Testing File --------------------------------------------------------------------------------------------------
# Sierpinski Triangle seed
# seed_tile = fl.Tile(None, ["E"])
# t1 = fl.Tile(["W"], ["N"])
# t2 = fl.Tile(["S"], None)
# seed_tile.tile_to_E = t1
# t1.tile_to_N, t1.tile_to_W = t2, seed_tile
# t2.tile_to_S = t1
# seed_tile.E = 'N'
# t1.W, t1.N = 'N', 'N'
# t2.S = 'N'
# seed_tile.key_tile_N, seed_tile.key_tile_E, seed_tile.key_tile_W, seed_tile.key_tile_S = ["E"], ["E"], None, ["E"]
# t1.key_tile_N, t1.key_tile_E, t1.key_tile_W, t1.key_tile_S = ["N"], None, ["W"], None
# t2.key_tile_N, t2.key_tile_E, t2.key_tile_W, t2.key_tile_S = None, ["S"], ["S"], ["S"]
# t2.terminal = True

# generate_xml_file([generate_state(seed_tile), generate_state(t1), generate_state(t2)], [], [], seed_tile)