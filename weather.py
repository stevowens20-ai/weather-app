import requests
import os 
from dotenv import load_dotenv
from pprint import pprint
import sys


load_dotenv()

def get_current_weather (name):
    print (
        """
        =======================================================================
        
                   GET CURRENT WEATHER CONDITIONS ⛅🌞 
                   
                   
                        from every where 
        
        this system find all wheather conditions for cities and countries
        ========================================================================
        """
        )
    
    city = input(f"Please,{name} our dear user type a country or a city name : ").strip()
    
    if city.lower().endswith(" city"):
        city = city[:-5].strip()
    
    request_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv('API_KEY')}&q={city}&units=metric"
    
    params = {
        "appid" : "Api_key",
        "q" : "city",
        "units" : "metric"
    }
    
    try:
        # getting weather information
        weather_data = requests.get(
            request_url,
            params=params,
            timeout= 10
            
            ).json()
    
    
    # except requests.exceptions.HTTPError:
    #     print("""
    #         City or country not found!

    #         Please check the spelling and try again.
    #     """)
    #     return
    
    except requests.exceptions.ConnectionError:
        print("""
                 Poor connecting network ...
                 
                 please wait ...
                 
                 connecting error!, please check you internet connection !
                 
              """)
        return
    
    except requests.exceptions.Timeout:
        print("""
                Current weather checking took so long ....
                
                Time out, please try again later ...
                
              """)
        return
    
    except requests.exceptions.RequestException:
        print("\n    something went wrong, please try again later ..\n")
        return
    
    finally:
        print("\nCurrent weather checking has been completed, thank you \n")
        
    
      # simplified for the user's only 
    
    print(  
        f"""
        ---------------------------------------------------------
           Current weather results ; 
                   Current weather condition for : {weather_data['name']} 
                   Current temperature : {weather_data['main']['temp']:.2f} C
                   Feels like :  {weather_data['main']['feels_like']:.2f}
                   Current humidity  : {weather_data['main']['humidity']:.1f} C
                   Current pressure {weather_data['main']['pressure']:.1f}
                   Current weather : {weather_data['weather'][0]['description']}
                    
        ----------------------------------------------------------
        """)
    
    print("\nIs there any other city or country you could like to check for?")
    while True:
        wanna_check = input("""
                            Please chose;
                                   'yes' for weather checking again 
                                   'quit' for quitting 
                                   Your chose : """)
        if wanna_check.lower() not in ['yes','quit']:
            continue
        else:
            break
    
    if wanna_check.lower() == "yes":
        return get_current_weather()
    
    else:
        sys.exit(f"\nThank you {name} for you best support\n")
        
        
        
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Provide a personalized name "
    )
    
    parser.add_argument(
        "-n", "-name", metavar="True", 
        required=True, help="the name of the person checking the weather"
    )
    args = parser.parse_args()
    
    get_current_weather(args.name)