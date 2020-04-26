from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen

class MyLabel(QLabel):



    Rois = []
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False
    #鼠标点击事件
    moved = False
    #鼠标移动
    def clear(self):
        self.Rois.clear()

    def addFunc(self,func):
        self.func = func

    def mousePressEvent(self,event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()
    #鼠标释放事件
    def mouseReleaseEvent(self,event):
        self.flag = False
        if(self.moved):
            self.Rois.append(self.rect)   #释放鼠标时将roi添加进列表
            self.func()
            self.moved = False

    #鼠标移动事件
    def mouseMoveEvent(self,event):
        self.moved = True
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()
    #绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)  #调用的父类label的paintEvent？？
        self.rect =QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
        # self.rect.height()
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green,1,Qt.SolidLine))
        painter.drawRect(self.rect)

        for roi in self.Rois:           #重新绘制之前添加的roi
            # print(roi.x(),roi.y(),roi.width()+roi.x(),roi.height()+roi.y())
            painter.drawRect(roi[0])

        pqscreen = QApplication.primaryScreen()  # 保存截图
        # pixmap2 = pqscreen.grabWindow(self.winId(), self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
        # # pixmap2 = pqscreen.grabWindow(self.winId(), self.x0 + 1, self.y0 + 1, abs((self.x1 - 1) - (self.x0 + 1)),abs((self.y1 - 1) - (self.y0 + 1)))
        # pixmap2.save('cut.png')