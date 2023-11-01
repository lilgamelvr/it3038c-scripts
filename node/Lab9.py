import requests

url = "http://localhost:3000"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        widget_dict = {}

        for widget in data:
            widget_name = widget["name"]
            widget_color = widget["color"]
            widget_dict[widget_name] = widget_color

        for widget_name, widget_color in widget_dict.items():
            print(f"{widget_name} is {widget_color}.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")