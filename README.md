# ArcGIS Online (AGOL) Backup, and Append CSV

## Scripts 

1. backup_items.py is for backing up your typical data from AGOL. The script first gets a list of all items owned by you, the user. It exports all Feature Services as date-stamped File Geodatabases. Then, it checks for existing downloadable file types, including File Geodatabase, CSV, KML, KML Collection, Shapefile, Pro Map, Map Document, Map Package, Map Template, Layer, and Layer Package. The script does not check for Story Maps, Web Maps, Web Mapping Apps, Scene Layers or other items. All of the newly converted File Geodatabases and existing files are then downloaded to a new date-stamped backup folder in the current working directory. 

2. append_csv.py appends a specified CSV file to a feature service/layer in AGOL. 

## Instructions

1. Install dependencies by running the command ```pip install -r requirements.txt```
2. Run the script from an IDE. I used Visual Studio Code and the Python interpreter "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe".
3. Both scripts will prompt you to input your AGOL credentials.
    - Note:
        > The AGOL username is case sensitive. The password input appears blank. 
        > Make sure to exclude quotation marks from the folder path.     
4. append_csv.py asks for the source CSV's location and the feature layer's URL, including the numerical Layer ID at the end (i.e. https://services8.arcgis.com/exgR4BNI38IIwXOt/arcgis/rest/services/Preserves_FeatureToPoint/FeatureServer/0). Do not include quotation marks here.
    - Update the following:
        > The item_properties parameter in add_csv()'s gis.content.add() call.
        > The field_mappings and append_fields paramaters in the append_to_layer()'s feature_layer.append() call.

## Sources

1. https://support.esri.com/en/technical-article/000018909 
2. https://developers.arcgis.com/python/api-reference/arcgis.gis.toc.html 
3. https://developers.arcgis.com/rest/users-groups-and-items/item.htm
4. https://developers.arcgis.com/rest/users-groups-and-items/items-and-item-types.htm
5. https://support.esri.com/en/technical-article/000028111
6. For extracting data from ArcGIS Server map services, see https://support.esri.com/en/technical-article/000019645 

