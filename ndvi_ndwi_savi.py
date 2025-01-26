# -*- coding: utf-8 -*-
"""NDVI_NDWI_SAVI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ar6Umed9ZGqGdfnsd7YaU5tQBI87X3jM
"""

import geemap.geemap as gm
import ee
import folium

ee.Authenticate()
ee.Initialize(project='bha5vya')

# maps
map1 = gm.Map()
map2 = gm.Map()
map3 = gm.Map()



area_of_interest = ee.FeatureCollection('projects/bha5vya/assets/Trivandrum')

# Adding the study area to the maps
map1.addLayer(area_of_interest, {}, 'Area of Interest')
map2.addLayer(area_of_interest, {}, 'Area of Interest')
map3.addLayer(area_of_interest, {}, 'Area of Interest')

# Centering the maps on the study area
map1.centerObject(area_of_interest, 9)
map2.centerObject(area_of_interest, 9)
map3.centerObject(area_of_interest, 9)



image_1985 = ee.ImageCollection("LANDSAT/LT05/C02/T1").filterDate('1985-01-01', '1985-12-31').filterMetadata('CLOUD_COVER', 'less_than', 5).mean().clip(area_of_interest)  # For 1985

image_1990 = ee.ImageCollection("LANDSAT/LT05/C02/T1").filterDate('1990-01-01', '1990-12-31').filterMetadata('CLOUD_COVER', 'less_than', 5).mean().clip(area_of_interest)  # For 1990

image_2000 = ee.ImageCollection("LANDSAT/LE07/C02/T1").filterDate('2000-01-01', '2000-12-31').filterMetadata('CLOUD_COVER', 'less_than', 5).mean().clip(area_of_interest)  # For 2000

image_2010 = ee.ImageCollection("LANDSAT/LE07/C02/T1").filterDate('2010-01-01', '2010-12-31').filterMetadata('CLOUD_COVER', 'less_than', 5).mean().clip(area_of_interest)  # For 2010

image_2020 = ee.ImageCollection("LANDSAT/LC08/C02/T1").filterDate('2020-01-01', '2020-12-31').filterMetadata('CLOUD_COVER', 'less_than', 5).mean().clip(area_of_interest)  # For 2020

image_2024 = ee.ImageCollection("LANDSAT/LC09/C02/T1").filterDate('2024-01-01', '2024-12-31').filterMetadata('CLOUD_COVER', 'less_than', 5).mean().clip(area_of_interest)  # For 2024

# Define a custom NDVI color palette
ndvi_palette = ['#8B4513', '#9A5120', '#A9602D', '#B8703A', '#C58047', '#D49055', '#E3A063', '#E9B081', '#EEC09F', '#F3D0BD', '#F8E0DB', '#FCF0F9', '#FCF3E1', '#FDF6C8', '#FDF9AF', '#FEFC96',
    '#F7F580', '#E7E86C', '#D7DC58', '#C7CF45', '#B7C332', '#A7B71F', '#97AA0D', '#889E0A', '#789209', '#698607', '#5A7A06', '#4B6E05', '#3C6203', '#2D5602', '#1F4A01', '#154000', '#133800', '#123000', '#112800', '#102000', '#101800', '#101000', '#101000', '#122200']

#using the normalizedDifference function
ndvi_year_1985 = image_1985.normalizedDifference(['B4', 'B3'])
ndvi_year_1990 = image_1990.normalizedDifference(['B4', 'B3'])
ndvi_year_2000 = image_2000.normalizedDifference(['B4', 'B3'])
ndvi_year_2010 = image_2010.normalizedDifference(['B4', 'B3'])
ndvi_year_2020 = image_2020.normalizedDifference(['B5', 'B4'])
ndvi_year_2024 = image_2024.normalizedDifference(['B5', 'B4'])

# Adding NDVI layers to the map
map1.addLayer(ndvi_year_1985, {'min': -1, 'max': 1, 'palette': ndvi_palette}, 'NDVI 1985')
map1.addLayer(ndvi_year_1990, {'min': -0.2, 'max': 0.5, 'palette': ndvi_palette}, 'NDVI 1990')
map1.addLayer(ndvi_year_2000, {'min': -0.4, 'max': 0.5, 'palette': ndvi_palette}, 'NDVI 2000')
map1.addLayer(ndvi_year_2010, {'min': -0.4, 'max': 0.3, 'palette': ndvi_palette}, 'NDVI 2010')
map1.addLayer(ndvi_year_2020, {'min': -0.1, 'max': 0.4, 'palette': ndvi_palette}, 'NDVI 2020')
map1.addLayer(ndvi_year_2024, {'min': 0, 'max': 0.4, 'palette': ndvi_palette}, 'NDVI 2024')

# Add a layer control to the map
map1.addLayerControl()

# Display the map
map1

# Define a custom NDWI color palette
ndwi_palette = ['#CEFFFD', '#76E3DE', '#76CCE3', '#40B4D3', '#4078D3', '#2126BB']

# Calculate NDWI for different years
ndwi_year_1985 = image_1985.normalizedDifference(['B2', 'B4'])  # 1985
ndwi_year_1990 = image_1990.normalizedDifference(['B2', 'B4'])  # 1990
ndwi_year_2000 = image_2000.normalizedDifference(['B2', 'B4'])  # 2000
ndwi_year_2010 = image_2010.normalizedDifference(['B2', 'B4'])  # 2010
ndwi_year_2020 = image_2020.normalizedDifference(['B3', 'B5'])  # 2020
ndwi_year_2024 = image_2024.normalizedDifference(['B3', 'B5'])  # 2024

# Adding NDWI layers
map2.addLayer(ndwi_year_1985, {'min': -1, 'max': 1, 'palette': ndwi_palette}, 'NDWI 1985')
map2.addLayer(ndwi_year_1990, {'min': -0.4, 'max': 0.4, 'palette': ndwi_palette}, 'NDWI 1990')
map2.addLayer(ndwi_year_2000, {'min': -0.4, 'max': 0.4, 'palette': ndwi_palette}, 'NDWI 2000')
map2.addLayer(ndwi_year_2010, {'min': -0.2, 'max': 0.5, 'palette': ndwi_palette}, 'NDWI 2010')
map2.addLayer(ndwi_year_2020, {'min': -0.4, 'max': 0.1, 'palette': ndwi_palette}, 'NDWI 2020')
map2.addLayer(ndwi_year_2024, {'min': -0.3, 'max': 0.1, 'palette': ndwi_palette}, 'NDWI 2024')

# Add a layer control to the map
map2.addLayerControl()

# the map
map2

# Define a custom SAVI color palette
custom_savi_palette = ['#5A2C0F', '#6A3A1C', '#7B4C28', '#8C5E34', '#9D7040', '#AE8250', '#BF9360', '#D1A472', '#E2B684', '#F3C896', '#F7DAA8', '#F9E1B6', '#FBE9C4', '#FFEECC',
    '#FFF4D2', '#F7F8B4', '#E5F6A6', '#D2F599', '#C0F38B', '#AEF17E', '#9DEF71', '#88EA66', '#74E65B', '#60E250', '#4EDD47', '#3DD93E', '#30CC3A', '#28B532', '#209E2B', '#188825', '#117320', '#0A5E1A', '#064A14', '#00360F']

savi_year_1985 = image_1985.expression('((1.5) * (NIR - RED)) / (NIR + RED + 0.5)', {'NIR': image_1985.select('B4'), 'RED': image_1985.select('B3')})
savi_year_1990 = image_1990.expression('((1.5) * (NIR - RED)) / (NIR + RED + 0.5)', {'NIR': image_1990.select('B4'), 'RED': image_1990.select('B3')})
savi_year_2000 = image_2000.expression('((1.5) * (NIR - RED)) / (NIR + RED + 0.5)', {'NIR': image_2000.select('B4'), 'RED': image_2000.select('B3')})
savi_year_2010 = image_2010.expression('((1.5) * (NIR - RED)) / (NIR + RED + 0.5)', {'NIR': image_2010.select('B4'), 'RED': image_2010.select('B3')})
savi_year_2020 = image_2020.expression('((1.5) * (NIR - RED)) / (NIR + RED + 0.5)', {'NIR': image_2020.select('B5'), 'RED': image_2020.select('B4')})
savi_year_2024 = image_2024.expression('((1.5) * (NIR - RED)) / (NIR + RED + 0.5)', {'NIR': image_2024.select('B5'), 'RED': image_2024.select('B4')})

# Add SAVI layers to the map with visualization parameters
map3.addLayer(savi_year_1985, {'min': -1, 'max': 1, 'palette': custom_savi_palette}, 'SAVI 1985')
map3.addLayer(savi_year_1990, {'min': -0.3, 'max': 0.8, 'palette': custom_savi_palette}, 'SAVI 1990')
map3.addLayer(savi_year_2000, {'min': -0.6, 'max': 0.9, 'palette': custom_savi_palette}, 'SAVI 2000')
map3.addLayer(savi_year_2010, {'min': -0.7, 'max': 0.7, 'palette': custom_savi_palette}, 'SAVI 2010')
map3.addLayer(savi_year_2020, {'min': -0.1, 'max': 0.7, 'palette': custom_savi_palette}, 'SAVI 2020')
map3.addLayer(savi_year_2024, {'min': -0.1, 'max': 0.6, 'palette': custom_savi_palette}, 'SAVI 2024')

# Add a layer control to the map
map3.addLayerControl()

# Display the map
map3

# Define the years and corresponding images for each index
years = [1985, 1990, 2000, 2010, 2020, 2024]

# SAVI export loop
savi_images = [savi_year_1985, savi_year_1990, savi_year_2000, savi_year_2010, savi_year_2020, savi_year_2024]
for year, savi_image in zip(years, savi_images):
    task = ee.batch.Export.image.toDrive(
        image=savi_image,
        description=f'SAVI_{year}',
        folder='EarthEngineExports',
        scale=30,
        region=area_of_interest.geometry(),
        maxPixels=1e13
    )
    task.start()

# NDVI export loop
ndvi_images = [ndvi_year_1985, ndvi_year_1990, ndvi_year_2000, ndvi_year_2010, ndvi_year_2020, ndvi_year_2024]
for year, ndvi_image in zip(years, ndvi_images):
    task = ee.batch.Export.image.toDrive(
        image=ndvi_image,
        description=f'NDVI_{year}',
        folder='EarthEngineExports',
        scale=30,
        region=area_of_interest.geometry(),
        maxPixels=1e13
    )
    task.start()

# NDWI export loop
ndwi_images = [ndwi_year_1985, ndwi_year_1990, ndwi_year_2000, ndwi_year_2010, ndwi_year_2020, ndwi_year_2024]
for year, ndwi_image in zip(years, ndwi_images):
    task = ee.batch.Export.image.toDrive(
        image=ndwi_image,
        description=f'NDWI_{year}',
        folder='EarthEngineExports',
        scale=30,
        region=area_of_interest.geometry(),
        maxPixels=1e13
    )
    task.start()