import tkinter as tk 
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from genetic import Genetic

fig, ax = plt.subplots()
maxFitness = 0
def execute() :
    genetic = Genetic(
        n = int(nEntry.get()) , 
        populationCount= int(popEntry.get()),
        csrate= float(csoverEntry.get()),
        mrrate= float(MREntry.get()),
        elitrate= float(EREntry.get()),
        generations= int(genEntry.get()))
    solution = genetic.solution()
    print(genetic.solution())
    # maxFitness = genetic.maxFitness
    Resultlbl.config(text=solution)
    print("Avg: " , genetic.getAvg())
    plot_array(genetic.getBOG() , genetic.getAvg())
    genetic.clearBOG()
    genetic.clearAvg()

def plot_array(best , avg):
    ax.clear()
    ax.plot(best , 'b.-' , label="best")
    ax.plot(avg , 'g.--' , label="average")
    # ax.set_ylim(maxFitness, maxFitness/2)
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.set_title("Best of Generations")
    ax.set_xlabel("Generation")
    ax.set_ylabel("Fitness")
    canvas.draw()

root = tk.Tk()
root.geometry("1024x600")
root.title("8-Queen Solver")

greeting = tk.Label(root , text="N-Queen Solver" ,
font="Monospace 18 bold" ,
)
greeting.grid(row=0 , columnspan=2)

codedBy = tk.Label(text="coded by Mohsen Farajollahi" ,
font="Monospace 12 " ,
fg="grey"
)
codedBy.grid(row=1 , columnspan=2)

nlbl = tk.Label(root , text="N:")
nlbl.grid(row=2 , column=0)

nEntry = tk.Entry(root)
nEntry.insert(0, '8')
nEntry.grid(row=2 , column=1)

poplbl = tk.Label(root , text="Population")
poplbl.grid(row= 3 , column= 0)

popEntry = tk.Entry(root)
popEntry.insert(0, '150')
popEntry.grid(row= 3 , column= 1)

csoverlbl = tk.Label(root , text="CrossOver Rate")
csoverlbl.grid(row= 4 , column= 0)

csoverEntry = tk.Entry(root)
csoverEntry.insert(0, '0.7')
csoverEntry.grid(row=4 , column=1)

MRlbl = tk.Label(root , text="Mutation Rate")
MRlbl.grid(row = 5 , column= 0)

MREntry = tk.Entry(root)
MREntry.insert(0, '0.2')
MREntry.grid(row=5 , column=1)

ERlbl = tk.Label(root , text="Elitisim Rate")
ERlbl.grid(row=6 , column=0)

EREntry = tk.Entry(root)
EREntry.insert(0, '0.05')
EREntry.grid(row=6 , column=1)

genlbl = tk.Label(root , text="Generations")
genlbl.grid(row=7 , column=0)

genEntry = tk.Entry(root)
genEntry.insert(0, '1000')
genEntry.grid(row=7 , column=1)

Execbtn = tk.Button(root , text="Execute" , command=execute)
Execbtn.grid(row=8 , columnspan=2)

Resultlbl = tk.Label(root , text="Results")
Resultlbl.grid(row=9 , columnspan=2)

canvas = FigureCanvasTkAgg(figure=fig , master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=3, columnspan=1, rowspan=8 , padx=10 , pady=10)

# Configure row and column weights to make the cells expand with the window
for i in range(9):
    root.grid_rowconfigure(i, weight=1)
for j in range(2):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
