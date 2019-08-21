from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 680)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgOther/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon10.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Infinity_Edge_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Guardian_Angel_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Zekes_Herald_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/The_Bloodthirster_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Hextech_Gunblade_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Sword_Of_The_Divine_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Youmous_Ghostblade_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Spear_of_Shojin_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Thornmail_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Red_Buff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Sword_Breaker_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Locket_of_the_Iron_Solari_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Phantom_Dancer_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Knights_Vow_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Frozen_Heart_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Warmogs_Armor_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Zephyr_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Morellonomicon_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Titanic_Hydra_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Frozen_Mallet_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Redemption_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Dragons_Claw_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Ionic_Spark_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Dervish_Blade_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Runaans_Hurricane_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Hush_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Rabadons_Deathcap_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Guinsoos_Rageblade_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Yuumi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Ludens_Echo_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Rapid_Firecannon_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Blade_of_the_Ruined_King_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Statikk_Shiv_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Force_of_Nature_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Darkin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap(":/imgCombined/img/combined/Seraphs_Embrace_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        icon100 = QtGui.QIcon()
        icon100.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/KhaZixSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon101 = QtGui.QIcon()
        icon101.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/PykeSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon102 = QtGui.QIcon()
        icon102.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/ZedSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon103 = QtGui.QIcon()
        icon103.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/Katarina_HighCommandSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon104 = QtGui.QIcon()
        icon104.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/EvelynnSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon105 = QtGui.QIcon()
        icon105.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/RengarSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon106 = QtGui.QIcon()
        icon106.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/AkaliSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon107 = QtGui.QIcon()
        icon107.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/CamilleSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon108 = QtGui.QIcon()
        icon108.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/FioraSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon109 = QtGui.QIcon()
        icon109.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/ShenSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon110 = QtGui.QIcon()
        icon110.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/AatroxSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon111 = QtGui.QIcon()
        icon111.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/Gangplank_CaptainSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon112 = QtGui.QIcon()
        icon112.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/Draven_GladiatorSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon113 = QtGui.QIcon()
        icon113.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/YasuoSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon114 = QtGui.QIcon()
        icon114.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/LissandraSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon115 = QtGui.QIcon()
        icon115.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/KennenSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon116 = QtGui.QIcon()
        icon116.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/BrandSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon117 = QtGui.QIcon()
        icon117.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/AniviaSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon118 = QtGui.QIcon()
        icon118.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/WarwickSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon119 = QtGui.QIcon()
        icon119.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/ViSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon120 = QtGui.QIcon()
        icon120.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/RekSaiSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon121 = QtGui.QIcon()
        icon121.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/BlitzcrankSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon122 = QtGui.QIcon()
        icon122.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/VolibearSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon123 = QtGui.QIcon()
        icon123.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/ChoGathSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon124 = QtGui.QIcon()
        icon124.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/Vayne_ArclightSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon125 = QtGui.QIcon()
        icon125.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/VarusSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon126 = QtGui.QIcon()
        icon126.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/AsheSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon127 = QtGui.QIcon()
        icon127.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/KindredSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon128 = QtGui.QIcon()
        icon128.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/Graves_CutthroatSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon129 = QtGui.QIcon()
        icon129.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/JinxSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon130 = QtGui.QIcon()
        icon130.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/TristanaSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon131 = QtGui.QIcon()
        icon131.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/LucianSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon132 = QtGui.QIcon()
        icon132.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/Miss_Fortune_CaptainFortuneSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon133 = QtGui.QIcon()
        icon133.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/DariusSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon134 = QtGui.QIcon()
        icon134.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/GarenSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon135 = QtGui.QIcon()
        icon135.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/MordekaiserSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon136 = QtGui.QIcon()
        icon136.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/PoppySquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon137 = QtGui.QIcon()
        icon137.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/SejuaniSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon138 = QtGui.QIcon()
        icon138.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/KayleSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon139 = QtGui.QIcon()
        icon139.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/BraumSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon140 = QtGui.QIcon()
        icon140.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/LeonaSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon141 = QtGui.QIcon()
        icon141.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/KassadinSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon142 = QtGui.QIcon()
        icon142.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/AhriSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon143 = QtGui.QIcon()
        icon143.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/Twisted_Fate_CutpurseSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon144 = QtGui.QIcon()
        icon144.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/LuluSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon145 = QtGui.QIcon()
        icon145.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/VeigarSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon146 = QtGui.QIcon()
        icon146.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/MorganaSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon147 = QtGui.QIcon()
        icon147.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/Aurelion_SolSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon148 = QtGui.QIcon()
        icon148.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/KarthusSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon149 = QtGui.QIcon()
        icon149.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/NidaleeSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon150 = QtGui.QIcon()
        icon150.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/EliseSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon151 = QtGui.QIcon()
        icon151.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/JayceSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon152 = QtGui.QIcon()
        icon152.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/ShyvanaSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon153 = QtGui.QIcon()
        icon153.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/GnarSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon154 = QtGui.QIcon()
        icon154.addPixmap(QtGui.QPixmap(":/imgChampions/img/champions/SwainSquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.baseItems = {
            "BF": {"name": "B.F. Sword", "icon": icon3},
            "CV": {"name": "Chain Vest", "icon": icon2},
            "GB": {"name": "Giant's Belt", "icon": icon1},
            "NC": {"name": "Negatron Cloak", "icon": icon5},
            "NLR": {"name": "Needlessly Large Rod", "icon": icon4},
            "RB": {"name": "Recurve Bow", "icon": icon6},
            "Spat": {"name": "Spatula", "icon": icon7},
            "Tear": {"name": "Tear of the Goddess", "icon": icon8},
        }
        self.fullItems = {
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
        self.championGuide = {
            "Kha'Zix": {"items": ['RBRB', 'BFBF', 'TearTear', 'NLRTear'], "icon": icon100},
            "Pyke": {"items": ['BFTear', 'CVTear', 'GBNLR', 'SpatTear'], "icon": icon101},
            "Zed": {"items": ['RBRB', 'BFBF', 'BFNC', 'BFGB'], "icon": icon102},
            "Katarina": {"items": ['GBNLR', 'BFNLR', 'NLRNLR', 'NLRSpat'], "icon": icon103},
            "Evelynn": {"items": ['TearTear', 'GBNLR', 'NLRNLR', 'NLRSpat'], "icon": icon104},
            "Rengar": {"items": ['RBRB', 'BFCV', 'BFNC', 'NCNC'], "icon": icon105},
            "Akali": {"items": ['TearTear', 'NCNC', 'BFNLR', 'CVRB', 'GBGB', 'BFCV'], "icon": icon106},
            "Camille": {"items": [], "icon": icon107},
            "Fiora": {"items": ['RBTear', 'BFNLR', 'BFNC', 'RBRB'], "icon": icon108},
            "Shen": {"items": ['NCNC', 'CVCV', 'BFCV', 'GBGB'], "icon": icon109},
            "Aatrox": {"items": ['BFNLR', 'BFCV', 'NCNC', 'CVRB', 'NLRSpat'], "icon": icon110},
            "Gangplank": {"items": ['NCTear', 'GBCV', 'GBNLR', 'BFTear', 'BFCV', 'CVNC'], "icon": icon111},
            "Draven": {"items": ['RBRB', 'BFNC', 'NLRRB', 'NCNC', 'BFBF', 'CVRB', 'BFCV'], "icon": icon112},
            "Yasuo": {"items": ['TearTear', 'CVGB', 'GBGB', 'NCTear', 'CVNC', 'NCNC'], "icon": icon113},
            "Lissandra": {"items": [], "icon": icon114},
            "Kennen": {"items": ['GBNLR', 'BFCV', 'NLRNLR', 'NCNC', 'CVRB'], "icon": icon115},
            "Brand": {"items": ['BFTear', 'RBRB', 'GBNLR'], "icon": icon116},
            "Anivia": {"items": ['GBNLR', 'NLRNLR', 'TearTear'], "icon": icon117},
            "Warwick": {"items": [], "icon": icon118},
            "Vi": {"items": ['CVTear', 'GBGB', 'NLRSpat', 'GBNLR', 'BFTear'], "icon": icon119},
            "Rek'Sai": {"items": ['BFTear', 'NLRRB', 'RBRB', 'CVRB', 'GBGB', 'BFCV'], "icon": icon120},
            "Blitzcrank": {"items": ['NLRNLR', 'BFTear'], "icon": icon121},
            "Volibear": {"items": ['RBRB', 'SpatTear', 'BFBF', 'GBRB', 'NCSpat', 'GBCV', 'BFNC'], "icon": icon122},
            "Cho'Gath": {"items": ['TearTear', 'BFCV', 'GBNLR', 'NLRNLR', 'RBRB', 'NLRSpat'], "icon": icon123},
            "Vayne": {"items": ['RBTear', 'GBRB', 'RBRB', 'NLRRB'], "icon": icon124},
            "Varus": {"items": ['BFTear', 'GBNLR', 'NLRRB', 'RBTear', 'NLRNLR', 'NLRSpat'], "icon": icon125},
            "Ashe": {"items": ['RBTear', 'RBRB', 'NLRRB', 'BFTear'], "icon": icon126},
            "Kindred": {"items": ['NLRSpat', 'BFCV', 'CVRB', 'RBTear'], "icon": icon127},
            "Graves": {"items": ['CVGB', 'GBRB', 'BFBF'], "icon": icon128},
            "Jinx": {"items": ['NCSpat', 'RBSpat', 'RBRB', 'BFNC', 'NLRRB', 'CVGB'], "icon": icon129},
            "Tristana": {"items": ['NCRB', 'NCTear', 'RBSpat', 'BFBF', 'GBRB'], "icon": icon130},
            "Lucian": {"items": ['NCRB', 'NCTear', 'CVGB', 'NLRTear', 'CVNC', 'TearTear'], "icon": icon131},
            "Miss Fortune": {"items": ['TearTear', 'GBNLR', 'BFCV'], "icon": icon132},
            "Darius": {"items": ['GBGB', 'NCNC'], "icon": icon133},
            "Garen": {"items": ['NCNC', 'GBGB', 'CVRB', 'GBNLR'], "icon": icon134},
            "Mordekaiser": {"items": [], "icon": icon135},
            "Poppy": {"items": ['NLRSpat', 'NCNC', 'CVRB', 'GBGB', 'NCNLR'], "icon": icon136},
            "Sejuani": {"items": ['GBNLR', 'BFCV', 'NCNC', 'CVRB', 'GBGB'], "icon": icon137},
            "Kayle": {"items": ['RBSpat', 'NLRSpat', 'BFTear', 'RBTear', 'NCSpat', 'NLRRB', 'RBRB'], "icon": icon138},
            "Braum": {"items": ['CVCV', 'NCNC', 'GBGB'], "icon": icon139},
            "Leona": {"items": ['NLRTear', 'TearTear'], "icon": icon140},
            "Kassadin": {"items": ['RBRB', 'NLRRB', 'NCNC', 'CVRB', 'BFNC', 'NLRNLR'], "icon": icon141},
            "Ahri": {"items": ['RBTear', 'NLRTear', 'TearTear', 'GBNLR', 'NLRNLR'], "icon": icon142},
            "Twisted Fate": {"items": ['RBTear', 'TearTear', 'NLRTear', 'RBRB'], "icon": icon143},
            "Lulu": {"items": ['BFTear', 'NLRRB', 'NLRNLR', 'NCNLR'], "icon": icon144},
            "Veigar": {"items": ['TearTear', 'BFNLR', 'NCNC', 'CVRB', 'RBRB'], "icon": icon145},
            "Morgana": {"items": ['NLRNLR', 'GBNLR', 'CVTear', 'TearTear', 'NCNC', 'BFCV'], "icon": icon146},
            "Aurelion Sol": {"items": ['RBRB', 'BFTear', 'NLRNLR', 'GBNLR'], "icon": icon147},
            "Karthus": {"items": ['GBNLR', 'NLRNLR', 'BFTear', 'TearTear'], "icon": icon148},
            "Nidalee": {"items": ['RBRB', 'RBTear', 'BFNC'], "icon": icon149},
            "Elise": {"items": ['GBGB', 'CVTear'], "icon": icon150},
            "Jayce": {"items": [], "icon": icon151},
            "Shyvana": {"items": ['GBGB', 'CVCV', 'CVRB', 'RBRB', 'BFNC', 'NLRRB'], "icon": icon152},
            "Gnar": {"items": ['GBGB', 'GBRB', 'CVRB', 'NCNC'], "icon": icon153},
            "Swain": {"items": ['GBGB', 'NLRNLR', 'BFNLR', 'GBNLR', 'BFCV', 'TearTear', 'NCNC', 'CVRB'], "icon": icon154},
        }
        self.userInventory = []
        self.doubleInventory = []
        self.inventoryButtons = {}
        self.doubleButtons = {}
        





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
        self.label_5.raise_()
        self.frame_3.raise_()
        self.label_10.raise_()
        self.buttonReset.raise_()
        self.buttonQuit.raise_()
        self.buttonCraft.raise_()
        MainWindow.setCentralWidget(self.centralwidget)






        def addInventory(itemID):
            self.userInventory.append(itemID)
            inventoryButtonID = ("invItem" + str(len(self.userInventory)))
            self.inventoryButtons[inventoryButtonID] = QtWidgets.QToolButton(self.centralwidget)
            self.inventoryButtons[inventoryButtonID].setGeometry(QtCore.QRect(((len(self.userInventory) * 50) - 40), 100, 46, 46)) #adds 50 pixels per item in userInventory
            self.inventoryButtons[inventoryButtonID].setToolTip(self.baseItems[itemID]["name"])
            self.inventoryButtons[inventoryButtonID].setIcon(self.baseItems[itemID]["icon"])
            self.inventoryButtons[inventoryButtonID].setIconSize(QtCore.QSize(46, 46))
            self.inventoryButtons[inventoryButtonID].setObjectName(inventoryButtonID)
            self.inventoryButtons[inventoryButtonID].show()
            self.userInventory.sort()

        def clearInventory():
            for buttonKey in self.inventoryButtons:
                self.inventoryButtons[buttonKey].deleteLater()
            self.inventoryButtons = {}
            self.userInventory = []
            self.doubleInventory = []

        def craftItems():
            count = 0
            for i in range(len(self.userInventory)):
                for j in range(i+1, len(self.userInventory)):
                    if (self.userInventory[i] + self.userInventory[j]) not in self.doubleInventory:
                        craftedItem = self.userInventory[i] + self.userInventory[j]
                        self.doubleInventory.append(craftedItem)
                        self.doubleButtons[craftedItem] = QtWidgets.QToolButton(self.centralwidget)
                        self.doubleButtons[craftedItem].setGeometry(QtCore.QRect(10, ((count * 50) + 180), 46, 46)) #adds 50 pixels vertically per item
                        self.doubleButtons[craftedItem].setToolTip(self.fullItems[craftedItem]["name"])
                        self.doubleButtons[craftedItem].setIcon(self.fullItems[craftedItem]["icon"])
                        self.doubleButtons[craftedItem].setIconSize(QtCore.QSize(46, 46))
                        self.doubleButtons[craftedItem].setObjectName(craftedItem)
                        self.doubleButtons[craftedItem].show()
                        count += 1
            








        self.retranslateUi(MainWindow)
        self.buttonQuit.clicked.connect(MainWindow.close)
        self.buttonBF.clicked.connect(lambda: addInventory("BF"))
        self.buttonCV.clicked.connect(lambda: addInventory("CV"))
        self.buttonGB.clicked.connect(lambda: addInventory("GB"))
        self.buttonNC.clicked.connect(lambda: addInventory("NC"))
        self.buttonNLR.clicked.connect(lambda: addInventory("NLR"))
        self.buttonRB.clicked.connect(lambda: addInventory("RB"))
        self.buttonSpat.clicked.connect(lambda: addInventory("Spat"))
        self.buttonTear.clicked.connect(lambda: addInventory("Tear"))
        self.buttonReset.clicked.connect(lambda: clearInventory())
        self.buttonCraft.clicked.connect(lambda: craftItems())
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
    app = QtWidgets.QApplication(sys.argv)x
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
