GPS Requirments
===============

Requirements
------------

    - Longitude
        - +/- 180 degrees
    - Latitude
        - +/- 90 degrees
    - Save Current Position as waypoint
        - Associate name to point
        - w/o ability to truly get current lat/lon location, generate valid lat/lon location
    - Save and Retrieve named paths
        - Paths consist of waypoints
    - Calculate path length
        - Assume straight lines between waypoints
    - Calculate distance to a waypoint from current location


Ideas for structure
-------------------

getLoc method:
    get current location and returns a lat/lon tuple

    put a random lat/lon generator in since desktop is incapable of finding its own lat/lon location

saveWaypoint method:
    takes a lat/lon tuple and a name

    saves it into a dictionary with the name as a key and the tuple as the value

createPath method:
    takes a name

    saves it into a dictionary with the name as the key and an empty value for the value

addWaypoint method:
    takes two names, one for the path and one for the waypoint

    gets the path entry based off of the dictionary value for the path name

    if the value is null, it saves the name for the waypoint as the only entry in a list

    if there is already a list, it adds the waypoint name to the end of the list

distance method:
    takes one or two lat/lon tuples

    gets the absolute value the following formula:

        lat1 - lat2
        -----------
        lon1 - lon2

    If only a single tuple was passed in, the second tuple is retrieved as the current location

    returns the value

pathDistance method:
    takes a path

    sends each sequential pair of waypoints to the distance method to get a total for the whole path

    reurns the total
