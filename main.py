import tkinter as tk 
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from genetic import Genetic

fig, ax = plt.subplots()
maxFitness = 0
def execute() :
    populationCount = int(popEntry.get()) 
    if populationCount % 2 == 1:
        populationCount += 1
    genetic = Genetic(
        n = int(nEntry.get()) , 
        populationCount= populationCount,
        csrate= float(csoverEntry.get()),
        mrrate= float(MREntry.get()),
        elitrate= float(EREntry.get()),
        generations= int(genEntry.get()),
        tourSize = int(tourEntry.get())
        )
    solution = genetic.solution()
    print(solution)
    # maxFitness = genetic.maxFitness
    Resultlbl.config(text=solution)
    print("Avg: " , genetic.getAvg())
    print("Best: " , genetic.getBOG())
    plot_array(genetic.getBOG() , genetic.getAvg())
    genetic.clearBOG()
    genetic.clearAvg()
    print("---\t---\t---\t---\t---")

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

nlbl = tk.Label(root , text="N:")
nlbl.grid(row=1 , column=0)

nEntry = tk.Entry(root)
nEntry.insert(0, '15')
nEntry.grid(row=1 , column=1)

poplbl = tk.Label(root , text="Population")
poplbl.grid(row= 2 , column= 0)

popEntry = tk.Entry(root)
popEntry.insert(0, '500')
popEntry.grid(row= 2 , column= 1)

csoverlbl = tk.Label(root , text="CrossOver Rate")
csoverlbl.grid(row= 3 , column= 0)

csoverEntry = tk.Entry(root)
csoverEntry.insert(0, '0.7')
csoverEntry.grid(row=3 , column=1)

MRlbl = tk.Label(root , text="Mutation Rate")
MRlbl.grid(row = 4 , column= 0)

MREntry = tk.Entry(root)
MREntry.insert(0, '0.2')
MREntry.grid(row=4 , column=1)

ERlbl = tk.Label(root , text="Elitisim Rate")
ERlbl.grid(row=5 , column=0)

EREntry = tk.Entry(root)
EREntry.insert(0, '0.02')
EREntry.grid(row=5 , column=1)

genlbl = tk.Label(root , text="Generations")
genlbl.grid(row=6 , column=0)

genEntry = tk.Entry(root)
genEntry.insert(0, '100')
genEntry.grid(row=6 , column=1)

tourlbl = tk.Label(root , text="tournament size")
tourlbl.grid(row=7 , column=0)

tourEntry = tk.Entry(root)
tourEntry.insert(0, '20')
tourEntry.grid(row=7 , column=1)

Execbtn = tk.Button(root , text="Execute" , command=execute , pady=10)
Execbtn.grid(row=8 , columnspan=2)

canvas = FigureCanvasTkAgg(figure=fig , master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=3, columnspan=1, rowspan=8 , padx=10 , pady=10)

Resultlbl = tk.Label(root , text="Results" , height=5 , wraplength=500)
Resultlbl.grid(row=9 , column=3 ,  columnspan=1)
# Configure row and column weights to make the cells expand with the window
for i in range(10):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
