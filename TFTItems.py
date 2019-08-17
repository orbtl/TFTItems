baseItems = {
    "BF": "B.F. Sword",
    "CV": "Chain Vest",
    "GB": "Giant's Belt",
    "NC": "Negatron Cloak",
    "NLR": "Needlessly Large Rod",
    "RB": "Recurve Bow",
    "Spat": "Spatula"
    "Tear": "Tear of the Goddess",

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
    "CVRB":
}
userInventory = []
combinedItems = []

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



printBaseItems()
getItems()

