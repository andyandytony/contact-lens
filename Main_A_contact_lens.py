import sys
import numpy as np
import time
import cv2
from PyQt5 import QtCore
from PyQt5.QtCore  import pyqtSlot, QTimer
from PyQt5.QtGui import QImage , QPixmap ,QPalette
from PyQt5.QtWidgets import  (QApplication, QDialog,QFileDialog,
                        QColorDialog,QFontDialog,QProgressDialog,
                        QLineEdit,QInputDialog,QMessageBox)

from ui_paw_lens import Ui_Dialog
from ui_setting_B import Ui_Setting
import json
from detect_contact_json import DetectYolo
# from detect_contact import detect
class Main_Contact_Ui(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.setting = Main_setting_Ui()
        # read level.json
        # self.Yolo = DetectYolo()
        # self.DetectYolo = DetectYolo()

    def displayImage_Burr(self, img2, window=1):
        qformat = QImage.Format_Indexed8
        if len(img2.shape) == 3:
            if (img2.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img2 = QImage(img2, img2.shape[1], img2.shape[0], qformat)
        img2 = img2.rgbSwapped()
        self.ui.label_Burr.setPixmap(QPixmap.fromImage(img2))
        self.ui.label_Burr.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        QApplication.processEvents()

    def displayImage_Scratch(self, img2, window=1):
        qformat = QImage.Format_Indexed8
        if len(img2.shape) == 3:
            if (img2.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img2 = QImage(img2, img2.shape[1], img2.shape[0], qformat)
        img2 = img2.rgbSwapped()
        self.ui.label_Yolo.setPixmap(QPixmap.fromImage(img2))
        self.ui.label_Yolo.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        QApplication.processEvents()

    def on_pushButton_3_clicked(self):
        self.hide()
        print('push setting buttom')
        dialog = Main_setting_Ui(parent=self)  # 呼叫 Face_Recognition
        if dialog.exec():
            pass  # do stuff on success
        self.show()
        sys.exit(app.exec_())

    def on_pushButton_2_clicked(self):
        self.DetectYolo = DetectYolo()
        QApplication.processEvents()

    def on_pushButton_clicked(self):
        print('Run')
        img_path = r'D:\yolov5-master\1-1.png'
        img = cv2.imread(img_path ,1)
        img1 = self.DetectYolo.detect(img)
        img2 = cv2.resize(img1, (700, 600), interpolation=cv2.INTER_CUBIC)

        self.displayImage_Scratch(img2, window=1)
        QApplication.processEvents()
#--------------------------------------------------------------------
#--------------------------- setting --------------------------------
#--------------------------------------------------------------------
class Main_setting_Ui(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Setting()
        self.ui.setupUi(self)
        # read level.json
        # self.level = r
# ----------------------------------------------------------------------------------------------------
# --------------------------------------------- save -------------------------------------------------
# ----------------------------------------------------------------------------------------------------
    def on_pushButton_clicked(self):
        self.hide()
        print('-'*15)
        dialog = Main_Contact_Ui(parent=self)  # 呼叫 Face_Recognition
        if dialog.exec():
            pass  # do stuff on success
        self.show()
        sys.exit(app.exec_())

# ----------------------------------------------------------------------------------------------------
# ---------------------------------------------- AOI Burr  -------------------------------------------
# ----------------------------------------------------------------------------------------------------
    def Burr_save_json(self,standard_thickness,extended,shrink):
        # if you not input any parameter it'll passs the function
        if standard_thickness == '' or extended == '' or shrink == '':
            print('set your parameters')

        print('thicknes:', standard_thickness)
        print('extended:', extended)
        print('shrink:', shrink)

        file = r'config\main.json'  # read the json file path
        with open(file, 'r', encoding="utf-8") as f:
            data = json.load(f)

            for layer_1 in data['al5']:
                print(layer_1)
                if layer_1 == 'standard_thickness':
                    data['al5'][layer_1] = float(standard_thickness)
                elif layer_1 == 'extended':
                    data['al5'][layer_1] = float(extended)
                elif layer_1 == 'shrink':
                    data['al5'][layer_1] = float(shrink)

            with open(file, 'w') as outfile:
                json.dump(data, outfile)


    def on_radioButton_burr_1_clicked(self):    #  Burr level 1
        self.Burr_save_json(0,4,4)
    def on_radioButton_burr_2_clicked(self):    #  Burr level 2
        self.Burr_save_json(0,8,8)
    def on_radioButton_burr_3_clicked(self):    #  Burr level 3
        self.Burr_save_json(0,10,10)

# ----------------------------------------------------------------------------------------------------
# ---------------------------------------------- AOI p point  -----------------------------------------
# ----------------------------------------------------------------------------------------------------
    def point_save_json(self,PPoint_conf_thres,weights1,json_file):
        print('radioButton click point')
        with open(json_file, 'r', encoding="utf-8") as f:
            data2 = json.load(f)
            # print(data2)

            for layer_1 in data2:
                # print(layer_1)
                if layer_1 == 'conf_thres':
                    data2['conf_thres'] = float(PPoint_conf_thres)
                    print('finish conf_thres setting: ', PPoint_conf_thres)
                elif layer_1 == 'weights':
                    data2['weights'] = weights1
                    print('finish weights1 setting: ', weights1)

            with open(json_file, 'w') as outfile:
                json.dump(data2, outfile)

    @pyqtSlot()  # do more than one thing
    def on_radioButton_ppoint_1_clicked(self): # ppoint level 1
        self.point_save_json(0.7,'weights/point.pt','config\detect_class_Scratch_0.2.json')
        self.point_save_json(self.level.scratch.level,'weights/point.pt','config\detect_class_Scratch_0.2.json')
        QApplication.processEvents()

    @pyqtSlot()  # do more than one thing
    def on_radioButton_ppoint_2_clicked(self): # ppoint level 2
        self.point_save_json(0.5, 'weights/point.pt', 'config\detect_class_Scratch_0.2.json')

    @pyqtSlot()  # do more than one thing
    def on_radioButton_ppoint_3_clicked(self):  # ppoint level 3
        self.point_save_json(0.2, 'weights/point.pt', 'config\detect_class_Scratch_0.2.json')

# ----------------------------------------------------------------------------------------------------
# ---------------------------------------------- AOI Scratch  ----------------------------------------
# ----------------------------------------------------------------------------------------------------
    def Scratch_save_json(self,Scratch_conf_thres,weights1,file):
        with open(file, 'r', encoding="utf-8") as f:
            data2 = json.load(f)
            # print(data2)

            for layer_1 in data2:
                # print(layer_1)
                if layer_1 == 'conf_thres':
                    data2['conf_thres'] = float(Scratch_conf_thres)
                    print('finish conf_thres setting: ', Scratch_conf_thres)
                elif layer_1 == 'weights':
                    data2['weights'] = weights1
                    print('finish weights1 setting: ', weights1)


            with open(file, 'w') as outfile:
                json.dump(data2, outfile)

    @pyqtSlot()  #do more than one thing
    def on_radioButton_scratch_1_clicked(self): # scratch level 1
        self.Scratch_save_json(0.2,'weights/scratch_.pt',r'config\detect_class_Scratch_0.2.json')

    @pyqtSlot()  # do more than one thing
    def on_radioButton_scratch_2_clicked(self):  # scratch level 2
        self.Scratch_save_json(0.5, 'weights/scratch_.pt', r'config\detect_class_Scratch_0.2.json')

    @pyqtSlot()  # do more than one thing
    def on_radioButton_scratch_3_clicked(self):  # scratch level 3
        self.Scratch_save_json(0.7, 'weights/scratch_.pt', r'config\detect_class_Scratch_0.2.json')


if __name__ == "__main__":  # 用於目前窗體測試
    app = QApplication(sys.argv)  # 建立GUI套用程式
    form = Main_Contact_Ui()  # 建立窗體
    form.show()
    sys.exit(app.exec_())