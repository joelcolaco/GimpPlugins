#!/usr/bin/env python
import os
from gimpfu import *
def run(sourceFolder, outputFolder, gridColor, dpi, lineThickness):

    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    filenames = [f for f in os.listdir(sourceFolder) if os.path.isfile(os.path.join(sourceFolder, f))]
    for filename in filenames:
        sourceFile = os.path.join(sourceFolder, filename)
        outputFileName = "Grid_" + filename
        outputFile = os.path.join(outputFolder, outputFileName)
        image = loadImage(sourceFile)
        addGrid(image, gridColor, dpi, lineThickness)
        if isJPEG(sourceFile):
            saveImage(outputFile, image)
        elif isPNG(sourceFile):
            savePngImage(outputFile, image)

def loadImage(sourceFile):
    if isJPEG(sourceFile):
        return pdb.file_jpeg_load(sourceFile, sourceFile)
    if isPNG(sourceFile):
        return pdb.file_png_load(sourceFile, sourceFile)

def addGrid(image, gridColor, dpi, lineThickness):
    layer = image.active_layer
    pdb.plug_in_grid(image, layer, lineThickness, dpi, 0, gridColor, 255, lineThickness, dpi, 0, gridColor, 255, 0, 0, 0, gridColor, 255)

def saveImage(outputFile, image):
    drawable = pdb.gimp_image_get_active_drawable(image)
    pdb.gimp_file_save(image, drawable, outputFile, '?')

def savePngImage(outputFile, image):
    drawable = pdb.gimp_image_get_active_drawable(image)
    pdb.file_png_save(image, drawable, outputFile, '?',0, 6, 0, 0, 0, 0, 0)

def isJPEG(sourceFile):
	if sourceFile.count('.jpg') > 0:
		return True
	else:
		return False
def isPNG(sourceFile):
	if sourceFile.count('.png') > 0:
		return True
	else:
		return False

def add_grid_script(customtext, font, size):
  img = gimp.Image(1, 1, RGB)
  layer = pdb.gimp_text_fontname(img, None, 0, 0, customtext, 10, True, size, PIXELS, font)
  img.resize(layer.width, layer.height, 0, 0)
  gimp.Display(img)
  gimp.displays_flush()
register(
 "python_fu_add_grid",
 "Process files in the specified folder and add a grid to them  ",
 "Process files in the specified folder and add a grid to them  ",
 "Joel Colaco",
 "Joel Colaco",
 "2021",
 "Generate Grids",
 "",
 [
 (PF_DIRNAME, "sourceFolder", "Source directory", "C:\Temp\Source"),
 (PF_DIRNAME, "outputFolder", "Output directory", "C:\Temp\Output"),
 (PF_COLOR, "gridColor", "select a color:", (0, 0, 0) ),
 (PF_INT32, "dpi", "DPI", 70),
 (PF_INT32, "lineThickness", "Grid Thickness", 1) 
 ],
 [],
 run, menu="<Image>/File/Create")
main()
