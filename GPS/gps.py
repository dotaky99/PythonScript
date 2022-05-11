from PIL import Image
from PIL.ExifTags import TAGS
import sys, os

# import folium

# Get image in folder
path_dir = 'F:/Gallery/앨범_1/'
file_list = os.listdir(path_dir)

gmaps = "https://www.google.com/maps?q={},{}"
Lat = ""
Lon = ""
for image in file_list:
    try:
        img_file = Image.open(path_dir + image)
        exif_data = img_file._getexif()
        img_file.close()
        print(image)

        taglabe = {}
        for tag, value in exif_data.items():
            decoded = TAGS.get(tag, tag)
            taglabe[decoded] = value

        exifGPS = taglabe['GPSInfo']
        latData = exifGPS[2]
        lonData = exifGPS[4]

        Lat = (latData[0] + (latData[1] + latData[2] / 60.0) / 60.0)
        if exifGPS[1] == 'S': Lat = Lat * -1

        Lon = (lonData[0] + (lonData[1] + lonData[2] / 60.0) / 60.0)
        if exifGPS[3] == 'W':
            Lon = Lon * -1

        # print("{} = {}. {}".format(image, Lat, Lon))
        # print("GPS Coordinates : {}. {}".format(Lat, Lon))
        # print("Google Maps URL : {}".format(gmaps.format(Lat, Lon)))
        print(gmaps.format(Lat, Lon))

    except:
        continue
