# This program is written by Python3
# coding : UTF-8
# developer : Masazumi Katoh
# filename : GraphViewer_Ver.1.0.0.py
# last update : 2017/11/02
# version : 1.0.0

from tkinter import *
from tkinter import ttk
#import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# initial setting of matplotlib
font = {'family':'monospace', 'size':'9'}
mpl.rc('font', **font)

#  class of realtime plot
class realtime_plot(object):

	# define __init__
	def __init__(self):
		self.fig = plt.figure(figsize = (12, 8))
		self.initialize()

	def initialize(self):
		self.fig.suptitle("Monitoring of environment", size = 12)
		self.fig.grid(True)

# create main frame
root = Tk()
root.title("Graph Viewer Ver.1.0.0")
frame1 = ttk.Frame(root)
label1 = ttk.Label(frame1, text = "Sampling Rate")

root.mainloop()
