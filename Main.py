import Fractal_Logic as fl
import tkinter as tk

# Tile size and locations
TILE_SIZE = 30

# Useful functions
def get_tag(x, y):
    return str(x) + ',' + str(y)

def get_xy(x, y):
    return [60 * round(x / 60), 60 * round(y / 60)]

# Main
class main(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.tile_positions=dict([])
        self.origin_tile = None

        for F in (draw_seed, choose_origin):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(draw_seed)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def update_frame(self, cont):
        frame = self.frames[cont]
        frame.update(self)
        self.frames[cont] = frame

    def finish(self):
        if self.origin_tile != None:
            print('Done!')

class draw_seed(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text = "Left click to place tile. Right click to delete. Done to finish.")
        label.pack()

        # Canvas for drawing
        canvas = tk.Canvas(self, bg='lightgray')
        canvas.pack(anchor='nw', fill='both', expand=1)

        def add_tile(event):
            global lasx, lasy
            lasx, lasy = event.x, event.y

            # Round
            x, y = get_xy(lasx, lasy)

            if get_tag(x, y) not in controller.tile_positions:
                tile = canvas.create_rectangle(x - TILE_SIZE, y - TILE_SIZE, x + TILE_SIZE, y + TILE_SIZE, fill='white')
                controller.tile_positions[get_tag(x,y)] = (tile, x, y, 0)


        def remove_tile(event):
            global lasx, lasy
            lasx, lasy = event.x, event.y

            # Round
            x, y = get_xy(lasx, lasy)

            if get_tag(x,y) in controller.tile_positions:
                canvas.delete(controller.tile_positions[get_tag(x, y)][0])
                del controller.tile_positions[get_tag(x, y)]

        canvas.bind("<Button-1>", add_tile)
        canvas.bind("<Button-3>", remove_tile)

        def display_choose_origin():
            controller.update_frame(choose_origin)
            controller.show_frame(choose_origin)

        button = tk.Button(self, text="Done", command=display_choose_origin)
        button.pack()

class choose_origin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

    def update(self, controller):
        label = tk.Label(self, text = "Left click to select origin tile. Done to finish.")
        label.pack()

        # Redraw canvas
        canvas = tk.Canvas(self, bg='lightgray')
        canvas.pack(anchor='nw', fill='both', expand=1)

        for cord in controller.tile_positions:
            [x,y] = cord.split(',')
            x, y = int(x), int(y)
            canvas.create_rectangle(x - TILE_SIZE, y - TILE_SIZE, x + TILE_SIZE, y + TILE_SIZE, fill='white')

        def choosing_tile(event):
            global lasx, lasy
            lasx, lasy = event.x, event.y

            # Round
            x, y = get_xy(lasx, lasy)
            
            if get_tag(x,y) in controller.tile_positions: 
                for cord in controller.tile_positions:
                    [w,z] = cord.split(',')
                    w, z = int(w), int(z)
                    if controller.tile_positions[get_tag(w,z)][3] == 1:
                        canvas.delete(controller.tile_positions[get_tag(w, z)][0])
                        del controller.tile_positions[get_tag(w, z)]

                        tile = canvas.create_rectangle(w - TILE_SIZE, z - TILE_SIZE, w + TILE_SIZE, z + TILE_SIZE, fill='white')
                        controller.tile_positions[get_tag(w,z)] = (tile, w, z, 0)

                        break
                
                canvas.delete(controller.tile_positions[get_tag(x, y)])
                del controller.tile_positions[get_tag(x, y)]

                tile = canvas.create_rectangle(x - TILE_SIZE, y - TILE_SIZE, x + TILE_SIZE, y + TILE_SIZE, fill='black')
                controller.tile_positions[get_tag(x,y)] = (tile, x, y, 1)

                controller.origin_tile = tile
        
        canvas.bind("<Button-1>", choosing_tile)

        button = tk.Button(self, text="Done",
                            command=lambda: controller.finish())
        button.pack()

app = main()
app.mainloop()


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



# # Sierpinski triangle ("Schweller" way)
# seed_tile = fl.Tile(None, ['N', 'E'])
# t1 = fl.Tile(['S'], None)
# t2 = fl.Tile(['W'], None)

# seed_tile.tile_to_N, t1.tile_to_S = t1, seed_tile
# seed_tile.tile_to_E, t2.tile_to_W = t2, seed_tile

# seed_tile.N, t1.S = 'N', 'N'
# seed_tile.E, t2.W = 'N', 'N'

# seed_tile.key_tile_N, seed_tile.key_tile_E, seed_tile.key_tile_W, seed_tile.key_tile_S = ['N'], ['E'], None, None
# t1.key_tile_N, t1.key_tile_E, t1.key_tile_W, t1.key_tile_S = None, ['S'], ['S'], ['S']
# t2.key_tile_N, t2.key_tile_E, t2.key_tile_W, t2.key_tile_S = ['W'], None, ['W'], ['W']

# t1.terminal, t2.terminal = True, True
# seed_tile.terminal = False


# # Doesnt change
# seed_tile.original_seed = True

# Plot --------------------------------------------------------------------------------------------------------
# result = fl.run_simulation(seed_tile, 1)

# # Plot the result onto graph
# fl.plot_graph(seed_tile)