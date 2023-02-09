from arcgis.gis import GIS
from arcgis.features import FeatureLayer

username = input("Input your username: ")
gis = GIS('https://arcgis.com', username)
data_path = input("Please enter the source file location: ") # C:/KML to Maps/Exports/Preserves_FeatureToPoint.csv


def addCSV(gis, data_path)
    try:
        # Check if CSV file already exists
        item_csv = gis.content.search(query="type:CSV, title:Preserves_FeatureToPoint")
        if  item_csv:
            item_csv[0].delete()
            print("Successfully deleted " + str(item_csv[0])) 
        # Add zipped FGDB to AGOL, to be the source of the Append
        item_csv = gis.content.add(item_properties={"type": "CSV",
                                                    "title" : "Preserves_FeatureToPoint",
                                                    "tags": "Test, Preserves, CSV",
                                                    "description" : "UCO points of interest in CSV",
                                                    "commentsEnabled" : False}, 
                                   data=data_path)
        print(f"Successfully added {item_csv}" + f" to {gis}")
    except Exception as e:
            print("An error occurred with the AddCSV function: ")
            print(e)
    print("The AddCSV function has completed")

def appendToFS(gis, data_path):
    try:
        item_url = 'https://services8.arcgis.com/exgR4BNI38IIwXOt/arcgis/rest/services/Preserves_FeatureToPoint/FeatureServer/0'
        feature_layer = FeatureLayer(item_url) 
        # Alternatively, get the feature layer using item id
        # item_url = gis.content.get('624d64134a0042d4a7cfb840ff67358b') #returns single feature service unlike search 
        # feature_layer = item_url.layers[0] # b/c feature service multiple layers   
        
        feature_layer.append(item_id=item_csv.id,
                     upload_format='csv',
                     field_mappings=[{"source":"Agency",  
                                      "name":"Agency"},
                                     {"source":"CreationDate","name":"CreationDate"},
                                     {"source":"Creator","name":"Creator"},
                                     {"source":"EditDate","name":"EditDate"},
                                     {"source":"Editor","name":"Editor"},
                                     {"source":"Latitude","name":"latitude"},
                                     {"source":"Longitude","name":"longitude"},
                                     {"source":"Notes","name":"Notes"},
                                     {"source":"PRESERVENAME","name":"PRESERVENAME"}],
                     source_info=source_info['publishParameters'],
                     upsert=False,
                     skip_updates=False,
                     use_globalids=False,
                     update_geometry=True,
                     append_fields=["Agency","CreationDate","Creator","EditDate","Editor","latitude","longitude","Notes","PRESERVENAME"],
                     rollback=True,
                     skip_inserts=False)
        print("Successfully appended to " + item_url + f" in {gis}")
        item_csv.delete() # Delete the CSV file here
        print("Successfully deleted " + str(item_csv) + f" from {gis}") 
    except Exception as e:
            print("An error occurred with the AppendToFS function: ")
            print(e)
    print("The AppendToFS function has completed")


addCSV(gis, data_path)
appendToFS(gis, data_path)
    
    