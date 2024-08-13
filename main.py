from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QTableWidgetItem,QTableWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QMetaObject, pyqtSignal, pyqtSlot
from server import ServerSide
from PyQt5 import QtCore
from PyQt5.uic import loadUi

import sys
import socket
import threading
import json
import msgpack
import time
import datetime
import sqlite3
import os
import csv

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.sure_artis=0
        loadUi("mainwindow.ui", self)
        self.connect.clicked.connect(self.baglan_func_th)
        self.bt_disconnect.clicked.connect(self.disconnect_func)
        self.bt_start.clicked.connect(self.start_function)
        self.bt_stop.clicked.connect(self.stop_function)
        self.pbClearinfo.clicked.connect(self.clearbtn_info)
        self.pbClearErr.clicked.connect(self.clearbtn_err)
        self.levite.clicked.connect(lambda: self.mesth("A"))
        self.levite_stop.clicked.connect(lambda: self.mesth("B"))
        self.controlled_stop_bt.clicked.connect(lambda: self.mesth("C"))
        self.motor.clicked.connect(lambda: self.mesth("D"))

        self.turnback_bt.clicked.connect(lambda: self.mesth("T"))        
        self.baglan.setText("Connection Failed")
        self.info_mes=""
        self.info_mes+="Connection Failed\n"
        self.bilgi_message.setText(self.info_mes)
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.veritabani)
        self.timer4 = QTimer()
        self.timer4.timeout.connect(self.deneme)
        self.timer4.start(1000)

    def deneme(self):
        message="H"
        thread_baslat = threading.Thread(target=server.send_message,args=(message,))
        thread_baslat.start()

#THREAD KISMI
    @pyqtSlot()
    def baglan_func_th(self): 
        thread = threading.Thread(target=self.baglan_function)
        thread.start()
        
        self.timer2.start(700)
 
    def baslat_thread(self):
        message="K"
        thread_baslat = threading.Thread(target=server.send_message,args=(message,))
        thread_baslat.start()
        
       
    def durdur_thread(self):
        message="Z"
        thread_durdur = threading.Thread(target=server.send_message,args=(message,))
        thread_durdur.start()

    def mesth(self,message):
        print(message)
        thread = threading.Thread(target=server.send_message, args=(message,))
        thread.start()
        thread.join()
                
    def sure_a(self):
        self.timer3 = QTimer()
        self.timer3.timeout.connect(self.sure_art)
        self.timer3.start(1000)

    def sure_art(self):
        self.sure_artis += 1
        self.repaint()
        self.sure.setTime(QtCore.QTime(0, 0, self.sure_artis))        

    def clearbtn_info(self):
        self.bilgi_message.setText("")

    def clearbtn_err(self):
        self.hata_message.setText("")

    def start_function(self):
        self.sure_a()
        self.baslat_thread()

    def stop_function(self):
        self.durdur_thread()
        self.timer2.stop()

    def decode_tele(self, liste):
        #ax,ay,az,gx,gy,gz
        self.roll_veri.setText(str(liste[1]))
        self.pitch_veri.setText(str(liste[2]))
        self.yaw_veri.setText(str(liste[3]))

        self.acceleration_x.setText(str(liste[4]))
        self.acceleration_y.setText(str(liste[5]))
        self.acceleration_z.setText(str(liste[6]))
                

        self.tableWidget.setItem(0, 0, QTableWidgetItem(str(liste[7])))
        self.tableWidget.setItem(0, 2, QTableWidgetItem(str(liste[9])))
        self.tableWidget.setItem(0, 4, QTableWidgetItem(str(liste[10])))
        self.tableWidget.setItem(0, 6, QTableWidgetItem(str(liste[8])))
        self.tableWidget.setItem(0, 8, QTableWidgetItem(str(liste[16])))
        self.tableWidget.setItem(0, 10, QTableWidgetItem(str(liste[12])))
        self.tableWidget.setItem(0, 12, QTableWidgetItem(str(liste[13])))
        self.tableWidget.setItem(0, 14, QTableWidgetItem(str(liste[14])))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(str(liste[15])))
        self.tableWidget.setItem(0, 3, QTableWidgetItem(str(liste[11])))

        #mesafe
        self.location_2.setText(str(liste[17]))

        self.dist=str(liste[17])
        self.s_40.setText("")
                
        #basınc
        self.perssure_lbl.setText(str(liste[18]))

        #akım
        self.x_on_veri_3.setText(str(liste[19]))
        self.y_on_veri_3.setText(str(liste[20]))
        self.x_arka_veri_3.setText(str(liste[21]))
        self.y_arka_veri_3.setText(str(liste[22]))
                
        self.x_on_veri_4.setText(str(liste[23]))
        self.y_arka_veri_4.setText(str(liste[24]))
        self.x_on_veri_4.setText(str(liste[25]))
        self.y_arka_veri_4.setText(str(liste[26]))
                
        #batarya
        self.batarya1.setText("%" +str(liste[27]))
        self.batarya2.setText("%" +str(liste[28]))

        #4 tof var
        self.levit1_veri.setText(str(liste[29]))
        self.levit2_veri.setText(str(liste[30]))
        self.levit3_veri.setText(str(liste[31]))
        self.levit4_veri.setText(str(liste[32]))
                
        #titresim
        self.x_on_veri_2.setText(str(liste[33][0:6]))
        self.y_on_veri_2.setText(str(liste[34][0:6]))
        self.z_on_veri_2.setText(str(liste[35][0:6]))
        self.x_arka_veri_2.setText(str(liste[36][0:6]))
        self.y_arka_veri_2.setText(str(liste[37][0:6]))
        self.z_arka_veri_2.setText(str(liste[38][0:6]))
    
                
        #ls
        self.lsdeger=str(liste[39])
        if self.lsdeger=="1":
            self.sw_1.setStyleSheet("QCheckBox {\n""color:white;\n""}\n""\n"
                    "QCheckBox::indicator {\n""width:20px;\n""height:20px;\n""border-radius:11px;\n""}\n""\n"
                    "QCheckBox::indicator:checked {\n""background-color:green;\n""border:1px solid green;\n""}\n""\n"
                    "QCheckBox::indicator:unchecked {\n""background-color:green;\n""border:1px solid green;\n""}")

        self.lsdeger2=str(liste[40])
        if self.lsdeger2=="1":
            self.sw_2.setStyleSheet("QCheckBox {\n""color:white;\n""}\n""\n"
                    "QCheckBox::indicator {\n""width:20px;\n""height:20px;\n""border-radius:11px;\n""}\n""\n"
                    "QCheckBox::indicator:checked {\n""background-color:green;\n""border:1px solid green;\n""}\n""\n"
                    "QCheckBox::indicator:unchecked {\n""background-color:green;\n""border:1px solid green;\n""}")

        self.lsdeger3=str(liste[41])
        if self.lsdeger3=="1":
            self.sw_3.setStyleSheet("QCheckBox {\n""color:white;\n""}\n""\n"
                    "QCheckBox::indicator {\n""width:20px;\n""height:20px;\n""border-radius:11px;\n""}\n""\n"
                    "QCheckBox::indicator:checked {\n""background-color:green;\n""border:1px solid green;\n""}\n""\n"
                    "QCheckBox::indicator:unchecked {\n""background-color:green;\n""border:1px solid green;\n""}")

        self.lsdeger4=str(liste[42])
        if self.lsdeger4=="1":
            self.sw_4.setStyleSheet("QCheckBox {\n""color:white;\n""}\n""\n"
                    "QCheckBox::indicator {\n""width:20px;\n""height:20px;\n""border-radius:11px;\n""}\n""\n"
                    "QCheckBox::indicator:checked {\n""background-color:green;\n""border:1px solid green;\n""}\n""\n"
                    "QCheckBox::indicator:unchecked {\n""background-color:green;\n""border:1px solid green;\n""}")
                

        #konum
        self.loc_lbl.setText(str(liste[43]))
                
        #hız
        self.labelPercentage.setText(str(liste[44]))    
                
        #warning
        self.hata_message.setText(liste[45])
                
        #self.info_mes+=str(liste[46])+"\n"
        #info
        #self.bilgi_message.setText(str(self.info_mes)) 
               
        #time.sleep(1)
        

# ERROR paket decoder
    def decode_err(self, son_satir):
        self.hata_message.setText(str(son_satir))

# INFO paket decoder
    def decode_info(self, son_satir):
        self.bilgi_message.setText(str(son_satir))

#bağlantı kısmı  --baslangıç
    def veritabani(self):
            #self.mesth("H") 
            dosya_adı="verii.csv"
            with open(dosya_adı, 'r', newline='') as dosya:
                okuyucu = csv.reader(dosya, delimiter=';')
                    # Satırları okuyarak son satıra ulaşın
                for satir in okuyucu:
                    son_satir = satir

                # Son satırdaki verileri noktalı virgülle ayırarak bir liste elde edin
                #print("son_satir", son_satir)
                if len(son_satir)== 0:
                    return
                
                liste = son_satir[0].split(';')
                key=str(liste[0])
                if key == "TELE":
                    self.decode_tele(liste)
                elif key == "INFO":
                    self.decode_info(son_satir)
                elif key == "ERROR":
                    self.decode_err(son_satir)
                else:
                    print("Hatalı gönderi: ", son_satir)
                    #UNEXPECTED MESSAGE

                
                
                #ax,ay,az,gx,gy,gz
                """
                self.roll_veri.setText(str(liste[0]))
                
                self.pitch_veri.setText(str(liste[1]))
                
                self.yaw_veri.setText(str(liste[3]))
                
                self.acceleration_x.setText(str(liste[4]))
                self.acceleration_y.setText(str(liste[5]))
                self.acceleration_z.setText(str(liste[6]))
                

                #sıcaklık
                self.tableWidget.setItem(0, 0, QTableWidgetItem(str(liste[7])))
                self.tableWidget.setItem(0, 2, QTableWidgetItem(str(liste[8])))
                self.tableWidget.setItem(0, 4, QTableWidgetItem(str(liste[9])))
                self.tableWidget.setItem(0, 6, QTableWidgetItem(str(liste[10])))
                self.tableWidget.setItem(0, 8, QTableWidgetItem(str(liste[11])))
                self.tableWidget.setItem(0, 10, QTableWidgetItem(str(liste[12])))
                self.tableWidget.setItem(0, 12, QTableWidgetItem(str(liste[13])))
                self.tableWidget.setItem(0, 14, QTableWidgetItem(str(liste[14])))
                self.tableWidget.setItem(0, 1, QTableWidgetItem(str(liste[15])))
                self.tableWidget.setItem(0, 3, QTableWidgetItem(str(liste[16])))


                 #mesafe
                self.location_2.setText(str(liste[17]))

                self.dist=str(liste[17])
                self.s_40.setText("")
                
                #basınc
                self.perssure_lbl.setText(str(liste[18]))

                #akım
                self.x_on_veri_3.setText(str(liste[19]))
                self.y_on_veri_3.setText(str(liste[20]))
                self.x_arka_veri_3.setText(str(liste[21]))
                self.y_arka_veri_3.setText(str(liste[22]))
                
                self.x_on_veri_4.setText(str(liste[23]))
                self.y_arka_veri_4.setText(str(liste[24]))
                self.x_on_veri_4.setText(str(liste[25]))
                self.y_arka_veri_4.setText(str(liste[26]))
                
                #batarya
                self.batarya1.setText("%" +str(liste[27]))
                self.batarya2.setText("%" +str(liste[28]))

                #4 tof var
                self.levit1_veri.setText(str(liste[29]))
                self.levit2_veri.setText(str(liste[30]))
                self.levit3_veri.setText(str(liste[31]))
                self.levit4_veri.setText(str(liste[32]))
                
                #titresim
                self.x_on_veri_2.setText(str(liste[33][0:6]))
                self.y_on_veri_2.setText(str(liste[34][0:6]))
                self.z_on_veri_2.setText(str(liste[35][0:6]))
                self.x_arka_veri_2.setText(str(liste[36][0:6]))
                self.y_arka_veri_2.setText(str(liste[37][0:6]))
                self.z_arka_veri_2.setText(str(liste[38][0:6]))
    
                
                #ls
                self.lsdeger=str(liste[39])
                if self.lsdeger=="1":
                    self.sw_1.setStyleSheet("QCheckBox {\n""color:white;\n""}\n""\n"
                    "QCheckBox::indicator {\n""width:20px;\n""height:20px;\n""border-radius:11px;\n""}\n""\n"
                    "QCheckBox::indicator:checked {\n""background-color:green;\n""border:1px solid green;\n""}\n""\n"
                    "QCheckBox::indicator:unchecked {\n""background-color:green;\n""border:1px solid green;\n""}")

                self.lsdeger2=str(liste[40])
                if self.lsdeger2=="1":
                    self.sw_2.setStyleSheet("QCheckBox {\n""color:white;\n""}\n""\n"
                    "QCheckBox::indicator {\n""width:20px;\n""height:20px;\n""border-radius:11px;\n""}\n""\n"
                    "QCheckBox::indicator:checked {\n""background-color:green;\n""border:1px solid green;\n""}\n""\n"
                    "QCheckBox::indicator:unchecked {\n""background-color:green;\n""border:1px solid green;\n""}")

                self.lsdeger3=str(liste[41])
                if self.lsdeger3=="1":
                    self.sw_3.setStyleSheet("QCheckBox {\n""color:white;\n""}\n""\n"
                    "QCheckBox::indicator {\n""width:20px;\n""height:20px;\n""border-radius:11px;\n""}\n""\n"
                    "QCheckBox::indicator:checked {\n""background-color:green;\n""border:1px solid green;\n""}\n""\n"
                    "QCheckBox::indicator:unchecked {\n""background-color:green;\n""border:1px solid green;\n""}")

                self.lsdeger4=str(liste[42])
                if self.lsdeger4=="1":
                    self.sw_4.setStyleSheet("QCheckBox {\n""color:white;\n""}\n""\n"
                    "QCheckBox::indicator {\n""width:20px;\n""height:20px;\n""border-radius:11px;\n""}\n""\n"
                    "QCheckBox::indicator:checked {\n""background-color:green;\n""border:1px solid green;\n""}\n""\n"
                    "QCheckBox::indicator:unchecked {\n""background-color:green;\n""border:1px solid green;\n""}")
                

                #konum
                self.loc_lbl.setText(str(liste[43]))
                
                #hız
                self.labelPercentage.setText(str(liste[44]))
                
                
                #warning
                self.hata_message.setText(liste[45])
                
                self.info_mes+=str(liste[46])+"\n"
                #info
                self.bilgi_message.setText(str(self.info_mes)) 
                """
            


            
    def baglan_function(self):
        self.ip_adress.setText("192.168.77.218")
        self.user.setText("Thunderloop")
        self.port.setText("37256")
        thread = threading.Thread(target=server.connect)
        thread.start()
        while not server.is_connected():
            time.sleep(1)
        self.info_mes += "Connected\n"
        self.baglan.setText("Connected\n")
        self.bilgi_message.setText(self.info_mes)
        self.veritabani()

        

        
#bağlantı kısmı  --son
    
    def disconnect_func(self):
        server.disconnect
        self.baglan.setText("Disconnected")
        self.info_mes=""
        self.info_mes+="Disconnected\n"
        self.hata_message.setText(self.info_mes)        
        self.timerHeartBeat.stop()


server=ServerSide()
app = QApplication([])
window = MyForm()
window.show()
app.exec_()

