import requests

url = "https://remoteok.io/api"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    jobs = response.json()[1:]  # First item is metadata, skip it
    for job in jobs[:100]:  # Get first 100 jobs
        print(f"🔹 **{job['position']}**")
        print(f"🏢 **Company:** {job['company']}")
        print(f"🔗 **Apply Here:** {job['url']}")
        print("-" * 50)
else:
    print(f"Failed to fetch jobs. Status Code: {response.status_code}")
