# Data for locations
locations = [
    {"location_id": 1000, "street_address": "1297 Via Cola di Rie", "postal_code": "989", "city": "Roma", "state_province": "", "country_id": "IT"},
    {"location_id": 1100, "street_address": "93091 Calle della Te", "postal_code": "10934", "city": "Venice", "state_province": "", "country_id": "IT"},
    {"location_id": 1200, "street_address": "2017", "postal_code": "1689", "city": "Shinjuku-ku", "state_province": "Tokyo Prefecture", "country_id": "JP"},
    {"location_id": 1300, "street_address": "9450 Kamiya-cho", "postal_code": "6823", "city": "Hiroshima", "state_province": "", "country_id": "JP"},
    {"location_id": 1400, "street_address": "2014 Jabberwocky Rd", "postal_code": "26192", "city": "Southlake", "state_province": "Texas", "country_id": "US"},
    {"location_id": 1500, "street_address": "2011 Interiors Blvd", "postal_code": "99236", "city": "South San Francisco", "state_province": "California", "country_id": "US"},
    {"location_id": 1600, "street_address": "2007 2004 Charade Rd", "postal_code": "50090", "city": "South Brunswick", "state_province": "New Jersey", "country_id": "US"},
    {"location_id": 1700, "street_address": "98199 Seattle Blvd", "postal_code": "98199", "city": "Seattle", "state_province": "Washington", "country_id": "US"},
    {"location_id": 1800, "street_address": "147 Spadina Ave", "postal_code": "MSV 2L7", "city": "Toronto", "state_province": "Ontario", "country_id": "CA"}
]

# Data for countries
countries = [
    {"country_id": "AR", "country_name": "Argentina", "region_id": 2},
    {"country_id": "AU", "country_name": "Australia", "region_id": 3},
    {"country_id": "BE", "country_name": "Belgium", "region_id": 1},
    {"country_id": "BR", "country_name": "Brazil", "region_id": 2},
    {"country_id": "CA", "country_name": "Canada", "region_id": 2},
    {"country_id": "CH", "country_name": "Switzerland", "region_id": 1},
    {"country_id": "CN", "country_name": "China", "region_id": 3},
    {"country_id": "DE", "country_name": "Germany", "region_id": 1}
]

# Find Canadian country ID
canadian_country_id = [country['country_id'] for country in countries if country['country_name'] == "Canada"][0]

# Find locations in Canada
canadian_locations = [location for location in locations if location['country_id'] == canadian_country_id]

# Print results
for location in canadian_locations:
    print(f"Location ID: {location['location_id']}, Address: {location['street_address']}, City: {location['city']}, State: {location['state_province']}, Country: Canada")