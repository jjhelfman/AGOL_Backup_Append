from arcgis.gis import GIS

import datetime as dt

username = input("Input your username: ")

gis = GIS('https://arcgis.com', username)

folder_path = input("Please enter the file location to store the backups: ") 
query_string = "type:Feature Service, owner:{}".format(username)
items = gis.content.search(query=query_string, sort_field='modifed', sort_order='desc')

print("There are a total of " + str(len(items)) + " Feature Services that will be backed up to " + folder_path)


def list_and_export(item_list):
    fgdbs = []
    for item in item_list:
        if item.type == 'Feature Service':
            version = dt.datetime.now().strftime("%d_%b_%Y")
            fgdb = item.export(item.title + "_" + version, "File Geodatabase")
            fgdbs.append(fgdb)
    return fgdbs


def download(fgdbs, backup_location):
    for fgdb in fgdbs:
        try:
            print("Downloading " + fgdb.title)
            fgdb.download(backup_location)
            fgdb.delete()
            print("Successfully downloaded " + fgdb.title)
        except Exception as e:
            print("An error occurred downloading " + fgdb.title + ": ")
            print(e)
    print("The download function has completed")

fgdbs = list_and_export(items)
print(fgdbs)
download(fgdbs, folder_path)
