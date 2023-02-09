from arcgis.gis import GIS
import datetime as dt
import os

username = input("Input your username: ")
gis = GIS('https://arcgis.com', username)

query_string = "type:Feature Service, owner:{}".format(username)
all_items = gis.content.search(query=query_string, sort_field='modifed', sort_order='desc')
items_list = []
types_list = ["File Geodatabase", "CSV", "Image", "KML", "KML Collection", "Shapefile", "Pro Map", 
              "Map Document", "Map Package", "Map Template", "Layer", "Layer Package"]


def list_and_export(all_items, items_list, types_list):
    try:
        for item in all_items:
            if item.type == 'Feature Service':
                timestamp = dt.datetime.now().strftime("%d_%b_%Y")
                fgdb = item.export(item.title + "_" + timestamp, "File Geodatabase")
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
    backup_directory = os.path.join(current_directory, r'BackUp_' + timestamp)
    print("There are a total of " + str(len(items_list)) + " files that will be backed up to " + backup_directory)
    print(items_list)
    # Download items
    for item in items_list:
        try:
            print("Downloading " + fgdb.title)
            item.download(backup_directory)
            print("Successfully downloaded " + item.title " to " + backup_directory)
        except Exception as e:
            print("An error occurred downloading " + fgdb.title + ": ")
            print(e)
    print("The download function has completed")


items_list = list_and_export(all_items)
download(items_list)
