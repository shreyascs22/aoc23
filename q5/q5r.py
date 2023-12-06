lines = [line.strip() for line in open("q5.txt").readlines()]
seeds = lines[0].split(':')[1].split()
seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temp, temp_humidity, humidity_loc = {}, {}, {}, {}, {}, {}, {}
seed_soilarr , soil_fertilizerarr, fertilizer_waterarr, water_lightarr, light_temparr, temp_humidityarr, humidity_locarr = [],[],[],[],[],[],[]
seed_soildict, soil_fertilizerdict, fertilizer_waterdict, water_lightdict, light_tempdict, temp_humiditydict, humidity_locdict = {},{},{},{},{},{},{}
def data(arr,index):
    j = 0
    while index < len(lines):
        arr.append([lines[index]])
        if (index + 1 < len(lines) and lines[index + 1] == ""):
            break
        index += 1
        j += 1
    return arr
def insert(arr,dict):
    for sublist in arr:
        items = sublist[0].split()
        source, destination, repetitions = items[0], items[1], int(items[2])
        s = int(source)
        r = int(destination)
        for i in range(repetitions):
            print(i/repetitions)
            dict[r] = int(s)
            s += 1
            r += 1
    return dict
def fill(dict):
    for i in range(100):
        if(i not in dict):
            dict[i] = i
    return dict
headers = ["seed-to-soil map:","soil-to-fertilizer map:","fertilizer-to-water map:","water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]
index = lines.index("seed-to-soil map:")
seed_soilarr = data(seed_soilarr,index+1)
index = lines.index("soil-to-fertilizer map:")
soil_fertilizerarr = data(soil_fertilizerarr,index+1)
index = lines.index("fertilizer-to-water map:")
fertilizer_waterarr = data(fertilizer_waterarr,index+1)
index = lines.index("water-to-light map:")
water_lightarr = data(water_lightarr,index+1)
index = lines.index("light-to-temperature map:")
light_temparr = data(light_temparr,index+1)
index = lines.index("temperature-to-humidity map:")
temp_humidityarr = data(temp_humidityarr,index+1)
index = lines.index("humidity-to-location map:")
humidity_locarr = data(humidity_locarr,index+1)
seed_soildict = insert(seed_soilarr,seed_soildict)
soil_fertilizerdict = insert(soil_fertilizerarr,soil_fertilizerdict)
fertilizer_waterdict = insert(fertilizer_waterarr,fertilizer_waterdict)
water_lightdict = insert(water_lightarr,water_lightdict)
light_tempdict = insert(light_temparr,light_tempdict)
temp_humiditydict = insert(temp_humidityarr,temp_humiditydict)
humidity_locdict = insert(humidity_locarr,humidity_locdict)
seed_soildict = fill(seed_soildict)
soil_fertilizerdict = fill(soil_fertilizerdict)
fertilizer_waterdict = fill(fertilizer_waterdict)
water_lightdict = fill(water_lightdict)
light_tempdict = fill(light_tempdict)
temp_humiditydict = fill(temp_humiditydict)
humidity_locdict = fill(humidity_locdict)
for seed in seeds:
    print(seed)
    val = humidity_locdict[temp_humiditydict[light_tempdict[water_lightdict[fertilizer_waterdict[soil_fertilizerdict[seed_soildict[int(seed)]]]]]]]
    print(val)