import requests
import json
import math
import time
import numpy as np
import matplotlib.pyplot as plt

# What do I do:
#   I crawl the raider.io API gently and make graphs and statistics for Mythic Plus seasons.
#
# Prerequistes:
#   pip3 install -r requirements.txt
#   pip3 install requests numpy matplotlib
#
# Extra Notes:
#   Raider.io's API is a weird mess. Really. Unauthenticated, inconsistent. You can tell it's a fan project at heart.
#
#   Some classes use the /api/mythic-plus/rankings/specs endpoint and some use ../rankings/characters.
#
#   That means if you want to select between one class or another, you have different URL endpoints. The constant TYPE
#   is used to add in new endpoints (in the hackiest way possible).
#
#   KEYSTONE_ACHIEVEMENT_LINES is used to draw on the amount of points required to score a mythic keystone achievement.
#   Later in the season, you'll see groups of players stop playing as they reach these lines (because they've achieved
#   what they wanted.) It's kinda neat to watch the data.
#
# Adding new endpoints (using Firefox, but adapt for your browser of choice)
#   0. Open up Firebug/Inspector
#   1. In the Inspector, click on the Network tab and refresh the page
#   2. In the Inspector, in Filter URLs, type in "domain:raider.io url:*api*" without quotes
#   3. Go to raider.io (https://raider.io/characters/eu/tarren-mill/Brewery) and scroll down to Class Ranks
#   4. Click on the number under the (H) Realm / Monk Tanks (or whatever spec/option you want to graph) and observe the
#      inspector. You'll notice a new URL being added ("characters?region=eu...")
#   5. Right click on the URL from the inspector and copy value. Confirm the URL looks like this:
#      https://raider.io/api/mythic-plus/rankings/characters?region=eu&season=season-df-1&realm=tarren-mill...
#      This will be your API endpoint to scan.

TYPE = "healer-count"
KEYSTONE_ACHIEVEMENT_LINES = True
API_REQUEST_WAIT_IN_SECONDS = 0.5

# The API URL to hit.
base_url = str()

# The title on the matpltlib graph
title = str()

if TYPE == "tank-monk":
    base_url = "https://raider.io/api/mythic-plus/rankings/specs?region=eu&season=season-df-1&realm=tarren-mill&class=monk&spec=tank&faction=horde&page="
    title = "Horde - Monk - Brewmaster"
    KEYSTONE_ACHIEVEMENT_LINES = True

if TYPE == "dps-dh":
    base_url = "https://raider.io/api/mythic-plus/rankings/characters?region=eu&season=season-df-1&realm=tarren-mill&class=demon-hunter&role=dps&faction=horde&page="
    title = "Horde - Demon Hunter - Havok"
    KEYSTONE_ACHIEVEMENT_LINES = True

if TYPE == "dps-evoker":
    base_url = "https://raider.io/api/mythic-plus/rankings/characters?region=eu&season=season-df-1&realm=tarren-mill&class=evoker&role=dps&faction=horde&page="
    title = "Horde - Evoker - Devestation"
    KEYSTONE_ACHIEVEMENT_LINES = True

if TYPE == "dps-warlock":
    base_url = "https://raider.io/api/mythic-plus/rankings/specs?region=eu&season=season-df-1&realm=tarren-mill&class=warlock&spec=demonology&faction=horde&page="
    title = "Horde - Warlock - Demonology"
    KEYSTONE_ACHIEVEMENT_LINES = True

# These two below are used for counting the number of players of a class and spec, rather than making any graphs.
# They will result in behaviour exiting early in the script.

if TYPE == "tank-count":
    base_url = "https://raider.io/api/mythic-plus/rankings/characters?region=world&season=season-df-1&class=all&role=tank&page="
    title = ""
    KEYSTONE_ACHIEVEMENT_LINES = False

if TYPE == "healer-count":
    base_url = "https://raider.io/api/mythic-plus/rankings/characters?region=world&season=season-df-1&class=all&role=healer&page="
    title = ""
    KEYSTONE_ACHIEVEMENT_LINES = False

final_list = list()

# Keep a track of classes and specs if we're going to do counts instead of graphs
class_spec_count = {
    "evoker_preservation": 0,
    "priest_holy": 0,
    "priest_discipline": 0,
    "paladin_holy": 0,
    "monk_mistweaver": 0,
    "druid_restoration": 0,
    "shaman_restoration": 0
}

# We will allow the script to scan 5000 API requests. You get 20 characters back per API request by default. Would there
# ever be a season with 100 000 players of a spec or role?
MAX = 5000

for i in range(0, MAX):
    # Send the API request, and iterate over each parameter "page", grabbing 20 characters.
    r = requests.get("{0}{1}".format(base_url, i))

    if r.text is None:
        break

    print("{0}/{1}".format(i, MAX))

    # Did the JSON response make sense? If not, gtfo.
    try:
        results = json.loads(r.text)
    except:
        print(r.headers)
        print(r.text)
        exit()

    # JSON response made sense but there were no characters for the class and spec combination.
    if len(results["rankings"]["rankedCharacters"]) == 0:
        break

    # If we're doing statistics only (and not graphs) then we'll execute this fragment and gtfo...
    if TYPE == "tank-count" or TYPE == "healer-count":
        for result in results["rankings"]["rankedCharacters"]:
            cls_name = "{0}-{1}".format(
                result["character"]["class"]["slug"],
                result["character"]["spec"]["slug"]
            )
            cls_name = cls_name.replace("-", "_")

            try:
                class_spec_count[cls_name] = class_spec_count[cls_name] + 1
            except:
                pass

            # 20 per page, so top 200 players
            if i > 10:
                print(class_spec_count)
                labels = class_spec_count.keys()
                sizes = class_spec_count.values()

                fig1, ax1 = plt.subplots()
                ax1.pie(
                    sizes,
                    labels=labels,
                    autopct='%1.1f%%',
                    shadow=True,
                    startangle=90
                )

                # Equal aspect ratio ensures that pie is drawn as a circle.
                ax1.axis('equal')

                plt.show()
                exit()

    # ...or just get the scores of all the players and make the graph
    else:
        for result in results["rankings"]["rankedCharacters"]:
            final_list.append(math.floor(result["score"]))

    # Be gentle the raider.io API and only make two requests per second. They do rate limit and these was a stable
    # choice.
    time.sleep(API_REQUEST_WAIT_IN_SECONDS)

# This block of code draws the matpltlib graphs from the data we've just harvested. You don't really need to edit
# anything below this point.
bins = np.linspace(
    math.ceil(min(final_list)),
    math.floor(max(final_list)),
    50 # how many 'count' should be in each bar of the graph
)

plt.xlim([min(final_list)-5, max(final_list)+5])

plt.hist(final_list, bins=bins, alpha=0.5)

# Mythic plus rating requirements for each of the keystone achievements.
plt.axvline(750, c='yellow')
plt.axvline(1500, c='orange')
plt.axvline(2000, c='red')
plt.axvline(2500, c='blue')

plt.title("Raider.io score - Tarren Mill - {}".format(title))
plt.xlabel('IO Score (bin size = 50)')
plt.ylabel('Count')

plt.show()
