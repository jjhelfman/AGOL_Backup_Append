# You can copy lines directly from here and paste into the ArcGIS Python window or scipt tool properties: 

# Appending/copying records:
import arcpy

inFC = <the input Feature Class - make this 1st param a feature layer>
targetFC = <the Target Feature Class>

# Collect all fields except the Geometry field
inFields = [field.name for field in arcpy.ListFields(inFC) if field.type not in ['Geometry']]
inFields.append("SHAPE@") # add the full Geometry object
# Similar to previous with fields specified
targetCursor = arcpy.da.InsertCursor(targetFC,inFields)
with arcpy.da.SearchCursor(inFC,inFields) as cursor:
    for row in cursor:
        targetCursor.insertRow(row)
print("Complete")

# =====================================================================================
# Date string field calculator expression:
import datetime

date = datetime.datetime(2003, 12, 31) # first datetime object
def autoIncrement():
    global date
    pInterval = 1  # adjust interval value, if req'd
    date += datetime.timedelta(pInterval)
    date_time = date.strftime("%m/%d/%Y")
    return date_time

# =====================================================================================
# This script is intended to be used in a script tool for an ArcGIS Pro project
# From the script tool properties, assign the figFolder string parameter as a Folder data type.
import arcpy

aprx = arcpy.mp.ArcGISProject("CURRENT")
figFolder = arcpy.GetParameterAsText(0)

for lyt in aprx.listLayouts():
    print(" {0} ({1} x {2} {3})".format(lyt.name, lyt.pageHeight, lyt.pageWidth, lyt.pageUnits))
    lyt.exportToPDF(figFolder + "\\" + lyt.name + ".pdf")





