
import sqlite3 as sql
busnumber=[
    "1J", "1P/25i", "1V", "2c", "2j", "2U", "2Z", "3", "3D", "3H", "3K", "3KJ", 
    "5K", "5M", "1R", "5R", "5S", "6H", "6B", "8A", "8C/229", "8M", "8R", "8R/21", 
    "8R/25", "9F", "9K", "9K/B", "9M", "9x", "9x", "9Y", "10", "10F", "10/16", 
    "10FY", "10H", "10K", "16", "16/49M", "16K", "17H", "17H/", "226C", "18", "20P", 
    "102C", "102K/127j", "104M", "107H", "107V", "113C", "113E", "113K", "113M", 
    "113S", "113Y", "115", "118T", "127j/100V", "127j", "147", "156J", "158F", 
    "158J", "171/w", "187D", "187/JA", "189E/M", "189M", "189R", "190S", "204S", 
    "205F", "207", "217D", "225C", "225C/A", "224S", "225S", "225V", "226", "230X", 
    "250", "250/40M", "253K", "253M", "253M/8A", "277", "280C", "280S", "290", 
    "299", "156/299M"]
busroute=[
"JITYAGUDA AFZALGUNJ KOTI YMCA CH. PALLY RTC'X'RD MSRD PADMARAONAGAR SECUNDRABAD",
"ALWAL JBS PATNY SECUNDRABAD CHILKALGUDA PADMARAO NAGAR MSRD RTCXROAD YMCA KOTI",
"NGO'SCOLONY LAKDIKAPOOLB. NAGAR DSN. M.PET CH. GHAT KOTI YMCA RTCXROAD MSRD SECUNDRABAD AFZALGUNJ CBS",
"YMCA CH.PALLY RTCXROAD MSRD SECUNDRABAD JBS LALBAZAR YAPRAL",
"SECUNDRABAD RTCXROAD SMUTT BKP KUSHAIGUDA IMLIBUN AFZALGUNJ CHARMINAR CHANDRAYANGUTTAGUTTA BARKAS",
"SECUNDRABAD MSRD RTCXROAD SMUTT BKP K.GUDA IMLIBUN AFZALGUNJ CHUDI BAZAR JIAGUDA",
"UPPUGUDA CHARMINAR KACHIGUDA SMUTT RTCXROAD MSRD SECUNDRABAD",
"MADHUBAN CLNY CHARMINAR KACHIGUDA SMUTT RTCXROAD MSRD SECUNDRABAD",
"KUSHAIGUDA MOULAALI TARNAKA USMANIYAUNIVERSITY YMCA KOTI AFZALGUNJ",
"DAMMAIGUDA NAGARAM MOULAL TARNAKA VIDYANAGAR KOTL AFZALGUNJ",
"ECILXROAD MOULAALL TARNAKA USMANIYAUNIVERSITY YMCA KOTI AFZALGUNJ",
"KUSHAIGUDA MOULAALL TARNAKA USMANIYAUNIVERSITY YMCA KOTI AFZALGUNJ",
"KUSHAIGUDA ECIL TARNAKA AFZALGUNJ JUMARATHBAZAR JIYAGUDA",
"MEHADIPATNAM MASABTANK LAKDIKAPOOL BOATSCLUB SANGEETH SECUNDRABAD  AFZALGUNJ MADINA BAHADURPURA ZOOPARK",
"SECUNDRABAD PARADISE RNG TANKBUND SECRETARIAT BIRLA MAND",
"LAKDIKAPOOL GOLCONDA HOTEL NMDC MIYAPUR. TOLICHOWKI",
"RISALABAZAR BOLARUM LALBAZAR JBS BATA TANKBUND SECRETARIAT LAKDIKAPOOL MUSABTANK LANGARHOUZ",
"ECIXROAD SAINIKPURI NEREDMET M-GIRI SECUNDRABAD TANKBUND MUSABTANK MIYAPUR.",
"MEHADIPATNAM MTANK SECRETARIAT. H.B.COLONY ECIL'X' ROAD",
"RAMNAGAR RAMNAGAR B.LAKDI KA POOLPALLY N.GUDA LAKDIKAPOOL MIYAPUR. OCEAN PARK",
"SECUNDRABAD  BATA TANKBUND LIBERTY ABIDS AFZALGUNJ CHARMINAR",
"MEDCHAL KOMPALLY SECUNDRABAD  NAMPALLY AFZALGUNJ CHARMINAR",
"SECUNDRABAD  BATA TANKBUND AG-OFFICE NAMPALLY AFZALGUNJ CHARMINAR",
"RISALABAZAR BOLLARAM JBS NAMPALLY AFZALGUNJ MADINA CHARMINAR",
"VENKATAPUR ALWAL JIBS NAMPALLY AFZALGUNJ MADINA CHARMINAR",
"OLDALWAL/TEMPLE ALWAL NAMPALLY AFZALGUNJ CHARMINAR",
"BORABANDA ERRAGADDA NAMPALLY M.J.MARKET AFZALGUNJ CHARMINAR",
"APURUPACOLONY JEEDIMETLA MOOSAPET ABIDS KOTI AFZALGUNJ CHARMINAR",
"BALANAGAR MOOSAPET ESI KAIRATHABAD ABIDS KOTI AFZALGUNJ CHARMINAR",
"CHARMINAR AFZALGUNJ NAMPALLY PUNJAGUTTA ERRAGUDDA SANATHNAGAR",
"APURUPA COLONY JEEDIMETLA MOOSAPET NAMPALLY AFZALGUNJ CHARMINAR",
"CHARMINAR AFZALGUNJ LAKDIKAPOOL MOOSAPET IDPL BALANAGAR",

"YOUSUFGUOA AMEERPET NAMPALLY M.MARKET AFZALGUNJ CHARMINAR"
"SECUNDRABAD  PARADISE BEGUMPET AMEERPET ESI ERRAGADDA SANATHNAGAR",
"BORABANDA ERRAGADDA ESI PARADISE PATNY SECUNDRABAD ",
"SANATHNAGAR ERRAGADDA BEGUMET PATNY N.MUTT ECILXROAD",
"BORABANDA RAHAMATHNAGAR BEGUMPET PARADISE PATNY SECUNDRABAD ",
"SECUNDRABAD  PATNY CYBER TOWERS KOTHAGUDAXROAD KONDAPUR",
"KPHBCOLONY KUKATPALLY AMEERPET GREEN LANDS SANGEETH SECUNDRABAD ",
"APECILXROAD NEREDMET SECUNDRABAD  PLAZA AIRPORT",
"NEREOMET SAFILGUDA SECUNDRABAD  PLAZA AIRPORT",
"NEREDMETXROAD SAFIGUDA MALKAJGIRI METTUGUDA MSRD RTCXROAD KOTI MALAKPET DILSUKHNAGAR",
"KPHBCOLONY JTS RLY QTRS LALAPET TARNAKA METTUGUDA SECUNDRABAD",
"ECILXROAD MOULAALL KPHBCOLONY TARNAKA",
"SECUNDRABAD BOYANPALLY BALANAGAR KUKATPALLY KPHB MIYAPUR BHEL",
"SECUNDRABAD METTUGUDA HUBSIGUDA UPPALXROAD UPPALDEPOT",
"SECUNDRABAD PADMARAO NAGAR MSRD KAVADIGUDA GANDHINAGAR ASHOKNAGAR INDIRAPARK SECRETARIAT AG.OFFICE N.PALLV",
"BALAPUR CHANDRAYANGUTTA WOMENSCOLLEGE MUSHEERABAD SECUNDRABAD SIN",
"KESHAVAGIRI PISALBANDA WOMENSCOLLEGE MASAB TANK APOLLO MADHAPUR",
"AMEERPET I.S.SADAN WOMENSCOLLEGE RTCXRD SECUNDRABAD",
"SAROORNAGAR KOTHAPETXRD WOMENSCOLLEGE CHILKAL GUDA SECUNDRABAD",
"SECUNDRABAD S.MANDI WOMENS GUDA VIDYANAGAR SHIVAM6NUMBER AMBERPET MOOSARAMBAGH DILSUKHNAGAR",
"ESI AMEERPET NARAYANAGUDA CHIKKADPALLY RAMANTHAPUR UPPAL",
"UPPAL RAMANTHAPUR VST S.MUTT NARAYANAGUDA LIBERTY LAKDIKAPOOL PANJAGUTTA AMEERPET ESI",
"KUKATPALLY AMEERPET KAIRATHABAD SECRETARIAT NARAYANAGUDA BKP AMBERPET RAMANTHAPUR UPPAL UPPALDEPO",
"UPPAL RAMANTHPUR AMBERPET TILAKNAGAR BKP NARAYANAGUDA HIMAYATHNAGAR SECRETARIAT LAKDIKAPOOL MUSABTANK MIYAPUR",
"UPPAL RAMANTHPUR BAGHPALLY LIBERTY LAKDIKAPOOL ESI SANATHNAGAR",
"UPPAL RAMANTHPUR BAGHPALLY LIBERTY LAKDIKAPOOL ESI SANATHNAGAR YOUSUFGUDA",
"UPPAL RAMANTHPUR AMBERPET GOLNAKA NIMBOLIADDA CH GHAT KOTI",
"KOTI NAMPALLI LAKDIKAPOOL M.PXROAD MURADNAGAR TALLAGADDA",
"NGO' COLONY DILSUKHNAGAR NAMPALLY MASABTANK BANJARAHILLS JUBLIHILLS / C.POST",
"KOTI ABIDS NAMPALLY LAKDIKAPOOL MASABTANK ROADNO.12 APOLLOJUBLIHILLS",
"KONDAPUR KOTHAGUDA LAKDIAPOOLV.PRASAD EYE HOSPITAL ECIL ECIL X RD",
"NGO'S COLONY LAKDIKAPOOL NAGAR DILSUKHNAGAR LAKDIKAPOOL PANJAGUTTA JUBLIHILLS C / POST",
"DILSUKHNAGAR MALAKPET KOTI ABIDS NARKETPLLY LAKDIKAPOOL AMEERPET EARRAGADDA BORABANDA",
"DILSUKHNAGAR KOTI LAKDIKAPOOL AMEERPETEARRAGADDA BORABANDA",
"GAJULARAMARAM BALAANAGAR SANATHNAGAR AMEERPET LAKDIKAPOOL M.JMARKET CHARMINAR",
"KPHBCOLONY KUKATPALLY ERRAGADDA AMEERPET LAKDIKAPOOL KOTI DILSUKH NAGAR",
"JALAVIHAR NAGAR KUKATPALLY ESI AMEERPET LAKDIKAPOOL ABIDS KOTI",
"APURUPACOLONY JEEDIMETLA SANATHNAGAR MASABTANK MIYAPUR",
"JDM BALANAGAR ESI PANJAGUTTA JUBLIBHILLS M.TANK MIYAPUR",
"RAJENDRANAGAR RINGRDAD MIYAPUR JUBLIBHILLS PANJAGUTTA SANATNAGAR BALANAGAR",
"RAMNAGAR KPHBCOLONY RAMNAGAR AMEERPET S.R.NAGAR KUKATPALLY KPHB",
"SANGINAGAR AMBERPET HIMAYATHNAGAR LAKDIKAPOOL NAGAR DILSUKHNAGAR NLGXROAD WOMENS COLLEGE",
"MIYAPUR LAKDIKAPOOL KOTI NLGXROAD HIMAYATHNAGAR KOHEDA SANGHI RAMOJI FILM CITY",
"RAMOJFILMCITY SANGHINAGAR KOHED.PEDDAAMBERPET HIMAYATHNAGAR DILSUKHNAGAR WOMENS COLLEGE",
"DILSUKHNAGAR NGL XRD LAKDIKAPOOL MIYAPUR HCU BHEL PATANCHERU",
"PATANCHERU R C.PURAM MIYAPUR PANJAGUTTA AFZALGUNJ CHARMINAR",
"CHARMINAR AFZALGUNJ AMEERPET ASHOKNAGAR R.CPURAIVI PATANCHERU",
"IDABOLARUM INDXROAD MIYAPUR KUKATPALLY BALANAGAR BACHUPALLY PATNY SECUNDRABAD",
"PATANCHERUVU R.C.PURAM BHEL JNTU KPHB KUKATPALLY ESI LAKDIKAPOOL CHARMINAR",
"VST HIMAYATHNAGAR SECRETARIAT LAKDIKAPOOL AMIRPET EARRAGADDA KUKATPALLY KPHS MIYAPUR BHEL",
"PATTANCHERVU RCPURAM MIYAPUR KPHS KUKATPALLY BALANAGAR BOYANPALLY PATNY SECUNDRABAD",
"DUNDIGAL JDM BALANAGAR SANATHNAGAR AMIRPET LAKDIKAPOOL MJMARKET CHARMINAR",
"SECUNDRABAD INK HAYATHNAGAR NACHARAM NFC ECIL ECILXROAD",
"ECILXRD TARNAKA SECUNDRABAD PANJAGUTTA JUBLIBHILLS MASABTANK MIYAPUR MEHADIPATNAM",
"KANDUKUR TUKKUGUDA PAHADI CHANDRAYANAGUTTA MADINA SAIDABAD WOMENSCOLLEGE",
"CHARMINAR ENGINEBOWLI CHANDRAYANAGUTTA PAHADI TUKKUGUDA MAHESHWARAM",
"MANCHANPALLY MAHESHAWARAM CHARMINAR NAMPALLY BATA SECUNDRABAD",
"IMLIBU NLGXROAD IS SADAN BIRAMALGUDA TURKAEMZAL IBP",
"KOTI BKP VIDYANAGAR TARNAKA UPPAL MEDIPALLY GHATKESAR",
"GHATKESAR MEDIPALLY UPPAL TARNAKA METTUGUDA SECUNDRABAD",
"HAYATHNAGAR  LAKDIKAPOOL B.NAGAR NAGOLEXROAD TARNAKA METTUGUDA SECUNDRABAD",
"HAYATHNAGAR LAKDIKAPOOL NAGAR DILSUKHNAGAR MALAKPET SALARJUNGMUSEUM CHARMINAR",
"HAYATHNAGAR DILSUKHNAGAR WOMENSCOLLEGE ABIDS NAMPALLY MASABTANK MEHADIPATNAM"]

con=sql.connect('hyderabad_busroute_database')
curs=con.cursor()
for i in range(len(busnumber)):
    data= "INSERT INTO busroute(BUS_NUMBER, BUS_ROUTE) VALUES (?, ?)"
    j=busnumber[i]
    k=busroute[i]
    curs.execute(data,(j,k))
con.commit()
con.close()   
print("data inserted")