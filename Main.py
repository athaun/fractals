import Fractal_Logic as fl

# # Sierpinski Triangle seed
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




# # Horseshoe
# seed_tile = fl.Tile(None, ['S'])
# t1 = fl.Tile(['N'], ['S'])
# t2 = fl.Tile(['N'], ['E'])
# t3 = fl.Tile(['W'], ['E'])
# t4 = fl.Tile(['W'], ['N'])
# t5 = fl.Tile(['S'], ['N'])
# t6 = fl.Tile(['S'], None)

# seed_tile.tile_to_S, t1.tile_to_N = t1, seed_tile
# t1.tile_to_S, t2.tile_to_N = t2, t1
# t2.tile_to_E, t3.tile_to_W = t3, t2
# t3.tile_to_E, t4.tile_to_W = t4, t3
# t4.tile_to_N, t5.tile_to_S = t5, t4
# t5.tile_to_N, t6.tile_to_S = t6, t5

# seed_tile.S = 'N'
# t1.N, t1.S = 'N', 'N'
# t2.N, t2.E = 'N', 'N'
# t3.W, t3.E = 'N', 'N'
# t4.W, t4.N = 'N', 'N'
# t5.S, t5.N = 'N', 'N'
# t6.S = 'N'

# seed_tile.key_tile_N, seed_tile.key_tile_E, seed_tile.key_tile_W, seed_tile.key_tile_S = None, ['S'], ['S'], ['S']
# t1.key_tile_N, t1.key_tile_E, t1.key_tile_W, t1.key_tile_S = ['N'], ['S'], ['S'], ['S']
# t2.key_tile_N, t2.key_tile_E, t2.key_tile_W, t2.key_tile_S = ['N'], ['E'], None, None
# t3.key_tile_N, t3.key_tile_E, t3.key_tile_W, t3.key_tile_S = ['W'], ['E'], ['W'], ['W']
# t4.key_tile_N, t4.key_tile_E, t4.key_tile_W, t4.key_tile_S = ['W'], None, ['W'], ['W']
# t5.key_tile_N, t5.key_tile_E, t5.key_tile_W, t5.key_tile_S = ['S'], ['S'], ['S'], ['S']
# t6.key_tile_N, t6.key_tile_E, t6.key_tile_W, t6.key_tile_S = ['S'], ['S'], ['S'], ['S']

# seed_tile.terminal = True
# t6.terminal = True




# # Sierpinski Carpet
# seed_tile = fl.Tile(None, ['S'])
# t1 = fl.Tile(['N'], ['S'])
# t2 = fl.Tile(['N'], ['E'])
# t3 = fl.Tile(['W'], ['E'])
# t4 = fl.Tile(['W'], ['N'])
# t5 = fl.Tile(['S'], ['N'])
# t6 = fl.Tile(['S'], ['W'])
# t7 = fl.Tile(['E'], None)

# seed_tile.tile_to_S, t1.tile_to_N = t1, seed_tile
# t1.tile_to_S, t2.tile_to_N = t2, t1
# t2.tile_to_E, t3.tile_to_W = t3, t2
# t3.tile_to_E, t4.tile_to_W = t4, t3
# t4.tile_to_N, t5.tile_to_S = t5, t4
# t5.tile_to_N, t6.tile_to_S = t6, t5
# t6.tile_to_W, t7.tile_to_E = t7, t6

# seed_tile.S = 'N'
# t1.N, t1.S = 'N', 'N'
# t2.N, t2.E = 'N', 'N'
# t3.W, t3.E = 'N', 'N'
# t4.W, t4.N = 'N', 'N'
# t5.S, t5.N = 'N', 'N'
# t6.S, t6.W = 'N', 'N'
# t7.E = 'N'

# seed_tile.key_tile_N, seed_tile.key_tile_E, seed_tile.key_tile_W, seed_tile.key_tile_S = None, ['S'], ['S'], ['S']
# t1.key_tile_N, t1.key_tile_E, t1.key_tile_W, t1.key_tile_S = ['N'], ['S'], ['S'], ['S']
# t2.key_tile_N, t2.key_tile_E, t2.key_tile_W, t2.key_tile_S = ['N'], ['E'], None, None
# t3.key_tile_N, t3.key_tile_E, t3.key_tile_W, t3.key_tile_S = ['W'], ['E'], ['W'], ['W']
# t4.key_tile_N, t4.key_tile_E, t4.key_tile_W, t4.key_tile_S = ['W'], None, ['W'], ['W']
# t5.key_tile_N, t5.key_tile_E, t5.key_tile_W, t5.key_tile_S = ['S'], ['S'], ['S'], ['S']
# t6.key_tile_N, t6.key_tile_E, t6.key_tile_W, t6.key_tile_S = ['S'], ['S'], ['S'], ['S']
# t7.key_tile_N, t7.key_tile_E, t7.key_tile_W, t7.key_tile_S = ['E'], ['E'], ['E'], ['E']

# seed_tile.terminal = True
# t7.terminal = True


# # Plus
# seed_tile = fl.Tile(None, ['N', 'E', 'W', 'S'])
# t1 = fl.Tile(['S'], None)
# t2 = fl.Tile(['W'], None)
# t3 = fl.Tile(['E'], None)
# t4 = fl.Tile(['N'], None)

# seed_tile.tile_to_N, t1.tile_to_S = t1, seed_tile
# seed_tile.tile_to_E, t2.tile_to_W = t2, seed_tile
# seed_tile.tile_to_W, t3.tile_to_E = t3, seed_tile
# seed_tile.tile_to_S, t4.tile_to_N = t4, seed_tile

# seed_tile.N, t1.S = 'N', 'N'
# seed_tile.E, t2.W = 'N', 'N'
# seed_tile.W, t3.E = 'N', 'N'
# seed_tile.S, t4.N = 'N', 'N'

# seed_tile.key_tile_N, seed_tile.key_tile_E, seed_tile.key_tile_W, seed_tile.key_tile_S = ['N'], ['E'], ['W'], ['S']
# t1.key_tile_N, t1.key_tile_E, t1.key_tile_W, t1.key_tile_S = None, ['S'], ['S'], ['S']
# t2.key_tile_N, t2.key_tile_E, t2.key_tile_W, t2.key_tile_S = ['W'], None, ['W'], ['W']
# t3.key_tile_N, t3.key_tile_E, t3.key_tile_W, t3.key_tile_S = ['E'], ['E'], None, ['E']
# t4.key_tile_N, t4.key_tile_E, t4.key_tile_W, t4.key_tile_S = ['N'], ['N'], ['N'], None

# t1.terminal, t2.terminal, t3.terminal, t4.terminal = True, True, True, True
# seed_tile.terminal = False



# Sierpinski triangle ("Schweller" way)
seed_tile = fl.Tile(None, ['N', 'E'])
t1 = fl.Tile(['S'], None)
t2 = fl.Tile(['W'], None)

seed_tile.tile_to_N, t1.tile_to_S = t1, seed_tile
seed_tile.tile_to_E, t2.tile_to_W = t2, seed_tile

seed_tile.N, t1.S = 'N', 'N'
seed_tile.E, t2.W = 'N', 'N'

seed_tile.key_tile_N, seed_tile.key_tile_E, seed_tile.key_tile_W, seed_tile.key_tile_S = ['N'], ['E'], None, None
t1.key_tile_N, t1.key_tile_E, t1.key_tile_W, t1.key_tile_S = None, ['S'], ['S'], ['S']
t2.key_tile_N, t2.key_tile_E, t2.key_tile_W, t2.key_tile_S = ['W'], None, ['W'], ['W']

t1.terminal, t2.terminal = True, True
seed_tile.terminal = False


# Doesnt change
seed_tile.original_seed = True

# Plot --------------------------------------------------------------------------------------------------------
result = fl.run_simulation(seed_tile, 1)

# Plot the result onto graph
fl.plot_graph(seed_tile)