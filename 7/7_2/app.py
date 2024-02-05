from external_api import fetch_data_from_api, process_data

def get_and_process_data():
    data = fetch_data_from_api()
    if data:
        return process_data(data)
    else:
        return None