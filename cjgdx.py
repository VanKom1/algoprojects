from PyQt5.QtWidgets import QFileDialog,QApplication,QWidget,QPushButton,QLabel,QListWidget,QVBoxLayout,QHBoxLayout
import os
from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

app = QApplication([])
window = QWidget()
window.resize(700,500)
window.setWindowTitle("Редактор картинок")

image_label = QLabel("Картинка")
button_dir = QPushButton("Папка")
file_list = QListWidget()

button_left = QPushButton("Лево")
button_right = QPushButton("Вправо")
button_flip = QPushButton("Зеркало")
button_sharp = QPushButton("Резкость")
button_bw = QPushButton("Ч/Б")

main_line = QHBoxLayout()

col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

col_1.addWidget(button_dir)
col_1.addWidget(file_list)

col_2.addWidget(image_label)

button_line = QHBoxLayout()

button_line.addWidget(button_right)
button_line.addWidget(button_left)
button_line.addWidget(button_flip)
button_line.addWidget(button_sharp)
button_line.addWidget(button_bw)

col_2.addLayout(button_line)

main_line.addLayout(col_1,20)
main_line.addLayout(col_2,80)
window.setLayout(main_line)

workdir = ""

def chooseworkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files,extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename) 
    return result
def showFilesinlist():
    extensions = [".jpg",".jpeg",".png",".gif"]
    chooseworkDir()
    filenames = filter(os.listdir(workdir), extensions)
    file_list.clear()
    for filename in filenames:
        file_list.addItem(filename)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"    

    def loadImage(self,dir,filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir,filename)
        self.image = Image.open(image_path)

    def showImage(self,path):
        image_label.hide()
        pixmapimage = QPixmap(path)
        w, h = image_label.width(),image_label.height()
        pixmapimage = pixmapimage.scaled(w,h, Qt.KeepAspectRatio)
        image_label.setPixmap(pixmapimage)
        image_label.show()
def showChosenImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        workimage.loadImage(workdir,filename)
        image_path = os.path.join(workimage.dir,workimage.filename)
        workimage.showImage(image_path)

workimage = ImageProcessor()

file_list.currentRowChanged.connect(showChosenImage)
button_dir.clicked.connect(showFilesinlist)
window.show()
app.exec()
