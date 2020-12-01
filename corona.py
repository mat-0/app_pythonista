# import
from requests import get
import re
import json
import pathlib
import os

root = pathlib.Path(__file__).parent.parent.resolve()
city = os.getenv('city_code') or 'Cheltenham'

def get_covid_data(num_days):
    endpoint = (
        f'https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=ltla;areaName={city}&'
        'structure={"date":"date","newCases":"newCasesByPublishDate","deaths":"newDeathsByDeathDate"}'
    )
    response = get(endpoint, timeout=10)
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
    string_builder = ""
    data = response.json()['data'][:num_days]
    for i in range(0, num_days):
        string_builder += (f"\n• {0 if data[i]['newCases'] == None else data[i]['newCases']} new cases & "
        f"{0 if data[i]['deaths'] == None else data[i]['deaths']} deaths ")
        if i == 0:
            string_builder += "today"
        elif i == 1:
            string_builder += "yesterday"
        else:
            string_builder += f"on {data[i]['date']}"
    return string_builder


# output
if __name__ == "__main__":
    string_output = get_covid_data(100)
    print(string_output)
