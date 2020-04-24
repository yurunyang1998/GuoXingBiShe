import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import  os
from mainUI import Ui_MainWindow
from mylabel import MyLabel


def listdir(path, list_name): #传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        list_name.append(file_path)


def alert(Qwidget, message):
        reply = QMessageBox.information(Qwidget, '提示', message, QMessageBox.Ok | QMessageBox.Close,
                                        QMessageBox.Close)


class MyPyQT_Form(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.actionreadfile.triggered.connect(self.actionreadfile_click)
        self.lb = MyLabel(self)
        self.lb.setGeometry(QtCore.QRect(290,40,681,631))
        self.lb.addFunc(self.addRoiListitem)
        self.listWidget.itemSelectionChanged.connect(self.getListitems)

    def getListitems(self):
        item = self.listWidget.currentItem()

        print(item.text())
        self.showSelectedPic(item.text())

    def addRoiListitem(self):
        self.roilistwidget.addItem(str(self.lb.Rois[-1]))


    def showSelectedPic(self,picname):
        print(picname)
        self.lb.clear()
        self.roilistwidget.clear()
        self.lb.setPixmap(QPixmap(picname))  #标签
        self.lb.setScaledContents(True)


    def actionreadfile_click(self):
        # image_file, _ = QFileDialog.getOpenFileName(self, 'Open file', 'd:\Pictures','Image files (*.jpg *.gif *.png *.jpeg)')
        # self.lb.setPixmap(QPixmap(image_file))  #标签
        # self.lb.setScaledContents(True)
        try:
            self.rootdir = QFileDialog.getExistingDirectory(self, '打开文件','./')
            self.filelist = []
            listdir(self.rootdir,self.filelist)   #获取当前文件夹下所有文件路径
            self.listWidget.clear()
            for i in self.filelist:
                # print(i)
                self.listWidget.addItem(i)
        except Exception as e:
            alert(self,str(e))
            print(e)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())
