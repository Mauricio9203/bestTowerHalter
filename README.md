# Project: Farm Towers Data Analysis

This project uses Python to access an API providing data about farm towers and performs an analysis to find the tower with the highest average RSSI for a specific farm.

## Requirements

Before running this code, make sure you meet the following requirements:

- **Python 3.11.5**: If you haven't installed Python 3.11.5, you can download it from the [official Python website](https://www.python.org/downloads/).
- Necessary Python libraries are installed. You can install them using `pip`:

```bash
pip install requests pandas
```

## Installation

1. Clone this repository or download the `.py` file to your system.

2. Open a terminal and navigate to the location of the `.py` file.

## Usage

1. Execute the code using the following command:

```bash
python bestTower.py
```

2. The code will make a GET request to the API provided in the `url` variable.

3. If the request is successful (status code 200), JSON data about farm towers will be downloaded, and the analysis will be performed.

4. The average RSSI for each tower will be calculated, and the tower with the highest average will be identified.

5. The results will be printed in the console.

## Configuration

- You can change the `farmId` variable in the code to search for the tower with the highest average in a different farm. Ensure that the `farmId` is a valid UUID string.

## Notes

- Ensure that your system has access to the API at the URL provided in the `url` variable.
- Make sure you have an active internet connection for the code to make requests to the API.

## Execution in Google Colaboratory

This project can also be executed in Google Colaboratory, a cloud-based collaborative notebook environment. Click the following link to open the notebook in Google Colaboratory:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yOxzZ65xsx9vLyKCh-GofpZhbnahwMOI?usp=sharing#scrollTo=SYUY45DynjdI)

Once the notebook is loaded, you can execute the code cells one by one or select **Runtime** in the menu bar and click **Run all** to execute the entire notebook.

**Note:** Ensure you have an active internet connection for the code to make requests to the API.

## Credits

This project utilizes the Python libraries `requests` and `pandas` for handling requests and data analysis.

---
