from pypresence import Presence
import time
from datetime import datetime
import json

with open("config.json", "r", encoding='utf-8') as config_json_file:
    config_json = json.load(config_json_file)

with open("profiles.json", "r", encoding='utf-8') as profiles_json_file:
    profiles_json = json.load(profiles_json_file)

active_profile = config_json["active_profile"]
config_profile = profiles_json[active_profile]

application_id = config_profile['application_id']
profile = profiles_json[active_profile]['presence']


def check_if_none(element_name):
    return profile[element_name] if profile[element_name].strip() != '' else None

def check_if_on(element_name):
    if profile[element_name].lower().strip() == 'start':
        return time.time()
    
    elif profile[element_name].strip().isnumeric():
        return profile[element_name].strip()

    else:
        return None

def check_if_party_is_empty(element_name):
    if profile[element_name] == [0,0]:
        return None
    
    elif type(profile[element_name]) == list and len(profile[element_name]) == 2 and profile[element_name][0] > 0: 
        return profile[element_name]

    else:
        return None

def check_buttons(element_name):
    buttons_loaded = []
    if profile[element_name]['first']['label'].strip() != '' and len(profile[element_name]['first']['label'].strip()) > 3:
        if profile[element_name]['first']['url'].strip() != '' and len(profile[element_name]['first']['url'].strip()) > 3:
            buttons_loaded.append({"label": profile[element_name]['first']['label'], "url": profile[element_name]['first']['url'].strip()})
   
    if profile[element_name]['second']['label'].strip() != '' and len(profile[element_name]['second']['label'].strip()) > 3:
        if profile[element_name]['second']['url'].strip() != '' and len(profile[element_name]['second']['url'].strip()) > 3:
            buttons_loaded.append({"label": profile[element_name]['second']['label'], "url": profile[element_name]['second']['url'].strip()})

    if len(buttons_loaded) == 0:
        return None

    elif 3 > len(buttons_loaded) > 0:
        return buttons_loaded

def curretly_time():
    return datetime.now().strftime("%H:%M:%S")

RPC = Presence(application_id)
RPC.connect()

print("\n" * 100)
print(f"[{curretly_time()}] Started!")

RPC.update(
    details=check_if_none('upper_line_description'),
    state=check_if_none('lower_line_description'),
    party_size=check_if_party_is_empty('party_size'),
    start=check_if_on('start_time_count'),
    end=check_if_on('end_time_count'),
    large_image=check_if_none('large_image'),
    large_text=check_if_none('large_image_description'),
    small_image=check_if_none('small_image'),
    small_text=check_if_none('small_image_description'),
    buttons=check_buttons('button')
)

input()