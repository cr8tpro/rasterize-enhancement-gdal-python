#02-03-2020
#Bojan Stojanovic

#Used builtin gdal function and execute using os.system because
#all gdal functions were built with C++ to enhance speed and memory management
#On Windows, install osgeo4w and on Linux/Ubuntu, install GDAL package using pip
#Then gdal builtin functions can be used at any projects
#or you can use gdaltest.runexternal method

import os

from osgeo import gdal
from osgeo import ogr
from osgeo import osr
import gdaltest
import test_cli_utilities
import pytest

#assume small tiff files are generated using multithreading - implemented on your side
#if it's not implemented, I recommend thread or threading module of Python

#import threading
"""
class myThread (threading.Thread):
    def __init__(self, threadID, fileHandler):
        threading.Thread.__init__(self)
        self.threadID = threadID
        ...
    def generate_tiff():
	fileHandler.write(tiffFileName + '\n');
	...
    def run(self):
	generate_tiff();


fileHandler = open("source_filenames.txt", "w+")
for i in tiffs_count:
    thread = myThread(i, fileHandler)
    thread.start()
    
fileHandler.close()
"""

#assume tiff files are generated to /source directory
def generate_vrt():
    if test_cli_utilities.get_gdalbuildvrt_path() is None:
	pytest.skip()

    gdaltest.runexternal(test_cli_utilities.get_gdalbuildvrt_path() + ' -input_file_list ./source_filenames.txt ./merged_mosaic.vrt')

def generate_tiff():
    if test_cli_utilities.get_gdal_translate_path() is None:
	pytest.skip()

    gdaltest.runexternal(test_cli_utilities.get_gdal_translate_path() + ' params in doc ' + './merged.vrt ./merged.tif')
    
# or you can use os.system for executing gdalbuildvrt and gdal_translate builtin commands.