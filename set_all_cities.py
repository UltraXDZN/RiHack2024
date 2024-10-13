import os
import django

# Set up Django environment to use the models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HackatonTemplate.settings')
django.setup()

from location.models import County, City

# The dictionary containing counties and their corresponding cities
gradovi_zupanije = {
    "Istarska županija": [
        # Major cities and towns
        "Pula", "Pazin", "Rovinj", "Poreč", "Umag", "Labin", "Buzet", "Vodnjan", "Buje", "Novigrad", "Žminj", "Fažana",
        "Medulin",
        # Additional municipalities
        "Bale", "Barban", "Brtonigla", "Gračišće", "Grožnjan", "Kanfanar", "Karojba", "Kaštelir-Labinci", "Kršan",
        "Lanišće", "Ližnjan", "Lupoglav", "Marčana", "Motovun", "Oprtalj", "Pićan", "Raša", "Sveti Lovreč",
        "Sveti Petar u Šumi", "Svetvinčenat", "Tar-Vabriga", "Tinjan", "Višnjan", "Vižinada", "Vrsar"
    ],
    "Zagrebačka županija": [
        # Major cities and towns
        "Velika Gorica", "Samobor", "Zaprešić", "Jastrebarsko", "Ivanić-Grad", "Dugo Selo", "Vrbovec",
        "Sveti Ivan Zelina", "Sveti Nedelja", "Bistra",
        # Additional municipalities
        "Bedenica", "Brckovljani", "Brdovec", "Dubrava", "Farkaševac", "Gradec", "Jakovlje", "Klinča Sela",
        "Kloštar Ivanić", "Krašić", "Križ", "Luka", "Marija Gorica", "Orle", "Pisarovina", "Pokupsko", "Preseka",
        "Pušća", "Rugvica", "Stupnik", "Zdenci Brdovečki", "Žumberak"
    ],
    "Krapinsko-zagorska županija": [
        # Major cities and towns
        "Krapina", "Zabok", "Pregrada", "Donja Stubica", "Zlatar", "Oroslavje", "Klanjec", "Stubičke Toplice",
        # Additional municipalities
        "Bedekovčina", "Budinščina", "Desinić", "Đurmanec", "Gornja Stubica", "Hrašćina", "Hum na Sutli", "Jesenje",
        "Konjščina", "Krapinske Toplice", "Kumrovec", "Lobor", "Marija Bistrica", "Mihovljan", "Novi Golubovec",
        "Petrovsko", "Radoboj", "Sveti Križ Začretje", "Tuhelj", "Veliko Trgovišće", "Zagorska Sela", "Zlatar Bistrica"
    ],
    "Sisačko-moslavačka županija": [
        # Major cities and towns
        "Sisak", "Petrinja", "Kutina", "Novska", "Glina", "Hrvatska Kostajnica", "Popovača",
        # Additional municipalities
        "Donji Kukuruzari", "Dvor", "Gvozd", "Hrvatska Dubica", "Jasenovac", "Lekenik", "Lipovljani", "Majur", "Sunja",
        "Topusko", "Velika Ludina"
    ],
    "Karlovačka županija": [
        # Major cities and towns
        "Karlovac", "Ogulin", "Duga Resa", "Slunj", "Ozalj", "Vojnić",
        # Additional municipalities
        "Barilović", "Bosiljevo", "Cetingrad", "Draganić", "Generalski Stol", "Josipdol", "Kamanje", "Krnjak",
        "Lasinja", "Netretić", "Plaški", "Rakovica", "Ribnik", "Saborsko", "Tounj", "Žakanje"
    ],
    "Varaždinska županija": [
        # Major cities and towns
        "Varaždin", "Ivanec", "Ludbreg", "Novi Marof", "Lepoglava", "Varaždinske Toplice",
        # Additional municipalities
        "Bednja", "Breznica", "Breznički Hum", "Cestica", "Donja Voća", "Gornji Kneginec", "Jalžabet", "Klenovnik",
        "Ljubešćica", "Mali Bukovec", "Maruševec", "Petrijanec", "Sračinec", "Sveti Đurđ", "Sveti Ilija",
        "Trnovec Bartolovečki", "Veliki Bukovec", "Vidovec", "Vinica"
    ],
    "Koprivničko-križevačka županija": [
        # Major cities and towns
        "Koprivnica", "Križevci", "Đurđevac",
        # Additional municipalities
        "Drnje", "Đelekovec", "Ferdinandovac", "Gola", "Gornja Rijeka", "Hlebine", "Kalinovac", "Kloštar Podravski",
        "Koprivnički Bregi", "Koprivnički Ivanec", "Legrad", "Molve", "Novigrad Podravski", "Novo Virje", "Peteranec",
        "Podravske Sesvete", "Rasinja", "Sokolovac", "Sveti Ivan Žabno", "Sveti Petar Orehovec", "Virje"
    ],
    "Bjelovarsko-bilogorska županija": [
        # Major cities and towns
        "Bjelovar", "Daruvar", "Garešnica", "Čazma", "Grubišno Polje",
        # Additional municipalities
        "Berek", "Dežanovac", "Đulovac", "Hercegovac", "Ivanska", "Kapela", "Končanica", "Nova Rača", "Rovišće",
        "Severin", "Sirač", "Šandrovac", "Štefanje", "Velika Pisanica", "Velika Trnovitica", "Veliki Grđevac",
        "Veliko Trojstvo", "Zrinski Topolovac"
    ],
    "Primorsko-goranska županija": [
        # Major cities and towns
        "Rijeka", "Opatija", "Crikvenica", "Delnice", "Krk", "Rab", "Cres", "Mali Lošinj", "Novi Vinodolski", "Kastav",
        # Additional municipalities
        "Baška", "Bakar", "Čabar", "Čavle", "Dobrinj", "Fužine", "Jelenje", "Klana", "Kostrena", "Kraljevica", "Lokve",
        "Lopar", "Lovran", "Malinska-Dubašnica", "Matulji", "Mošćenička Draga", "Mrkopalj", "Omišalj", "Punat",
        "Ravna Gora", "Skrad", "Vrbnik", "Vinodolska općina", "Viškovo", "Vrbovsko"
    ],
    "Ličko-senjska županija": [
        # Major cities and towns
        "Gospić", "Otočac", "Senj", "Novalja",
        # Additional municipalities
        "Brinje", "Donji Lapac", "Karlobag", "Lovinac", "Perušić", "Plitvička Jezera", "Udbina", "Vrhovine"
    ],
    "Virovitičko-podravska županija": [
        # Major cities and towns
        "Virovitica", "Slatina", "Orahovica",
        # Additional municipalities
        "Crnac", "Čačinci", "Čađavica", "Gradina", "Lukač", "Mikleuš", "Nova Bukovica", "Pitomača", "Sopje",
        "Suhopolje", "Špišić Bukovica", "Voćin", "Zdenci"
    ],
    "Požeško-slavonska županija": [
        # Major cities and towns
        "Požega", "Pakrac", "Lipik", "Pleternica", "Kutjevo",
        # Additional municipalities
        "Brestovac", "Čaglin", "Jakšić", "Kaptol", "Velika"
    ],
    "Brodsko-posavska županija": [
        # Major cities and towns
        "Slavonski Brod", "Nova Gradiška",
        # Additional municipalities
        "Bebrina", "Brodski Stupnik", "Bukovlje", "Cernik", "Davor", "Donji Andrijevci", "Dragalić", "Garčin",
        "Gornja Vrba", "Gornji Bogićevci", "Gundinci", "Klakar", "Nova Kapela", "Okučani", "Oprisavci", "Oriovac",
        "Podcrkavlje", "Rešetari", "Sibinj", "Sikirevci", "Slavonski Šamac", "Stara Gradiška", "Staro Petrovo Selo",
        "Velika Kopanica", "Vrbje", "Vrpolje"
    ],
    "Zadarska županija": [
        # Major cities and towns
        "Zadar", "Biograd na Moru", "Benkovac", "Pag", "Obrovac", "Nin",
        # Additional municipalities
        "Bibinje", "Gračac", "Jasenice", "Kali", "Kukljica", "Lišane Ostrovičke", "Novigrad", "Pašman", "Poličnik",
        "Polača", "Posedarje", "Povljana", "Preko", "Privlaka", "Ražanac", "Sali", "Starigrad", "Sukošan",
        "Sveti Filip i Jakov", "Škabrnja", "Tkon", "Vir", "Vrsi", "Zemunik Donji"
    ],
    "Osječko-baranjska županija": [
        # Major cities and towns
        "Osijek", "Đakovo", "Našice", "Beli Manastir", "Valpovo", "Belišće", "Donji Miholjac",
        # Additional municipalities
        "Antunovac", "Bilje", "Bizovac", "Čeminac", "Čepin", "Donja Motičina", "Draž", "Drenje", "Đurđenovac",
        "Ernestinovo", "Feričanci", "Gorjani", "Jagodnjak", "Kneževi Vinogradi", "Koška", "Levanjska Varoš",
        "Magadenovac", "Marijanci", "Petlovac", "Petrijevci", "Podgorač", "Popovac", "Punitovci", "Satnica Đakovačka",
        "Semeljci", "Strizivojna", "Šodolovci", "Trnava", "Viljevo", "Viškovci", "Vuka"
    ],
    "Šibensko-kninska županija": [
        # Major cities and towns
        "Šibenik", "Knin", "Drniš", "Vodice", "Skradin",
        # Additional municipalities
        "Bilice", "Civljane", "Ervenik", "Kijevo", "Murter-Kornati", "Pirovac", "Primošten", "Promina", "Rogoznica",
        "Ružić", "Tisno", "Unešić"
    ],
    "Vukovarsko-srijemska županija": [
        # Major cities and towns
        "Vukovar", "Vinkovci", "Županja", "Ilok", "Otok",
        # Additional municipalities
        "Andrijaševci", "Bogdanovci", "Borovo", "Bošnjaci", "Cerna", "Drenovci", "Gradište", "Gunja", "Ivankovo",
        "Jarmina", "Lovas", "Markušica", "Nijemci", "Nuštar", "Privlaka", "Slakovci", "Stari Jankovci",
        "Stari Mikanovci", "Štitar", "Tordinci", "Tovarnik", "Trpinja", "Vođinci"
    ],
    "Splitsko-dalmatinska županija": [
        # Major cities and towns
        "Split", "Sinj", "Trogir", "Omiš", "Makarska", "Solin", "Kaštela", "Imotski", "Supetar", "Hvar", "Vis",
        # Additional municipalities
        "Baška Voda", "Bol", "Brela", "Dicmo", "Dugi Rat", "Dugopolje", "Gradac", "Hrvace", "Jelsa", "Klis", "Komiža",
        "Lećevica", "Marina", "Muć", "Nerežišća", "Otok", "Podbablje", "Podgora", "Podstrana", "Postira",
        "Primorski Dolac", "Proložac", "Pučišća", "Runovići", "Seget", "Selca", "Šestanovac", "Šolta", "Stari Grad",
        "Sućuraj", "Trilj", "Tučepi", "Vrgorac", "Vrlika", "Zadvarje", "Zmijavci"
    ],
    "Dubrovačko-neretvanska županija": [
        # Major cities and towns
        "Dubrovnik", "Metković", "Ploče", "Korčula", "Opuzen", "Cavtat",
        # Additional municipalities
        "Blato", "Dubrovačko primorje", "Janjina", "Konavle", "Kula Norinska", "Lastovo", "Lumbarda", "Mljet", "Orebić",
        "Pojezerje", "Slivno", "Ston", "Trpanj", "Vela Luka", "Zažablje"
    ],
    "Međimurska županija": [
        # Major cities and towns
        "Čakovec", "Mursko Središće", "Prelog",
        # Additional municipalities
        "Belica", "Dekanovec", "Domašinec", "Donja Dubrava", "Donji Kraljevec", "Donji Vidovec", "Goričan", "Kotoriba",
        "Mala Subotica", "Nedelišće", "Orehovica", "Podturen", "Pribislavec", "Selnica", "Strahoninec", "Sveta Marija",
        "Sveti Juraj na Bregu", "Sveti Martin na Muri", "Šenkovec", "Vratišinec"
    ],
    "Grad Zagreb": [
        "Zagreb"
    ]
}


def populate_counties_and_cities():
    # Iterate over the dictionary
    for county_name, city_names in gradovi_zupanije.items():
        # Create or get the county
        county, created = County.objects.get_or_create(name=county_name)
        if created:
            print(f"Created county: {county_name}")
        else:
            print(f"County already exists: {county_name}")

        # Iterate through each city in the county
        for city_name in city_names:
            # Create or get the city
            city, city_created = City.objects.get_or_create(name=city_name, county=county)
            if city_created:
                print(f"Added city: {city_name} to {county_name}")
            else:
                print(f"City {city_name} already exists in {county_name}")


# Run the population script
if __name__ == '__main__':
    populate_counties_and_cities()
