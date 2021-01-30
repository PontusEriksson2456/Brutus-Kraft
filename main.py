"""
GC8PDFN - Brutus Kraft

!!! SPOILERS NEDAN !!!
Hej! Jag ser att du är ute på jakt efter att få tag i Brutus Kraft. Då har du kommit till rätt ställe om du vill bli
spoilad på lösningen. Även om du inte vill lösa cachen själv hoppas jag att du lär dig något på vägen och att du kanske
blir inspirerad att börja labba lite med programmering. Notera gärna att du hittade hit i loggen :)
























TLDR: Brute Force av sha256

Brutus Kraft syftar till lösningsmetoden Brute Force (https://en.wikipedia.org/wiki/Brute-force_search) där man provar
alla möjliga värden för att hitta vad som söks. I detta fall är det koordinaterna som eftersöks och man får med lite
sunt förnuft välja sin sökrymd (minsta och största värden) för att inte programmet ska ta för lång tid att köra.
Vill man räkna antal försök så blir det:
    antal_försök = (lat_övre_gräns - lat_undre_gräns) * (long_övre_gräns - long_undre_gräns)

Exempel:
    lat_undre_gräns = 0
    lat_övre_gräns = 10
    long_undre_gräns = 0
    long_övre_gräns = 10
        0 + 0
        0 + 1
        0 + 2
        ...
        1 + 0
        1 + 1
        ...
        10 + 10

En extra del i problemet är att identifiera algoritmen som använts för att skapa det 'hemliga meddelandet' som står på
lappen. Har man lite kunskap om hashning kan man känna igen att det är just ett hash som är skrivet. Algoritmen hintas
i signaturen på lappen (Sha-man 256 år) vilket ska leda en till algoritmen sha256 (https://en.wikipedia.org/wiki/SHA-2).

Programmet kommer givet de angivna parametrarna prova alla värden från min till max och se om det hashade värdet av
lat + long stämmer överens med hashet som eftersöks.


Lite jobb kvarstår dock med att färdigställa programmet.
Den hash som eftersöks måste fyllas i samt att gränserna för latitude och longitude måste justeras för att inte
programmet ska ta flera timmar att köra färdigt. Tänk efter vad som är rimligt i verkliga världen i.o.m. gränsen på
3km radie.
"""
import hashlib

hash_som_eftersöks = 'här kan man fylla i hashen som eftersöks'

lat_undre_gräns = 63_00_000
lat_övre_gräns = 64_00_000

long_undre_gräns = 20_00_000
long_övre_gräns = 21_00_000


def skriv_ut_progress(i):
    if i % 100 == 0:
        print(i)


def hasha_sträng(sträng):
    return hashlib.sha256(sträng.encode('utf-8')).hexdigest()


def hitta_koordinater_som_eftersöks(lat_min, lat_max, long_min, long_max):
    # För varje värde från lat_min till lat_max
    for lat in range(lat_min, lat_max):
        skriv_ut_progress(lat)

        # För varje värde från long_min till long_max
        for long in range(long_min, long_max):
            # Slå ihop lat och long till en och samma sträng
            lat_long_sträng = str(lat) + str(long)

            hash_att_prova = hasha_sträng(lat_long_sträng)

            # Kolla om hashen vi provar är samma som hashen som eftersöks
            if hash_att_prova == hash_som_eftersöks:
                # Om så är fallet så skriver vi ut lat och long och stänger av programmet
                print(lat, long)
                exit(0)


if __name__ == '__main__':
    hitta_koordinater_som_eftersöks(lat_undre_gräns, lat_övre_gräns, long_undre_gräns, long_övre_gräns)

