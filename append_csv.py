from arcgis.gis import GIS
from arcgis.features import FeatureLayer

username = input("Input your username: ")
gis = GIS("https://arcgis.com", username)
source_csv = input(
    "Please enter the source file location: "
)  # C:/KML to Maps/Exports/Preserves_FeatureToPoint.csv
layer_url = input(
    "Please enter the feature layer's URL, with the Layer ID specified \n"
    + "(i.e. https://services8.arcgis.com/exgR4BNI38IIwXOt/arcgis/rest/services/Preserves_FeatureToPoint/FeatureServer/0): "
)


def add_csv(gis, source_csv):
    try:
        # Check if CSV file already exists
        item_csv = gis.content.search(
            query="type:CSV, title:Preserves_FeatureToPoint"
        )
        if item_csv:
            item_csv[0].delete()
            print(f"Successfully deleted {str(item_csv[0])}")
        # Add CSV to AGOL, to be the source of the Append
        item_csv = gis.content.add(
            item_properties={
                "type": "CSV",
                "title": "Preserves_FeatureToPoint",
                "tags": "Test, Preserves, CSV",
                "description": "UCO points of interest in CSV",
                "commentsEnabled": False,
            },
            data=source_csv,
        )
        print(f"Successfully added {str(item_csv)} to {str(gis)}")
    except Exception as e:
        print("An error occurred with the add_csv function: ")
        print(e)
    print("The add_csv function has completed")

    return item_csv


def append_to_layer(gis, layer_url, item_csv):
    try:
        # Analyze the CSV
        source_info = gis.content.analyze(
            item=item_csv.id, file_type="csv", location_type="coordinates"
        )
        # Get the feature layer from the layer URL
        feature_layer = FeatureLayer(layer_url)
        # Alternatively, get the feature layer using item id
        # item_url = gis.content.get('624d64134a0042d4a7cfb840ff67358b')
        # returns single feature service unlike search
        # feature_layer = item_url.layers[0]
        # b/c feature service can have multiple layers

        feature_layer.append(
            item_id=item_csv.id,
            upload_format="csv",
            field_mappings=[
                {"source": "Agency", "name": "Agency"},
                {"source": "CreationDate", "name": "CreationDate"},
                {"source": "Creator", "name": "Creator"},
                {"source": "EditDate", "name": "EditDate"},
                {"source": "Editor", "name": "Editor"},
                {"source": "Latitude", "name": "latitude"},
                {"source": "Longitude", "name": "longitude"},
                {"source": "Notes", "name": "Notes"},
                {"source": "PRESERVENAME", "name": "PRESERVENAME"},
            ],
            source_info=source_info["publishParameters"],
            upsert=False,
            skip_updates=False,
            use_globalids=False,
            update_geometry=True,
            append_fields=[
                "Agency",
                "CreationDate",
                "Creator",
                "EditDate",
                "Editor",
                "latitude",
                "longitude",
                "Notes",
                "PRESERVENAME",
            ],
            rollback=True,
            skip_inserts=False,
        )
        print(f"Successfully appended to {str(feature_layer)} in {str(gis)}")
        item_csv.delete()  # Delete the CSV file here
        print(f"Successfully deleted {str(item_csv)} from {str(gis)}")
    except Exception as e:
        print("An error occurred with the append_to_layer function: ")
        print(e)
    print("The append_to_layer function has completed")


item_csv = add_csv(gis, source_csv)
append_to_layer(gis, layer_url, item_csv)
