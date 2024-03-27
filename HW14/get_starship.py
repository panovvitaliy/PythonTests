import requests
import json


def get_starship_data(starship_name):
    # Make GET request to SWAPI for all starships
    url = 'https://swapi.dev/api/starships/'
    response = requests.get(url)

    # Find Millennium Falcon
    for starship in response.json()['results']:
        if starship['name'] == starship_name:
            return starship
    return None


def get_pilots_data(pilots_urls):
    pilots_data = []
    for url in pilots_urls:
        response = requests.get(url)
        pilot = response.json()
        pilot_homeworld_data = requests.get(pilot["homeworld"])
        pilot_homeworld_name = pilot_homeworld_data.json()["name"]
        pilot_data = {
            "name": pilot["name"],
            "height": pilot["height"],
            "mass": pilot["mass"],
            "homeworld_name": pilot_homeworld_name,
            "homeworld_url": pilot["homeworld"]
        }
        pilots_data.append(pilot_data)
    return pilots_data


def main():
    starship_name = "Millennium Falcon"
    starship_data = get_starship_data(starship_name)

    if starship_data:

        # Extract pilot data
        pilots_urls = starship_data["pilots"]
        pilots_info = get_pilots_data(pilots_urls)

        # Extract relevant starship data
        starship_info = {
            "name": starship_data["name"],
            "max_atmosphering_speed": starship_data["max_atmosphering_speed"],
            "starship_class": starship_data["starship_class"],
            "pilots": pilots_info
        }

        # Save to JSON file
        with open("millennium_falcon_data.json", "w") as json_file:
            json.dump(starship_info, json_file, indent=4)
        print("Data saved to millennium_falcon_data.json")
    else:
        print(f"{starship_name} not found in the data.")


if __name__ == "__main__":
    main()
