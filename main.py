import tkinter as tk
from PIL import Image, ImageTk
from random import choice
import os
import itertools

root = tk.Tk()
size = (500, 711) # Changing this tuple will modify both the image size and the window size together
gif_file = 'gifs_2'
# Browse directory containing images to stitch together
file_list = os.listdir(gif_file)
file_list.sort() # Will be unordered unless sorted



images = [i for i in file_list]
images = iter(images) # iterator
images = itertools.cycle(images) # repeates iteration loop endlessly


# Main application window

class Application(tk.Frame):
	
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.title('都好')
		self.pack()	
		self.create_widgets()
		self.next_img()
		self.update()
		
	def next_img(self):
		"""
		Iterate through images

		"""
		try:
			img = next(images)
		except StopIteration:
			return


		img = Image.open(f'{gif_file}/{img}')
		img = img.resize(size)
		img = ImageTk.PhotoImage(img)
		self.bg.img = img
		self.bg['image'] = img

		
	def create_widgets(self):
		"""
		This method is called to populate the window upon startup

		"""
		self.bg = tk.Label(self)
		self.bg.pack()
		

	def update(self):
		"""
		Queue a call to this method, which in turn calls the next_img method to iterate through the gif

		"""
		self.next_img()
		root.after(25, self.update)

		


app = Application(master=root)
root.geometry(f'{size[0]}'+'x'+f'{size[1]}')
root.resizable(0,0)
app.mainloop()