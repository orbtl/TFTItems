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
i=10 #sets starting icon number

# these 3 lines make the dictionary
#for code, name in fullItems.items():
#    print('    "' + code + '": {"name": "' + name + '", "icon": icon' + str(i) + '},')
#    i += 1

# these 4 lines generate the icon code
for code, name in fullItems.items():
    print('    icon' + str(i) + ' = QtGui.QIcon()')
    print('    icon' + str(i) + '.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/' + (name.replace(' ', '_')).replace("'", "") + '_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)')
    i += 1