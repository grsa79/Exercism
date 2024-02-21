def convert(number):
    rain_sound = ""
    """
    initial solution with four if statements
    if number % 3 == 0:
        rain_sound += "Pling"
    if number % 5 == 0:
        rain_sound += "Plang"
    if number % 7 == 0:
        rain_sound += "Plong"
    if rain_sound == "":
        rain_sound = str(number)
    
    now I try it with one...
    """
    sound_scape = ["Pling", "Plang", "Plong"]

    for index, sound in enumerate(sound_scape):
        if (number % (2*index+3) == 0):
            rain_sound += sound
    if rain_sound =="":
        rain_sound = str(number)
    return rain_sound
