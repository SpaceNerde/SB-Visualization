import tkinter as tk

# ITS HARDCODING TIME BITCHES

class Legend(tk.Frame):
    def __init__(self, root, *args):
        super().__init__(root, *args)
        
        # placeholder
        e_1_1 = tk.Entry(self)
        e_1_1.insert(0, "des")
        e_1_1.grid(row=0, column=0)

        e_1_2 = tk.Entry(self, width=50)
        e_1_2.insert(0, "designation")
        e_1_2.grid(row=0, column=1)

        # placeholder
        e_2_1 = tk.Entry(self)
        e_2_1.insert(0, "h")
        e_2_1.grid(row=1, column=0)

        e_2_2 = tk.Entry(self, width=50)
        e_2_2.insert(0, "absolute magnitude")
        e_2_2.grid(row=1, column=1)

        # placeholder
        e_3_1 = tk.Entry(self)
        e_3_1.insert(0, "t_sigma_f ")
        e_3_1.grid(row=2, column=0)

        e_3_2 = tk.Entry(self, width=50)
        e_3_2.insert(0, "close-approach time")
        e_3_2.grid(row=2, column=1)

        # placeholder
        e_4_1 = tk.Entry(self)
        e_4_1.insert(0, "v_inf (km/s)")
        e_4_1.grid(row=3, column=0)

        e_4_2 = tk.Entry(self, width=50)
        e_4_2.insert(0, "velocity relative to a massless body")
        e_4_2.grid(row=3, column=1)

        # placeholder
        e_5_1 = tk.Entry(self)
        e_5_1.insert(0, "v_rel (km/s)")
        e_5_1.grid(row=4, column=0)

        e_5_2 = tk.Entry(self, width=50)
        e_5_2.insert(0, "velocity relative to the approach body at close approach")
        e_5_2.grid(row=4, column=1)

        # placeholder
        e_6_1 = tk.Entry(self)
        e_6_1.insert(0, "dist")
        e_6_1.grid(row=5, column=0)

        e_6_2 = tk.Entry(self, width=50)
        e_6_2.insert(0, "nominal approach distance")
        e_6_2.grid(row=5, column=1)

        # placeholder
        e_7_1 = tk.Entry(self)
        e_7_1.insert(0, "cd")
        e_7_1.grid(row=6, column=0)

        e_7_2 = tk.Entry(self, width=50)
        e_7_2.insert(0, "time of close-approach")
        e_7_2.grid(row=6, column=1)

        # placeholder
        e_8_1 = tk.Entry(self)
        e_8_1.insert(0, "jd")
        e_8_1.grid(row=7, column=0)

        e_8_2 = tk.Entry(self, width=50)
        e_8_2.insert(0, "time of close-approach")
        e_8_2.grid(row=7, column=1)

        # placeholder
        e_9_1 = tk.Entry(self)
        e_9_1.insert(0, "orbit_id")
        e_9_1.grid(row=8, column=0)

        e_9_2 = tk.Entry(self, width=50)
        e_9_2.insert(0, "orbit ID for close-approach")
        e_9_2.grid(row=8, column=1)