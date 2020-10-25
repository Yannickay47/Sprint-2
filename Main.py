# Yannick Bailey
# The program I'm creating is to be used for the game League of Legends it will tell you how many cs per minute you should be getting at the rank you are!
#  It will also tell you what items to get for the champion you have decided!

name = input("What is your name?: ")
x = ' '
ez = x*3
# Added the ez to enter three spaces inbetween popularity and winrate
# Added the x to create a space inbetween Hello and this
print("Hello" + x + name + x + "this program will help you climb in ranked League of Legends by telling you champions winrate, popularity, and best items and spells!")
# Now I'm adding all the data for the champs to then be linked to an input to display winrate, popularity, and best core items for the inputed champio.n
# I'm using the website called League Graphs for all of the data needed.
# used string operator + to make sure the spaces were added and popularity, winrate and items
ezreal = "Popularity = 27.6%" + ez + "Winrate = 48.2%" + ez + "Manamune,Iceborn Gauntlet, Death's Dance"
lucian = "Popularity = 27.6%" + ez + "Winrate = 47.9%" + ez + "Essence Reaver, Infinity Edge, Rapid Firecannon"
jhin = "Popularity 22.1%" + ez + "Winrate = 47.9%" + ez + "Infinity Edge, Rapid Firecannon, Stormrazor"
caitlyn = "Popularity 20.3%" + ez + "Winrate = 49.5%" + ez + "Infinity Edge, Stormrazor, Rapid Firecannon"
ashe = "Popularity 19.1%" + ez + "Winrate = 51%" + ez + "Essence Reaver, Runaan's Hurricane, Infinity Edge"
thresh = "Popularity 18%" + ez + "Winrate = 48.8%" + ez + "Zeke's Convergence, Knights Vow, Redemption"
lulu = "Popularity 17.6%" + ez + "Winrate = 52.2%" + ez + "Ardent Censer, Athene's Unholy Grail, Mikael's Crucible"
senna = "Popularity 16.7%" + ez + "Winrate = 50.2%" + ez + "Manamune, Black Cleaver, Runaan's Hurricane"
kaisa = "Popularity 16.2%" + ez + "Winrate = 49.2%" + ez + "Essence Reaver, Nashor's Tooth, Guinsoo's Rageblade"
leesin = "Popularity 15.9%" + ez + "Winrate = 45.9%" + ez + "Enchantment Warriors, Black Cleaver, Death's Dance"
yasuo = "Popularity = 14.8%" + ez + "Winrate = 48.8%" + ez + "Blade of the Ruined King, Phantom Dancer, Infinty Edge"
hecarim = "Popularity = 14.5%" + ez + "Winrate = 52.4%" + ez + "Trinity Force, Enchantment Cinderhulk, Death's Dance"
akali = "Popularity = 14.5%" + ez + "Winrate = 47.2%" + ez + "Hextech Gunblade, Liandry's Torment, Zhonyas Hourglass"
yone = "Popularity = 14.3%" + ez + "Winrate = 47.9%" + ez + "Statikk Shiv, Infinity Edge, Death's Dance"
vayne = "Popularity = 14.2%" + ez + "Winrate = 51.2%" + ez + "Blade of the Ruined King, Guinsoo's Rageblade, Phantom Dancer"
sylas = "Popularity = 13.8%" + ez + "Winrate = 47.9%" + ez + "Hextech GLP-800, Zhonya's Hourglass, Liandry's Torment"
zed = "Popularity = 13.7%" + ez + "Winrate = 52.4%" + ez + "Duskblade of Draktharr, Youmuu's Ghostblade, Edge of Night"
lux = "Popularity = 13.7%" + ez + "Winrate = 51.1%" + ez + "Athene's Unholy Grail, Ardent Censer, Redemption"
ekko = "Pupularity = 13.4%" + ez + "Winrate = 50.3%" + ez + "Hextech Protobelt-01, Lich Bane, Rabadon's Deathcap"
sett= "Popularity = 12.6%" + ez + "Winrate = 48.6%" + ez + "Blade of the Ruined King, Black Cleaver"
kayn = "Popularity = 12%" + ez + "Winrate = 51%" + ez + "Enchantment Warrior, Black Cleaver, Death's Dance"
irelia = "Popularity = 11.9%" + ez + "Winrate = 46.9%" + ez + "Blade of the Ruined King, Trinity Force, Death's Dance"
graves = "Popularity = 11.7%" + ez + "Winrate = 50.2%" + ez + "Enchantment Warriors, Black Cleaver, Phantom Dancer"
shen = "Popularity 11.6%" + ez + "Winrate = 51.1%" + ez + "Titanic Hydra, Sunfire Cape, Spirit Visage"
camille = "Popularity = 11.3%" + ez + "Winrate = 50.1%" + ez + "Trinity Force, Death's Dance, Ravenous Hydra"
pyke = "Popularity = 11.1%" + ez + "Winrate = 49.5%" + ez + "Umbral Glaive, Youmuu's Ghostblade, Guardian Angel"
yuumi = "Popularity = 11.1%" + ez + "Winrate = 49.5%" + ez + "Athene's Unholy Grail, Ardent Censer, Mikael's Crucible"
khazix = "Popularity = 10.6%" + ez + "Winrate = 51.6%"
morgana = "Popularity = 10.5%" + ez + "Winrate = 50.1%"
jax = "Popularity = 9.5%" + ez + "Winrate = 50.5%"
pantheon = "Popularity = 9.3%" + ez + "Winrate = 49.6%"
miss_fortune = "Popularity = 9.2%" + ez + "Winrate = 51.5%"
nautilus = "Popularity = 9.2%" + ez + "Winrate = 49.3%"
renekton = "Popularity = 9.0%" + ez + "Winrate = 49.4%"
leona = "Popularity = 8.9%" + ez + "Winrate = 50.5%"
malphite = "Popularity = 8.9%" + ez + "50.6%"
vladimir = "Popularity = 8.8%" + ez + "Winrate = 49.7%"
lillia = "Popularity = 8.6%" + ez + "Winrate = 46.9%"
ahri = "Popularity = 8.5%" + ez + "Winrate = 52%"
fiora = "Popularity = 8.5%" + ez + "Winrate = 51.8%"
darius = "Popularity = 7.9%" + ez + "Winrate = 50.1%"
blitzcrank = "Popularity = 7.5%" + ez + "Winrate = 51%"
twitch = "Popularity = 7.5%" + ez + "Winrate = 51%"
nunuandwillump = "Popularity = 7.5%" + ez + "Winrate = 53.4%"
orianna = "Popularity = 7.3%" + ez + "Winrate = 49.4%"
mordekaiser = "Popularity = 7.3%" + ez + "Winrate = 49.3%"
katarina = "Popularity = 7.1%" + ez + "Winrate = 51.7%"
maokai = "Popularity = 7.1%" + ez + "Winrate = 52.5%"
volibear = "Popularity = 7%" + ez + "Winrate = 49.3%"
soraka = "Popularity = 7%" + ez + "Winrate = 51.7%"
garen = "Popularity = 7%" + ez + "Winrate = 49.8%"
jinx = "Popularity = 7%" + ez + "Winrate = 51.6%"
nami = "Popularity = 7%" + ez + "Winrate = 52.3%"
kassadin = "Popularity = 6.6%" + ez + "Winrate = 51.6%"
janna = "Popularity = 6.4%" + ez + "Winrate = 52.5%"
evelynn = "Popularity = 6.4%" + ez + "Winrate = 49.5%"
zac = "Popularity = 6.4%" + ez + "Winrate = 51%"
shaco = "Popularity = 6.2%" + ez + "Winrate = 50.6%"
masteryi = "Popularity = 6.1%" + ez + "Winrate = 51.1%"
bard = "Popularity = 6%" + ez + "Winrate = 51.4%"
karma = "Popularity = 6%" + ez + "Winrate = 46.9%"
riven = "Popularity = 5.9%" + ez + "Winrate = 50.8%"
nidalee = "Popularity = 5.9%" + ez + "Winrate = 48%"
kayle = "Popularity = 5.8%" + ez + "Winrate = 51.5%"
swain = "Popularity = 5.7%" + ez + "Winrate = 50.7%"
fizz = "Popularity = 5.7%" + ez + "Winrate = 51.3%"
galio = "Popularity = 5.7%" + ez + "Winrate = 51.7%"
tristana = "Popularity = 5.6%" + ez + "Winrate = 49.9%"
draven = "Popularity = 5.6%" + ez + "Winrate = 49.8%"
elise = "Popularity = 5.5%" + ez + "Winrate = 51%"
leblanc = "Popularity = 5.4%" + ez + "Winrate = 47.3%"
fiddlesticks = "Popularity = 5.4%" + ez + "Winrate = 52%"
zoe = "Popularity = 5.3%" + ez + "Winrate = 48.4%"
rengar = "Popularity = 5.2%" + ez + "Winrate = 50.3%"
veigar = "Popularity = 5.2%" + ez + "Winrate = 49.9%"
vi = "Popularity = 5.2%" + ez + "Winrate = 52%"
urgot = "Popularity = 5.1%" + ez + "Winrate = 49.9%"
rakan = "Popularity = 5%" + ez + "Winrate = 52%"
velkoz = "Popularity = 4.8%" + ez + "Winrate = 51%"
karthus = "Popular = 4.8%" + ez + "Winrate = 52%"
ornn = "Popularity = 4.7%" + ez + "Winrate = 52%"
gragas = "Popularity = 4.7%" + ez + "Winrate = 47.3%"
aphelios = "Popularity = 4.7%" + ez + "Winrate = 46.2%"
warwick = "Popularity = 4.6%" + ez + "Winrate = 51.4%"
diana = "Popularity = 4.5%" + ez + "Winrate = 51.4%"
wukong = "Popularity = 4.5% " + ez + "Winrate = 52.6%"
syndra = "Popularity = 4.5%" + ez + "Winrate = 47.7%"
xerath = "Popularity = 4.5%" + ez + "Winrate = 50%"
cassiopeia = "Popularity = 4.4%" + ez + "Winrate = 50.9%"
zilean = "Popularity = 4.4%" + ez + "Winrate = 51.3%"
jarvaniv = "Popularity = 4.1%" + ez + "Winrate = 48.9%"
olaf = "Popularity = 4%" + ez + "Winrate = 49.9"
teemo = "Popularity = 4%" + ez + "Winrate = 50.5%"
shyvana = "Popularity = 4%" + ez + "Winrate = 50.8%"
brand = "Popularity = 4%" + ez + "Winrate = 48.9%"
alistar = "Popularity = 4%" + ez + "Winrate = 50.8%"
aatrox = "Popularity = 3.9%" + ez + "Winrate = 48.6%"
zyra = "Popularity = 3.9%" + ez + "Winrate = 50%"
xayah = "Popularity = 3.9%" + ez + "Winrate = 48.3%"
talon = "Popularity = 3.8%" + ez + "Winrate = 51.4%"
jayce = "Popularity = 3.8%" + ez + "Winrate = 47.2%"
sona = "Popularity = 3.7%" + ez + "Winrate = 52.4%"
twistedfate = "Popularity = 3.6%" + ez + "Winrate = 46.4%"
tryndamere = "Popularity = 3.6%" + ez + "Winrate = 49.5%"
gangplank = "Popularity = 3.5%" + ez + "Winrate = 47.2%"
nasus = "Popularity = 3.5%" + ez + "Winrate = 50.4%"
nocturne = "Popularity = 3.4%" + ez + "Winrate = 49%"
sivir = "Popularity = 3.4%" + ez + "Winrate = 51%"
reksai = "Popularity = 3.4%" + ez + "Winrate = 58.7%"
rammus = "Popularity = 3.3%" + ez + "Winrate = 51.1%"
poppy = "Popularity = 3.3" + ez + "Winrate = 50.6%"
kalista = "popularity = 3.3%" + ez + "Winrate = 47%"
braum = "Popularity = 3.2%" + ez + "Winrate = 47.5%"
kindred = "Popularity = 3.2%" + ez + "Winrate = 49.2%"
malzahar = "Popularity = 3.1%" + ez + "Winrate = 50.9%"
amumu = "Popularity = 3.1%" + ez + "Winrate = 50.2%"
annie = "Popularity = 3.1%" + ez + "Winrate = 52.9%"
sion = "Popularity = 3%" + ez + "Winrate = 48.4%"
taric = "Popularity = 3%" + ez + "Winrate = 53.3%"
ziggs = "Popularity = 2.9%" + ez + "Winrate = 50.3%"
gnar = "Popularity = 2.9%" + ez + "Winrate = 48.5%"
rumble = "Popularity = 2.8%" + ez + "Winrate = 49.4%"
viktor = "Popularity = 2.8%" + ez + "Winrate = 49.8%"
ryze = "Popularity = 2.8%" + ez + "Winrate = 47.6%"
udyr = "Popularity = 2.8%" + ez + "Winrate = 48.3%"
neeko = "Popularity = 2.8%" + ez + "Winrate = 50.7%"
lissandra = "Popularity = 2.6%" + ez + "Winrate = 49.4%"
kled = "Popularity = 2.4%" + ez + "Winrate = 51.7%"
singed = "Popularity = 2.4%" + ez + "Winrate = 50.7%"
sejuani = "Popularity = 2.4%" + ez + "Winrate = 49.1%"
qiyana = "Popularity = 2.4%" + ez + "Winrate = 47.5%"
quinn = "Popularity = 2.3%" + ez + "Winrate = 52.9%"
xinzhao = "Popularity = 2.3%" + ez + "Winrate = 50.4%"
illoai = "Popularity = 2.1%" + ez + "Winrate = 49.1%"
skarner = "Popularity = 2%" + ez + "Winrate = 51.8%"
drmundo = "Popularity = 2%" + ez + "Winrate = 50.3%"
kennen = "Popularity = 1.9%" + ez + "Winrate = 49.9%"
ivern = "Popularity = 1.9%" + ez + "Winrate = 1.9%"
anivia = "Popularity = 1.9%" + ez + "Winrate = 50.3%"
azir = "Popularity = 1.8%" + ez + "Winrate = 44.6%"
heimerdinger = "Popularity = 1.8%" + ez + "Winrate = 51.4%"
kogmaw = "Popularity = 1.8%" + ez + "Winrate = 50.3%"
yorick = "Popularity = 1.8%" + ez + "Winrate = 50.8%"
tahmkench = "Popularity = 1.7%" + ez + "Winrate = 46.2%"
corki = "Popularity = 1.5%" + ez + "Winrate = 47.7%"
trundle = "Popularity = 1.4%" + ez + "Winrate = 46.7%"
varus = "Popularity = 1.3%" + ez + "Winrate = 47.7%"
aurelionsol = "Popularity = 1.2%" + ez + "Winrate = 50.5%"
taliyah = "Popularity = 1.1%" + ez + "Winrate = 50%"

# setting champion to an input that will be taken out of the list and displayed
champion = input("Input your Champion: ")
# Now I'm making the input of champion = to to the inputed champion and displaying the stats and items.

if champion == "Ezreal":
    print(ezreal)
elif champion == "Lucian":
    print(lucian)
elif champion == "Jhin":
    print(jhin)
elif champion == "Caitlyn":
    print(caitlyn)
elif champion == "Ashe":
    print(ashe)
elif champion == "Thresh":
    print(thresh)
elif champion == "Lulu":
    print(lulu)
elif champion == "Senna":
    print(senna)
elif champion == "Kai'sa":
    print(kaisa)
elif champion == "Leesin":
    print(leesin)
elif champion == "Yasuo":
    print(yasuo)
elif champion == "Hecarim":
    print(hecarim)
elif champion == "Akali":
    print(akali)
elif champion == "Yone":
    print(yone)
elif champion == "Vayne":
    print(vayne)
elif champion == "Sylas":
    print(sylas)
elif champion == "Zed":
    print(zed)
elif champion == "Lux":
    print(lux)
elif champion == "Ekko":
    print(ekko)
elif champion == "Sett":
    print(sett)
elif champion == "Kayn":
    print(kayn)
elif champion == "Irelia":
    print(irelia)
elif champion == "Graves":
    print(graves)
elif champion == "Shen":
    print(shen)
elif champion == "Camille":
    print(camille)
elif champion == "Pyke":
    print(pyke)
elif champion == "Yuumi":
    print(yuumi)
elif champion == "Kha'Zix":
    print(khazix)
elif champion == "Morgana":
    print(morgana)
elif champion == "Jax":
    print(jax)
elif champion == "Pantheon":
    print(pantheon)
elif champion == "Miss Fortune":
    print(miss_fortune)
elif champion == "Nautilus":
    print(nautilus)
elif champion == "Renekton":
    print(renekton)
elif champion == "Leona":
    print(leona)
elif champion == "Malphite":
    print(malphite)
elif champion == "Vladimir":
    print(vladimir)
elif champion == "Lillia":
    print(lillia)
elif champion == "Ahri":
    print(ahri)
elif champion == "Fiora":
    print(fiora)
elif champion == "Darius":
    print(darius)
elif champion == "Blitzcrank":
    print(blitzcrank)
elif champion == "Twitch":
    print(twitch)
elif champion == "Nunu and Willump":
    print(nunuandwillump)
elif champion == "Orianna":
    print(orianna)
elif champion == "Mordekaiser":
    print(mordekaiser)
elif champion == "Katarina":
    print(katarina)
elif champion == "Maokai":
    print(maokai)
elif champion == "Volibear":
    print(volibear)
elif champion == "Soraka":
    print(soraka)
elif champion == "Garen":
    print(garen)
elif champion == "Jinx":
    print(jinx)
elif champion == "Nami":
    print(nami)
elif champion == "Kassadin":
    print(kassadin)
elif champion == "Janna":
    print(janna)
elif champion == "Evelynn":
    print(evelynn)
elif champion == "Zac":
    print(zac)
elif champion == "Shaco":
    print(shaco)
elif champion == "Master Yi":
    print(masteryi)
elif champion == "Bard":
    print(bard)
elif champion == "Karma":
    print(karma)
elif champion == "Riven":
    print(riven)
elif champion == "Nidalee":
    print(nidalee)
elif champion == "Kayle":
    print(kayle)
elif champion == "Swain":
    print(swain)
elif champion == "Fizz":
    print(fizz)
elif champion == "Galio":
    print(galio)
elif champion == "Tristanna":
    print(tristana)
elif champion == "Draven":
    print(draven)
elif champion == "ELise":
    print(elise)
elif champion == "Leblanc":
    print(leblanc)
elif champion == "Fiddlesticks":
    print(fiddlesticks)
elif champion == "Zoe":
    print(zoe)
elif champion == "Rengar":
    print(rengar)
elif champion == "Veigar":
    print(veigar)
elif champion == "Vi":
    print(vi)
elif champion == "Urgot":
    print(urgot)
elif champion == "Rakan":
    print(rakan)
elif champion == "Vel'Koz":
    print(velkoz)
elif champion == "Karthus":
    print(karthus)
elif champion == "Ornn":
    print(ornn)
elif champion == "Gragas":
    print(gragas)
elif champion == "Aphelios":
    print(aphelios)
elif champion == "Warwick":
    print(warwick)
elif champion == "Diana":
    print(diana)
elif champion == "Wukong":
    print(wukong)
elif champion == "Syndra":
    print(syndra)
elif champion == "Xerath":
    print(xerath)
elif champion == "Cassiopeia":
    print(cassiopeia)
elif champion == "Zilean":
    print(zilean)
elif champion == "Jarvan IV":
    print(jarvaniv)
elif champion == "Olaf":
    print(olaf)
elif champion == "Teemo":
    print(teemo)
elif champion == "Shyvana":
    print(shyvana)
elif champion == "Brand":
    print(brand)
elif champion == "Alistar":
    print(alistar)
elif champion == "Aatrox":
    print(aatrox)
elif champion == "Zyra":
    print(zyra)
elif champion == "Xayah":
    print(xayah)
elif champion == "Talon":
    print(talon)
elif champion == "Jayce":
    print(jayce)
elif champion == "Sona":
    print(sona)
elif champion == "Twisted Fate":
    print(twistedfate)
elif champion == "Tryndamere":
    print(tryndamere)
elif champion == "Gang Plank":
    print(gangplank)
elif champion == "Nasus":
    print(nasus)
elif champion == "Nocturne":
    print(nocturne)
elif champion == "Sivir":
    print(sivir)
elif champion == "Rek'Sai":
    print(reksai)
elif champion == "Rammus":
    print(rammus)
elif champion == "Poppy":
    print(poppy)
elif champion == "Kalista":
    print(kalista)
elif champion == "Braum":
    print(braum)
elif champion == "Kindred":
    print(kindred)
elif champion == "Malzahar":
    print(malzahar)
elif champion == "Amumu":
    print(amumu)
elif champion == "Annie":
    print(annie)
elif champion == "Sion":
    print(sion)
elif champion == "Taric":
    print(taric)
elif champion == "Ziggs":
    print(ziggs)
elif champion == "Gnar":
    print(gnar)
elif champion == "Rumble":
    print(rumble)
elif champion == "Viktor":
    print(viktor)
elif champion == "Ryze":
    print(ryze)
elif champion == "Udyr":
    print(udyr)
elif champion == "Neeko":
    print(neeko)
elif champion == "Lissandra":
    print(lissandra)
elif champion == "Kled":
    print(kled)
elif champion == "Singed":
    print(singed)
elif champion == "Sejuani":
    print(sejuani)
elif champion == "Qiyana":
    print(qiyana)
elif champion == "Quinn":
    print(quinn)
elif champion == "Xin Zhao":
    print(xinzhao)
elif champion == "Illaoi":
    print(illoai)
elif champion == "Skarner":
    print(skarner)
elif champion == "Dr Mundo":
    print(drmundo)
elif champion == "Kennen":
    print(kennen)
elif champion == "Ivern":
    print(ivern)
elif champion == "Anivia":
    print(anivia)
elif champion == "Azir":
    print(azir)
elif champion == "Heimerdinger":
    print(heimerdinger)
elif champion == "Kog'Maw":
    print(kogmaw)
elif champion == "Yorick":
    print(yorick)
elif champion == "Tahm Kench":
    print(tahmkench)
elif champion == "Corki":
    print(corki)
elif champion == "Trundle":
    print(trundle)
elif champion == "Varus":
    print(varus)
elif champion == "Aurelion Sol":
    print(aurelionsol)
elif champion == "Taliyah":
    print(taliyah)
else :
    print("Not a valid champion :D")
print("Thanks for using my program good luck getting to Master! ;D")
# Uses addition to add the two numbers
#print(10+5)
# Uses multiplication to times the to numbers
#print(10*5)
# Uses division to divide the two numbers
#print(10/5)
# Uses floor division to return floor values for both integer and floating-point arguments
#print(10//5)
# Uses Modulus to return the remainder from the division
#print(10%5)
# Multiplies 10 five times uses exponentiation to get your answer
#print(10**5)
# Assignment and shortcut operators
#a = 21
#b = 10
#c = 0
#c = a + b
#print("Line 1 - Value of c is ", c)
# c += a is equivalent to c = c + a
#c += a
#print("Line 2 - Value of c is ", c)

# c *= a is equivalent to c = c * a
#c *= a
#print("Line 3 - Value of c is ", c)

# c /= a is equivalent to c = c / a
#c /= a
#print("Line 5 - Value of c is ", c)

# c %= a is equivalent to c = c % a
#c %= a
#print("Line 5 - Value of c is ", c)

# c **= a is equivalent to c = c ** a
#c **= a
#print("Line 6 - Value of c is ", c)

# c //= a is equivalent to c = c // a
#c //= a
#print("Line 7 - Value of c is ", c)

# I'm now creating a program to track when you'll be locked out of the instance you're grinding in classic World of Warcraft.
# There is a max of 5 instances you can use every hour#
#importing time to add a countdown for the 5 instances per hour
# importing the time module
import time


# defining the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Instance is unlocked!!!')


# input time in seconds
t = input("Enter the time in seconds 3600 seconds in 1 hour: ")

# function call
countdown(int(t))

# Now I'm making the sure the user knows what dungeon to start.
deadMines = ("10 to 15")
instance = input("What dungeon?: ")
if instance != "DeadMines":
    print("You need to start at Deamines for lvl 10-15")
#dungeons = ["DeadMines","Stockades","Scarlet Monastery"]
#for g in dungeons:
    #if g == "DeadMines":
       # break
    #print(g)


#x = range(3, 6)
#for n in x:
  #print(n)
#Examples of not, and, or
#isSunday = True
#isHoliday = True

#if isHoliday and isSunday:
    #print('Sunday is a Funday!!')
#else:
    p#rint('Not holiday bro!! Please start working :(')

#isSunday = True
#isHoliday = False

#if isHoliday or isSunday:
    #print('Sunday is a Funday!!')
#else:
    #print('Not holiday bro!! Please start working :(')

#isSunday = True
#isHoliday = False

#if not isHoliday:
    #print('Please start working, it is not holiday')
#else:
    #print('Today is holiday pal!!')


















