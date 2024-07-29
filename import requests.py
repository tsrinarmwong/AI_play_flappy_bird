import requests
from requests.models import HTTPBasicAuth

response = requests.get(
    'https://api.clickup.com/api/v2/task/1py8vgm/',
    auth=HTTPBasicAuth('pk_25541319_2K0B16H4CTHLOQE9GQSTYJTGZ18OG2H5','8ceM81ZHJw')
)

print(response)