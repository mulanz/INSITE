# from bs4 import BeautifulSoup
# import requests
import urllib.parse
import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3

url = "https://gateway.watsonplatform.net/personality-insights/api"
username = "96e5a015-c7cc-4a04-b367-22b7960820a6"
password = "cHWmBJpvvmjN"
# Getting the webpage, creating a Response object.

personality_insights = PersonalityInsightsV3(
    version='2016-10-20',
    username=username,
    password=password)

with open(join(dirname(__file__), 'profile.json')) as profile_json:
    profile = personality_insights.profile(
        profile_json.read(), content_type='application/json',
        raw_scores=True, consumption_preferences=True)

    print(json.dumps(profile, indent=2))

# # Extracting the source code of the page.
# data = response.text
#
# # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
#
# soup = BeautifulSoup(data, 'lxml')
#
# # Extracting all the <a> tags into a list.
# tags = soup.find_all("a", "ga_job")
#
# company_list = []
# company_url_list = []
#
# # Extracting URLs from the attribute href in the <a> tags.
# for tag in tags:
#     current_url = base_url + tag.get("href")
#     this_response = requests.get(current_url)
#     this_soup = BeautifulSoup(this_response.text, 'lxml')
#     company_list.append(this_soup.find("div", class_ = "job-data-basics clearfix").find_all("span")[4].string)
#     #company_list.append(<span>H.I.M. Recruiters</span>)
# for company in company_list:
# 	new_url = 'http://www.google.com/search?&q=' + urllib.parse.quote_plus(company)
# 	redirected_html = requests.get(new_url)
# 	link_soup = BeautifulSoup(redirected_html.text, 'lxml')
# 	links = link_soup.find_all('cite')
# 	current_contents = links[0].contents
# 	current_url_string = ""
# 	for i in current_contents:
# 		current_url_string += i.string
# 	company_url_list.append(current_url_string)
#
# for i in company_url_list:
# 	api_url = "https://api.hunter.io/v2/domain-search?domain=" + i + "&api_key=5ec25a39348ec20db8456cc1abb170f55faf623d&limit=1"
# 	print(requests.get(api_url).json()["data"]["emails"][0]["value"])
