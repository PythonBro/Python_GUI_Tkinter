from tkinter import *

# Windowを作成
root = Tk()
# Canvasを貼り付け
cv = Canvas(root, width = 600, height = 400)
cv.pack()

# draw rectangle
# cv.create_rectangle(x_start, y_start, x_end, y_end, fill = "color")
cv.create_rectangle(50, 150, 150, 250, fill = "red")
cv.create_rectangle(320, 270, 370, 320, fill = "green")

# draw line
# cv.create_line(x_start, y_start, x_end, y_end, fill = "color", width = "px")
cv.create_line(10, 90, 580, 90, fill = "blue", width = 5)
cv.create_line(90, 10, 90, 380, fill = "blue", width = 5)

root.mainloop()
