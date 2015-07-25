
from gcm import GCM

REG_ID = ''
REG_IDS = []
API_KEY = 'AIzaSyBS-Wc9WOph-YE8ezZoFaZ-lt593ygrkbo'

gcm = GCM(API_KEY)
data = {'param1': 'value1', 'param2': 'value2'}

# Plaintext request
reg_id = REG_ID
gcm.plaintext_request(registration_id=reg_id, data=data)

# JSON request
reg_ids = REG_IDS
response = gcm.json_request(registration_ids=reg_ids, data=data)

# Extra arguments
res = gcm.json_request(
    registration_ids=reg_ids, data=data,
    collapse_key='uptoyou', delay_while_idle=True, time_to_live=3600
)
