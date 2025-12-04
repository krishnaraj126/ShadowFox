justice_league = ["Superman", "Batman", "WonderWoman", "Flash", "Aquaman", "Green Lantern"]

total_members = len(justice_league)
print("Total Members :", total_members)


justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing :", justice_league)


justice_league.remove("WonderWoman")
justice_league.insert(0, "WonderWoman")
print("Wonder Woman at first :", justice_league)


justice_league.remove("Superman") 

index_flash = justice_league.index("Flash")
justice_league.insert(index_flash + 1, "Superman")
print("After moving Superman between Flash and Aquaman:", justice_league)


justice_league = ["Cyborg", "Shazam", "Hawkgirl", "MartianManhunter", "Green Arrow"]
print("New Justice League :", justice_league)


justice_league.sort()
print("Sorted Justice League :", justice_league)


print("New Leader :", justice_league[0])
