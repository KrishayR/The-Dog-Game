import random
import time
import sys
dog = ["German Shepherd","Affenpinscher","Afghan Hound","Afghan Shepherd","Aidi","Airedale Terrier","Akbash","Akita","Alano Español","Alaskan husky","Alaskan Klee Kai","Alaskan Malamute","Alaunt","Alopekis","Alpine Dachsbracke","Alpine Mastiff","Alpine Spaniel","American Akita","American Bully","American Bulldog","American Cocker Spaniel","American English Coonhound","American Eskimo Dog","American Foxhound","American Hairless Terrier","American Pit Bull Terrier","American Staffordshire Terrier","American Water Spaniel","Anatolian Shepherd Dog","Andalusian Hound","Anglo-Français de Petite Vénerie","Appenzeller Sennenhund","Argentine Polar Dog","Ariegeois","Armant","Armenian Gampr dog","Artois Hound","Australian Cattle Dog","Australian Kelpie","Australian Shepherd","Australian Stumpy Tail Cattle Dog[10]","Australian Terrier","Austrian Black and Tan Hound","Austrian Pinscher","Azawakh","Bakharwal dog","Barbado da Terceira","Barbet","Basenji","Basque Shepherd Dog","Basset Artésien Normand","Basset Bleu de Gascogne","Basset Fauve de Bretagne","Basset Hound","Bavarian Mountain Hound","Beagle","Beagle-Harrier","Bearded Collie","Beauceron","Bedlington Terrier","Belgian Shepherd Dog (Groenendael)","Belgian Shepherd Dog (Laekenois)","Belgian Shepherd Dog (Malinois)","Belgian Shepherd Dog (Tervuren)","Bergamasco Shepherd","Berger Blanc Suisse","Berger Picard","Bernese Mountain Dog","Bichon Frisé","Billy","Black and Tan Coonhound","Black and Tan Virginia Foxhound","Black Norwegian Elkhound","Black Russian Terrier","Black Mouth Cur","Bloodhound","Blue Heeler","Blue Lacy","Blue Paul Terrier","Blue Picardy Spaniel","Bluetick Coonhound","Boerboel","Bohemian Shepherd","Bolognese","Border Collie","Border Terrier","Borzoi","Bosnian Coarse-haired Hound","Boston Terrier","Bouvier des Ardennes","Bouvier des Flandres","Boxer","Boykin Spaniel","Bracco Italiano","Braque d'Auvergne","Braque de l'Ariege","Braque du Bourbonnais","Braque du Puy","Braque Francais","Braque Saint-Germain","Brazilian Dogo","Brazilian Terrier","Briard","Briquet Griffon Vendéen","Brittany","Broholmer","Bruno Jura Hound","Brussels Griffon","Bucovina Shepherd Dog","Bull and Terrier","Bull Terrier","Bulldog","Bullenbeisser","Bullmastiff","Bully Kutta","Burgos Pointer","Cairn Terrier","Canaan Dog","Canadian Eskimo Dog","Cane Corso","Cantabrian Water Dog","Cão da Serra de Aires","Cão de Castro Laboreiro","Cão de Gado Transmontano","Cão Fila de São Miguel","Carolina Dog","Carpathian Shepherd Dog","Catalan Sheepdog","Caucasian Shepherd Dog","Cavalier King Charles Spaniel","Central Asian Shepherd Dog","Cesky Fousek","Cesky Terrier","Chesapeake Bay Retriever","Chien Français Blanc et Noir","Chien Français Blanc et Orange","Chien Français Tricolore","Chien-gris","Chihuahua","Chilean Terrier","Chinese Chongqing Dog","Chinese Crested Dog","Chinese Imperial Dog","Chinook","Chippiparai","Chiribaya Dog","Chow Chow","Cierny Sery","Cirneco dell'Etna","Clumber Spaniel","Collie, Rough","Collie, Smooth","Combai","Cordoba Fighting Dog","Coton de Tulear","Cretan Hound","Croatian Sheepdog","Cumberland Sheepdog","Curly-Coated Retriever","Cursinu","Czechoslovakian Wolfdog","Dachshund","Dalbo dog","Dalmatian","Dandie Dinmont Terrier","Danish-Swedish Farmdog","Deutsche Bracke","Doberman Pinscher","Dogo Argentino","Dogo Cubano","Dogue de Bordeaux","Drentse Patrijshond","Drever","Dunker","Dutch Shepherd","Dutch Smoushond","East Siberian Laika","East European Shepherd","Elo","English Cocker Spaniel","English Foxhound","English Mastiff","English Pointer","English Setter","English Shepherd","English Springer Spaniel","English Toy Terrier (Black & Tan)","English Water Spaniel","English White Terrier","Entlebucher Mountain Dog","Estonian Hound","Estrela Mountain Dog","Eurasier","Eurohound","Field Spaniel","Fila Brasileiro","Finnish Hound","Finnish Lapphund","Finnish Spitz","Flat-Coated Retriever","Fox Terrier, Smooth","Fox Terrier, Wire","French Brittany","French Bulldog","French Spaniel","Gaddi Kutta","Galgo Español","Galician Shepherd Dog","Garafian Shepherd","Gascon Saintongeois","Georgian Shepherd","German Longhaired Pointer","German Pinscher","German Roughhaired Pointer","German Shepherd Dog","German Shorthaired Pointer","German Spaniel","German Spitz","German Wirehaired Pointer","Giant Schnauzer","Glen of Imaal Terrier","Golden Retriever","Gordon Setter","Gran Mastín de Borínquen","Grand Anglo-Français Blanc et Noir","Grand Anglo-Français Blanc et Orange","Grand Anglo-Français Tricolore","Grand Basset Griffon Vendéen","Grand Bleu de Gascogne","Grand Griffon Vendéen","Great Dane","Great Pyrenees","Greater Swiss Mountain Dog","Greek Harehound","Greek Shepherd","Greenland Dog","Greyhound","Griffon Bleu de Gascogne","Griffon Fauve de Bretagne","Griffon Nivernais","Guatemalan Dogo","Gull Terrier","Hamiltonstövare","Hanover Hound","Hare Indian Dog","Harrier","Havanese","Hawaiian Poi Dog","Himalayan Sheepdog","Hokkaido","Hortaya borzaya","Hovawart","Huntaway","Hygen Hound","Ibizan Hound","Icelandic Sheepdog","Indian pariah dog","Indian Spitz","Irish Red and White Setter","Irish Setter","Irish Terrier","Irish Water Spaniel","Irish Wolfhound","Istrian Coarse-haired Hound","Istrian Short-haired Hound","Italian Greyhound","Jack Russell Terrier","Jagdterrier","Swedish Elkhound","Japanese Chin","Japanese Spitz","Japanese Terrier","Jindo","Jonangi","Kaikadi dog","Kai Ken","Kangal Shepherd Dog","Kanni","Karakachan dog","Karelian Bear Dog","Karst Shepherd","Keeshond","Kerry Beagle","Kerry Blue Terrier","King Charles Spaniel","King Shepherd","Kintamani","Kishu Ken","Komondor","Koolie","Koyun dog","Kromfohrländer","Kumaon Mastiff","Kunming Wolfdog","Kurī","Kuvasz","Kyi-Leo","Labrador Husky","Labrador Retriever","Lagotto Romagnolo","Lakeland Terrier","Lancashire Heeler","Landseer","Lapponian Herder","Lapponian Shepherd","Large Münsterländer","Leonberger","Lhasa Apso","Lithuanian Hound","Louisiana Catahoula Leopard Dog","Löwchen","Mackenzie River husky","Magyar agár","Mahratta Greyhound","Ratonero Mallorquin","Maltese","Manchester Terrier","Maremma Sheepdog","Marquesan Dog","McNab dog","Miniature American Shepherd","Miniature Bull Terrier","Miniature Fox Terrier","Miniature Pinscher","Miniature Schnauzer","Miniature Shar Pei","Molossus","Molossus of Epirus","Montenegrin Mountain Hound","Moscow Watchdog","Moscow Water Dog","Mountain Cur","Mucuchies","Mudhol Hound","Mudi","Neapolitan Mastiff","Nederlandse Kooikerhondje","Nenets Herding Laika","Newfoundland","New Guinea singing dog","New Zealand Heading Dog","Norfolk Spaniel","Norfolk Terrier","Norrbottenspets","North Country Beagle","Northern Inuit Dog","Norwegian Buhund","Norwegian Elkhound","Norwegian Lundehund","Norwich Terrier","Nova Scotia Duck Tolling Retriever","Old Croatian Sighthound","Old Danish Pointer","Old English Bulldog","Old English Sheepdog","Old English Terrier","Old German Shepherd Dog","Old Spanish Pointer","Old Time Farm Shepherd","Olde English Bulldogge","Otterhound","Pachon Navarro","Pandikona","Paisley Terrier","Papillon","Parson Russell Terrier","Pastore della Lessinia e del Lagorai","Patterdale Terrier","Pekingese","Perro de Pastor Mallorquin","Perro de Presa Canario","Perro de Presa Mallorquin","Peruvian Inca Orchid","Petit Basset Griffon Vendéen","Petit Bleu de Gascogne","Phalène","Pharaoh Hound","Phu Quoc Ridgeback","Picardy Spaniel","Plummer Terrier","Plott Hound","Podenco Canario","Poitevin","Polish Greyhound","Polish Hound","Polish Hunting Dog","Polish Lowland Sheepdog","Polish Tatra Sheepdog","Pomeranian","Pont-Audemer Spaniel","Poodle","Porcelaine","Portuguese Podengo","Portuguese Pointer","Portuguese Water Dog","Posavac Hound","Potsdam Greyhound","Pražský Krysařík","Pudelpointer","Pug","Puli","Pumi","Pungsan dog","Pyrenean Mastiff","Pyrenean Shepherd","Rafeiro do Alentejo","Rajapalayam","Rampur Greyhound","Rastreador Brasileiro","Rat Terrier","Ratonero Bodeguero Andaluz","Ratonero Murciano de Huerta","Ratonero Valenciano","Redbone Coonhound","Rhodesian Ridgeback","Romanian Mioritic Shepherd Dog","Romanian Raven Shepherd Dog","Rottweiler","Russian Salon Dog","Russian Spaniel","Russian Toy","Russian Tracker","Russo-European Laika","Russell Terrier","Saarloos Wolfdog","Sabueso Español","Sabueso fino Colombiano","Saint Bernard","Saint John's water dog","Saint-Usuge Spaniel","Sakhalin Husky","Salish Wool Dog","Saluki","Samoyed","Sapsali","Šarplaninac","Schapendoes","Schillerstövare","Schipperke","Schweizer Laufhund","Schweizerischer Niederlaufhund","Scotch Collie","Scottish Deerhound","Scottish Terrier","Sealyham Terrier","Segugio Italiano","Segugio Maremmano","Seppala Siberian Sleddog","Serbian Hound","Serbian Tricolour Hound","Seskar Seal Dog","Shar Pei","Shetland Sheepdog","Shiba Inu","Shih Tzu","Shikoku","Shiloh Shepherd","Siberian Husky","Silken Windhound","Silky Terrier","Sinhala Hound","Skye Terrier","Sloughi","Slovakian Wirehaired Pointer","Slovensky Cuvac","Slovensky Kopov","Smålandsstövare","Small Münsterländer","Small Greek Domestic Dog","Soft-Coated Wheaten Terrier","South Russian Ovcharka","Southern Hound","Spanish Mastiff","Spanish Water Dog","Spinone Italiano","Sporting Lucas Terrier","Stabyhoun","Staffordshire Bull Terrier","Standard Schnauzer","Stephens Cur","Styrian Coarse-haired Hound","Sussex Spaniel","Swedish Lapphund","Swedish Vallhund","Tahitian Dog","Tahltan Bear Dog","Taigan","Taiwan Dog","Talbot Hound","Tamaskan Dog","Teddy Roosevelt Terrier","Telomian","Tenterfield Terrier","Terceira Mastiff","Thai Bangkaew Dog","Thai Ridgeback","Tibetan Mastiff","Tibetan Spaniel","Tibetan Terrier","Tornjak","Tosa","Toy Bulldog","Toy Fox Terrier","Toy Manchester Terrier","Toy Trawler Spaniel","Transylvanian Hound","Treeing Cur","Treeing Tennessee Brindle","Treeing Walker Coonhound","Trigg Hound","Tweed Water Spaniel","Tyrolean Hound","Cimarrón Uruguayo","Vanjari Hound","Villano de Las Encartaciones","Villanuco de Las Encartaciones","Vizsla","Volpino Italiano","Weimaraner","Welsh Corgi, Cardigan","Welsh Corgi, Pembroke","Welsh Sheepdog","Welsh Springer Spaniel","Welsh Terrier","West Highland White Terrier","West Siberian Laika","Westphalian Dachsbracke","Wetterhoun","Whippet","White Shepherd","Wirehaired Pointing Griffon","Wirehaired Vizsla","Xiasi Dog","Xoloitzcuintli","Yakutian Laika","Yorkshire Terrier"]
coins = random.randint(0,400)
coins2 = random.randint(0,400)
coinst = coins + coins2
try:
    dog_choose = input("Choose a dog breed: ").title()
    if dog_choose in dog:
        pass
    else:
        print("Sorry! Looks like that dog breed does not exist in my memory! Try to check your spelling maybe! ")
        dog_choose = input("Choose a dog breed: ").title()
        if dog_choose in dog:
            pass
        else:
            print("Sorry! Looks like that dog breed does not exist in my memory! Try to check your spelling maybe! ")
            dog_choose = input("Choose a dog breed: ").title()
            if dog_choose in dog:
                pass
            else:
                print("FOR THE LAST TIME! CHOOSE A DIFFERENT DOG BREED!")
                dog_choose = input("Choose a dog breed: ").title()
                if dog_choose in dog:
                    pass
                else:
                    print("FINE WHATEVER THAT WAS YOUR LAST TRY")
                    pass
    time.sleep(1)
    dog_name = input("Choose the name of your dog: ").capitalize()
    time.sleep(1)
    print(f"Your dog is a {dog_choose} named {dog_name}!")
    print("Creating...\nThis may take a moment")
    time.sleep(2)
    print("Created dog!")
    # hungry minigame for coins
    hi = input(f"Do you want to feed {dog_name}, play with {dog_name}, or shop for your dog?").upper()
    if hi == "FEED" or "F" or "1":
            print(f"Your dog is hungry! {dog_choose}s sure do love to eat! Too buy food you must get 100 coins. Where do you want to look?(ENTER TO QUIT)")
            value1 = input("Air, Pillow, or Car: ").upper()    
            if value1 == '':
                sys.exit()
            elif value1 == "AIR":
                print(f'YOU GOT {coins} COINS. HOW in the world did you find coins in the air?!?!?')
                if coins >= 100:
                    a = input(f"Do you want to feed {dog_name}? : ").upper()
                    if a == 'YES':
                        print("SURE\nFeeding...\nThis may take a minute")
                        time.sleep(5)
                        print(f"{dog_name} is fed well!")
                        print('|--LEVEL ONE COMPLETE--|')
                elif coins <= 100:
                    print("OOOF. Looks like you didn't get enough coins. Tough luck.")
                    b = input("Do you want to play again?: ").upper()
                    if b == 'YES' or 'Y':
                        print("Sure thing!")
                        print("\n\n\n")
                        v2 = input("Bed, couch, bank: ").upper()
                        if v2 == 'BED':
                            print(f"You checked under the bed huh? WOW you got {coins}. Nice, kid.")
                        elif v2 == 'COUCH':
                            print(f"You found {coins2} under your couch.")
                        elif v2 == 'BANK':
                            print("BRUHHH. You Just Robbed A Bank. GO TO JAIL! Oh and by the way you were caught. 0 coins.")
                            pass
                        else:
                            print("THAT IS NOT A VALID OPTION FROM THE LIST. FOR THE SECOND TIME! GOODBYE!")
                            pass
                    elif b == 'NO' or 'N':
                        print("Ok that's fine. Good Bye!")
                        pass
                    else:
                        print("WELL YOU DID'NT SAY A YES OR NO SO IMMA ASK YOU AGAIN")
                        b = input("Do you want to play again?: ").upper()
                        if b == 'YES' or 'Y':
                            print("Sure thing!")
                            print("\n\n")
                            
                            v2 = input("Bed, couch, bank: ").upper()
                            if v2 == 'BED':
                                print(f"You checked under the bed huh? WOW you got {coins2}. Nice, kid.")
                            elif v2 == 'COUCH':
                                print(f"You found {coins2} under your couch.")
                            elif v2 == 'BANK':
                                print("BRUHHH. You Just Robbed A Bank. GO TO JAIL! Oh and by the way you were caught. 0 coins.")
                               
                            else:
                                print("THAT IS NOT A VALID OPTION FROM THE LIST. FOR THE SECOND TIME! GOODBYE!")
                                
                        elif b == 'NO' or 'N':
                            print("Ok that's fine. Good Bye!")
                            
                        else:
                            print("WELL YOU DID'NT SAY A YES OR NO SO BYE!")

            elif value1 == "PILLOW":
                print(f'Looks like the tooth fairy left {coins} coins behind. ')
            elif value1 == 'CAR':
                print(f"HAHAHA you didnt find any coins. Try again?")
                value1 = input("Air, Pillow, or Car: ").upper()
                if value1 == '':
                    sys.exit()
                elif value1 == "AIR":
                    print(f'YOU GOT {coins} COINS. HOW in the world did you find coins in the air?!?!?')
                elif value1 == "PILLOW":
                    print(f'Looks like the tooth fairy left {coins} coins behind. ')
                    pass
            else:
                print(f"WHAT WERE YOU THINKING MAN! Do you see {value1} anywhere in the list!?")
            r = input('Do you want to play again FOR MORE COINS!?').upper()
            if r == 'YES' or 'Y':
                print("OK")
                print("\n\n\n\n\n\n")
                print("Sure thing!")
                print("\n\n\n")
                v2 = input("Bed, couch, bank: ").upper()
                if v2 == 'BED':
                    print(f"You checked under the bed huh? WOW you got {coins2}. Nice, kid.")
                elif v2 == 'COUCH':
                    print(f"You found {coins2} under your couch.")
                elif v2 == 'BANK':
                    print("BRUHHH. You Just Robbed A Bank. GO TO JAIL! Oh and by the way you were caught. 0 coins.")
                    pass
                else:
                    print("THAT IS NOT A VALID OPTION FROM THE LIST. FOR THE SECOND TIME! GOODBYE!")
                    pass
            elif b == 'NO' or 'N':
                print("Ok that's fine. Good Bye!")
                pass
            else:
                print("WELL YOU DID'NT SAY A YES OR NO SO IMMA ASK YOU AGAIN")
                b = input("Do you want to play again?: ").upper()
                if b == 'YES' or 'Y':
                    print("Sure thing!")
                    print("\n\n\n")
                    v2 = input("Bed, couch, bank: ").upper()
                    if v2 == 'BED':
                        print(f"You checked under the bed huh? WOW you got {coins2}. Nice, kid.")
                    elif v2 == 'COUCH':
                        print(f"You found {coins2} under your couch.")
                    elif v2 == 'BANK':
                        print("BRUHHH. You Just Robbed A Bank. GO TO JAIL! Oh and by the way you were caught. 0 coins.")
                        
                    else:
                        print("THAT IS NOT A VALID OPTION FROM THE LIST. FOR THE SECOND TIME! GOODBYE!")
                        
                elif b == 'NO' or 'N':
                    print("Ok that's fine. Good Bye!")
                    
                else:
                    print("WELL YOU DID'NT SAY A YES OR NO SO BYE!")
                    print("--LEFT--")
                    
            md = input("DO YOU WANT TO SEE YOUR TOTAL?: ").upper
            if md == "YES" or "Y":
                print(f"Your total is {coinst} coins")
            else:
                print("OK FINE BYE!")
                
        
    elif hi == "PLAY" or "P" or "2":
        print("Sorry still in making...")
        


except:
    print("Their has been an error")
    print("Their has been an error")
    print("Their has been an error")
    
finally:
    print("--GOODBYE--")
