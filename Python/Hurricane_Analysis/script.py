# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def strings_to_dollars(list):
    new_list = []
    for item in list:
        if item == "Damages not recorded":
            new_list.append(item)
        else:
            if item[-1] == "M":
                item = float(item[:-1]) * 1000000
                new_list.append(item)
            elif item[-1] == "B":
                item = float(item[:-1]) * 1000000000
                new_list.append(item)
            else:
                print("Something went wrong.")
    return new_list
                    
new_damages = strings_to_dollars(damages)
#print(new_damages)

# write your construct hurricane dictionary function here:
def construct_hurricane_dictionary(names_list, months_list, years_list, max_sustained_winds_list, areas_affected_list, damages_list, deaths_list):
    new_dictionary = {}
    for i in range(len(names_list)):
        new_dictionary[names_list[i]] = {"Name": names_list[i], "Month": months_list[i], "Year": years_list[i], "Max Sustained Wind": max_sustained_winds_list[i], "Areas Affected": areas_affected_list[i], "Damage": damages_list[i], "Deaths": deaths_list[i]}
    return new_dictionary

hurricane_dictionary = construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)
#print(hurricane_dictionary["Cuba I"]["Damage"])

# write your construct hurricane by year dictionary function here:
def convert_to_year(dictionary):
    new_dictionary = {}
    for item in dictionary:
        current_year = dictionary[item]["Year"]
        current_item = dictionary[item]
        if current_year not in new_dictionary:
            new_dictionary[current_year] = [current_item]
        else:
            new_dictionary[current_year].append(current_item)
    return new_dictionary

year_dictionary = convert_to_year(hurricane_dictionary)
#print(year_dictionary[1932])

# write your count affected areas function here:
def areas_affected_frequency(hurricane_dictionary):
    new_dictionary = {}
    for hurricane in hurricane_dictionary:
        for area in hurricane_dictionary[hurricane]["Areas Affected"]:
            if area not in new_dictionary:
                new_dictionary[area] = 1
            else:
                new_dictionary[area] += 1
    return new_dictionary

area_count_dictionary = areas_affected_frequency(hurricane_dictionary)
#print(area_count_dictionary)

# write your find most affected area function here:
def most_affected(area_dictionary):
    area = ""
    affect_count = 0
    for key, value in area_dictionary.items():
        if value > affect_count:
            area = key
            affect_count = value
    return area, affect_count

most_affected_area = most_affected(area_count_dictionary)
#print(most_affected_area)

# write your greatest number of deaths function here:
def most_deaths(hurricane_dictionary):
    hurricane_name = ""
    death_count = 0
    for hurricane in hurricane_dictionary:
        if hurricane_dictionary[hurricane]["Deaths"] > death_count:
            death_count = hurricane_dictionary[hurricane]["Deaths"]
            hurricane_name = hurricane_dictionary[hurricane]["Name"]
    return hurricane_name, death_count

highest_deaths = most_deaths(hurricane_dictionary)
#print(highest_deaths)

# write your categorize by mortality function here:
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}

def mortality_rating(hurricane_dictionary):
    mortality_dictionary = {key: [] for key in range(5)}
    for hurricane in hurricane_dictionary:
        for i in range(4):
            if hurricane_dictionary[hurricane]["Deaths"] > mortality_scale[i] and hurricane_dictionary[hurricane]["Deaths"] <= mortality_scale[i + 1]:
                mortality_dictionary[i + 1].append(hurricane_dictionary[hurricane]["Name"])       
    return mortality_dictionary

mortality_dictionary = mortality_rating(hurricane_dictionary)
#print(mortality_dictionary)

# write your greatest damage function here:
def most_damage(hurricane_dictionary):
    hurricane_name = ""
    damage_count = 0
    for hurricane in hurricane_dictionary:
        if hurricane_dictionary[hurricane]["Damage"] != "Damages not recorded":
            if hurricane_dictionary[hurricane]["Damage"] > damage_count:
                damage_count = hurricane_dictionary[hurricane]["Damage"]
                hurricane_name = hurricane_dictionary[hurricane]["Name"]
    return hurricane_name, damage_count

highest_damage = most_damage(hurricane_dictionary)
#print(highest_damage)


# write your catgeorize by damage function here:
damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}

def damage_rating(hurricane_dictionary):
    damage_dictionary = {key: [] for key in range(5)}
    for hurricane in hurricane_dictionary:
        for i in range(4):
            if hurricane_dictionary[hurricane]["Damage"] != "Damages not recorded":
                if hurricane_dictionary[hurricane]["Damage"] > damage_scale[i] and hurricane_dictionary[hurricane]["Damage"] <= damage_scale[i + 1]:
                    damage_dictionary[i + 1].append(hurricane_dictionary[hurricane]["Name"])   
    return damage_dictionary

damage_dictionary = damage_rating(hurricane_dictionary)
#print(damage_dictionary)