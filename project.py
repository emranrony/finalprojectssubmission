import arcpy
arcpy.env.workspace = r"C:\GE\Test_workspace"
arcpy.env.overwriteOutput = True
dem_file = r"C:\Users\JULFIKAR\Downloads\rasters_NASADEM\output_NASADEM.tif"

contour_shapefile = r"C:\GE\Test_workspace\output\contour\contour_lines.shp"
hillshade_output = r"C:\GE\Test_workspace\output\hillshade\hillshade.tif"

def create_contour_lines(dem, output_shapefile, interval):
    try:
        arcpy.sa.Contour(dem, output_shapefile, interval)
        print("Contour lines created: {}".format(output_shapefile))
    except Exception as e:
        print("Error generating contour lines: {}".format(str(e)))

def create_hillshade(dem, output_hillshade):
    try:
        hillshade = arcpy.sa.Hillshade(dem, azimuth=315, altitude=45)
        hillshade.save(output_hillshade)
        print("Hillshade created: {}".format(output_hillshade))
    except Exception as e:
        print("Error generating hillshade: {}".format(str(e)))

if _name_ == "_main_":
    try:
        arcpy.CheckOutExtension("Spatial")
        contour_interval = 10
        create_contour_lines(dem_file, contour_shapefile, contour_interval)
        create_hillshade(dem_file, hillshade_output)
        arcpy.CheckInExtension("Spatial")
    except Exception as main_e:
        print("An error occurred: {}".format(str(main_e)))
