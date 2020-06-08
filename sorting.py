from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort          #importing from other python files in which the necessary algorithms are written
from insertionSort import insertion_sort
from mergeSort import merge_sort

root = Tk()
root.title('Sorting Visualizer')
root.maxsize(1100,1100)
root.config(bg = 'black')

#valriables
selected_alg = StringVar()
data = []

def drawData(data, colorArray):
    canvas.delete('all')
    c_height = 580
    c_width = 1000
    x_width = c_width / (len(data)+1)  #setting the width of each rectangle according to canvas width and no. of rectangles
    normalisedData = [i / max(data) for i in data]
    
    for i,height in enumerate(normalisedData):
        #top left
        x0 = i * x_width 
        y0 = c_height - height * 540
        #bottom right
        x1 = (i+1) * x_width 
        y1 = c_height

        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i]) #drawing the rectangles and filling with color
    
    root.update_idletasks()

def Generate():
    global data
    #minVal = int(MinEntry.get()) 
    #maxVal = int(MaxEntry.get())
    size  = int(sizeEntry.get())

    data = []

    for _ in range(size):                       
        data.append(random.randrange(1,size))           #generating reguired amount of graphs randomly by entering required size

    drawData(data, ['red' for x in range(len(data))]) # making all red [red,red,red]

def startAlgorith():
    global data
    #Calling the necessary algorith
    if alg_menu.get() == 'BubbleSort':
        bubble_sort(data, drawData, speedScale.get())
    
    elif alg_menu.get() == 'InsertionSort':
        insertion_sort(data, drawData, speedScale.get())

    elif alg_menu.get() == 'MergeSort':
        merge_sort(data, drawData, speedScale.get())


#frame and base layout
UI_frame = Frame(root,width=1000,height=300,bg='grey')
UI_frame.grid(row=0,column=0,padx=10,pady=5)

canvas = Canvas(root,width=1000,height=580,bg='white')
canvas.grid(row=1,column=0,padx=10,pady=5)

#user interface area / setting the scales in UI_frame
#Row - 0

speedScale = Scale(UI_frame,from_=0.01 ,to=1.0, length= 200, digits=3, resolution=0.01, orient = HORIZONTAL,label='Select Speed [s]')
speedScale.grid(row =0,column=2,padx=5,pady=5)

Button(UI_frame,text='Start',bg='red',command= startAlgorith).grid(row=0,column=3,padx=5,pady=5)

Label(UI_frame,text='Algorithm',bg='grey').grid(row = 0,column=0,padx=5,pady=5,sticky=W)
alg_menu = ttk.Combobox(UI_frame,textvariable = selected_alg, values = ['BubbleSort','InsertionSort', 'MergeSort'])
alg_menu.grid(row=0,column=1,padx=5,pady=5)
alg_menu.current(0)


#Row - 1
sizeEntry = Scale(UI_frame,from_=3 ,to=500, resolution=1,length=200, orient = HORIZONTAL,label='Data Size')
sizeEntry.grid(row = 1,column=0,padx=5,pady = 5)
'''
MinEntry = Scale(UI_frame,from_=1 ,to=10, resolution=1, orient = HORIZONTAL,label='Minimum Value')
MinEntry.grid(row = 1,column=1,padx=5,pady = 5)                                                   #if you want minval and maxval scale uncomment this

MaxEntry = Scale(UI_frame,from_=10 ,to=100, resolution=1, orient = HORIZONTAL,label='Maximum Value')
MaxEntry.grid(row = 1,column=2,padx=5,pady = 5)
'''
Button(UI_frame,text='Generate',bg='white',command= Generate).grid(row=1,column=3,padx=5,pady=5)





root.mainloop()
