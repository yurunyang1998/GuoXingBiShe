
import xml.dom.minidom

class XMLP:
    def __init__(self, xmltemplete, objxml):
        self.xmltemplete = xmltemplete
        self.objxml = objxml
        self.readTemplete()

    def readTemplete(self):
        if(self.xmltemplete and self.objxml):
            self.DOMTree = xml.dom.minidom.parse(self.xmltemplete)
            self.objTree = xml.dom.minidom.parse(self.objxml)

        else:
            raise FileExistsError

    def setfilename(self,filename):
        node = self.DOMTree.documentElement.getElementsByTagName("filename")
        node[0].firstChild.data = "hahaha"

    def setSize(self, width, height):
        node = self.DOMTree.documentElement.getElementsByTagName("width")
        node[0].firstChild.data = width
        node = self.DOMTree.documentElement.getElementsByTagName("height")
        node[0].firstChild.data = height

    def insert(self,name, xmin,ymin, xmax, ymax):

        tempnode = self.objTree.cloneNode(deep=True)

        node = tempnode.documentElement.getElementsByTagName("name")
        node[0].firstChild.data = name

        node = tempnode.documentElement.getElementsByTagName("xmin")
        node[0].firstChild.data = xmin

        node = tempnode.documentElement.getElementsByTagName("ymin")
        node[0].firstChild.data = ymin

        node = tempnode.documentElement.getElementsByTagName("xmax")
        node[0].firstChild.data = xmax

        node = tempnode.documentElement.getElementsByTagName("ymax")
        node[0].firstChild.data = ymax


        self.DOMTree.documentElement.appendChild(tempnode.documentElement)



        print(self.DOMTree.toxml())

    def write(self,filename):
        with open(filename,"w") as f:
            self.DOMTree.writexml(f)
            f.close()

if __name__ == '__main__':
    xmlp = XMLP("./xmltemplete.xml","objxmltemplete.xml")
    # xmlp.setfilename("hahahaha")
    xmlp.setSize(100,100)

    xmlp.insert("haha",10,100,10,100)
    xmlp.insert("hasdfha",10,3,32,43)
    xmlp.write("test.xml")