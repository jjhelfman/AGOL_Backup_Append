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

# Create backup folder
current_directory = os.getcwd()
timestamp = dt.datetime.now().strftime("%d_%b_%Y")
backup_directory = os.path.join(current_directory, r"BackUp_" + timestamp)

file_items = []
file_types = frozenset(
    [
        "File Geodatabase",
        "CSV",
        "Image",
        "KML",
        "KML Collection",
        "Layer",
        "Layer Package",
        "Locator Package",
        "Map Document",
        "Map Package",
        "Map Template",
        "Microsoft Excel",
        "Microsoft Powerpoint",
        "Microsoft Word",
        "Mobile Map Package",
        "PDF",
        "Pro Map",
        "Scene Package",
        "Shapefile",
        "Tile Package",
        "Vector Tile Package",
    ]
)


def download_item_data(all_items, backup_directory):
    print(
        "There are a total of "
        + str(len(all_items))
        + " items that will be backed up to "
        + backup_directory
    )
    for item in all_items:
        try:
            print("==================================================")
            print("Downloading JSON data," +
                  "thumbnail and metadata for " + item.title)
            item_folder = backup_directory + "//" + str(item["title"]) + "\\"
            if not os.path.exists(item_folder):
                os.makedirs(item_folder)
            file_path = item_folder + str(
                item["title"] + "." + item["type"] + ".json"
            ).replace(" ", "_")
            item_data = item.get_data(try_json=False)
            if item_data != None:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(item_data)
            item.download_thumbnail(item_folder)
            item.download_metadata(item_folder)
            print(
                "Successfully downloaded the the data for "
                + item.title
                + " to "
                + backup_directory
            )
        except Exception as e:
            print("An error occurred downloading: ")
            print(e)
    print("The download_item_data function has completed")


def export_file_items(all_items, file_items, file_types):
    for item in all_items:
        try:
            if item.type == "Feature Service":
                print("Exporting " + item.title)
                timestamp = dt.datetime.now().strftime("%d_%b_%Y")
                fgdb = item.export(item.title +
                                   "_" + timestamp, "File Geodatabase")
                file_items.append(fgdb)
            if item.type in file_types:
                file_items.append(item)
        except Exception as e:
            print("An error occurred downloading: ")
            print(e)
    print("The list_and_export function has completed")

    return file_items


def download_file_items(file_items, backup_directory):
    print(
        "There are a total of "
        + str(len(file_items))
        + " files that will be backed up to "
        + backup_directory
    )
    # Download items
    for item in file_items:
        try:
            print("Downloading " + item.title)
            item.download(backup_directory)
            item.download_thumbnail(backup_directory)
            item.download_metadata(backup_directory)
            print("Successfully downloaded " +
                  item.title + " to " + backup_directory)
        except Exception as e:
            print("An error occurred downloading " + item.title + ": ")
            print(e)
    print("The download function has completed")


download_item_data(all_items, backup_directory)
file_items = export_file_items(all_items, file_items, file_types)
download_file_items(file_items, backup_directory)
