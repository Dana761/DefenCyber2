import requests

API_KEY = "e2ef72e1601145a01ca2d00555497f7a20b3e8d1765a06106026fd381bd5cd12daa365f03a5137f5"
IP_ADDRESS = "130.95.40.100"

url = "https://api.abuseipdb.com/api/v2/check"

headers = {
    "Accept": "application/json",
    "Key": API_KEY
}

params = {
    "ipAddress": IP_ADDRESS,
    "maxAgeInDays": 90
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()["data"]

    score = data["abuseConfidenceScore"]
    reports = data["totalReports"]
    country = data.get("countryCode", "Unknown")
    isp = data.get("isp", "Unknown")
    domain = data.get("domain", "Unknown")

    if score <= 20:
        verdict = "Safe"
    elif score <= 60:
        verdict = "Suspicious"
    else:
        verdict = "Malicious"

    print("=== Threat Intelligence Result ===")
    print(f"IP Address : {IP_ADDRESS}")
    print(f"Country    : {country}")
    print(f"ISP        : {isp}")
    print(f"Domain     : {domain}")
    print(f"Reports    : {reports}")
    print(f"Abuse Score: {score}")
    print(f"Verdict    : {verdict}")

else:
    print("Error:", response.status_code)
    print(response.text)