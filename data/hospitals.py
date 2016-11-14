import glob
import pandas as pd
import numpy as np


HOSPITAL_DATA = "Mapped_HHC.xlsx"
DATA_DIR = 'data/*'
file_path_names = glob.glob(DATA_DIR)

frames = []

#open hospital data as PD
hospitals = pd.ExcelFile(HOSPITAL_DATA)
hosp_locations = pd.read_excel(hospitals)

#individually read trip data
for pathname in file_path_names:
	filename = pathname[5:]
	trip_data = pd.read_csv(pathname, parse_dates=['pickup_datetime', 'dropoff_datetime'])
	print("reading ", filename)

	med_trips = []

	for row in trip_data.rows:
		for row in hosp_locations.rows:
			if row['pickup_longitude'] == hosp_locations['hospital_longitude'] &&
			trip_data['pickup_latitude'] == hosp_locations['hospital_latitude'] 

			OR IF?
			if trip_data['dropoff_longitude'] == hosp_locations['hospital_longitude'] &&
			trip_data['dropoff_latitude'] == hosp_locations['hospital_latitude'] 

			med_trips.append(row)

	frames.append(med_trips)
	

df = pd.concat(frames)
df.to_csv('medical_trips.csv')




