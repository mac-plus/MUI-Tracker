import requests
from bs4 import BeautifulSoup

# Load the HTML file
with open("index.html", "r", encoding="utf-8") as file:
    html = file.read()

# Fetch the live page
url = "https://aeinfo.nhs.wales/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract patient data for each hospital
# NOTE: These class names or structure may change depending on the live site layout
hospitals = {
    "Barry Hospital MIU": "Barry Hospital",
    "Royal Gwent Hospital MIU": "Royal Gwent Hospital",
    "University Hospital of Wales (UHW) Emergency Department": "University Hospital of Wales"
}

# Find data on the page
data = {}
for section in soup.find_all("div", class_="ae-card"):
    name = section.find("h2")
    if not name:
        continue
    hospital_name = name.text.strip()
    if hospital_name in hospitals.values():
        count_tag = section.find("span", class_="ae-count")
        if count_tag:
            count = count_tag.text.strip()
            data[hospital_name] = count

# Replace current patient numbers in HTML
for html_name, nhs_name in hospitals.items():
    if nhs_name in data:
        html = html.replace(
            f"<h2>{html_name}</h2>\n  <div class=\"patients",
            f"<h2>{html_name}</h2>\n  <div class=\"patients".replace("Current Patients: ", f"Current Patients: {data[nhs_name]}")
        )

# Save the updated HTML
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html)

print("HTML updated with live patient numbers.")
