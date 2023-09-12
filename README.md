# Variable definitions
- `base_url`: Contains the domain of the website to be processed.
- `path`: Contains the path to be appended to the domain, in this context, it is the page to be processed.
- `search_path`: Contains the alternate path of the domain that returns a `path` using a search term and a few filters.
- `base_headers`: Contains the required headers and `cookie` needed to pass Cloudflare bot protection and get access to the webpage.
- `base_headers[Cookie]`: Generated from visiting the website using a normal browser, opening the network tab of the developer tab using inspect element, and refreshing to get the `Request Headers` of a `GET` action which includes the `Cookie`. It appears that this cookie should be valid for a year.

# Code block
```python3
with requests.Session() as s:
    get_page = s.get(f"{base_url}{path}", headers=base_headers)
    print(f"HTTP Response Status Code: {get_page.status_code}\n")
    with open(f"index.html","w") as f:
        f.write(get_page.text)
```
The whole functional code is encapsulated in a `with` block which instantiates a `requests` `Session` as the variable `s`.

Here, `s` acts as if it is a "persistent browser", not one that just loads one page.

As an example, `get_page = s.get(URL_1, headers=base_headers)` uses the existing session to get a page. If we'd need to load another page, say `URL_2`, we can simply do `get_another_page = s.get(URL_2, headers=base_headers)` and it is treated as if we visited `URL_1` then proceeded to visit `URL_2`.

For further processing, the returned `Response` page can be accessed by using the `get_page.text` which is a `string` or `get_page.content` which is a `Bytes object`.
