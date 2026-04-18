class weather:
    
    def weather_check(self, temp:float)->str:
        if temp < 0:
            return "It's freezing outside!"
        elif temp < 15:
            return "It's a bit chilly."
        elif temp < 25:
            return "The weather is pleasant."
        else:
            return "It's hot outside!"
        
    def rain_check(self, rain_chance:float)->str:
        if rain_chance > 0.7:
            return "It's likely to rain. Don't forget your umbrella!"
        elif rain_chance > 0.3:
            return "There's a chance of rain. You might want to carry an umbrella."
        else:
            return "It's unlikely to rain today."