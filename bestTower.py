import requests
import pandas as pd
import io
import requests

# URL of the endpoint
url = 'https://api.onizmx.com/lambda/tower_stream'

# Make a GET request
response = requests.get(url)

# Check the status code of the response
if response.status_code == 200:
    # Convert the JSON response into a Python list
    urls = response.json()
else:
    print('Error making GET request. Status code:', response.status_code)

def bestTower(urls, farmId):   
    # List to store CSV file data
    dataframes = []

    # Iterate over the URLs and download CSV data
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            # Read the CSV file and convert it into a pandas DataFrame
            csv_data = pd.read_csv(io.StringIO(response.text))
            dataframes.append(csv_data)
        else:
            print(f'Error downloading CSV file from: {url}')

    # Merge the DataFrames into one
    merged_dataframe = pd.concat(dataframes, ignore_index=True)

    # Filter the DataFrame for a specific farmId, for example, farmId = 1
    specific_farmId = farmId
    filtered_data = merged_dataframe[merged_dataframe['farmId'] == specific_farmId]

    # Calculate the average rssi for each towerId
    average_rssi_per_tower = filtered_data.groupby('towerId')['rssi'].mean().reset_index()

    # Identify the tower with the highest average
    tower_with_highest_average = average_rssi_per_tower.loc[average_rssi_per_tower['rssi'].idxmax()]

    # Convert to dictionaries
    average_rssi_per_tower_dict = average_rssi_per_tower.to_dict(orient='records')
    tower_with_highest_average_dict = tower_with_highest_average.to_dict()

    # Print the DataFrame with the average rssi for each towerId
    print("___________________________________________________________________")
    print("Farm Towers Details")
    print(average_rssi_per_tower)
    print("___________________________________________________________________")
    return tower_with_highest_average

farmId = "0b515fbb-2981-4f99-9141-dce1c46beb6f"
theBestTower = bestTower(urls, farmId)

print("________________________________________________________________________________________________________________")
print("The best tower is:")
print(theBestTower)