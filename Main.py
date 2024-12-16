import Fractal_Logic as fl
import Generate_XML as g
import tkinter as tk
import tkinter.messagebox
import math
from collections import deque

# Specify up to what stage (DO NOT RECOMMEND MORE THAN 3)
STAGE = 3

# Tile size and locations
TILE_SIZE = 30

# Useful functions
def check_valid_seed(tile_positions):
    valid, error = True, []
    
    # Check for at least 1 tile
    if len(tile_positions) < 1:
        valid = False
        error = "Left click to place tiles"

    # Check for connectivitiy
    else:
        for cord in tile_positions:
            [x,y] = cord.split(',')
            x, y = int(x), int(y)

            if get_tag(x, y-TILE_SIZE*2) not in tile_positions and get_tag(x+TILE_SIZE*2, y) not in tile_positions and get_tag(x-TILE_SIZE*2, y) not in tile_positions and get_tag(x, y+TILE_SIZE*2) not in tile_positions: 
                valid = False
                error = "Fractal must be connected"
                break

    if not valid: return [valid, error]

    # Check if feasible generator
    else: 
        min_x, max_x, min_y, max_y = math.inf, -1, math.inf, -1
        for cord in tile_positions:
            [x,y] = cord.split(',')
            x, y = int(x), int(y)

            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

        n, e, w, s = False, False, False, False
        for cord in tile_positions:
            [x,y] = cord.split(',')
            x, y = int(x), int(y)

            if (x == min_x and get_tag(max_x, y) in tile_positions) or (x == max_x and get_tag(min_x, y) in tile_positions):
                e, w = True, True
            if (y == min_y and get_tag(x, max_y) in tile_positions) or (y == max_y and get_tag(x, min_y) in tile_positions):
                n, s = True, True

        if not (n and s): 
            return [False, "Not feasible generator (north/south)"]
        if not (e and w): 
            return [False, "Not feasible generator (east/west)"]
        
        return [True, error]



def get_tag(x, y):
    return str(x) + ',' + str(y)

def get_xy(x, y):
    return [(TILE_SIZE * 2) * round(x / (TILE_SIZE * 2)), (TILE_SIZE * 2) * round(y / (TILE_SIZE * 2))]

# Create seed given tile positions
def create_seed(tile_positions, origin_tile_cords):
    new_tiles = dict([])
    stack = deque()
    stack.append([origin_tile_cords[0], origin_tile_cords[1], None])
    seed_tile = None

    min_x, max_x, min_y, max_y = math.inf, -1, math.inf, -1

    visited = []

    # Find the min/max values
    min_x, max_x, min_y, max_y = math.inf, -1, math.inf, -1
    for cord in tile_positions:
        [x,y] = cord.split(',')
        x, y = int(x), int(y)

        if x < min_x: min_x = x
        if x > max_x: max_x = x
        if y < min_y: min_y = y
        if y > max_y: max_y = y

    while len(stack) > 0:
        [x,y, prev] = stack.popleft()
        next = []

        if [x,y] not in visited: visited.append([x,y])

        if get_tag(x, y-TILE_SIZE*2) in tile_positions and get_tag(x, y-TILE_SIZE*2) not in visited: 
            stack.append([x, y-TILE_SIZE*2, 'S'])
            visited.append(get_tag(x, y-TILE_SIZE*2))
            next.append('N')
        if get_tag(x+TILE_SIZE*2, y) in tile_positions and get_tag(x+TILE_SIZE*2, y) not in visited: 
            stack.append([x+TILE_SIZE*2, y, 'W'])
            visited.append(get_tag(x+TILE_SIZE*2, y))
            next.append('E')
        if get_tag(x-TILE_SIZE*2, y) in tile_positions and get_tag(x-TILE_SIZE*2, y) not in visited: 
            stack.append([x-TILE_SIZE*2, y, 'E'])
            visited.append(get_tag(x-TILE_SIZE*2, y))
            next.append('W')
        if get_tag(x, y+TILE_SIZE*2) in tile_positions and get_tag(x, y+TILE_SIZE*2) not in visited: 
            stack.append([x, y+TILE_SIZE*2, 'N'])
            visited.append(get_tag(x, y+TILE_SIZE*2))
            next.append('S')

        if get_tag(x,y) in tile_positions: del tile_positions[get_tag(x,y)]

        if len(next) == 0: next = None

        if prev == None: tile = fl.Tile(prev, next)
        else: tile = fl.Tile([prev], next)

        if prev == None or next == None: tile.terminal = True
        new_tiles[get_tag(x,y)] = tile

        if prev == 'N':
            tile.tile_to_N = new_tiles[get_tag(x,y-TILE_SIZE*2)] 
            new_tiles[get_tag(x,y-TILE_SIZE*2)].tile_to_S = tile

            tile.N = 'N' 
        if prev == 'E':
            tile.tile_to_E = new_tiles[get_tag(x+TILE_SIZE*2,y)] 
            new_tiles[get_tag(x+TILE_SIZE*2,y)].tile_to_W = tile

            tile.E = 'N' 
        if prev == 'W':
            tile.tile_to_W = new_tiles[get_tag(x-TILE_SIZE*2,y)] 
            new_tiles[get_tag(x-TILE_SIZE*2,y)].tile_to_E = tile

            tile.W = 'N' 
        if prev == 'S':
            tile.tile_to_S = new_tiles[get_tag(x,y+TILE_SIZE*2)] 
            new_tiles[get_tag(x,y+TILE_SIZE*2)].tile_to_N = tile

            tile.S = 'N' 

        if next != None: 
            for d in next: 
                if d == 'N': tile.N = 'N'
                if d == 'E': tile.E = 'N'
                if d == 'W': tile.W = 'N'
                if d == 'S': tile.S = 'N'

        if [x,y] == origin_tile_cords: 
            seed_tile = tile
            tile.original_seed = True
            if len(tile.next) > 1: tile.terminal = False

    # Decide key tiles:
    ktn, kte, ktw, kts = None, None, None, None

    for cord in new_tiles:
        [x,y] = cord.split(',')
        x, y = int(x), int(y)

        if (x == min_x and get_tag(max_x, y) in new_tiles) or (x == max_x and get_tag(min_x, y) in new_tiles):
            if [x,y] == origin_tile_cords: ktw, kte = new_tiles[get_tag(min_x, y)], new_tiles[get_tag(max_x, y)]
            elif ktw == None and kte == None: ktw, kte = new_tiles[get_tag(min_x, y)], new_tiles[get_tag(max_x, y)]
        if (y == min_y and get_tag(x, max_y) in new_tiles) or (y == max_y and get_tag(x, min_y) in new_tiles):
            if [x,y] == origin_tile_cords: ktn, kts = new_tiles[get_tag(x, min_y)], new_tiles[get_tag(x, max_y)]
            elif ktn == None and kts == None: ktn, kts = new_tiles[get_tag(x, min_y)], new_tiles[get_tag(x, max_y)]
    ktn.key_tile_N = None
    kte.key_tile_E = None
    ktw.key_tile_W = None
    kts.key_tile_S = None

    # North
    visited_tiles = []
    stack = deque()
    stack.append(ktn)
    while len(stack) > 0:
        cur_tile = stack.pop()
        visited_tiles.append(cur_tile)

        if cur_tile.next != None:
            for n in cur_tile.next: 
                adj_tile = fl.retrieve_tile(cur_tile, n)
                if adj_tile not in visited_tiles:
                    adj_tile.key_tile_N = [fl.opp(n)]
                    stack.append(adj_tile)

        if cur_tile.previous != None:
            for n in cur_tile.previous: 
                adj_tile = fl.retrieve_tile(cur_tile, n)
                if adj_tile not in visited_tiles:
                    adj_tile.key_tile_N = [fl.opp(n)]
                    stack.append(adj_tile)

    # East
    visited_tiles = []
    stack = deque()
    stack.append(kte)
    while len(stack) > 0:
        cur_tile = stack.pop()
        visited_tiles.append(cur_tile)

        if cur_tile.next != None:
            for n in cur_tile.next: 
                adj_tile = fl.retrieve_tile(cur_tile, n)
                if adj_tile not in visited_tiles:
                    adj_tile.key_tile_E = [fl.opp(n)]
                    stack.append(adj_tile)

        if cur_tile.previous != None:
            for n in cur_tile.previous: 
                adj_tile = fl.retrieve_tile(cur_tile, n)
                if adj_tile not in visited_tiles:
                    adj_tile.key_tile_E = [fl.opp(n)]
                    stack.append(adj_tile)

    # West
    visited_tiles = []
    stack = deque()
    stack.append(ktw)
    while len(stack) > 0:
        cur_tile = stack.pop()
        visited_tiles.append(cur_tile)

        if cur_tile.next != None:
            for n in cur_tile.next: 
                adj_tile = fl.retrieve_tile(cur_tile, n)
                if adj_tile not in visited_tiles:
                    adj_tile.key_tile_W = [fl.opp(n)]
                    stack.append(adj_tile)

        if cur_tile.previous != None:
            for n in cur_tile.previous: 
                adj_tile = fl.retrieve_tile(cur_tile, n)
                if adj_tile not in visited_tiles:
                    adj_tile.key_tile_W = [fl.opp(n)]
                    stack.append(adj_tile)

    # South
    visited_tiles = []
    stack = deque()
    stack.append(kts)
    while len(stack) > 0:
        cur_tile = stack.pop()
        visited_tiles.append(cur_tile)

        if cur_tile.next != None:
            for n in cur_tile.next: 
                adj_tile = fl.retrieve_tile(cur_tile, n)
                if adj_tile not in visited_tiles:
                    adj_tile.key_tile_S = [fl.opp(n)]
                    stack.append(adj_tile)

        if cur_tile.previous != None:
            for n in cur_tile.previous: 
                adj_tile = fl.retrieve_tile(cur_tile, n)
                if adj_tile not in visited_tiles:
                    adj_tile.key_tile_S = [fl.opp(n)]
                    stack.append(adj_tile)

    return seed_tile

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
        self.stages = 1

        for F in (draw_seed, choose_origin, select_stages):
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
            seed_tile = create_seed(self.tile_positions, self.origin_tile)

            # Run simulation
            [seed_tile, states, transitions, affinities, original_seed_tile] = fl.run_simulation(seed_tile, self.stages)

            # Output XML file
            g.generate_xml_file(states, transitions, affinities, original_seed_tile)

            # Plot the result onto graph
            fl.plot_graph(seed_tile)
            self.destroy()

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
            [valid, error] = check_valid_seed(controller.tile_positions)

            if valid:
                controller.update_frame(choose_origin)
                controller.show_frame(choose_origin)
            else: 
                tk.messagebox.showinfo("Invalid seed", error)

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

                controller.origin_tile = [x, y]
        
        canvas.bind("<Button-1>", choosing_tile)

        def display_number_stages(): 
            if controller.origin_tile != None:
                controller.update_frame(select_stages)
                controller.show_frame(select_stages)

        button = tk.Button(self, text="Done",
                            command=display_number_stages)
        button.pack()

class select_stages(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text = "Select the number of stages to complete.")
        label.pack()

    def update(self, controller):
        # Add the options
        options = []
        num_tiles = len(controller.tile_positions)
        stage = 1
        actual_stage = 1

        while num_tiles < 30000:
            v = str(stage) + " - (stage: %s)" % actual_stage
            options.append(v)
            num_tiles *= num_tiles
            stage += 1
            actual_stage *= 2

        # Stores value selected
        var = tk.StringVar(controller)
        var.set(options[0])

        drop_down = tk.OptionMenu(self, var, *options)
        drop_down.pack()

        def finish():
            s = var.get().split(' ')
            controller.stages = int(s[0])
            controller.finish()

        button = tk.Button(controller, text="Done", command=finish)
        button.pack()

app = main()
app.geometry('1000x625')
app.title('Fractals in Seeded TA')
app.mainloop()