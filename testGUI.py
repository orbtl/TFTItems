from PyQt5 import QtCore, QtGui, QtWidgets

baseItems = {
    "BF": {"name": "B.F. Sword", "icon": icon1},
    "CV": "Chain Vest",
    "GB": "Giant's Belt",
    "NC": "Negatron Cloak",
    "NLR": "Needlessly Large Rod",
    "RB": "Recurve Bow",
    "Spat": "Spatula",
    "Tear": "Tear of the Goddess"
}
fullItems = {
    "BFBF": {"name": "Infinity Edge", "icon": icon10},
    "BFCV": {"name": "Guardian Angel", "icon": icon11},
    "BFGB": {"name": "Zeke's Herald", "icon": icon12},
    "BFNC": {"name": "Bloodthirster", "icon": icon13},
    "BFNLR": {"name": "Hextech Gunblade", "icon": icon14},
    "BFRB": {"name": "Sword Of The Divine", "icon": icon15},
    "BFSpat": {"name": "Youmou's Ghostblade", "icon": icon16},
    "BFTear": {"name": "Spear of Shojin", "icon": icon17},
    "CVCV": {"name": "Thornmail", "icon": icon18},
    "CVGB": {"name": "Red Buff", "icon": icon19},
    "CVNC": {"name": "Sword Breaker", "icon": icon20},
    "CVNLR": {"name": "Locket of the Iron Solari", "icon": icon21},
    "CVRB": {"name": "Phantom Dancer", "icon": icon22},
    "CVSpat": {"name": "Knight's Vow", "icon": icon23},
    "CVTear": {"name": "Frozen Heart", "icon": icon24},
    "GBGB": {"name": "Warmog's Armor", "icon": icon25},
    "GBNC": {"name": "Zephyr", "icon": icon26},
    "GBNLR": {"name": "Morellonomicon", "icon": icon27},
    "GBRB": {"name": "Titanic Hydra", "icon": icon28},
    "GBSpat": {"name": "Frozen Mallet", "icon": icon29},
    "GBTear": {"name": "Redemption", "icon": icon30},
    "NCNC": {"name": "Dragon's Claw", "icon": icon31},
    "NCNLR": {"name": "Ionic Spark", "icon": icon32},
    "NCRB": {"name": "Cursed Blade", "icon": icon33},
    "NCSpat": {"name": "Hurricane", "icon": icon34},
    "NCTear": {"name": "Hush", "icon": icon35},
    "NLRNLR": {"name": "Rabadon's Deathcap", "icon": icon36},
    "NLRRB": {"name": "Guinsoo's Rageblade", "icon": icon37},
    "NLRSpat": {"name": "Yuumi", "icon": icon38},
    "NLRTear": {"name": "Luden's Echo", "icon": icon39},
    "RBRB": {"name": "Rapidfire Cannon", "icon": icon40},
    "RBSpat": {"name": "Blade of the Ruined King", "icon": icon41},
    "RBTear": {"name": "Statikk Shiv", "icon": icon42},
    "SpatSpat": {"name": "Force of Nature", "icon": icon43},
    "SpatTear": {"name": "Darkin", "icon": icon44},
    "TearTear": {"name": "Seraph's Embrace", "icon": icon45},
}
championGuide = {
    "Kha'Zix": ["RBRB", "BFBF", "TearTear", "NLRTear"],
    "Pyke": ["BFTear", "CVTear", "GBNLR", "SpatTear"],
    "Zed": ["RBRB", "BFBF", "BFNC", "BFGB"],
    "Katarina": ["GBNLR", "BFNLR", "NLRNLR", "NLRSpat"],
    "Evelynn": ["TearTear", "GBNLR", "NLRNLR", "NLRSpat"],
    "Rengar": ["RBRB", "BFCV", "BFNC", "NCNC"],
    "Akali": ["TearTear", "NCNC", "BFNLR", "CVRB", "GBGB", "BFCV"],
    "Camille": [],
    "Fiora": ["RBTear", "BFNLR", "BFNC", "RBRB"],
    "Shen": ["NCNC", "CVCV", "BFCV", "GBGB"],
    "Aatrox": ["BFNLR", "BFCV", "NCNC", "CVRB", "NLRSpat"],
    "Gangplank": ["NCTear", "GBCV", "GBNLR", "BFTear", "BFCV", "CVNC"],
    "Draven": ["RBRB", "BFNC", "NLRRB", "NCNC", "BFBF", "CVRB", "BFCV"],
    "Yasuo": ["TearTear", "CVGB", "GBGB", "NCTear", "CVNC", "NCNC"],
    "Lissandra": [],
    "Kennen": ["GBNLR", "BFCV", "NLRNLR", "NCNC", "CVRB"],
    "Brand": ["BFTear", "RBRB", "GBNLR"],
    "Anivia": ["GBNLR", "NLRNLR", "TearTear"],
    "Warwick": [],
    "Vi": ["CVTear", "GBGB", "NLRSpat", "GBNLR", "BFTear"],
    "Rek'Sai": ["BFTear", "NLRRB", "RBRB", "CVRB", "GBGB", "BFCV"],
    "Blitzcrank": ["NLRNLR", "BFTear"],
    "Volibear": ["RBRB", "SpatTear", "BFBF", "GBRB", "NCSpat", "GBCV", "BFNC"],
    "Cho'Gath": ["TearTear", "BFCV", "GBNLR", "NLRNLR", "RBRB", "NLRSpat"],
    "Vayne": ["RBTear", "GBRB", "RBRB", "NLRRB"],
    "Varus": ["BFTear", "GBNLR", "NLRRB", "RBTear", "NLRNLR", "NLRSpat"],
    "Ashe": ["RBTear", "RBRB", "NLRRB", "BFTear"],
    "Kindred": ["NLRSpat", "BFCV", "CVRB", "RBTear"],
    "Graves": ["CVGB", "GBRB", "BFBF"],
    "Jinx": ["NCSpat", "RBSpat", "RBRB", "BFNC", "NLRRB", "CVGB"],
    "Tristana": ["NCRB", "NCTear", "RBSpat", "BFBF", "GBRB"],
    "Lucian": ["NCRB", "NCTear", "CVGB", "NLRTear", "CVNC", "TearTear"],
    "Miss Fortune": ["TearTear", "GBNLR", "BFCV"],
    "Darius": ["GBGB", "NCNC"],
    "Garen": ["NCNC", "GBGB", "CVRB", "GBNLR"],
    "Mordekaiser": [],
    "Poppy": ["NLRSpat", "NCNC", "CVRB", "GBGB", "NCNLR"],
    "Sejuani": ["GBNLR", "BFCV", "NCNC", "CVRB", "GBGB"],
    "Kayle": ["RBSpat", "NLRSpat", "BFTear", "RBTear", "NCSpat", "NLRRB", "RBRB"],
    "Braum": ["CVCV", "NCNC", "GBGB"],
    "Leona": ["NLRTear", "TearTear"],
    "Kassadin": ["RBRB", "NLRRB", "NCNC", "CVRB", "BFNC", "NLRNLR"],
    "Ahri": ["RBTear", "NLRTear", "TearTear", "GBNLR", "NLRNLR"],
    "Twisted Fate": ["RBTear", "TearTear", "NLRTear", "RBRB"],
    "Lulu": ["BFTear", "NLRRB", "NLRNLR", "NCNLR"],
    "Veigar": ["TearTear", "BFNLR", "NCNC", "CVRB", "RBRB"],
    "Morgana": ["NLRNLR", "GBNLR", "CVTear", "TearTear", "NCNC", "BFCV"],
    "Aurelion Sol": ["RBRB", "BFTear", "NLRNLR", "GBNLR"],
    "Karthus": ["GBNLR", "NLRNLR", "BFTear", "TearTear"],
    "Nidalee": ["RBRB", "RBTear", "BFNC"],
    "Elise": ["GBGB", "CVTear"],
    "Jayce": [],
    "Shyvana": ["GBGB", "CVCV", "CVRB", "RBRB", "BFNC", "NLRRB"],
    "Gnar": ["GBGB", "GBRB", "CVRB", "NCNC"],
    "Swain": ["GBGB", "NLRNLR", "BFNLR", "GBNLR", "BFCV", "TearTear", "NCNC", "CVRB"]
}







class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 680)
        
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName("centralwidget")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgOther/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgBase/img/base/Giants_Belt_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imgBase/img/base/Chain_Vest_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imgBase/img/base/B._F._Sword_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imgBase/img/base/Needlessly_Large_Rod_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imgBase/img/base/Negatron_Cloak_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/imgBase/img/base/Recurve_Bow_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/imgBase/img/base/Spatula_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/imgBase/img/base/Tear_of_the_Goddess_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Infinity_Edge_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Guardian_Angel_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Zekes_Herald_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/The_Bloodthirster_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Hextech_Gunblade_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Sword_Of_The_Divine_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Youmous_Ghostblade_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Spear_of_Shojin_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Thornmail_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Red_Buff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Sword_Breaker_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Locket_of_the_Iron_Solari_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Phantom_Dancer_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Knights_Vow_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Frozen_Heart_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Warmogs_Armor_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Zephyr_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Morellonomicon_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Titanic_Hydra_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Frozen_Mallet_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Redemption_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Dragons_Claw_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Ionic_Spark_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Dervish_Blade_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Hurricane_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Hush_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Rabadons_Deathcap_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Guinsoos_Rageblade_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Yuumi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Ludens_Echo_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Rapid_Firecannon_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Blade_of_the_Ruined_King_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Statikk_Shiv_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Force_of_Nature_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Darkin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap(":/imgBase/img/combined/Seraphs_Embrace_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)












        self.buttonGB = QtWidgets.QToolButton(self.centralwidget)
        self.buttonGB.setGeometry(QtCore.QRect(110, 10, 46, 46))
        
        self.buttonGB.setIcon(icon1)
        self.buttonGB.setIconSize(QtCore.QSize(46, 46))
        self.buttonGB.setObjectName("buttonGB")
        self.buttonCV = QtWidgets.QToolButton(self.centralwidget)
        self.buttonCV.setGeometry(QtCore.QRect(60, 10, 46, 46))
        
        self.buttonCV.setIcon(icon2)
        self.buttonCV.setIconSize(QtCore.QSize(46, 46))
        self.buttonCV.setObjectName("buttonCV")
        self.buttonBF = QtWidgets.QToolButton(self.centralwidget)
        self.buttonBF.setGeometry(QtCore.QRect(10, 10, 46, 46))
        
        self.buttonBF.setIcon(icon3)
        self.buttonBF.setIconSize(QtCore.QSize(46, 46))
        self.buttonBF.setObjectName("buttonBF")
        self.buttonNLR = QtWidgets.QToolButton(self.centralwidget)
        self.buttonNLR.setGeometry(QtCore.QRect(160, 10, 46, 46))
        
        self.buttonNLR.setIcon(icon4)
        self.buttonNLR.setIconSize(QtCore.QSize(46, 46))
        self.buttonNLR.setObjectName("buttonNLR")
        self.buttonNC = QtWidgets.QToolButton(self.centralwidget)
        self.buttonNC.setGeometry(QtCore.QRect(210, 10, 46, 46))
        
        self.buttonNC.setIcon(icon5)
        self.buttonNC.setIconSize(QtCore.QSize(46, 46))
        self.buttonNC.setObjectName("buttonNC")
        self.buttonRB = QtWidgets.QToolButton(self.centralwidget)
        self.buttonRB.setGeometry(QtCore.QRect(260, 10, 46, 46))
        
        self.buttonRB.setIcon(icon6)
        self.buttonRB.setIconSize(QtCore.QSize(46, 46))
        self.buttonRB.setObjectName("buttonRB")
        self.buttonSpat = QtWidgets.QToolButton(self.centralwidget)
        self.buttonSpat.setGeometry(QtCore.QRect(310, 10, 46, 46))
        
        self.buttonSpat.setIcon(icon7)
        self.buttonSpat.setIconSize(QtCore.QSize(46, 46))
        self.buttonSpat.setObjectName("buttonSpat")
        self.buttonTear = QtWidgets.QToolButton(self.centralwidget)
        self.buttonTear.setGeometry(QtCore.QRect(360, 10, 46, 46))
        
        self.buttonTear.setIcon(icon8)
        self.buttonTear.setIconSize(QtCore.QSize(46, 46))
        self.buttonTear.setObjectName("buttonTear")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(12, 55, 47, 13))
        
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 55, 47, 13))

        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 55, 47, 13))

        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 55, 47, 21))

        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(210, 55, 47, 21))

        self.label_7.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 55, 47, 21))

        self.label_8.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(360, 55, 47, 21))

        self.label_9.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 55, 47, 13))

        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.exInvItem_0 = QtWidgets.QLabel(self.centralwidget)
        self.exInvItem_0.setEnabled(True)
        self.exInvItem_0.setGeometry(QtCore.QRect(10, 100, 46, 46))
        self.exInvItem_0.setText("")
        self.exInvItem_0.setPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Blade_of_the_Ruined_King_item.png"))
        self.exInvItem_0.setObjectName("exInvItem_0")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 77, 691, 10))

        self.frame.setPalette(palette)
        self.frame.setStyleSheet("border-color: rgb(209, 209, 209);")
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(410, 0, 16, 81))

        self.frame_2.setPalette(palette)
        self.frame_2.setStyleSheet("border-color: rgb(209, 209, 209);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(324, 85, 47, 13))

        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 150, 691, 10))

        self.frame_3.setPalette(palette)
        self.frame_3.setStyleSheet("border-color: rgb(209, 209, 209);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setMidLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(230, 160, 241, 16))

        self.label_10.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.exCompItem_0 = QtWidgets.QLabel(self.centralwidget)
        self.exCompItem_0.setEnabled(True)
        self.exCompItem_0.setGeometry(QtCore.QRect(10, 180, 46, 46))
        self.exCompItem_0.setText("")
        self.exCompItem_0.setPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Blade_of_the_Ruined_King_item.png"))
        self.exCompItem_0.setObjectName("exCompItem_0")
        self.exCompItem_1 = QtWidgets.QLabel(self.centralwidget)
        self.exCompItem_1.setEnabled(True)
        self.exCompItem_1.setGeometry(QtCore.QRect(10, 230, 46, 46))
        self.exCompItem_1.setText("")
        self.exCompItem_1.setPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Blade_of_the_Ruined_King_item.png"))
        self.exCompItem_1.setObjectName("exCompItem_1")
        self.exCompItem_2 = QtWidgets.QLabel(self.centralwidget)
        self.exCompItem_2.setEnabled(True)
        self.exCompItem_2.setGeometry(QtCore.QRect(10, 280, 46, 46))
        self.exCompItem_2.setText("")
        self.exCompItem_2.setPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Blade_of_the_Ruined_King_item.png"))
        self.exCompItem_2.setObjectName("exCompItem_2")
        self.exCompItem_3 = QtWidgets.QLabel(self.centralwidget)
        self.exCompItem_3.setEnabled(True)
        self.exCompItem_3.setGeometry(QtCore.QRect(10, 330, 46, 46))
        self.exCompItem_3.setText("")
        self.exCompItem_3.setPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Blade_of_the_Ruined_King_item.png"))
        self.exCompItem_3.setObjectName("exCompItem_3")
        self.exCompItem_4 = QtWidgets.QLabel(self.centralwidget)
        self.exCompItem_4.setEnabled(True)
        self.exCompItem_4.setGeometry(QtCore.QRect(10, 380, 46, 46))
        self.exCompItem_4.setText("")
        self.exCompItem_4.setPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Blade_of_the_Ruined_King_item.png"))
        self.exCompItem_4.setObjectName("exCompItem_4")
        self.exCompItem_5 = QtWidgets.QLabel(self.centralwidget)
        self.exCompItem_5.setEnabled(True)
        self.exCompItem_5.setGeometry(QtCore.QRect(10, 430, 46, 46))
        self.exCompItem_5.setText("")
        self.exCompItem_5.setPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Blade_of_the_Ruined_King_item.png"))
        self.exCompItem_5.setObjectName("exCompItem_5")
        self.exCompItem_6 = QtWidgets.QLabel(self.centralwidget)
        self.exCompItem_6.setEnabled(True)
        self.exCompItem_6.setGeometry(QtCore.QRect(10, 480, 46, 46))
        self.exCompItem_6.setText("")
        self.exCompItem_6.setPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Blade_of_the_Ruined_King_item.png"))
        self.exCompItem_6.setObjectName("exCompItem_6")
        self.exInvItem_1 = QtWidgets.QLabel(self.centralwidget)
        self.exInvItem_1.setEnabled(True)
        self.exInvItem_1.setGeometry(QtCore.QRect(60, 100, 46, 46))
        self.exInvItem_1.setText("")
        self.exInvItem_1.setPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Blade_of_the_Ruined_King_item.png"))
        self.exInvItem_1.setObjectName("exInvItem_1")
        self.exCompItem_7 = QtWidgets.QLabel(self.centralwidget)
        self.exCompItem_7.setEnabled(True)
        self.exCompItem_7.setGeometry(QtCore.QRect(10, 530, 46, 46))
        self.exCompItem_7.setText("")
        self.exCompItem_7.setPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Blade_of_the_Ruined_King_item.png"))
        self.exCompItem_7.setObjectName("exCompItem_7")
        self.exCompItem_8 = QtWidgets.QLabel(self.centralwidget)
        self.exCompItem_8.setEnabled(True)
        self.exCompItem_8.setGeometry(QtCore.QRect(10, 580, 46, 46))
        self.exCompItem_8.setText("")
        self.exCompItem_8.setPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Blade_of_the_Ruined_King_item.png"))
        self.exCompItem_8.setObjectName("exCompItem_8")
        self.exCompItem_9 = QtWidgets.QLabel(self.centralwidget)
        self.exCompItem_9.setEnabled(True)
        self.exCompItem_9.setGeometry(QtCore.QRect(10, 630, 46, 46))
        self.exCompItem_9.setText("")
        self.exCompItem_9.setPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Blade_of_the_Ruined_King_item.png"))
        self.exCompItem_9.setObjectName("exCompItem_9")
        self.buttonReset = QtWidgets.QToolButton(self.centralwidget)
        self.buttonReset.setGeometry(QtCore.QRect(520, 10, 71, 61))

        self.buttonReset.setPalette(palette)
        self.buttonReset.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(255, 255, 255);")
        self.buttonReset.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.buttonReset.setAutoRaise(False)
        self.buttonReset.setObjectName("buttonReset")
        self.buttonQuit = QtWidgets.QToolButton(self.centralwidget)
        self.buttonQuit.setGeometry(QtCore.QRect(610, 10, 71, 61))

        self.buttonQuit.setPalette(palette)
        self.buttonQuit.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(255, 255, 255);")
        self.buttonQuit.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.buttonQuit.setAutoRaise(False)
        self.buttonQuit.setObjectName("buttonQuit")
        self.buttonCraft = QtWidgets.QToolButton(self.centralwidget)
        self.buttonCraft.setGeometry(QtCore.QRect(430, 10, 71, 61))

        self.buttonCraft.setPalette(palette)
        self.buttonCraft.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(255, 255, 255);")
        self.buttonCraft.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.buttonCraft.setAutoRaise(False)
        self.buttonCraft.setObjectName("buttonCraft")
        self.frame.raise_()
        self.frame_2.raise_()
        self.buttonGB.raise_()
        self.buttonCV.raise_()
        self.buttonBF.raise_()
        self.buttonNLR.raise_()
        self.buttonNC.raise_()
        self.buttonRB.raise_()
        self.buttonSpat.raise_()
        self.buttonTear.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_4.raise_()
        self.exInvItem_0.raise_()
        self.label_5.raise_()
        self.frame_3.raise_()
        self.label_10.raise_()
        self.exCompItem_0.raise_()
        self.exCompItem_1.raise_()
        self.exCompItem_2.raise_()
        self.exCompItem_3.raise_()
        self.exCompItem_4.raise_()
        self.exCompItem_5.raise_()
        self.exCompItem_6.raise_()
        self.exInvItem_1.raise_()
        self.exCompItem_7.raise_()
        self.exCompItem_8.raise_()
        self.exCompItem_9.raise_()
        self.buttonReset.raise_()
        self.buttonQuit.raise_()
        self.buttonCraft.raise_()
        MainWindow.setCentralWidget(self.centralwidget)










        self.buttonTest = QtWidgets.QToolButton(self.centralwidget)
        self.buttonTest.setGeometry(QtCore.QRect(300, 300, 46, 46))
        testDict = {
            "GB": [icon1, "Giant's Belt"],
            "CV": [icon2, "Chain Vest"]
        }
        buttonTestName = "CV"
        self.buttonTest.setIcon(testDict[buttonTestName][0])
        self.buttonTest.setIconSize(QtCore.QSize(46, 46))
        self.buttonTest.setObjectName("buttonTest")
        self.buttonTest.setToolTip(testDict[buttonTestName][1])










        self.retranslateUi(MainWindow)
        self.buttonQuit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TFT Item/Champion Guide"))
        self.buttonGB.setText(_translate("MainWindow", "..."))
        self.buttonCV.setText(_translate("MainWindow", "..."))
        self.buttonBF.setText(_translate("MainWindow", "..."))
        self.buttonNLR.setText(_translate("MainWindow", "..."))
        self.buttonNC.setText(_translate("MainWindow", "..."))
        self.buttonRB.setText(_translate("MainWindow", "..."))
        self.buttonSpat.setText(_translate("MainWindow", "..."))
        self.buttonTear.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "BF Sword"))
        self.label_2.setText(_translate("MainWindow", "Chain Vest"))
        self.label_3.setText(_translate("MainWindow", "Giants Belt"))
        self.label_6.setText(_translate("MainWindow", "Recurve Bow"))
        self.label_7.setText(_translate("MainWindow", "Negatron Cloak"))
        self.label_8.setText(_translate("MainWindow", "Needlessly Large Rod"))
        self.label_9.setText(_translate("MainWindow", "Tear of the Goddess"))
        self.label_4.setText(_translate("MainWindow", "Spatula"))
        self.label_5.setText(_translate("MainWindow", "Inventory"))
        self.label_10.setText(_translate("MainWindow", "Craftable Items and Scarra\'s Recommended Champions"))
        self.buttonReset.setText(_translate("MainWindow", "Reset Items"))
        self.buttonQuit.setText(_translate("MainWindow", "Quit"))
        self.buttonCraft.setText(_translate("MainWindow", "Craft Items"))




import TFTItems_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
