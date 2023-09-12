import requests

base_url = "https://www.zoopla.co.uk/"
path = "for-sale/property/rugby/?q=Rugby&radius=20&results_sort=newest_listings&search_source=for-sale"
search_path = "api/search/resolver/?price_frequency=per_month&results_sort=newest_listings&new_homes=include&retirement_homes=true&shared_ownership=true&include_shared_accommodation=true&search_source=for-sale&section=for-sale&view_type=list&radius=20&q=Rugby&orig_q=Rugby&identifier=rugby"
base_headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "www.zoopla.co.uk",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept": "*/*",
    "X-Requested-With":"XMLHttpRequest",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Cookie": 'zid=91a5d25c21e541d2a129015a6e4e9e9f; zooplasid=91a5d25c21e541d2a129015a6e4e9e9f; zooplapsid=650a0a9d3cf44cf78fcee47d15f46351; ajs_anonymous_id=e68b6eadb92543f4b80f597844e50ebf; __cf_bm=fW4y8XWB6XuE7qPPToCRslOP030xhNILCF2D8vPj13E-1694494678-0-Aevov0UQRjy6ZLROh7mhtD0WupjCkPIoux6tIzx+Takjz/aNZ13H9t8er/5802gvByEypajhaGYVsczrRRjk/8g=; base_device_id=bc1fb82f-124a-4bc9-a1a4-5be1c9c6fb23; base_session_count=1; base_session_start_page=https://www.zoopla.co.uk/for-sale/property/rugby/?identifier=rugby&radius=20; base_request=https://www.zoopla.co.uk/for-sale/property/rugby/; base_session_id=c40d10ed-52a1-402f-9ea2-7526a4a33985; forced_features={}; forced_experiments={}; cf_clearance=asmu4bBVhAjnPG39W7WXIjf47sJU20zdJVly8D_5BXo-1694494680-0-1-dfa07fce.77b5a10f.88a1202e-0.2.1694494680; cookie_consents={"schemaVersion":4,"content":{"brand":1,"consents":[{"apiVersion":1,"stored":false,"date":"Tue, 12 Sep 2023 04:58:04 GMT","categories":[{"id":1,"consentGiven":true},{"id":3,"consentGiven":false},{"id":4,"consentGiven":false}]}]}}; active_session=anon'
}

with requests.Session() as s:
    get_page = s.get(f"{base_url}{path}", headers=base_headers)
    print(f"HTTP Response Status Code: {get_page.status_code}\n")
    with open(f"index.html","w") as f:
        f.write(get_page.text)
    print(get_page.content)