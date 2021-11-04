while True:
    print("je zit thuis te ontbijten wanneer je plots de lucht sirenes hoort. wat doe je?")
    print("A: je gaat onder de tafel zitten")
    print("B: je gaat in bed liggen")
    print("C: je gaat op het aanrecht staan")
    print("D: je gaat in de kelder zitten")
    a = input(":")
    if a == 'a' or a == 'A' :
        print("je hebt het bombardement overleeft, maar je bent gewond geraakt. wat ga je doen?")
        print("A: blijf onder al het puin liggen")
        print("B: ga op zoek naar hulp")
        aa = input(":")
        if aa == 'a' or aa == 'A' :
            print("je word gevonden door een hulp team. je krijgt een optie. wat kies je?")
            print("A: blijf daar tot je word ontslagen uit het ziekenhuis")
            print("B: ga mee in een vliegtuig met anderen gewonden")
            aaa = input(":")
            if aaa == 'a' or aaa == 'A' :
                print("je word weer gebombardeerd. je hebt het bombardement overleeft en ligt nu weer in het puin. wat ga je doen?")
                print("A: je blijft liggen in de hoop dat je blijft leven")
                print("B: je probeert weg te rennen")
                aaaa = input(":")
                if aaaa == 'a' or aaaa == 'A' :
                    print("de terroristen komen langs en schieten op alles op zijn minst eens in het hoofd om er zeker van te zijn dat allen dood zijn.")
                    print("")
                    print("ende #1: dood")
                    break
                if aaaa == 'b' or aaaa == 'B' :
                    print("je probeert weg te rennen, maar je verwondingen zijn te erg en je valt neer. je bent uitgeput en blijft liggen in de hoop op hulp. je bloed uiteindelijk dood.")
                    print("")
                    print("einde #1 dood")
                    break
            if aaa == 'b' or aaa == 'B' :
                print("je word gevlogen naar een veilig land in Europa waar je word geholpen. je hoort op tv dat het ziekenhuis waar je hiervoor lag was gebombardeerd. je geneest snel en word ontslagen uit het ziekenhuis. je vind werk en betaald een woning en leeft er nog lang en veilig.")
                print("")
                print("einde #2 veilig")
                break
        if aa == 'b' or aa == 'B' :
            print("je word gevonden door een paar terroristen en je word meteen neer geschoten.")
            print("")
            print("einde #1 dood")
            break
    if a == 'b' or a == 'B' :
        print("je word geraakt en bloed dood.")
        print("")
        print("einde #1 dood")
        break
    if a == 'c' or a == 'C' :
        print("je word geraakt en blaast op.")
        print("")
        print("einde #1 dood")
        break
    if a == 'd' or a == 'D' :
        print("je overleeft het bombardement zonder een schrammetje. waar ga je nu heen?")
        print("A: naar buiten, op zoek naar onderdak")
        print("B: ga door het riool kruipen")
        ad = input(":")
        if ad == 'a' or ad == 'A' :
            print("je gaat naar buiten en rent zo hard je kunt. je hoort soldaten praten. wat doe je?")
            print("A: je rent naar hun toe en roept om hulp")
            print("B: je maakt jezelf klein en roept op een afstand om hulp")
            ada = input(":")
            if ada == 'a' or ada == 'A' :
                print("je rent naar de soldaten toe met een fles water die je had meegenomen uit de kelder. de soldaten verwarren de fles water met een bom en schieten je neer.")
                print("")
                print("einde #1 dood")
                break
            if ada == 'b' or ada == 'B' :
                print("de soldaten horen je en rennen naar je toe om te helpen. na een paar vragen word je meegenomen in een jeep. achter je hoor je de soldaten vechten tegen de terroristen. wanneer je op het legerkamp aan komt, krijg je een optie. ga je naar Europa met...")
                print("A: het vliegtuig")
                print("B: de boot")
                print("C: een helikopter")
                adab = input(":")
                if adab == 'a' or adab == 'A' :
                    print("je stapt in het vliegtuig met een paar andere vluchtelingen. wanneer jullie boven in de lucht zijn, begint het vliegtuig agressief heen en weer te sturen. voor dat je iets kan doen, word je vliegtuig uit de lucht geschoten. je overleefd de val, maar je verdrinkt na een tijdje door niet genoeg kracht meer in de benen.")
                    print("")
                    print("einde #1 dood")
                    break
                if adab == 'b' or adab == 'B' :
                    print("je stapt in de boot met een aantal andere vluchtelingen. na een tijdje word er op jullie beschoten. een groot deel van de bemanning overlijd. ook jij bent geraakt, maar je overleefd de wonden. niet veel later zijn de vliegtuigen die jullie aanviel uit de lucht geschoten. je begint langzaam maar zeker gek te worden van de reis. wanner je aankomt in Europa, val je iedereen aan die je kunt zien. je word opgepakt en in de gevangenis gezet.")
                    print("")
                    print("einde #3 gevangen")
                    break
                if adab == 'c' or adab == 'C' :
                    print("je gaat naar de helikopter, maar hij zit vol. je word naar een buurt gebracht die al bevrijd is. je leeft daar voor de rest van je leven.")
                    print("")
                    print("einde #4 leven in angst")
                    break
        if ad == 'b' or ad == 'B' :
            print("je kruipt door het riool. je ziet 3 uitgangen. welke uitgang neem je?")
            print("A: links")
            print("B: rechtdoor")
            print("C: rechts")
            adb = input(":")
            if adb == 'a' or adb == 'A' :
                print("je kruipt naar links en ziet een uitgang. je gaat het riool uit en komt terecht in een lege straat. je kijkt om je heen en ziet een hutje. je gaat naar het hutje voor hulp, maar wat je tegen komt valt enorm tegen. een paar terroristen waren daar aan het lunchen en schieten jou daar meteen neer.")
                print("")
                print("einde #1 dood")
                break
            if adb == 'b' or adb == 'B' :
                print("je blijft rechtdoor kruipen en komt uit in een afgelegen have. je kijkt om je heen wanneer je plots een stem hoort. het is een schipper die jou wel wilt helpen. je stapt op zijn boot en jullie gaan varen naar Europa. wanneer jullie aankomt in Europa, worden jullie aangehouden. na een lang gesprek met de agent krijg je toestemming om daar te blijven voor een half jaar. als je voor die tijd geen huis heb kunnen regelen in een ander land word je terug gestuurd. na een half jaar heb je nog steeds geen huis in een ander land en je word terug gestuurd.")
                print("")
                print("einde #4 leven in angst")
                break
            if adb == 'c' or adb == 'C' :
                print("je gaat naar rechts en komt uit in een lege straat. je ziet een klein huisje. je loopt naar binnen en je komt andere vluchtelingen tegen. je blijft daar voor een tijdje totdat iemand een telefoontje krijgt. nemen jullie hem op?")
                print("A: ja")
                print("B: nee")
                adbc = input(":")
                if adbc == 'a' or adbc == 'A' :
                    print("jullie nemen het telefoontje op. jullie horen een man praten over een boot naar Europa. jullie besluiten naar die boot te komen om middernacht, zoals de man wilde. jullie stappen op de boot met heel veel andere vluchtelingen. na een aantal uur komen jullie aan in Europa. na een tijdje krijg je te horen dat je in een noordelijker land kunt wonen. je vind daar werk en leeft nog lang en veilig.")
                    print("")
                    print("einde #2 veilig")
                    break
                if adbc == 'b' or adbc == 'B' :
                    print("jullie nemen de telefoon niet op. na nog een paar weken worden jullie gevonden door een terrorist. jullie bespringen hem om zijn wapen te kunnen pakken, maar hij pakt een granaat en trekt de pin er uit. jullie hebben niks door en eventjes later blazen jullie allemaal op.")
                    print("")
                    print("einde #1 dood")
                    break
