class Tile():

    def __init__(self, p, n):
        self.previous = p
        self.next = n

    # What direction to copy
    copy_direction = None

    # Caps
    caps = []

    # Local tile information (and neighbors)
    status = None
    tile_to_N = None
    tile_to_E = None
    tile_to_W = None
    tile_to_S = None

    # If tile becomes new key tile or not
    new_kt_N = False
    new_kt_E = False
    new_kt_W = False
    new_kt_S = False

    # Breadcrumb trail
    N = None
    E = None
    W = None
    S = None

    # Holds information from breadcrumb trail (what the state was before)
    temp = None

    # What is being transferred
    transfer = None

    # If tile is a seed 
    original_seed = False
    pseudo_seed = False

    # If tile is on edge of sub-assembly
    wall = False

    # Direction to key tile
    key_tile_N = None
    key_tile_E = None
    key_tile_W = None
    key_tile_S = None

    # Has assembly been copied for tile
    copied = False

    # Is tile terminal
    terminal = False

    # The new previous and next for tile
    new_p = None
    new_n = None

    # If first tile copied
    first_tile = False

    # For seeds, number of times subassembly has been copied
    num_times_copied = 0

# RETURNS: adjacent tile in direction d from current tile
def retrieve_tile(tile, d):
    if (d == "N"):
        return tile.tile_to_N
    if (d == "E"):
        return tile.tile_to_E
    if (d == "W"):
        return tile.tile_to_W
    if (d == "S"):
        return tile.tile_to_S
    
def generate_transfer_state(tile):
    state = ""

    # Next
    if tile.next == None: state += "*|"
    else:
        for neighbor in tile.next: 
            state += neighbor
        state += '|'

    # Previous
    if tile.previous == None: state += "*|"
    else:
        for neighbor in tile.previous: 
            state += neighbor
        state += '|'

    # Copy direction
    if tile.copy_direction == None: state += "*|"
    else: state += tile.copy_direction + '|'

    # Caps
    if len(tile.caps) == 0: state += "*|"
    else:
        for c in tile.caps: 
            state += c
        state += '|'

    # Status
    if tile.status == None: state += "*|"
    else: state += tile.status + '|'

    # If there exists a tile in each direction
    if tile.tile_to_N == None: state += "*"
    else: state += 'Y'

    if tile.tile_to_E == None: state += "*"
    else: state += 'Y'

    if tile.tile_to_W == None: state += "*"
    else: state += 'Y'

    if tile.tile_to_S == None: state += "*|"
    else: state += 'Y|'

    # Whether new key tile or not
    if tile.new_kt_N: state += 'T'
    else: state += 'F'

    if tile.new_kt_E: state += 'T'
    else: state += 'F'

    if tile.new_kt_W: state += 'T'
    else: state += 'F'

    if tile.new_kt_S: state += 'T|'
    else: state += 'F|'

    # Breadcrumb trail
    if tile.N == None: state += '*'
    else: state += tile.N

    if tile.E == None: state += '*'
    else: state += tile.E

    if tile.W == None: state += '*'
    else: state += tile.W

    if tile.S == None: state += '*|'
    else: state += tile.S + '|'

    # Temp
    if tile.temp == None: state += '*|'
    else: state += tile.temp + '|'

    # Transfer
    if tile.transfer == None: state += '*|'
    else: state += tile.transfer + '|'

    # Pseudo seed
    if tile.pseudo_seed: state += 'T|'
    else: state += 'F|'

    # Original seed
    if tile.original_seed: state += 'T|'
    else: state += 'F|'

    # Wall
    if tile.wall: state += 'T|'
    else: state += 'F|'

    # Key tile directions
    if tile.key_tile_N == None: state += '*'
    else: state += tile.key_tile_N[0]

    if tile.key_tile_E == None: state += '*'
    else: state += tile.key_tile_E[0]

    if tile.key_tile_W == None: state += '*'
    else: state += tile.key_tile_W[0]

    if tile.key_tile_S == None: state += '*|'
    else: state += tile.key_tile_S[0]

    # Copied
    if tile.copied: state += 'T|'
    else: state += 'F|'

    # Terminal
    if tile.terminal: state += 'T|'
    else: state += 'F|'

    # First tile
    if tile.first_tile: state += 'T|'
    else: state += 'F|'

    # New next for tile
    if tile.new_n == None: state += "*|"
    else:
        for neighbor in tile.new_n: 
            state += neighbor
        state += '|'

    # New previous for tile
    if tile.new_p == None: state += "*|"
    else:
        for neighbor in tile.new_p: 
            state += neighbor
        state += '|'

    # Number of times copied
    state += str(tile.num_times_copied)

    return state

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
    else: state += generate_transfer_state(tile.transfer) + '.'

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
    else: state += tile.key_tile_S[0] + '.'

    # Copied
    if tile.copied: state += 'T.'
    else: state += 'F.'

    # Terminal
    if tile.terminal: state += 'T.'
    else: state += 'F.'

    # First tile
    if tile.first_tile: state += 'T.'
    else: state += 'F.'

    # New next for tile
    if tile.new_n == None: state += "*."
    else:
        for neighbor in tile.new_n: 
            state += neighbor
        state += '.'

    # New previous for tile
    if tile.new_p == None: state += "*."
    else:
        for neighbor in tile.new_p: 
            state += neighbor
        state += '.'

    # Number of times copied
    state += str(tile.num_times_copied)

    return state
