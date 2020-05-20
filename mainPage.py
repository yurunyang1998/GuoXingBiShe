import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import  os
from mainUI import Ui_MainWindow
from mylabel import MyLabel
import XMLP

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

        self.pushButton_2.clicked.connect(self.setSavePath)
        self.pushButton.clicked.connect(self.saveXML)
        self.pushButton_3.clicked.connect(self.addLabels)

        self.lb = MyLabel(self)
        # self.lb.setGeometry(QtCore.QRect(290,40,681,631))
        self.verticalLayout.addWidget(self.lb)

        self.lb.addFunc(self.addRoiListitem)
        self.listWidget.itemSelectionChanged.connect(self.getListitems)
        self.xmlSavePath = "./xmlfiles"
        self.XMLP = XMLP.XMLP("./xmltemplete.xml", "./objxmltemplete.xml")

        self.class_ = self.comboBox.currentText()
        self.comboBox.currentIndexChanged.connect(self.labelchanged)
        self.pushButton_4.clicked.connect(self.autoDectection)


    def autoDectection(self):
        if(self.lb.autodec == True):
            self.lb.autodec = False
        else:
            self.lb.autodec = True




    def getListitems(self):
        item = self.listWidget.currentItem()

        # print(item.text())
        self.showSelectedPic(item.text())

    def labelchanged(self):
        self.class_ = self.comboBox.currentText()


    def addRoiListitem(self):
        roi = self.lb.Rois.pop()
        self.roilistwidget.addItem(str(roi))
        self.lb.Rois.append([roi,self.class_])

    def addLabels(self):
        labels = self.textEdit.toPlainText()
        for i in labels.splitlines():
            self.comboBox.addItem(i)


    def setSavePath(self):
        self.xmlSavePath =  QFileDialog.getExistingDirectory(self, '设置xml文件保存路径','./')
        if(self.xmlSavePath==""):
            self.xmlSavePath = "./xmlfiles"

    def saveXML(self):

        filename = self.listWidget.currentItem().text()
        filename = os.path.split(filename)[-1]
        self.XMLP.setfilename(filename)
        # self.XMLP.setSize(self.lb.size()[0],self.lb.size()[1])
        for roi in self.lb.Rois:
            print(roi[0].x(),roi[0].y(),roi[0].width()+roi[0].x(),roi[0].height()+roi[0].y())
            # print(self.class_)
            self.XMLP.insert(roi[1], int(roi[0].x()/self.widthscale) ,int(roi[0].y()/self.heightscale),int(roi[0].width()+roi[0].x()/self.widthscale), int(roi[0].height()+roi[0].y()/self.heightscale))
        if(not os.path.exists(self.xmlSavePath)):
            os.mkdir(self.xmlSavePath)
        self.XMLP.write(os.path.join(self.xmlSavePath,filename.split('.')[0]+".xml"))


    def showSelectedPic(self,picname):
        print(picname)
        self.lb.clear()
        self.roilistwidget.clear()
        pic = QPixmap(picname)
        realwidth = pic.width()
        realheight = pic.height()


        self.lb.setPixmap(pic)  #标签
        showwidth = self.lb.width()
        showheight = self.lb.height()

        self.widthscale = showwidth/realwidth
        self.heightscale = showheight/realheight


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
