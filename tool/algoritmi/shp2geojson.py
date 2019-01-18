import shapefile
from json import dumps

def shp2geojson (input_path, output_path):
    reader = shapefile.Reader(input_path)
    fields = reader.fields[1:]
    field_names = [field[0] for field in fields]
    newlist = []
    for sr in reader.shapeRecords():
        atr = dict(zip(field_names, sr.record))
        geom = sr.shape.__geo_interface__
        newlist.append(dict(type="Feature", geometry=geom, properties=atr))
    geojson = open(output_path, 'w')
    geojson.write(dumps({"type": "FeatureCollection", "features": newlist}, indent=2) + "\n")
    geojson.close()
