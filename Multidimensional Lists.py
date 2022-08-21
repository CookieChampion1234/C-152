from tkinter import*
root=Tk()
root.title("Multidimensions Arrays")

root.geometry("500x500")
label=Label(root)

array_1d = ["John", "James", "Thomson"]
print(array_1d[1])

array_2d = [["John", "A"],["James", "B"],["Thomson", "C"]]
print(array_2d[1][1])

array_3d = [[["John", "A", "Excellent"],["James", "B", "Good"],["Thomson", "C", "Okay"]]]
print(array_3d[0][1][2])

def report():
    label['text'] = array_3d[0][1][0] + " got a grade of " + array_3d[0][1][1] + " and he is doing "  + array_3d[0][1][2]
    
btn = Button(text="Show Report", command=report)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()