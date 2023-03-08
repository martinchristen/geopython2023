###############################################################################
#### Collection of useful functions
####
#### Licensed under MIT License
###############################################################################
#
# Copyright (c) 2023 Martin Christen, martin.christen@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###############################################################################

from urllib.request import urlopen
import os
import sys
import json
 
######## shortcut for downloads ###################################################################
geodata = {"natural-earth": "http://naciscdn.org/naturalearth/packages/natural_earth_vector.gpkg.zip",
           "natural-earth-raster-shaded": "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/raster/NE1_HR_LC_SR_W_DR.zip",
           "landsat-ch-25": "https://data.geo.admin.ch/ch.swisstopo.images-landsat25/data.zip",
           "swissimage-25": "https://data.geo.admin.ch/ch.swisstopo.swissimage-25/data.zip",
           "geonames": "https://download.geonames.org/export/dump/cities500.zip",
           "bluemarble-jp2": "https://data.geopython.xyz/bluemarble/world.jp2",
           "BFS": "https://www.bfs.admin.ch/bfsstatic/dam/assets/11947559/master",
           "ourairports": "https://ourairports.com/data/airports.csv"}
###################################################################################################

def download(url, destfile, overwrite=True):
    print("Downloading", destfile, "from", url)

    if os.path.exists(destfile) and not overwrite:
        print("File already exists, not overwriting.")
        return
    
    response = urlopen(url) 
    info = response.info()
    cl = info["Content-Length"]
    
    if cl != None:
        filesize = int(cl)
        currentsize = 0
        
        with open(destfile, 'wb') as f:
            while True:
                chunk = response.read(16*1024)
                currentsize += len(chunk)
                
                if not chunk:
                    break
                f.write(chunk)
                percent = int(100*currentsize/filesize)
                
                bar = "*"*(percent)
                bar += "-"*((100-percent))
                print('\r{}% done \t[{}]'.format(percent, bar), end='')
        print("")
        
    else:
        print("Downloading please wait... (filesize unknown)")
        with open(destfile, 'wb') as f:
            while True:
                chunk = response.read(16*1024)
                if not chunk:
                    break
                f.write(chunk)
                
#------------------------------------------------------------------------------
# Convert a OpenStreetMap Polygon JSON to GeoJSON
# just a quick hack
def osm2geojson(s):
    geojson = {
        "type": "Feature",
        "geometry" : {},
        "properties": {},
    }
    data = json.loads(s)
    
    for key in data:
        if key == "geojson":
            geojson["geometry"] = data["geojson"]
        else:
            d = geojson["properties"]
            d[key] = data[key]
    
    return json.dumps(geojson)
#------------------------------------------------------------------------------
# Fix DLL/so path in notebooks. This is required sometimes, but not often...
# For proj4 we need to set the PROJ_LIB path manually
# Bug: https://github.com/jupyter/notebook/issues/4569


def fixenv():
    os.environ['PATH'] = os.path.split(sys.executable)[0] + "/Library/bin" + os.pathsep + os.environ['PATH'] 
    
    if 'PROJ_LIB' not in os.environ:
        os.environ['PROJ_LIB'] =  os.path.split(sys.executable)[0] + "/library/share/proj"
        os.environ['GDAL_DATA'] = os.path.split(sys.executable)[0] + "/../../../share/gdal/"


#------------------------------------------------------------------------------

