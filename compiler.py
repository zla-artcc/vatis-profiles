"""
Compile vATIS station files into vATIS profiles.
Each vATIS profile must exist and contain at least a defined "name" key.
The "stations" key is added or updated.
Example:
    {
        "name": "Los Angeles ARTCC (ZLA)"
    }
"""

from datetime import datetime
import json
import glob
import math

# Search for station files in all sub-folders of ./stations/
AVAILABLE_STATIONS = glob.glob("./stations/*/*.station")

# Each profile (key) has "stations" updated to those found using the search filter (value)
# Profile: Search filter
PROFILES = {
    "./vATIS-Profile-JCF.json": ['JCF'],
    "./vATIS-Profile-L30.json": ['L30'],
    "./vATIS-Profile-SBA.json": ['SBA'],
    "./vATIS-Profile-SCT.json": ['SCT'],
    "./vATIS-Profile-ZLA.json": ['KBFL', 'KBUR', 'KLAS', 'KLAX', 'KONT', 'KPSP', 'KSAN', 'KSBA', 'KSNA',
                                 'KVNY'],
    "./vATIS-Profile-ZLA-2.json": ['CTR'],
    "./vATIS-Profile-ZLA-CRAZY.json": ['CTR', 'L30', 'SCT', 'SBA', 'JCF'],
    "./vATIS-Profile-D-ATIS.json": ['KBUR', 'KLAS', 'KLAX', 'KONT', 'KSAN', 'KSNA',
                                 'KVNY']
}

# Exclude these airports from all profiles.
EXCLUDE_AIRPORTS = ['KPOC']

def filter_available_stations():
    """Remove airports in EXCLUDE_AIRPORTS from AVAILABLE_STATIONS."""
    for index, station in enumerate(AVAILABLE_STATIONS):
        for airport in EXCLUDE_AIRPORTS:
            if airport in station:
                AVAILABLE_STATIONS.pop(index)

def generate_serial(prev_serial):
    """
    Generate a new updateSerial based on a profile's current one. If the previous update was
    today, increment the version number. Otherwise, generate a serial for today.

    Args:
        prev_serial (int): Serial in YYYYMMDD## format where ## is a version from 00 to 99
    
    Returns:
        new_serial (int): The new serial based on the value of prev_serial

    Example:

    """
    today_int = int(datetime.today().strftime("%Y%m%d"))
    if math.floor(prev_serial / 100) != today_int:
        return today_int * 100
    return prev_serial + 1


def build_station_list(station_filter):
    """
    Build a list of station files matching the given filter.
    
    Args:
        station_filter (list): List of substrings to match (e.g., airport codes or folder names).
    
    Returns:
        profile_stations (list): A list of station file paths that match the filter.
    
    Example:
        station_filter = ['/SCT']
        AVAILABLE_STATIONS = ['./stations/SCT/KLAX.station', './stations/L30/KLAS.station']
        Result = ['./stations/SCT/KLAX.station']
    """
    profile_stations = []

    for station in AVAILABLE_STATIONS:
        for filter_item in station_filter:
            if filter_item in station:
                profile_stations.append(station)

    return profile_stations

def build_profile(profile_stations, vatis_profile):
    """
    Build a vATIS profile using a list of stations

    Args:
        profile_stations (list): A list of station files
        vatis_profile (str): A vATIS profile
    
    Example:
        profile_station_list = ['./stations/L30/KHND.station', './stations/L30/KLAS.station',
                                './stations/L30/KVGT.station']
        vatis_profile = "./vATIS-Profile-L30.json"
    """
    merged_stations = []

    # Open each station file from input_stations (a list of files) and appends to merged_stations
    for station in profile_stations:
        with open(station, "r", encoding="utf-8") as station_file:
            station_data = json.load(station_file)
            merged_stations.append(station_data)

    # Open and load the vATIS profile
    with open(vatis_profile, "r", encoding="utf-8") as vatis_profile_file:
        vatis_profile_data = json.load(vatis_profile_file)

    # Write merged_stations to "stations" key and save the vATIS profile
    with open(vatis_profile, "w", encoding="utf-8") as vatis_profile_file:
        vatis_profile_data["stations"] = merged_stations
        vatis_profile_data["updateSerial"] = generate_serial(vatis_profile_data["updateSerial"])
        json.dump(vatis_profile_data, vatis_profile_file, indent=2)

if len(EXCLUDE_AIRPORTS) > 0:
    filter_available_stations()

for profile_path, filters in PROFILES.items():
    station_list = sorted(build_station_list(filters))
    build_profile(station_list, profile_path)
