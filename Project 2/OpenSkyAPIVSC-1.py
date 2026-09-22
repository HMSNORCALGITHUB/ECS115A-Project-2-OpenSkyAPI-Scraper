from opensky_api import OpenSkyApi
api = OpenSkyApi()
s = api.get_states()

def activecounter(csvfile):
    # Check how many falses are in the csv column 'on_ground'
    import csv
    count = 0
    with open('FlightDataCSVTable.csv', 'r') as f:
        data = csv.DictReader(f)
        # Reads data into dict format
        
        # Initialize count
        for row in data:
            # Had to make header ' True', as my CSV Reader did not let me change header. Fix!
            grounded = row.get('on_ground', '')
            if "False" in grounded:
                count += 1
    return count
if __name__ == "__main__":
    count = activecounter('FlightDataCSVTable.csv')
    print(f'{count}')
