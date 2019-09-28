from PIL import ImageGrab
import win32com.client as win32
import os
import subprocess

def fetch(c):
	excel = win32.gencache.EnsureDispatch('Excel.Application')
	workbook = excel.Workbooks.Open(r'C:\\Users\\Subham Banerjee\\Desktop\\project\\project_sheet.xlsx')

	for sheet in workbook.Worksheets:
	    for i, shape in enumerate(sheet.Shapes):
	        if shape.Name.startswith('Picture'):
	            shape.Copy()
	            image = ImageGrab.grabclipboard()
	            c += 1
	            image.save('{}.jpg'.format(i+1), 'jpeg')
	move()
	delete(c)    
def delete(c):
	for i in range(c):
		os.remove(str(i+1)+".jpg")

def move():
	os.system("ffmpeg -r 0.75 -i %d.jpg -vcodec mpeg4 -y movie.mp4")
if __name__ == '__main__':
	c = 0
	fetch(c)
	       
      