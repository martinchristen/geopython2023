# Workshop GeoPython 2023

## Geospatial Data Processing in Python

In this workshop, you will learn about the various Python modules for processing geospatial data, including GDAL, Rasterio, Pyproj, Shapely, Folium, Fiona, OSMnx, Libpysal, Geopandas, Pydeck, Whitebox, ESDA, and Leaflet. You will gain hands-on experience working with real-world geospatial data and learn how to perform tasks such as reading and writing spatial data, reprojecting data, performing spatial analyses, and creating interactive maps. This tutorial is suitable for beginners as well as intermediate Python users who want to expand their knowledge in the field of geospatial data processing

Installation:

    conda create --name geopython39 python=3.9 jupyterlab -y

    conda activate geopython39
    
    conda install gdal rasterio matplotlib geopandas -y
    conda install geoplot folium osmnx folium -c conda-forge -y   

Do this everytime from now on:

    (You can ommit the notebook-dir or set to another path.)

    conda activate geopython39
    jupyter lab --notebook-dir C:\notebooks
    
    
