from arcgis.gis import GIS
from arcgis.features import FeatureLayer
import csv

username = input("Input your username: ")
gis = GIS('https://arcgis.com', username)
source_csv = input("Please enter the source csv file location: ") # C:/KML to Maps/Exports/Preserves_FeatureToPoint.csv
source_name = input("Please enter the csv file name: ") # Preserves_FeatureToPoint
source_tags = input("Please enter the csv file tags: ") # Test, Preserves, CSV
source_desc = input("Please enter the csv file description: ") # UCO points of interest in CSV
layer_url = input("Please enter the feature layer's URL, with the Layer ID specified \n" + "(i.e. https://services8.arcgis.com/exgR4BNI38IIwXOt/arcgis/rest/services/Preserves_FeatureToPoint/FeatureServer/0): ")


def add_csv(gis, source_csv, source_name, source_tags, source_desc):
    try:
        # Get the CSV's fields
        with open(source_csv) as f:
            reader = csv.reader(f)
            csv_fields = next(reader)
        # Check if CSV file already exists
        item_csv = gis.content.search(query="type:CSV, title:Preserves_FeatureToPoint")
        if  item_csv:
            item_csv[0].delete()
            print(f"Successfully deleted {str(item_csv[0])}") 
        # Add CSV to AGOL, to be the source of the Append
        item_csv = gis.content.add(item_properties={"type": "CSV",
                                                    "title" : source_name,
                                                    "tags": source_tags,
                                                    "description" : source_desc,
                                                    "commentsEnabled" : False}, 
                                   data=source_csv)
        print(f"Successfully added {str(item_csv)}" + f" to {str(gis)}")
    except Exception as e:
            print(f"An error occurred with the add_csv function: ")
            print(e)
    print(f"The add_csv function has completed")
    
    return item_csv, csv_fields

def append_to_layer(gis, layer_url, item_csv, csv_fields):
    try:
        #Analyze the CSV
        source_info = gis.content.analyze(item=item_csv.id, file_type='csv', location_type="coordinates")
        # Get the feature layer from the layer URL
        feature_layer = FeatureLayer(layer_url) 
        # Alternatively, get the feature layer using item id
        # item_url = gis.content.get('624d64134a0042d4a7cfb840ff67358b') #returns single feature service unlike search 
        # feature_layer = item_url.layers[0] # b/c feature service multiple layers   
        
        # Get and compare fields between csv and feature layer
        field_mappings = []
        # Get list of feature layer's fields
        feat_set = feature_layer.query(where="OBJECTID=1")
        feat = feat_set.features[0]
        layer_fields1 = [x.lower() for x in feat.fields]
        csv_fields1 = [y.lower() for y in csv_fields]
        for z in csv_fields1:
            if z in layer_fields1:
                i_layer = layer_fields1.index(z)
                i_csv = csv_fields1.index(z)
                field_mappings.append({"source":csv_fields[i_csv], "name":feat.fields[i_layer]})
        
        feature_layer.append(item_id=item_csv.id,
                            upload_format='csv',
                            field_mappings=field_mappings,
                            source_info=source_info['publishParameters'],
                            upsert=False,
                            skip_updates=False,
                            use_globalids=False,
                            update_geometry=True,
                            append_fields=csv_fields,
                            rollback=True,
                            skip_inserts=False)
        print(f"Successfully appended to {str(feature_layer)} in {str(gis)}")
        item_csv.delete() # Delete the CSV file here
        print(f"Successfully deleted {str(item_csv)} from {str(gis)}") 
    except Exception as e:
            print(f"An error occurred with the append_to_layer function: ")
            print(e)
    print(f"The append_to_layer function has completed")


item_csv, csv_fields = add_csv(gis, source_csv, source_name, source_tags, source_desc)
append_to_layer(gis, layer_url, item_csv, csv_fields)
    
    