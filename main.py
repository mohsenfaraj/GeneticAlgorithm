import tkinter as tk 

from genetic import Genetic
def execute() :
    genetic = Genetic(
    populationCount= int(popEntry.get()),
    csrate= float(csoverEntry.get()),
    mrrate= float(MREntry.get()),
    elitrate= float(EREntry.get()),
    generations= int(genEntry.get())
    )
    solution = genetic.solution()
    Resultlbl.config(text=solution)


root = tk.Tk()
root.geometry("600x500")
root.title("8-Queen Solver")

greeting = tk.Label(root , text="8-Queen Solver" ,
font="Monospace 18 bold" ,
)
greeting.grid(row=0 , columnspan=2)

codedBy = tk.Label(text="coded by Mohsen Farajollahi" ,
font="Monospace 12 " ,
fg="grey"
)
codedBy.grid(row=1 , columnspan=2)

poplbl = tk.Label(root , text="Population")
poplbl.grid(row= 2 , column= 0)

popEntry = tk.Entry(root)
popEntry.grid(row= 2 , column= 1)

csoverlbl = tk.Label(root , text="CrossOver Rate")
csoverlbl.grid(row= 3 , column= 0)

csoverEntry = tk.Entry(root)
csoverEntry.grid(row=3 , column=1)

MRlbl = tk.Label(root , text="Mutation Label")
MRlbl.grid(row = 4 , column= 0)

MREntry = tk.Entry(root)
MREntry.grid(row=4 , column=1)

ERlbl = tk.Label(root , text="Elitisim Rate")
ERlbl.grid(row=5 , column=0)

EREntry = tk.Entry(root)
EREntry.grid(row=5 , column=1)

genlbl = tk.Label(root , text="Generations")
genlbl.grid(row=6 , column=0)

genEntry = tk.Entry(root)
genEntry.grid(row=6 , column=1)

Execbtn = tk.Button(root , text="Execute" , command=execute)
Execbtn.grid(row=7 , columnspan=2)

Resultlbl = tk.Label(root , text="Results")
Resultlbl.grid(row=8 , columnspan=2)

# Configure row and column weights to make the cells expand with the window
for i in range(9):
    root.grid_rowconfigure(i, weight=1)
for j in range(2):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
