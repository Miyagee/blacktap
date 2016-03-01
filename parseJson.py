import json
from fastkml import kml

f = open('downtowncrosstown.json')

data = []
for i, line in enumerate(f):
  blob = json.loads(line)

  if blob.get('name') == 'longitude' or blob.get('name') == 'latitude':
    data.append(blob)


for li in data:
  print(li)
gps = []
for i in range(0, len(data)-1, 2):
  if data[i]['name'] == 'longitude':
    gps.append((data[i]['value'], data[i+1]['value']))
  elif data[i]['name'] == 'latitude':
    gps.append((data[i+1]['value'], data[i]['value']))

for li in gps:
  print(li)

w = open('gps.kml', 'w')
w.write('<?xml version="1.0" encoding="UTF-8"?>\n')
w.write('<kml xmlns="http://earth.google.com/kml/2.1">\n')
w.write('  <Document>\n')
w.write('    <name>Kult map</name>\n')
w.write("""    <Style id="blueLine">
      <LineStyle>
        <color>ffff0000</color>
        <width>4</width>
      </LineStyle>
    </Style>\n""")

w.write("""    <Placemark>
      <name>Blue Line</name>
      <styleUrl>#blueLine</styleUrl>
      <LineString>
        <altitudeMode>relative</altitudeMode>
        <coordinates>\n""")
for entry in gps:
  w.write("%r, %r, 0\n" % (entry[0], entry[1]))
w.write("""        </coordinates>
      </LineString>
    </Placemark>
  </Document>
</kml>""")
