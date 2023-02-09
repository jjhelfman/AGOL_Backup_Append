
# ArcGIS Online (AGOL) Backup

<!-- ## Scripts 

1. updateFromKML.py is for appending new KML point data to point feature classes and layers. It applies the following methods to an open ArcGIS Pro project:
    -   removeExisting() - Removes intermediate data from input
    -   kmlToFC() - Converts KML file to appropriately projected feature class (FC)
    -   appendTo() - Appends the new FC to a master FC  
    -   appendToFL() - Appends the new FC to the correct Feature Layer/Service in an ArcGIS Online (AGOL) website

2. exportToPDF.py is a script tool that exports all of the layouts from your ArcGIS Pro project into PDFs.  -->

## Instructions

1. Install dependencies by running the command ```pip install -r requirements.txt```
2. Run the script from an IDE. I used Visual Studio Code and the Python interpreter "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe".
3. The scripts will prompt you to provide your AGOL credentials, then the folder path ("file location") where you want to store the backups. 
    - Note:
        > The AGOL username is case sensitive. The password input appears blank. 
        > Make sure to exclude quotation marks from the folder path.

**backup_items.py**

The script first exports all Feature Services as datetime-stamped File Geodatabases. Then, it checks for existing downloadable file types (File Geodatabase, CSV, KML, KML Collection, Shapefile, Pro Map, Map Document, Map Package, Map Template, Layer, Layer Package). Story Maps, Web Mapping Apps, and other items not mentioned are not included. All of the files are then downloaded to your folder path and deleted from your AGOL site. 

The command line/terminal upon successful completion:
![alt text](https://i.imgur.com/aUrV1hN.jpg)

For extracting data from ArcGIS Server map services, see https://support.esri.com/en/technical-article/000019645 

## Sources

1. https://support.esri.com/en/technical-article/000018909 
2. https://developers.arcgis.com/python/api-reference/arcgis.gis.toc.html 
3. https://developers.arcgis.com/rest/users-groups-and-items/item.htm
4. https://developers.arcgis.com/rest/users-groups-and-items/items-and-item-types.htm

