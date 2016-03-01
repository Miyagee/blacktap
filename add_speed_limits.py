import json
from math import sqrt

MIN_SPEED_LIMIT = 30

def add_speed_limits(filename):
    """Filename ends with .json"""

    new_filename = filename[:-5] + "_speedlims.json"
    with open(filename, "r") as inp, open(new_filename, "w") as out:

        avg = None
        var = None
        n = 0.0
        mean_of_squares = None
        last = None

        normalZ = 1.96 # approximately 5 % chance ? 

        #Variance:
        # 1 / n * [sum of speeds^2] - [speed mean] ^2 

        buff = [] # buffer for holding lines to be written

        for line in inp:
            data = json.loads(line)
            buff.append(line)
            if data["name"] == "vehicle_speed":
                speed = data["value"] * 1.609344 # miles / h to km/h
                if avg is None:
                    avg = speed
                    mean_of_squares = speed ** 2
                    var = 0.0
                    n = 1.0
                else:
                    avg = (avg * n + speed) / (n+1)
                    mean_of_squares = (mean_of_squares *n + speed**2) / (n+1)
                    n += 1.0
                    var = mean_of_squares - avg**2

                    if n > 50 and not (avg - normalZ * sqrt(var / n) < speed < avg + normalZ * sqrt(var / n)):
                        limit = round(avg / 10.0) * 10
                        if limit == last:
                            continue

                        speedlimit = {"name" : "speedlimit", "value" : limit,
                                "timestamp" : json.loads(buff[0])["timestamp"]}

                        if MIN_SPEED_LIMIT <= limit: # Else, reset but not write
                            out.write(json.dumps(speedlimit) + "\n")
                            last = limit
                            print("wrote speed lim:", last)
                        for e in buff:
                            out.write(e)
                        avg = None
                        buff = []
        if len(buff) > 0:
            limit = round(avg / 10.0) * 10
            if limit != last:

                speedlimit = {"name" : "speedlimit", "value" : limit,
                        "timestamp" : json.loads(buff[0])["timestamp"]}

                if MIN_SPEED_LIMIT <= limit: # Else, reset but not write
                    out.write(json.dumps(speedlimit) + "\n")
                    last = limit
                    print("wrote speed lim:", last)
            for e in buff:
                out.write(e)

add_speed_limits("uptown-west.json")
