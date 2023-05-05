# ArcGIS Online (AGOL) Backup, and Append CSV

## Scripts 

1. backup_items.py is for backing up your typical data from AGOL. The script first gets a list of all items owned by you, the user. It exports all Feature Services as date-stamped File Geodatabases. Then, it checks for existing downloadable file types, including File Geodatabase, CSV, KML, KML Collection, Shapefile, Pro Map, Map Document, Map Package, Map Template, Layer, and Layer Package. The script does not check for Story Maps, Web Maps, Web Mapping Apps, Scene Layers or other items. All of the newly converted File Geodatabases and existing files are then downloaded to a new date-stamped backup folder in the current working directory. 

2. The append_csv scripts append a specified CSV file to a feature service/layer in AGOL. To publish line or polygon geometry you will need to use a different file format like a shapefile, File Geodatabase or GeoJson. If you need to use a CSV file for attributes, you may want to consider creating the polygon features from one of the above formats and use the Join tools to add the CSV data to the geometry.

## Instructions

1. Install dependencies by running the command ```pip install -r requirements.txt```
2. Run the script from an IDE. I used Visual Studio Code and the Python interpreter "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe".
3. Both scripts will prompt you to input your AGOL credentials.
    - Note:
        > The AGOL username is case sensitive. The password input appears blank. 
        > Make sure to exclude quotation marks from the folder path.     
4. When publishing to AGOL from a CSV file, the result will be point geometry, so make sure the CSV source file has a latitude and longitude (decimal degrees) in each row. 
5. The append_csv.py script is a developer-friendly script that asks for the source CSV's location and the feature layer's URL, including the numerical Layer ID at the end (i.e. https://services8.arcgis.com/exgR4BNI38IIwXOt/arcgis/rest/services/Preserves_FeatureToPoint/FeatureServer/0). Do not include quotation marks here.
    - Update the following:
        > The item_properties parameter in add_csv()'s gis.content.add() call.
        > The field_mappings and append_fields paramaters in the append_to_layer()'s feature_layer.append() call.
        > Comment out the item_csv.delete() call as needed. 
6. The append_csv_user_input.py script is more user-friendly, as it asks for the CSV's item properties and automatically defines the append's field parameters. The item_csv.delete() call can be commented out if you'd like to keep the CSV on AGOL.

## Sources

1. https://support.esri.com/en/technical-article/000018909 
2. https://developers.arcgis.com/python/api-reference/arcgis.gis.toc.html 
3. https://developers.arcgis.com/rest/users-groups-and-items/item.htm
4. https://developers.arcgis.com/rest/users-groups-and-items/items-and-item-types.htm
5. https://support.esri.com/en/technical-article/000028111
6. For cloning content (and maintaining folder structure), see https://developers.arcgis.com/python/samples/clone-portal-users-groups-and-content-rn/#copy-items. Folders are retrieved from `<source item>.<users><username>.folders`, which gets a list of the user's folders as dictionaries (with id, title and date keys).
7. For extracting data from ArcGIS Server map services, see https://support.esri.com/en/technical-article/000019645 

