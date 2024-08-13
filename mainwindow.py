from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ThunderloopTeam(object):
    def setupUi(self, ThunderloopTeam):
        ThunderloopTeam.setObjectName("ThunderloopTeam")
        ThunderloopTeam.resize(1949, 1047)
        ThunderloopTeam.setStyleSheet("background:black")
        self.gridLayout = QtWidgets.QGridLayout(ThunderloopTeam)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(ThunderloopTeam)
        self.tabWidget.setStyleSheet("background:black;\n"
"color:black")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.bt_start = QtWidgets.QPushButton(self.tab)
        self.bt_start.setGeometry(QtCore.QRect(10, 20, 141, 51))
        self.bt_start.setStyleSheet(".QPushButton{\n"
"    font: 16pt \"Oblivious font\";\n"
"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background-color: rgb(0, 150, 0);\n"
"}")
        self.bt_start.setObjectName("bt_start")
        self.bt_stop = QtWidgets.QPushButton(self.tab)
        self.bt_stop.setGeometry(QtCore.QRect(180, 20, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Oblivious font")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bt_stop.setFont(font)
        self.bt_stop.setStyleSheet(".QPushButton{\n"
"    font: 16pt \"Oblivious font\";\n"
"background-color:red;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background-color:rgb(214, 0, 0);\n"
"}")
        self.bt_stop.setObjectName("bt_stop")
        self.baglan = QtWidgets.QLabel(self.tab)
        self.baglan.setGeometry(QtCore.QRect(330, 30, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.baglan.setFont(font)
        self.baglan.setStyleSheet("color:white")
        self.baglan.setText("")
        self.baglan.setAlignment(QtCore.Qt.AlignCenter)
        self.baglan.setObjectName("baglan")
        self.hyperloop = QtWidgets.QPushButton(self.tab)
        self.hyperloop.setGeometry(QtCore.QRect(930, 30, 71, 41))
        self.hyperloop.setStyleSheet("background:none;\n"
"border:none;")
        self.hyperloop.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/hyperloop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hyperloop.setIcon(icon)
        self.hyperloop.setIconSize(QtCore.QSize(30, 30))
        self.hyperloop.setObjectName("hyperloop")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 200, 591, 231))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.orientation_widget = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.orientation_widget.setStyleSheet("border-radius:20%;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n"
"color:white\n"
"")
        self.orientation_widget.setObjectName("orientation_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.orientation_widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ROLL = QtWidgets.QLabel(self.orientation_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ROLL.setFont(font)
        self.ROLL.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ROLL.setObjectName("ROLL")
        self.verticalLayout_3.addWidget(self.ROLL)
        self.PITCH = QtWidgets.QLabel(self.orientation_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.PITCH.setFont(font)
        self.PITCH.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.PITCH.setObjectName("PITCH")
        self.verticalLayout_3.addWidget(self.PITCH)
        self.YAW = QtWidgets.QLabel(self.orientation_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.YAW.setFont(font)
        self.YAW.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.YAW.setObjectName("YAW")
        self.verticalLayout_3.addWidget(self.YAW)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(24)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.roll_veri = QtWidgets.QLabel(self.orientation_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.roll_veri.setFont(font)
        self.roll_veri.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.roll_veri.setAlignment(QtCore.Qt.AlignCenter)
        self.roll_veri.setObjectName("roll_veri")
        self.verticalLayout_4.addWidget(self.roll_veri)
        self.pitch_veri = QtWidgets.QLabel(self.orientation_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pitch_veri.setFont(font)
        self.pitch_veri.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.pitch_veri.setAlignment(QtCore.Qt.AlignCenter)
        self.pitch_veri.setObjectName("pitch_veri")
        self.verticalLayout_4.addWidget(self.pitch_veri)
        self.yaw_veri = QtWidgets.QLabel(self.orientation_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.yaw_veri.setFont(font)
        self.yaw_veri.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.yaw_veri.setStyleSheet("border:3px solid #fff;\n"
"border-radius:20%")
        self.yaw_veri.setAlignment(QtCore.Qt.AlignCenter)
        self.yaw_veri.setObjectName("yaw_veri")
        self.verticalLayout_4.addWidget(self.yaw_veri)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addWidget(self.orientation_widget)
        self.acceleration_widget = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.acceleration_widget.setStyleSheet("border-radius:20%;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n"
"color:white;\n"
"")
        self.acceleration_widget.setObjectName("acceleration_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.acceleration_widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, -1, 11, -1)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.ACCELERATION_x = QtWidgets.QLabel(self.acceleration_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_x.setFont(font)
        self.ACCELERATION_x.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_x.setObjectName("ACCELERATION_x")
        self.verticalLayout_7.addWidget(self.ACCELERATION_x)
        self.ACCELERATION_y = QtWidgets.QLabel(self.acceleration_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_y.setFont(font)
        self.ACCELERATION_y.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_y.setObjectName("ACCELERATION_y")
        self.verticalLayout_7.addWidget(self.ACCELERATION_y)
        self.ACCELERATION_z = QtWidgets.QLabel(self.acceleration_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_z.setFont(font)
        self.ACCELERATION_z.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_z.setObjectName("ACCELERATION_z")
        self.verticalLayout_7.addWidget(self.ACCELERATION_z)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(24)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.acceleration_x = QtWidgets.QLabel(self.acceleration_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.acceleration_x.setFont(font)
        self.acceleration_x.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.acceleration_x.setAlignment(QtCore.Qt.AlignCenter)
        self.acceleration_x.setObjectName("acceleration_x")
        self.verticalLayout_8.addWidget(self.acceleration_x)
        self.acceleration_y = QtWidgets.QLabel(self.acceleration_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.acceleration_y.setFont(font)
        self.acceleration_y.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.acceleration_y.setAlignment(QtCore.Qt.AlignCenter)
        self.acceleration_y.setObjectName("acceleration_y")
        self.verticalLayout_8.addWidget(self.acceleration_y)
        self.acceleration_z = QtWidgets.QLabel(self.acceleration_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.acceleration_z.setFont(font)
        self.acceleration_z.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.acceleration_z.setStyleSheet("border:3px solid #fff;\n"
"border-radius:20%")
        self.acceleration_z.setAlignment(QtCore.Qt.AlignCenter)
        self.acceleration_z.setObjectName("acceleration_z")
        self.verticalLayout_8.addWidget(self.acceleration_z)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addWidget(self.acceleration_widget)
        self.orientation_2 = QtWidgets.QLabel(self.tab)
        self.orientation_2.setGeometry(QtCore.QRect(60, 530, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orientation_2.setFont(font)
        self.orientation_2.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.orientation_2.setObjectName("orientation_2")
        self.vibration_widget = QtWidgets.QWidget(self.tab)
        self.vibration_widget.setGeometry(QtCore.QRect(50, 580, 591, 271))
        self.vibration_widget.setStyleSheet("border-radius:20%;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n"
"color:white")
        self.vibration_widget.setObjectName("vibration_widget")
        self.vibration_front_widget = QtWidgets.QWidget(self.vibration_widget)
        self.vibration_front_widget.setGeometry(QtCore.QRect(10, 40, 271, 209))
        self.vibration_front_widget.setStyleSheet("border-radius:20%;\n"
"background-color:none")
        self.vibration_front_widget.setObjectName("vibration_front_widget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.vibration_front_widget)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(-1, -1, 11, -1)
        self.verticalLayout_12.setSpacing(4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.ACCELERATION_x_4 = QtWidgets.QLabel(self.vibration_front_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_x_4.setFont(font)
        self.ACCELERATION_x_4.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_x_4.setObjectName("ACCELERATION_x_4")
        self.verticalLayout_12.addWidget(self.ACCELERATION_x_4)
        self.ACCELERATION_y_4 = QtWidgets.QLabel(self.vibration_front_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_y_4.setFont(font)
        self.ACCELERATION_y_4.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_y_4.setObjectName("ACCELERATION_y_4")
        self.verticalLayout_12.addWidget(self.ACCELERATION_y_4)
        self.ACCELERATION_z_4 = QtWidgets.QLabel(self.vibration_front_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_z_4.setFont(font)
        self.ACCELERATION_z_4.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_z_4.setObjectName("ACCELERATION_z_4")
        self.verticalLayout_12.addWidget(self.ACCELERATION_z_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(24)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.x_on_veri_2 = QtWidgets.QLabel(self.vibration_front_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.x_on_veri_2.setFont(font)
        self.x_on_veri_2.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.x_on_veri_2.setAlignment(QtCore.Qt.AlignCenter)
        self.x_on_veri_2.setObjectName("x_on_veri_2")
        self.verticalLayout_13.addWidget(self.x_on_veri_2)
        self.y_on_veri_2 = QtWidgets.QLabel(self.vibration_front_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.y_on_veri_2.setFont(font)
        self.y_on_veri_2.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.y_on_veri_2.setAlignment(QtCore.Qt.AlignCenter)
        self.y_on_veri_2.setObjectName("y_on_veri_2")
        self.verticalLayout_13.addWidget(self.y_on_veri_2)
        self.z_on_veri_2 = QtWidgets.QLabel(self.vibration_front_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.z_on_veri_2.setFont(font)
        self.z_on_veri_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.z_on_veri_2.setStyleSheet("border:3px solid #fff;\n"
"border-radius:20%")
        self.z_on_veri_2.setAlignment(QtCore.Qt.AlignCenter)
        self.z_on_veri_2.setObjectName("z_on_veri_2")
        self.verticalLayout_13.addWidget(self.z_on_veri_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_13)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.vibration_back_widget = QtWidgets.QWidget(self.vibration_widget)
        self.vibration_back_widget.setGeometry(QtCore.QRect(300, 40, 271, 209))
        self.vibration_back_widget.setStyleSheet("border-radius:20%;\n"
"background-color:none")
        self.vibration_back_widget.setObjectName("vibration_back_widget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.vibration_back_widget)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setContentsMargins(-1, -1, 11, -1)
        self.verticalLayout_15.setSpacing(4)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.ACCELERATION_x_5 = QtWidgets.QLabel(self.vibration_back_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_x_5.setFont(font)
        self.ACCELERATION_x_5.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_x_5.setObjectName("ACCELERATION_x_5")
        self.verticalLayout_15.addWidget(self.ACCELERATION_x_5)
        self.ACCELERATION_y_5 = QtWidgets.QLabel(self.vibration_back_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_y_5.setFont(font)
        self.ACCELERATION_y_5.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_y_5.setObjectName("ACCELERATION_y_5")
        self.verticalLayout_15.addWidget(self.ACCELERATION_y_5)
        self.ACCELERATION_z_5 = QtWidgets.QLabel(self.vibration_back_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_z_5.setFont(font)
        self.ACCELERATION_z_5.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_z_5.setObjectName("ACCELERATION_z_5")
        self.verticalLayout_15.addWidget(self.ACCELERATION_z_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setSpacing(24)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.x_arka_veri_2 = QtWidgets.QLabel(self.vibration_back_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.x_arka_veri_2.setFont(font)
        self.x_arka_veri_2.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.x_arka_veri_2.setAlignment(QtCore.Qt.AlignCenter)
        self.x_arka_veri_2.setObjectName("x_arka_veri_2")
        self.verticalLayout_16.addWidget(self.x_arka_veri_2)
        self.y_arka_veri_2 = QtWidgets.QLabel(self.vibration_back_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.y_arka_veri_2.setFont(font)
        self.y_arka_veri_2.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.y_arka_veri_2.setAlignment(QtCore.Qt.AlignCenter)
        self.y_arka_veri_2.setObjectName("y_arka_veri_2")
        self.verticalLayout_16.addWidget(self.y_arka_veri_2)
        self.z_arka_veri_2 = QtWidgets.QLabel(self.vibration_back_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.z_arka_veri_2.setFont(font)
        self.z_arka_veri_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.z_arka_veri_2.setStyleSheet("border:3px solid #fff;\n"
"border-radius:20%")
        self.z_arka_veri_2.setAlignment(QtCore.Qt.AlignCenter)
        self.z_arka_veri_2.setObjectName("z_arka_veri_2")
        self.verticalLayout_16.addWidget(self.z_arka_veri_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_16)
        self.verticalLayout_14.addLayout(self.horizontalLayout_5)
        self.front = QtWidgets.QLabel(self.vibration_widget)
        self.front.setGeometry(QtCore.QRect(11, 11, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.front.setFont(font)
        self.front.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.front.setObjectName("front")
        self.back = QtWidgets.QLabel(self.vibration_widget)
        self.back.setGeometry(QtCore.QRect(310, 11, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.back.setObjectName("back")
        self.power_con_widget = QtWidgets.QWidget(self.tab)
        self.power_con_widget.setGeometry(QtCore.QRect(790, 560, 301, 281))
        self.power_con_widget.setObjectName("power_con_widget")
        self.guctuketimi_label = QtWidgets.QLabel(self.power_con_widget)
        self.guctuketimi_label.setGeometry(QtCore.QRect(10, 10, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.guctuketimi_label.setFont(font)
        self.guctuketimi_label.setStyleSheet("color: #fdc600;")
        self.guctuketimi_label.setAlignment(QtCore.Qt.AlignCenter)
        self.guctuketimi_label.setObjectName("guctuketimi_label")
        self.layoutWidget = QtWidgets.QWidget(self.power_con_widget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 220, 281, 21))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(16)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.batarya_1_label = QtWidgets.QLabel(self.layoutWidget)
        self.batarya_1_label.setAutoFillBackground(False)
        self.batarya_1_label.setStyleSheet("color:white;")
        self.batarya_1_label.setFrameShape(QtWidgets.QFrame.Box)
        self.batarya_1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.batarya_1_label.setObjectName("batarya_1_label")
        self.horizontalLayout_6.addWidget(self.batarya_1_label)
        self.batarya_2_label = QtWidgets.QLabel(self.layoutWidget)
        self.batarya_2_label.setAutoFillBackground(False)
        self.batarya_2_label.setStyleSheet("color:white;")
        self.batarya_2_label.setFrameShape(QtWidgets.QFrame.Box)
        self.batarya_2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.batarya_2_label.setObjectName("batarya_2_label")
        self.horizontalLayout_6.addWidget(self.batarya_2_label)
        self.layoutWidget1 = QtWidgets.QWidget(self.power_con_widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 70, 251, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(90)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.batarya1 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.batarya1.setFont(font)
        self.batarya1.setStyleSheet("QLabel {\n"
"                       background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                                      stop: 0 rgba(200, 200, 200, 255), \n"
"                                                      stop: 0.6 rgba(0, 64, 0, 255),  \n"
"                                                      stop: 0.6 rgba(200, 200, 200, 255),\n"
"                                                      stop: 1 rgba(0, 255, 0, 255));\n"
"    color: black;\n"
"    padding: 5px;\n"
"    writing-mode: vertical-rl;\n"
"    transform: rotate(180deg);\n"
"    border:1px solid rgba(200, 200, 200, 230) ;\n"
"}\n"
"")
        self.batarya1.setAlignment(QtCore.Qt.AlignCenter)
        self.batarya1.setObjectName("batarya1")
        self.horizontalLayout_7.addWidget(self.batarya1)
        self.batarya2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.batarya2.setFont(font)
        self.batarya2.setStyleSheet("QLabel {\n"
"                       background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                                      stop: 0 rgba(200, 200, 200, 255), \n"
"                                                      stop: 0.6 rgba(0, 64, 0, 255),  \n"
"                                                      stop: 0.6 rgba(200, 200, 200, 255),\n"
"                                                      stop: 1 rgba(0, 255, 0, 255));\n"
"    color: black;\n"
"    padding: 5px;\n"
"    writing-mode: vertical-rl;\n"
"    transform: rotate(180deg);\n"
"    border:1px solid rgba(200, 200, 200, 230) ;\n"
"}\n"
"")
        self.batarya2.setAlignment(QtCore.Qt.AlignCenter)
        self.batarya2.setObjectName("batarya2")
        self.horizontalLayout_7.addWidget(self.batarya2)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(1440, 440, 301, 111))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.sw_1 = QtWidgets.QCheckBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sw_1.setFont(font)
        self.sw_1.setStyleSheet("QCheckBox {\n"
"    color:                  white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width:                  20px;\n"
"    height:                 20px;\n"
"    border-radius:          11px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:       green;\n"
"    border:                 1px solid green;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:       red;\n"
"    border:                 1px solid red;\n"
"}")
        self.sw_1.setObjectName("sw_1")
        self.verticalLayout_18.addWidget(self.sw_1)
        self.sw_2 = QtWidgets.QCheckBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sw_2.setFont(font)
        self.sw_2.setStyleSheet("QCheckBox {\n"
"    color:                  white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width:                  20px;\n"
"    height:                 20px;\n"
"    border-radius:          11px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:       green;\n"
"    border:                 1px solid green;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:       red;\n"
"    border:                 1px solid red;\n"
"}")
        self.sw_2.setObjectName("sw_2")
        self.verticalLayout_18.addWidget(self.sw_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.sw_3 = QtWidgets.QCheckBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sw_3.setFont(font)
        self.sw_3.setStyleSheet("QCheckBox {\n"
"    color:                  white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width:                  20px;\n"
"    height:                 20px;\n"
"    border-radius:          11px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:       green;\n"
"    border:                 1px solid green;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:       red;\n"
"    border:                 1px solid red;\n"
"}")
        self.sw_3.setObjectName("sw_3")
        self.verticalLayout_19.addWidget(self.sw_3)
        self.sw_4 = QtWidgets.QCheckBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sw_4.setFont(font)
        self.sw_4.setStyleSheet("QCheckBox {\n"
"    color:                  white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width:                  20px;\n"
"    height:                 20px;\n"
"    border-radius:          11px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:       green;\n"
"    border:                 1px solid green;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:       red;\n"
"    border:                 1px solid red;\n"
"}")
        self.sw_4.setObjectName("sw_4")
        self.verticalLayout_19.addWidget(self.sw_4)
        self.horizontalLayout_8.addLayout(self.verticalLayout_19)
        self.vibration_widget_2 = QtWidgets.QWidget(self.tab)
        self.vibration_widget_2.setGeometry(QtCore.QRect(1250, 190, 591, 201))
        self.vibration_widget_2.setStyleSheet("border-radius:20%;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n"
"color:white;\n"
"")
        self.vibration_widget_2.setObjectName("vibration_widget_2")
        self.vibration_front_widget_2 = QtWidgets.QWidget(self.vibration_widget_2)
        self.vibration_front_widget_2.setGeometry(QtCore.QRect(10, 40, 271, 141))
        self.vibration_front_widget_2.setStyleSheet("border-radius:20%;\n"
"background-color:none")
        self.vibration_front_widget_2.setObjectName("vibration_front_widget_2")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.vibration_front_widget_2)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_9.setSpacing(12)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setContentsMargins(-1, -1, 11, -1)
        self.verticalLayout_21.setSpacing(4)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.ACCELERATION_x_6 = QtWidgets.QLabel(self.vibration_front_widget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_x_6.setFont(font)
        self.ACCELERATION_x_6.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_x_6.setObjectName("ACCELERATION_x_6")
        self.verticalLayout_21.addWidget(self.ACCELERATION_x_6)
        self.ACCELERATION_y_6 = QtWidgets.QLabel(self.vibration_front_widget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_y_6.setFont(font)
        self.ACCELERATION_y_6.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_y_6.setObjectName("ACCELERATION_y_6")
        self.verticalLayout_21.addWidget(self.ACCELERATION_y_6)
        self.horizontalLayout_9.addLayout(self.verticalLayout_21)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setSpacing(30)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.x_on_veri_3 = QtWidgets.QLabel(self.vibration_front_widget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.x_on_veri_3.setFont(font)
        self.x_on_veri_3.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.x_on_veri_3.setAlignment(QtCore.Qt.AlignCenter)
        self.x_on_veri_3.setObjectName("x_on_veri_3")
        self.verticalLayout_22.addWidget(self.x_on_veri_3)
        self.y_on_veri_3 = QtWidgets.QLabel(self.vibration_front_widget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.y_on_veri_3.setFont(font)
        self.y_on_veri_3.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.y_on_veri_3.setAlignment(QtCore.Qt.AlignCenter)
        self.y_on_veri_3.setObjectName("y_on_veri_3")
        self.verticalLayout_22.addWidget(self.y_on_veri_3)
        self.horizontalLayout_9.addLayout(self.verticalLayout_22)
        self.verticalLayout_20.addLayout(self.horizontalLayout_9)
        self.vibration_back_widget_2 = QtWidgets.QWidget(self.vibration_widget_2)
        self.vibration_back_widget_2.setGeometry(QtCore.QRect(300, 40, 271, 141))
        self.vibration_back_widget_2.setStyleSheet("border-radius:20%;\n"
"background-color:none\n"
"")
        self.vibration_back_widget_2.setObjectName("vibration_back_widget_2")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.vibration_back_widget_2)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_10.setSpacing(12)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setContentsMargins(-1, -1, 11, -1)
        self.verticalLayout_24.setSpacing(4)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.ACCELERATION_x_7 = QtWidgets.QLabel(self.vibration_back_widget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_x_7.setFont(font)
        self.ACCELERATION_x_7.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_x_7.setObjectName("ACCELERATION_x_7")
        self.verticalLayout_24.addWidget(self.ACCELERATION_x_7)
        self.ACCELERATION_y_7 = QtWidgets.QLabel(self.vibration_back_widget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_y_7.setFont(font)
        self.ACCELERATION_y_7.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_y_7.setObjectName("ACCELERATION_y_7")
        self.verticalLayout_24.addWidget(self.ACCELERATION_y_7)
        self.horizontalLayout_10.addLayout(self.verticalLayout_24)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setSpacing(30)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.x_arka_veri_3 = QtWidgets.QLabel(self.vibration_back_widget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.x_arka_veri_3.setFont(font)
        self.x_arka_veri_3.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.x_arka_veri_3.setAlignment(QtCore.Qt.AlignCenter)
        self.x_arka_veri_3.setObjectName("x_arka_veri_3")
        self.verticalLayout_25.addWidget(self.x_arka_veri_3)
        self.y_arka_veri_3 = QtWidgets.QLabel(self.vibration_back_widget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.y_arka_veri_3.setFont(font)
        self.y_arka_veri_3.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.y_arka_veri_3.setAlignment(QtCore.Qt.AlignCenter)
        self.y_arka_veri_3.setObjectName("y_arka_veri_3")
        self.verticalLayout_25.addWidget(self.y_arka_veri_3)
        self.horizontalLayout_10.addLayout(self.verticalLayout_25)
        self.verticalLayout_23.addLayout(self.horizontalLayout_10)
        self.front_2 = QtWidgets.QLabel(self.vibration_widget_2)
        self.front_2.setGeometry(QtCore.QRect(11, 11, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.front_2.setFont(font)
        self.front_2.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.front_2.setObjectName("front_2")
        self.back_2 = QtWidgets.QLabel(self.vibration_widget_2)
        self.back_2.setGeometry(QtCore.QRect(310, 11, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_2.setFont(font)
        self.back_2.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.back_2.setObjectName("back_2")
        self.orientation_3 = QtWidgets.QLabel(self.tab)
        self.orientation_3.setGeometry(QtCore.QRect(1260, 150, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orientation_3.setFont(font)
        self.orientation_3.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.orientation_3.setObjectName("orientation_3")
        self.orientation_4 = QtWidgets.QLabel(self.tab)
        self.orientation_4.setGeometry(QtCore.QRect(1260, 610, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orientation_4.setFont(font)
        self.orientation_4.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.orientation_4.setObjectName("orientation_4")
        self.vibration_widget_3 = QtWidgets.QWidget(self.tab)
        self.vibration_widget_3.setGeometry(QtCore.QRect(1250, 650, 591, 201))
        self.vibration_widget_3.setStyleSheet("border-radius:20%;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n"
"color:white;\n"
"")
        self.vibration_widget_3.setObjectName("vibration_widget_3")
        self.vibration_front_widget_3 = QtWidgets.QWidget(self.vibration_widget_3)
        self.vibration_front_widget_3.setGeometry(QtCore.QRect(10, 40, 271, 141))
        self.vibration_front_widget_3.setStyleSheet("border-radius:20%;\n"
"background-color:none")
        self.vibration_front_widget_3.setObjectName("vibration_front_widget_3")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.vibration_front_widget_3)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_11.setSpacing(12)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setContentsMargins(-1, -1, 11, -1)
        self.verticalLayout_27.setSpacing(4)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.ACCELERATION_x_8 = QtWidgets.QLabel(self.vibration_front_widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_x_8.setFont(font)
        self.ACCELERATION_x_8.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_x_8.setObjectName("ACCELERATION_x_8")
        self.verticalLayout_27.addWidget(self.ACCELERATION_x_8)
        self.ACCELERATION_y_8 = QtWidgets.QLabel(self.vibration_front_widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_y_8.setFont(font)
        self.ACCELERATION_y_8.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_y_8.setObjectName("ACCELERATION_y_8")
        self.verticalLayout_27.addWidget(self.ACCELERATION_y_8)
        self.horizontalLayout_11.addLayout(self.verticalLayout_27)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setSpacing(30)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.x_on_veri_4 = QtWidgets.QLabel(self.vibration_front_widget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.x_on_veri_4.setFont(font)
        self.x_on_veri_4.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.x_on_veri_4.setAlignment(QtCore.Qt.AlignCenter)
        self.x_on_veri_4.setObjectName("x_on_veri_4")
        self.verticalLayout_28.addWidget(self.x_on_veri_4)
        self.y_on_veri_4 = QtWidgets.QLabel(self.vibration_front_widget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.y_on_veri_4.setFont(font)
        self.y_on_veri_4.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.y_on_veri_4.setAlignment(QtCore.Qt.AlignCenter)
        self.y_on_veri_4.setObjectName("y_on_veri_4")
        self.verticalLayout_28.addWidget(self.y_on_veri_4)
        self.horizontalLayout_11.addLayout(self.verticalLayout_28)
        self.verticalLayout_26.addLayout(self.horizontalLayout_11)
        self.vibration_back_widget_3 = QtWidgets.QWidget(self.vibration_widget_3)
        self.vibration_back_widget_3.setGeometry(QtCore.QRect(300, 40, 271, 141))
        self.vibration_back_widget_3.setStyleSheet("border-radius:20%;\n"
"background-color:none;\n"
"color:white\n"
"")
        self.vibration_back_widget_3.setObjectName("vibration_back_widget_3")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.vibration_back_widget_3)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_12.setSpacing(12)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setContentsMargins(-1, -1, 11, -1)
        self.verticalLayout_30.setSpacing(4)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.ACCELERATION_x_9 = QtWidgets.QLabel(self.vibration_back_widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_x_9.setFont(font)
        self.ACCELERATION_x_9.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_x_9.setObjectName("ACCELERATION_x_9")
        self.verticalLayout_30.addWidget(self.ACCELERATION_x_9)
        self.ACCELERATION_y_9 = QtWidgets.QLabel(self.vibration_back_widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ACCELERATION_y_9.setFont(font)
        self.ACCELERATION_y_9.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.ACCELERATION_y_9.setObjectName("ACCELERATION_y_9")
        self.verticalLayout_30.addWidget(self.ACCELERATION_y_9)
        self.horizontalLayout_12.addLayout(self.verticalLayout_30)
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setSpacing(30)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.x_arka_veri_4 = QtWidgets.QLabel(self.vibration_back_widget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.x_arka_veri_4.setFont(font)
        self.x_arka_veri_4.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.x_arka_veri_4.setAlignment(QtCore.Qt.AlignCenter)
        self.x_arka_veri_4.setObjectName("x_arka_veri_4")
        self.verticalLayout_31.addWidget(self.x_arka_veri_4)
        self.y_arka_veri_4 = QtWidgets.QLabel(self.vibration_back_widget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.y_arka_veri_4.setFont(font)
        self.y_arka_veri_4.setStyleSheet("border:3px solid #fff;\n"
"\n"
"border-radius:20%")
        self.y_arka_veri_4.setAlignment(QtCore.Qt.AlignCenter)
        self.y_arka_veri_4.setObjectName("y_arka_veri_4")
        self.verticalLayout_31.addWidget(self.y_arka_veri_4)
        self.horizontalLayout_12.addLayout(self.verticalLayout_31)
        self.verticalLayout_29.addLayout(self.horizontalLayout_12)
        self.front_3 = QtWidgets.QLabel(self.vibration_widget_3)
        self.front_3.setGeometry(QtCore.QRect(11, 11, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.front_3.setFont(font)
        self.front_3.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.front_3.setObjectName("front_3")
        self.back_3 = QtWidgets.QLabel(self.vibration_widget_3)
        self.back_3.setGeometry(QtCore.QRect(310, 11, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.back_3.setFont(font)
        self.back_3.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.back_3.setObjectName("back_3")
        self.basinc2_label = QtWidgets.QLabel(self.tab)
        self.basinc2_label.setGeometry(QtCore.QRect(1020, 360, 101, 31))
        self.basinc2_label.setAutoFillBackground(False)
        self.basinc2_label.setStyleSheet("color:white;")
        self.basinc2_label.setFrameShape(QtWidgets.QFrame.Box)
        self.basinc2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.basinc2_label.setObjectName("basinc2_label")
        self.arac_basinc = QtWidgets.QGroupBox(self.tab)
        self.arac_basinc.setGeometry(QtCore.QRect(1010, 400, 121, 121))
        self.arac_basinc.setStyleSheet("border:3px solid   #fdc600;\n"
"border-radius:60%;")
        self.arac_basinc.setTitle("")
        self.arac_basinc.setObjectName("arac_basinc")
        self.loc_lbl = QtWidgets.QLabel(self.arac_basinc)
        self.loc_lbl.setGeometry(QtCore.QRect(10, 30, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loc_lbl.setFont(font)
        self.loc_lbl.setStyleSheet("border:none;\n"
"color:white;\n"
"text-align:center;\n"
"background:none")
        self.loc_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.loc_lbl.setObjectName("loc_lbl")
        self.basnc1_label = QtWidgets.QLabel(self.tab)
        self.basnc1_label.setGeometry(QtCore.QRect(760, 360, 101, 31))
        self.basnc1_label.setAutoFillBackground(False)
        self.basnc1_label.setStyleSheet("color:white;")
        self.basnc1_label.setFrameShape(QtWidgets.QFrame.Box)
        self.basnc1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.basnc1_label.setObjectName("basnc1_label")
        self.motor_basinc = QtWidgets.QGroupBox(self.tab)
        self.motor_basinc.setGeometry(QtCore.QRect(750, 400, 121, 121))
        self.motor_basinc.setStyleSheet("border:3px solid  #fdc600;\n"
"border-radius:60%;")
        self.motor_basinc.setTitle("")
        self.motor_basinc.setObjectName("motor_basinc")
        self.perssure_lbl = QtWidgets.QLabel(self.motor_basinc)
        self.perssure_lbl.setGeometry(QtCore.QRect(10, 30, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.perssure_lbl.setFont(font)
        self.perssure_lbl.setStyleSheet("border:none;\n"
"color:white;\n"
"text-align:center;\n"
"background:none")
        self.perssure_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perssure_lbl.setObjectName("perssure_lbl")
        self.hiz = QtWidgets.QFrame(self.tab)
        self.hiz.setGeometry(QtCore.QRect(800, 110, 271, 241))
        self.hiz.setStyleSheet("QFrame{\n"
"    border-radius:100%;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 #fdc600);\n"
"}")
        self.hiz.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hiz.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hiz.setObjectName("hiz")
        self.container = QtWidgets.QFrame(self.hiz)
        self.container.setGeometry(QtCore.QRect(60, 10, 201, 201))
        self.container.setStyleSheet("QFrame{\n"
"    border-radius: 100px;\n"
"    background-color:white;\n"
"}")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.splitter = QtWidgets.QSplitter(self.container)
        self.splitter.setGeometry(QtCore.QRect(0, 10, 211, 181))
        self.splitter.setStyleSheet("background-color:none;\n"
"border:none")
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(0)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.labelTitle = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("background-color: none;\n"
"color: black;\n"
"text-align:center;")
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setWordWrap(False)
        self.labelTitle.setObjectName("labelTitle")
        self.labelPercentage = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(20)
        self.labelPercentage.setFont(font)
        self.labelPercentage.setStyleSheet("background-color: none;\n"
"color: black;")
        self.labelPercentage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentage.setObjectName("labelPercentage")
        self.labelLoadingInfo = QtWidgets.QLabel(self.splitter)
        self.labelLoadingInfo.setMinimumSize(QtCore.QSize(0, 24))
        self.labelLoadingInfo.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelLoadingInfo.setFont(font)
        self.labelLoadingInfo.setStyleSheet("QLabel{\n"
"    border-radius: 10px;    \n"
"    background-color:#fdc600;\n"
"    color: #FFFFFF;\n"
"    margin-left: 40px;\n"
"    margin-right: 40px;\n"
"}")
        self.labelLoadingInfo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelLoadingInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLoadingInfo.setObjectName("labelLoadingInfo")
        self.labelCredits = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.labelCredits.setFont(font)
        self.labelCredits.setStyleSheet("background-color: none;\n"
"color: black;")
        self.labelCredits.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits.setObjectName("labelCredits")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 160, 521, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.baslik_1 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.baslik_1.setContentsMargins(0, 0, 0, 0)
        self.baslik_1.setSpacing(100)
        self.baslik_1.setObjectName("baslik_1")
        self.orientation = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.orientation.setFont(font)
        self.orientation.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.orientation.setObjectName("orientation")
        self.baslik_1.addWidget(self.orientation)
        self.acceleration = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acceleration.setFont(font)
        self.acceleration.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00526316 rgba(16, 7, 13, 0), stop:0.7 rgba(0, 0, 0, 0), stop:0.926316 rgba(253, 208, 60, 0));\n"
"color: #fdc600;")
        self.acceleration.setObjectName("acceleration")
        self.baslik_1.addWidget(self.acceleration)
        self.logo_ct = QtWidgets.QPushButton(self.tab)
        self.logo_ct.setGeometry(QtCore.QRect(1720, 10, 130, 130))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_ct.sizePolicy().hasHeightForWidth())
        self.logo_ct.setSizePolicy(sizePolicy)
        self.logo_ct.setStyleSheet("")
        self.logo_ct.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo_ct.setIcon(icon1)
        self.logo_ct.setIconSize(QtCore.QSize(130, 130))
        self.logo_ct.setObjectName("logo_ct")
        self.sure = QtWidgets.QTimeEdit(self.tab)
        self.sure.setGeometry(QtCore.QRect(1520, 30, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.sure.setFont(font)
        self.sure.setStyleSheet("QDateTimeEdit {\n"
"  selection-background-color: #346792;\n"
"  border-style: solid;\n"
"  border:3px solid   #fdc600;\n"
"  border-radius:35px;\n"
"  padding-bottom: 2px;\n"
"  padding-left:10px;\n"
"  min-width: 10px;\n"
"color:white;\n"
"font-size:16px\n"
"}")
        self.sure.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sure.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.sure.setTime(QtCore.QTime(0, 0, 0))
        self.sure.setObjectName("sure")
        self.controlled_stop_bt = QtWidgets.QPushButton(self.tab)
        self.controlled_stop_bt.setGeometry(QtCore.QRect(1410, 20, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.controlled_stop_bt.setFont(font)
        self.controlled_stop_bt.setWhatsThis("")
        self.controlled_stop_bt.setStyleSheet("QPushButton{\n"
"border-radius:45%;\n"
"background-color:white;\n"
"border:6px solid gray;\n"
"padding-top:3px;\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border-radius:45%;\n"
"background-color:white;\n"
"border:6px solid red;\n"
"padding-top:3px;\n"
"color:black;\n"
"}")
        self.controlled_stop_bt.setAutoRepeat(False)
        self.controlled_stop_bt.setAutoExclusive(False)
        self.controlled_stop_bt.setAutoRepeatDelay(300)
        self.controlled_stop_bt.setObjectName("controlled_stop_bt")
        self.s_40 = QtWidgets.QLabel(self.tab)
        self.s_40.setGeometry(QtCore.QRect(1314, 30, 71, 41))
        self.s_40.setStyleSheet("background:none;")
        self.s_40.setText("")
        self.s_40.setObjectName("s_40")
        self.location_2 = QtWidgets.QLabel(self.tab)
        self.location_2.setGeometry(QtCore.QRect(520, 30, 871, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.location_2.setFont(font)
        self.location_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.location_2.setStyleSheet("                QLabel {\n"
"                    background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0,\n"
"                                                      stop: 0 rgba(200, 200, 200, 255), \n"
"                                                      stop: 0.5 rgb(253, 198, 0),  \n"
"                                                      stop: 0.2 rgba(200, 200, 200, 255),\n"
"                                                      stop: 0.5 rgb(253, 198, 0));\n"
"                    color: black;\n"
"                    padding: 5px;\n"
"                    transform: rotate(180deg);\n"
"                    border:1px solid rgba(200, 200, 200, 230) ;\n"
"                    border-radius:20%\n"
"                }")
        self.location_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.location_2.setObjectName("location_2")
        self.location_2.raise_()
        self.bt_start.raise_()
        self.bt_stop.raise_()
        self.baglan.raise_()
        self.hyperloop.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.orientation_2.raise_()
        self.vibration_widget.raise_()
        self.power_con_widget.raise_()
        self.layoutWidget_2.raise_()
        self.vibration_widget_2.raise_()
        self.orientation_3.raise_()
        self.orientation_4.raise_()
        self.vibration_widget_3.raise_()
        self.basinc2_label.raise_()
        self.arac_basinc.raise_()
        self.basnc1_label.raise_()
        self.motor_basinc.raise_()
        self.hiz.raise_()
        self.layoutWidget.raise_()
        self.logo_ct.raise_()
        self.sure.raise_()
        self.controlled_stop_bt.raise_()
        self.s_40.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(470, 20, 581, 71))
        self.groupBox_5.setStyleSheet("color:white;\n"
"")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.adres_3 = QtWidgets.QLabel(self.groupBox_5)
        self.adres_3.setObjectName("adres_3")
        self.horizontalLayout_13.addWidget(self.adres_3)
        self.ip_adress = QtWidgets.QLabel(self.groupBox_5)
        self.ip_adress.setMinimumSize(QtCore.QSize(71, 0))
        self.ip_adress.setFrameShape(QtWidgets.QFrame.Box)
        self.ip_adress.setLineWidth(2)
        self.ip_adress.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ip_adress.setObjectName("ip_adress")
        self.horizontalLayout_13.addWidget(self.ip_adress)
        self.line_8 = QtWidgets.QFrame(self.groupBox_5)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_13.addWidget(self.line_8)
        self.kullanici_3 = QtWidgets.QLabel(self.groupBox_5)
        self.kullanici_3.setObjectName("kullanici_3")
        self.horizontalLayout_13.addWidget(self.kullanici_3)
        self.user = QtWidgets.QLabel(self.groupBox_5)
        self.user.setMinimumSize(QtCore.QSize(71, 0))
        self.user.setFrameShape(QtWidgets.QFrame.Box)
        self.user.setLineWidth(2)
        self.user.setText("")
        self.user.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user.setObjectName("user")
        self.horizontalLayout_13.addWidget(self.user)
        self.line_9 = QtWidgets.QFrame(self.groupBox_5)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_13.addWidget(self.line_9)
        self.port_3 = QtWidgets.QLabel(self.groupBox_5)
        self.port_3.setObjectName("port_3")
        self.horizontalLayout_13.addWidget(self.port_3)
        self.port = QtWidgets.QLabel(self.groupBox_5)
        self.port.setMinimumSize(QtCore.QSize(71, 0))
        self.port.setFrameShape(QtWidgets.QFrame.Box)
        self.port.setLineWidth(2)
        self.port.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.port.setObjectName("port")
        self.horizontalLayout_13.addWidget(self.port)
        self.line_10 = QtWidgets.QFrame(self.groupBox_5)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_13.addWidget(self.line_10)
        self.connect = QtWidgets.QPushButton(self.tab_2)
        self.connect.setGeometry(QtCore.QRect(20, 20, 141, 51))
        self.connect.setStyleSheet(".QPushButton{\n"
"    font: 10pt \"Oblivious font\";\n"
"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background-color: rgb(0, 150, 0);\n"
"}")
        self.connect.setObjectName("connect")
        self.bt_disconnect = QtWidgets.QPushButton(self.tab_2)
        self.bt_disconnect.setGeometry(QtCore.QRect(170, 20, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Oblivious font")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bt_disconnect.setFont(font)
        self.bt_disconnect.setStyleSheet(".QPushButton{\n"
"    font: 10pt \"Oblivious font\";\n"
"background-color:red;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background-color:rgb(214, 0, 0);\n"
"}")
        self.bt_disconnect.setObjectName("bt_disconnect")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(1310, 120, 391, 241))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("color:white;\n"
"")
        self.groupBox_4.setObjectName("groupBox_4")
        self.line_2 = QtWidgets.QFrame(self.groupBox_4)
        self.line_2.setGeometry(QtCore.QRect(132, 23, 16, 17))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.groupBox_4)
        self.line_3.setGeometry(QtCore.QRect(263, 23, 16, 17))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.groupBox_4)
        self.line_4.setGeometry(QtCore.QRect(516, 23, 16, 17))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.layoutWidget_5 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 30, 371, 201))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.levit1_label = QtWidgets.QLabel(self.layoutWidget_5)
        self.levit1_label.setObjectName("levit1_label")
        self.verticalLayout_33.addWidget(self.levit1_label)
        self.levit1_veri = QtWidgets.QLabel(self.layoutWidget_5)
        self.levit1_veri.setMinimumSize(QtCore.QSize(71, 0))
        self.levit1_veri.setFrameShape(QtWidgets.QFrame.Box)
        self.levit1_veri.setLineWidth(2)
        self.levit1_veri.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.levit1_veri.setObjectName("levit1_veri")
        self.verticalLayout_33.addWidget(self.levit1_veri)
        self.levit2_label = QtWidgets.QLabel(self.layoutWidget_5)
        self.levit2_label.setObjectName("levit2_label")
        self.verticalLayout_33.addWidget(self.levit2_label)
        self.levit2_veri = QtWidgets.QLabel(self.layoutWidget_5)
        self.levit2_veri.setMinimumSize(QtCore.QSize(71, 0))
        self.levit2_veri.setFrameShape(QtWidgets.QFrame.Box)
        self.levit2_veri.setLineWidth(2)
        self.levit2_veri.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.levit2_veri.setObjectName("levit2_veri")
        self.verticalLayout_33.addWidget(self.levit2_veri)
        self.horizontalLayout_14.addLayout(self.verticalLayout_33)
        self.verticalLayout_34 = QtWidgets.QVBoxLayout()
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.levit3_label = QtWidgets.QLabel(self.layoutWidget_5)
        self.levit3_label.setObjectName("levit3_label")
        self.verticalLayout_34.addWidget(self.levit3_label)
        self.levit3_veri = QtWidgets.QLabel(self.layoutWidget_5)
        self.levit3_veri.setMinimumSize(QtCore.QSize(71, 0))
        self.levit3_veri.setFrameShape(QtWidgets.QFrame.Box)
        self.levit3_veri.setLineWidth(2)
        self.levit3_veri.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.levit3_veri.setObjectName("levit3_veri")
        self.verticalLayout_34.addWidget(self.levit3_veri)
        self.levit4_label = QtWidgets.QLabel(self.layoutWidget_5)
        self.levit4_label.setObjectName("levit4_label")
        self.verticalLayout_34.addWidget(self.levit4_label)
        self.levit4_veri = QtWidgets.QLabel(self.layoutWidget_5)
        self.levit4_veri.setMinimumSize(QtCore.QSize(71, 0))
        self.levit4_veri.setFrameShape(QtWidgets.QFrame.Box)
        self.levit4_veri.setLineWidth(2)
        self.levit4_veri.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.levit4_veri.setObjectName("levit4_veri")
        self.verticalLayout_34.addWidget(self.levit4_veri)
        self.horizontalLayout_14.addLayout(self.verticalLayout_34)
        self.levite = QtWidgets.QPushButton(self.tab_2)
        self.levite.setGeometry(QtCore.QRect(1070, 30, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Oblivious font")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.levite.setFont(font)
        self.levite.setStyleSheet(".QPushButton{\n"
"    font: 10pt \"Oblivious font\";\n"
"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background-color: rgb(0, 150, 0);\n"
"}")
        self.levite.setObjectName("levite")
        self.bilgimesaj_label = QtWidgets.QLabel(self.tab_2)
        self.bilgimesaj_label.setGeometry(QtCore.QRect(30, 110, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bilgimesaj_label.setFont(font)
        self.bilgimesaj_label.setStyleSheet("color:white;")
        self.bilgimesaj_label.setObjectName("bilgimesaj_label")
        self.bilgimesaj_label_2 = QtWidgets.QLabel(self.tab_2)
        self.bilgimesaj_label_2.setGeometry(QtCore.QRect(30, 520, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bilgimesaj_label_2.setFont(font)
        self.bilgimesaj_label_2.setStyleSheet("color:white;")
        self.bilgimesaj_label_2.setObjectName("bilgimesaj_label_2")
        self.hata_message = QtWidgets.QLabel(self.tab_2)
        self.hata_message.setGeometry(QtCore.QRect(32, 570, 481, 271))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.hata_message.setFont(font)
        self.hata_message.setStyleSheet("border: 1px solid rgb(255, 255, 255);\n"
"color:white;")
        self.hata_message.setText("")
        self.hata_message.setObjectName("hata_message")
        self.bilgi_message = QtWidgets.QLabel(self.tab_2)
        self.bilgi_message.setGeometry(QtCore.QRect(30, 150, 481, 271))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bilgi_message.setFont(font)
        self.bilgi_message.setStyleSheet("border: 1px solid rgb(255, 255, 255);\n"
"color:white;\n"
"")
        self.bilgi_message.setText("")
        self.bilgi_message.setObjectName("bilgi_message")
        self.pbClearinfo = QtWidgets.QPushButton(self.tab_2)
        self.pbClearinfo.setGeometry(QtCore.QRect(30, 430, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pbClearinfo.setFont(font)
        self.pbClearinfo.setStyleSheet("color:#437099;\n"
"border:1px solid #437099;\n"
"background-color:white;")
        self.pbClearinfo.setObjectName("pbClearinfo")
        self.bilgimesaj_label_3 = QtWidgets.QLabel(self.tab_2)
        self.bilgimesaj_label_3.setGeometry(QtCore.QRect(1310, 410, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bilgimesaj_label_3.setFont(font)
        self.bilgimesaj_label_3.setStyleSheet("color:white;")
        self.bilgimesaj_label_3.setObjectName("bilgimesaj_label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(1310, 470, 441, 421))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setStyleSheet("border:none;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:0.00568182, x2:1, y2:1, stop:0 #fdc600, stop:1 rgba(90, 90, 90, 255));\n"
"color:black !important;")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(7, 0, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.logo_c = QtWidgets.QPushButton(self.tab_2)
        self.logo_c.setGeometry(QtCore.QRect(1730, 10, 130, 130))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_c.sizePolicy().hasHeightForWidth())
        self.logo_c.setSizePolicy(sizePolicy)
        self.logo_c.setText("")
        self.logo_c.setIcon(icon1)
        self.logo_c.setIconSize(QtCore.QSize(130, 130))
        self.logo_c.setObjectName("logo_c")
        self.levite_stop = QtWidgets.QPushButton(self.tab_2)
        self.levite_stop.setGeometry(QtCore.QRect(1220, 30, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Oblivious font")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.levite_stop.setFont(font)
        self.levite_stop.setStyleSheet(".QPushButton{\n"
"    font: 10pt \"Oblivious font\";\n"
"background-color:red;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background-color:rgb(214, 0, 0);\n"
"}")
        self.levite_stop.setObjectName("levite_stop")
        self.aracimg = QtWidgets.QPushButton(self.tab_2)
        self.aracimg.setGeometry(QtCore.QRect(690, 190, 527, 308))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/arac_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aracimg.setIcon(icon2)
        self.aracimg.setIconSize(QtCore.QSize(527, 308))
        self.aracimg.setObjectName("aracimg")
        self.pbClearErr = QtWidgets.QPushButton(self.tab_2)
        self.pbClearErr.setGeometry(QtCore.QRect(30, 850, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbClearErr.setFont(font)
        self.pbClearErr.setStyleSheet("color:#f27a7a;;\n"
"border:1px solid #f27a7a;\n"
"background-color:white;")
        self.pbClearErr.setObjectName("pbClearErr")
        self.motor_set = QtWidgets.QTabWidget(self.tab_2)
        self.motor_set.setGeometry(QtCore.QRect(685, 670, 461, 121))
        self.motor_set.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(90, 90, 90, 255));\n"
"color:black;")
        self.motor_set.setTabPosition(QtWidgets.QTabWidget.North)
        self.motor_set.setObjectName("motor_set")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.motor = QtWidgets.QPushButton(self.tab_1)
        self.motor.setGeometry(QtCore.QRect(120, 30, 41, 41))
        self.motor.setStyleSheet("background:red;\n"
"border-radius:20%;\n"
"border:1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.motor.setObjectName("motor")
        self.motor_2 = QtWidgets.QPushButton(self.tab_1)
        self.motor_2.setGeometry(QtCore.QRect(180, 30, 41, 41))
        self.motor_2.setStyleSheet("background:red;\n"
"border-radius:20;\n"
"border:1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.motor_2.setObjectName("motor_2")
        self.motor_3 = QtWidgets.QPushButton(self.tab_1)
        self.motor_3.setGeometry(QtCore.QRect(241, 30, 41, 41))
        self.motor_3.setStyleSheet("background:red;\n"
"border-radius:20;\n"
"border:1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.motor_3.setObjectName("motor_3")
        self.motor_4 = QtWidgets.QPushButton(self.tab_1)
        self.motor_4.setGeometry(QtCore.QRect(300, 30, 41, 41))
        self.motor_4.setStyleSheet("background:red;\n"
"border-radius:20;\n"
"border:1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.motor_4.setObjectName("motor_4")
        self.motor_set.addTab(self.tab_1, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.motor_5 = QtWidgets.QPushButton(self.tab_21)
        self.motor_5.setGeometry(QtCore.QRect(120, 30, 41, 41))
        self.motor_5.setStyleSheet("background:red;\n"
"border-radius:20%;\n"
"border:1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.motor_5.setObjectName("motor_5")
        self.motor_7 = QtWidgets.QPushButton(self.tab_21)
        self.motor_7.setGeometry(QtCore.QRect(241, 30, 41, 41))
        self.motor_7.setStyleSheet("background:red;\n"
"border-radius:20;\n"
"border:1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.motor_7.setObjectName("motor_7")
        self.motor_8 = QtWidgets.QPushButton(self.tab_21)
        self.motor_8.setGeometry(QtCore.QRect(300, 30, 41, 41))
        self.motor_8.setStyleSheet("background:red;\n"
"border-radius:20;\n"
"border:1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.motor_8.setObjectName("motor_8")
        self.motor_6 = QtWidgets.QPushButton(self.tab_21)
        self.motor_6.setGeometry(QtCore.QRect(180, 30, 41, 41))
        self.motor_6.setStyleSheet("background:red;\n"
"border-radius:20;\n"
"border:1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.motor_6.setObjectName("motor_6")
        self.motor_set.addTab(self.tab_21, "")
        self.turnback_bt = QtWidgets.QPushButton(self.tab_2)
        self.turnback_bt.setGeometry(QtCore.QRect(1560, 30, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Oblivious font")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.turnback_bt.setFont(font)
        self.turnback_bt.setStyleSheet(".QPushButton{\n"
"    font: 10pt \"Oblivious font\";\n"
"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background-color: rgb(0, 150, 0);\n"
"}")
        self.turnback_bt.setObjectName("turnback_bt")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(ThunderloopTeam)
        self.tabWidget.setCurrentIndex(0)
        self.motor_set.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ThunderloopTeam)

    def retranslateUi(self, ThunderloopTeam):
        _translate = QtCore.QCoreApplication.translate
        ThunderloopTeam.setWindowTitle(_translate("ThunderloopTeam", "Form"))
        self.bt_start.setText(_translate("ThunderloopTeam", "START"))
        self.bt_stop.setText(_translate("ThunderloopTeam", "STOP"))
        self.ROLL.setText(_translate("ThunderloopTeam", "ROLL : "))
        self.PITCH.setText(_translate("ThunderloopTeam", "PITCH:"))
        self.YAW.setText(_translate("ThunderloopTeam", "YAW :"))
        self.roll_veri.setText(_translate("ThunderloopTeam", "0"))
        self.pitch_veri.setText(_translate("ThunderloopTeam", "0"))
        self.yaw_veri.setText(_translate("ThunderloopTeam", "0"))
        self.ACCELERATION_x.setText(_translate("ThunderloopTeam", "X :"))
        self.ACCELERATION_y.setText(_translate("ThunderloopTeam", "Y :"))
        self.ACCELERATION_z.setText(_translate("ThunderloopTeam", "Z :"))
        self.acceleration_x.setText(_translate("ThunderloopTeam", "0"))
        self.acceleration_y.setText(_translate("ThunderloopTeam", "0"))
        self.acceleration_z.setText(_translate("ThunderloopTeam", "0"))
        self.orientation_2.setText(_translate("ThunderloopTeam", "VIBRATION"))
        self.ACCELERATION_x_4.setText(_translate("ThunderloopTeam", "X :"))
        self.ACCELERATION_y_4.setText(_translate("ThunderloopTeam", "Y :"))
        self.ACCELERATION_z_4.setText(_translate("ThunderloopTeam", "Z :"))
        self.x_on_veri_2.setText(_translate("ThunderloopTeam", "0"))
        self.y_on_veri_2.setText(_translate("ThunderloopTeam", "0"))
        self.z_on_veri_2.setText(_translate("ThunderloopTeam", "0"))
        self.ACCELERATION_x_5.setText(_translate("ThunderloopTeam", "X :"))
        self.ACCELERATION_y_5.setText(_translate("ThunderloopTeam", "Y :"))
        self.ACCELERATION_z_5.setText(_translate("ThunderloopTeam", "Z :"))
        self.x_arka_veri_2.setText(_translate("ThunderloopTeam", "0"))
        self.y_arka_veri_2.setText(_translate("ThunderloopTeam", "0"))
        self.z_arka_veri_2.setText(_translate("ThunderloopTeam", "0"))
        self.front.setText(_translate("ThunderloopTeam", "FRONT"))
        self.back.setText(_translate("ThunderloopTeam", "BACK"))
        self.guctuketimi_label.setText(_translate("ThunderloopTeam", "POWER CONSUMPTION"))
        self.batarya_1_label.setText(_translate("ThunderloopTeam", "BATTERY_1"))
        self.batarya_2_label.setText(_translate("ThunderloopTeam", "BATTERY_2"))
        self.batarya1.setText(_translate("ThunderloopTeam", "%0"))
        self.batarya2.setText(_translate("ThunderloopTeam", "%0"))
        self.sw_1.setText(_translate("ThunderloopTeam", "sw_1"))
        self.sw_2.setText(_translate("ThunderloopTeam", "sw_2"))
        self.sw_3.setText(_translate("ThunderloopTeam", "sw_3"))
        self.sw_4.setText(_translate("ThunderloopTeam", "sw_4"))
        self.ACCELERATION_x_6.setText(_translate("ThunderloopTeam", "R :"))
        self.ACCELERATION_y_6.setText(_translate("ThunderloopTeam", "L :"))
        self.x_on_veri_3.setText(_translate("ThunderloopTeam", "0"))
        self.y_on_veri_3.setText(_translate("ThunderloopTeam", "0"))
        self.ACCELERATION_x_7.setText(_translate("ThunderloopTeam", "R :"))
        self.ACCELERATION_y_7.setText(_translate("ThunderloopTeam", "L :"))
        self.x_arka_veri_3.setText(_translate("ThunderloopTeam", "0"))
        self.y_arka_veri_3.setText(_translate("ThunderloopTeam", "0"))
        self.front_2.setText(_translate("ThunderloopTeam", "FRONT"))
        self.back_2.setText(_translate("ThunderloopTeam", "BACK"))
        self.orientation_3.setText(_translate("ThunderloopTeam", "LEVITATION MOTOR CURRENT"))
        self.orientation_4.setText(_translate("ThunderloopTeam", "PROPULSION  MOTOR CURRENT"))
        self.ACCELERATION_x_8.setText(_translate("ThunderloopTeam", "R :"))
        self.ACCELERATION_y_8.setText(_translate("ThunderloopTeam", "L :"))
        self.x_on_veri_4.setText(_translate("ThunderloopTeam", "0"))
        self.y_on_veri_4.setText(_translate("ThunderloopTeam", "0"))
        self.ACCELERATION_x_9.setText(_translate("ThunderloopTeam", "R :"))
        self.ACCELERATION_y_9.setText(_translate("ThunderloopTeam", "L :"))
        self.x_arka_veri_4.setText(_translate("ThunderloopTeam", "0"))
        self.y_arka_veri_4.setText(_translate("ThunderloopTeam", "0"))
        self.front_3.setText(_translate("ThunderloopTeam", "FRONT"))
        self.back_3.setText(_translate("ThunderloopTeam", "BACK"))
        self.basinc2_label.setText(_translate("ThunderloopTeam", "LOCATION"))
        self.loc_lbl.setText(_translate("ThunderloopTeam", "0"))
        self.basnc1_label.setText(_translate("ThunderloopTeam", "PRESSURE"))
        self.perssure_lbl.setText(_translate("ThunderloopTeam", "0"))
        self.labelTitle.setText(_translate("ThunderloopTeam", "<html><head/><body><p>SPEED</p></body></html>"))
        self.labelPercentage.setText(_translate("ThunderloopTeam", "<html><head/><body><p><span>0</span></p></body></html>"))
        self.labelLoadingInfo.setText(_translate("ThunderloopTeam", "loading.."))
        self.labelCredits.setText(_translate("ThunderloopTeam", "Thunderloop"))
        self.orientation.setText(_translate("ThunderloopTeam", "ORIENTATION"))
        self.acceleration.setText(_translate("ThunderloopTeam", "ACCELERATION"))
        self.sure.setDisplayFormat(_translate("ThunderloopTeam", "mm:ss"))
        self.controlled_stop_bt.setText(_translate("ThunderloopTeam", "CONTROLLED\n"
"STOP"))
        self.location_2.setText(_translate("ThunderloopTeam", "0m"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ThunderloopTeam", "Control Panel"))
        self.groupBox_5.setTitle(_translate("ThunderloopTeam", "INFORMATION"))
        self.adres_3.setText(_translate("ThunderloopTeam", "Adress :"))
        self.ip_adress.setText(_translate("ThunderloopTeam", "0"))
        self.kullanici_3.setText(_translate("ThunderloopTeam", "User :"))
        self.port_3.setText(_translate("ThunderloopTeam", "Port :"))
        self.port.setText(_translate("ThunderloopTeam", "0"))
        self.connect.setText(_translate("ThunderloopTeam", "CONNECT"))
        self.bt_disconnect.setText(_translate("ThunderloopTeam", "DISCONNECT"))
        self.groupBox_4.setTitle(_translate("ThunderloopTeam", "LEVITATION"))
        self.levit1_label.setText(_translate("ThunderloopTeam", "LEVIT_1"))
        self.levit1_veri.setText(_translate("ThunderloopTeam", "0"))
        self.levit2_label.setText(_translate("ThunderloopTeam", "LEVIT_2"))
        self.levit2_veri.setText(_translate("ThunderloopTeam", "0"))
        self.levit3_label.setText(_translate("ThunderloopTeam", "LEVIT_3"))
        self.levit3_veri.setText(_translate("ThunderloopTeam", "0"))
        self.levit4_label.setText(_translate("ThunderloopTeam", "LEVIT_4"))
        self.levit4_veri.setText(_translate("ThunderloopTeam", "0"))
        self.levite.setText(_translate("ThunderloopTeam", "LEVITATION"))
        self.bilgimesaj_label.setText(_translate("ThunderloopTeam", "INFORMATION MSG"))
        self.bilgimesaj_label_2.setText(_translate("ThunderloopTeam", "ERROR MSG"))
        self.pbClearinfo.setText(_translate("ThunderloopTeam", "CLEAR"))
        self.bilgimesaj_label_3.setText(_translate("ThunderloopTeam", "TEMPERATURE"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ThunderloopTeam", "Le_FR"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ThunderloopTeam", "Le_FL"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("ThunderloopTeam", "Le_BR"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("ThunderloopTeam", "Le_BL"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("ThunderloopTeam", "Pr_FR"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("ThunderloopTeam", "Pr_FL"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("ThunderloopTeam", "Pr_BL"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("ThunderloopTeam", "Pr_BL"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ThunderloopTeam", "MOTOR"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ThunderloopTeam", "BATTERY"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("ThunderloopTeam", "0"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("ThunderloopTeam", "0"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("ThunderloopTeam", "0"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("ThunderloopTeam", "0"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("ThunderloopTeam", "0"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("ThunderloopTeam", "0"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("ThunderloopTeam", "0"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("ThunderloopTeam", "0"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("ThunderloopTeam", "0"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("ThunderloopTeam", "0"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.levite_stop.setText(_translate("ThunderloopTeam", "STOP LEVITATION"))
        self.aracimg.setText(_translate("ThunderloopTeam", "PushButton"))
        self.pbClearErr.setText(_translate("ThunderloopTeam", "CLEAR"))
        self.motor.setText(_translate("ThunderloopTeam", "1"))
        self.motor_2.setText(_translate("ThunderloopTeam", "2"))
        self.motor_3.setText(_translate("ThunderloopTeam", "3"))
        self.motor_4.setText(_translate("ThunderloopTeam", "4"))
        self.motor_set.setTabText(self.motor_set.indexOf(self.tab_1), _translate("ThunderloopTeam", "LEVITATION"))
        self.motor_5.setText(_translate("ThunderloopTeam", "5"))
        self.motor_7.setText(_translate("ThunderloopTeam", "7"))
        self.motor_8.setText(_translate("ThunderloopTeam", "8"))
        self.motor_6.setText(_translate("ThunderloopTeam", "6"))
        self.motor_set.setTabText(self.motor_set.indexOf(self.tab_21), _translate("ThunderloopTeam", "PROPULSION"))
        self.turnback_bt.setText(_translate("ThunderloopTeam", "TURN BACK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ThunderloopTeam", "Connection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThunderloopTeam = QtWidgets.QWidget()
    ui = Ui_ThunderloopTeam()
    ui.setupUi(ThunderloopTeam)
    ThunderloopTeam.show()
    sys.exit(app.exec_())
