import requests
import json
API_AVAIMESI = "d8954e56f941715d0f1f86e7b514e943"  # Päivitetty avaimella
PERUS_URL = "http://api.openweathermap.org/data/2.5/weather"


def hae_saatiedot(paikkakunta):
    if not API_AVAIMESI:
        print("VIRHE: API-avain puuttuu.")
        return None
    parametrit = {
        "q": paikkakunta,
        "appid": API_AVAIMESI,
        "units": "metric",
        "lang": "fi"
    }
    try:
        vastaus = requests.get(PERUS_URL, params=parametrit)
        vastaus.raise_for_status()

        data = vastaus.json()

        if data["cod"] == 200:
            lampotila = data["main"]["temp"]
            saatila_kuvaus = data["weather"][0]["description"]
            return saatila_kuvaus, lampotila
        else:
            print(f"Paikkakuntaa '{paikkakunta}' ei löytynyt tai tapahtui virhe.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Yhteysvirhe: {e}")
        return None
    except KeyError:
        print("Virhe: Säädataa ei löytynyt odotetusta rakenteesta (tarkista paikkakunnan nimi).")
        return None


if __name__ == "__main__":
    print("--- OpenWeather Sääkysely ---")
    while True:
        kaupunki = input("Anna paikkakunnan nimi (tai 'lopeta'): ").strip()
        if kaupunki.lower() == "lopeta":
            print("Ohjelma lopetetaan. Kiitos!")
            break
        if kaupunki:
            tulos = hae_saatiedot(kaupunki)
            if tulos:
                kuvaus, temp = tulos
                print("-" * 30)
                print(f"Paikkakunta: {kaupunki.capitalize()}")
                print(f"Säätila:     {kuvaus.capitalize()}")
                print(f"Lämpötila:   {temp:.1f} °C")
                print("-" * 30)
        else:
            print("Syötä kelvollinen paikkakunnan nimi.")