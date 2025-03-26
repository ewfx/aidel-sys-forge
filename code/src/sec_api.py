import requests

def get_cik():
	
	api_url = "https://www.sec.gov/files/company_tickers.json"
	headers = {
		"User-Agent": "My Python Script - For research purposes (myemail@example.com)",
		"Accept-Encoding": "gzip, deflate",
		"Accept": "*/*",
		"Connection": "keep-alive"
	}
	response = requests.get(api_url, headers=headers)
	
	if response.status_code != 200:
		print("Failed to get CIK Data", response.status_code)
		return 0
	
	data = response.json()
	res = {}
	
	for i, obj in data.items():
		res[obj['title']] = str(obj['cik_str'])
	
	return res


def find_cik_number(entity_name, cik_data):
	
	try:
		cik_number = cik_data[entity_name]
		return cik_number.zfill(10)
		
	except Exception:
		print('Entity Not Found')
		return 0
	


def get_filings_for_entity(entity_name, cik_data):
	
	if cik_data == 0:
		cik_data = get_cik()
	
	if cik_data == 0:
		return 0
	
	entity_cik = find_cik_number(entity_name, cik_data)
	
	if entity_cik == 0:
		return 0
	
	api_url = f"https://data.sec.gov/submissions/CIK{entity_cik}.json"
	headers = {
		"User-Agent": "My Python Script - For research purposes (myemail@example.com)",
		"Accept-Encoding": "gzip, deflate",
		"Accept": "*/*",
		"Connection": "keep-alive"
	}
	response = requests.get(api_url, headers=headers)
	
	if response.status_code != 200:
		print("Failed to get CIK Data", response.status_code)
		return 0
	
	return response.json()

