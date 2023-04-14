from arcgis.gis import GIS
import datetime as dt
import os

username = input("Input your username: ")
gis = GIS("https://arcgis.com", username)

# query_string = "owner:{}, max_items=1000".format(username)
all_items = gis.content.search(
    query="owner: {}".format(username),
    max_items=10000,
    sort_field="modifed",
    sort_order="desc",
)
items_list = []
types_list = [
    "File Geodatabase",
    "CSV",
    "Image",
    "KML",
    "KML Collection",
    "Shapefile",
    "Pro Map",
    "Map Document",
    "Map Package",
    "Map Template",
    "Layer",
    "Layer Package",
]


def list_and_export(all_items, items_list, types_list):
    for item in all_items:
        try:
            if item.type == "Feature Service":
                timestamp = dt.datetime.now().strftime("%d_%b_%Y")
                fgdb = item.export(item.title + "_"
                                   + timestamp, "File Geodatabase")
                items_list.append(fgdb)
            if item.type in types_list:
                items_list.append(item)
        except Exception as e:
            print("An error occurred downloading: ")
            print(e)
    print("The list_and_export function has completed")

    return items_list


def download(items_list):
    # Create backup folder
    current_directory = os.getcwd()
    timestamp = dt.datetime.now().strftime("%d_%b_%Y")
    backup_directory = os.path.join(current_directory, r"BackUp_" + timestamp)
    print(
        "There are a total of "
        + str(len(items_list))
        + " files that will be backed up to "
        + backup_directory
    )
    # Download items
    for item in items_list:
        try:
            print("Downloading " + item.title)
            item.download(backup_directory)
            print("Successfully downloaded " + item.title
                  + " to " + backup_directory)
        except Exception as e:
            print("An error occurred downloading " + item.title + ": ")
            print(e)
    print("The download function has completed")


items_list = list_and_export(all_items, items_list, types_list)
download(items_list)
