baseItems = {
    "BF": "B.F. Sword",
    "CV": "Chain Vest",
    "GB": "Giant's Belt",
    "NC": "Negatron Cloak",
    "NLR": "Needlessly Large Rod",
    "RB": "Recurve Bow",
    "Spat": "Spatula",
    "Tear": "Tear of the Goddess"
}
fullItems = {
    "BFBF": "Infinity Edge",
    "BFCV": "Guardian Angel",
    "BFGB": "Zeke's Herald",
    "BFNC": "Bloodthirster",
    "BFNLR": "Hextech Gunblade",
    "BFRB": "Sword Of The Divine",
    "BFSpat": "Youmou's Ghostblade",
    "BFTear": "Spear of Shojin",
    "CVCV": "Thornmail",
    "CVGB": "Red Buff",
    "CVNC": "Sword Breaker",
    "CVNLR": "Locket of the Iron Solari",
    "CVRB": "Phantom Dancer",
    "CVSpat": "Knight's Vow",
    "CVTear": "Frozen Heart",
    "GBGB": "Warmog's Armor",
    "GBNC": "Zephyr",
    "GBNLR": "Morellonomicon",
    "GBRB": "Titanic Hydra",
    "GBSpat": "Frozen Mallet",
    "GBTear": "Redemption",
    "NCNC": "Dragon's Claw",
    "NCNLR": "Ionic Spark",
    "NCRB": "Cursed Blade",
    "NCSpat": "Hurricane",
    "NCTear": "Hush",
    "NLRNLR": "Rabadon's Deathcap",
    "NLRRB": "Guinsoo's Rageblade",
    "NLRSpat": "Yuumi",
    "NLRTear": "Luden's Echo",
    "RBRB": "Rapidfire Cannon",
    "RBSpat": "Blade of the Ruined King",
    "RBTear": "Statikk Shiv",
    "SpatSpat": "Force of Nature",
    "SpatTear": "Darkin",
    "TearTear": "Seraph's Embrace"
}
userInventory = []
combinedItems = []
doubleInventory = []

def printInventory():
    inventoryString = ', '.join([baseItems[item] for item in userInventory])
    print("Your current items: " + inventoryString)

def printBaseItems():
    print(f"""These are the available item codes, followed by their name
    BF: {baseItems["BF"]}
    CV: {baseItems["CV"]}
    GB: {baseItems["GB"]}
    NLR: {baseItems["NLR"]}
    RB: {baseItems["RB"]}
    Tear: {baseItems["Tear"]}
    Spat: {baseItems["Spat"]}
    """)

def getItems():
    print("Enter your items, separated by Enter.  When you are done press enter again.")
    isEmpty = False
    while isEmpty == False:
        newItem = input("Item? ")
        if len(newItem) > 0:
            if newItem in baseItems:
                userInventory.append(newItem)
                print(f"You added a {baseItems[newItem]}")
            else:
                print("Invalid Item Code.  Try again.")
        else:
            isEmpty = True
            userInventory.sort()
            printInventory()

def findCompleteItems():
    for i in range(len(userInventory)):
        for j in range(i+1, len(userInventory)):
            if (userInventory[i] + userInventory[j]) not in doubleInventory:
                doubleInventory.append(userInventory[i] + userInventory[j])
                print(doubleInventory)





printBaseItems()
getItems()

