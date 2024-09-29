def get_capital(capitals, country):
    return capitals.get(country)

capitals = {
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "UK": "London",
    "Canada": "Ottawa",
    "Japan": "Tokyo"
}

country = "USA"
print(f"The capital of {country} is {get_capital(capitals, country)}")
