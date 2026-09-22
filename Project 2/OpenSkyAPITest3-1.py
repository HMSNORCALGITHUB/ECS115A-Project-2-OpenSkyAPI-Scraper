from opensky_api import OpenSkyApi
api = OpenSkyApi()
s = api.get_states()
from collections import Counter
# https://docs.python.org/3/library/collections.html
# I wanted a way to count things. Counter module

def concentrate(csvfile):
    import csv
    with open('FlightDataCSVTable.csv', 'r') as file:
        data = csv.DictReader(file)
        countrycounter = Counter()

        for row in data:
            grounded = row.get('on_ground', '')
            country = row.get('origin_country', '')
            if grounded == ' False':
                countrycounter[country] += 1
        # Use Counter() docs and commands
        #most_common(1) will give the top most frequent item
        mostcommon = countrycounter.most_common(1)
        if mostcommon:
            country = mostcommon[0]
        else:
            print("didnt work")
        return country
    
if __name__ == "__main__":
    country = concentrate('FlightDataCSVTable.csv')
    print(f"{country}")

        


