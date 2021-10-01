#!/usr/bin/env python
import os
from gimpfu import *
def run(sourceFolder, outputFolder):

    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    filenames = [f for f in os.listdir(sourceFolder) if os.path.isfile(os.path.join(sourceFolder, f))]
    for filename in filenames:
        sourceFile = os.path.join(sourceFolder, filename)
        outputFile = os.path.join(outputFolder, filename)
        image = loadImage(sourceFile)
        saveImage(outputFile, image)	

def loadImage(sourceFile):
    if isJPEG(sourceFile):
        return pdb.file_jpeg_load(sourceFile, sourceFile)
    if isPNG(sourceFile):
        return pdb.file_png_load(sourceFile, sourceFile)

def saveImage(outputFile, image):
    drawable = pdb.gimp_image_get_active_drawable(image)
    if isJPEG(outputFile):
		pdb.gimp_file_save(image, drawable, outputFile, '?')
    if isPNG(outputFile):
        pdb.gimp_file_save(image, drawable, outputFile, '?')

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
 "python_test2",
 "TEST2",
 "TEST2",
 "Brad Jones",
 "Brad Jones",
 "2017",
 "TEST2",
 "",
 [
 (PF_DIRNAME, "sourceFolder", "Source directory", "C:\Users\jcolaco\Pictures\Python Test\Source"),
 (PF_DIRNAME, "outputFolder", "Output directory", "C:\Users\jcolaco\Pictures\Python Test\Out")
 ],
 [],
 run, menu="<Image>/File/Create")
main()