import requests
import pandas as pd
from datetime import datetime
import csv,sys

def get_data():
    api_key = 'AIR_QUALITY_API'

    aqicn_base_url = 'https://api.waqi.info/feed/Kurla, Mumbai, India '

    aqicn_url = f'{aqicn_base_url}?token={api_key}'

    response = requests.get(aqicn_url)

    if response.status_code == 200:
        data = response.json()  
        print("Air Quality Data fetched successfully:", data)
        return data
    else:
        print("Failed to fetch Air Quality Data. Status code:", response.status_code)
        return None


def update_csv(data, csv_filename='air_quality_data.csv'):
    header = ['Timestamp', 'PM2.5', 'PM10','O3','NO2','SO2', 'CO']
    row = [
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        data['data']['iaqi']['pm25']['v'],
        data['data']['iaqi']['pm10']['v'],
        data['data']['iaqi']['o3']['v'],

        data['data']['iaqi']['no2']['v'],
        data['data']['iaqi']['so2']['v'],
        data['data']['iaqi']['co']['v'],

    ]

    try:
        with open(csv_filename, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if csvfile.tell() == 0:
                csv_writer.writerow(header)
            csv_writer.writerow(row)
        print("Data successfully added to CSV.")
    except Exception as e:
        print(f"Error writing to CSV: {e}")


if __name__ == "__main__":
    air_quality_data = get_data()

    if air_quality_data:
        update_csv(air_quality_data)