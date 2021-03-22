import json
import os
import requests
from requests.exceptions import HTTPError
from decouple import config

url = config('AMP_STATIC_API_GRAPHQL_URI')
print('url: ' + url)

data = {'query': '{ productions(first: 20, where: {categoryNotIn: 21}) { edges { node { id title productionDetails { ampEventOneParagraphSummary } productionGallery { ampEventPhotoCredit ampEventPhotos { title uri } } productionDates { ampEventStartDate ampEventDatesTimes { ampEventDateTime } } productionTickets { ampEventExternalTicketing ampEventGetTicketsUrl ampEventTicketPrices { ampEventAdmissionLevel ampEventPrice } } productionPeople { fieldGroupName ampEventFeaturing ampEventFullBand ampEventFullCast ampEventStarring ampProductionTeam ampEventPersonnel { ampEventPersonnelName ampEventPersonnelRole } ampEventCrew { ampEventCrewName ampEventCrewRole } } featuredImage { node { sourceUrl(size: MEDIUM_LARGE) } } link } } } }'}

base_path = 'data/'
os.makedirs(base_path, exist_ok=True)

try:
    response = requests.post(url, data = data)
    print('status_code: ' + str(response.status_code))

    response.raise_for_status()
    jsonResponse = response.json()
    filename = base_path + 'upcoming-productions.json'
    with open(filename, 'w') as f:
        json.dump(jsonResponse, f, ensure_ascii=False)

except HTTPError as http_err:
    print('HTTP error occurred: ' +  str(http_err))
    raise
except Exception as err:
    print('Error occurred: ' + str(err))
    raise
