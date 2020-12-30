import re

from PyQt5.QtGui import QFont
from pytube import YouTube
from time import time
import os
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, \
    QLineEdit, QRadioButton, QLabel, QMessageBox
import moviepy.editor as mp

titleFont = QFont("Arial", 28, weight=400)
buttonFont = QFont("Arial", 16)
url = QFont("Arial", 16)

class Main(QWidget):

    def __init__(self):
        super().__init__()

        title = QLabel("Youtube Video Downloader")
        title.setFont(titleFont)

        self.url_edit = QLineEdit()
        self.url_edit.setPlaceholderText("Enter video url.")

        btn = QPushButton("Download")
        btn.setFont(buttonFont)
        btn.clicked.connect(self.download)

        credit = QLabel("Coded by Muhammet Kara")

        layout_h1 = QHBoxLayout()
        layout_h1.setAlignment(Qt.AlignCenter)
        layout_h1.addWidget(title)

        layout_h2 = QHBoxLayout()
        layout_h2.addWidget(self.url_edit)

        layout_h3 = QHBoxLayout()
        layout_h3.setAlignment(Qt.AlignCenter)
        layout_h3.addWidget(btn)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.addLayout(layout_h1)
        layout.addSpacing(10)
        layout.addLayout(layout_h2)
        layout.addLayout(layout_h3)
        layout.addWidget(credit)


        self.setLayout(layout)

        self.setWindowTitle("Youtube Downloader")
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.setFixedSize(QSize(600, 250))
        self.offset = None
        self.show()

    def download(self):

        url = self.url_edit.text()

        x = YouTube(url)

        title = x.title

        if title == "YouTube":
            title = x.author + str(time())

        output_folder_name = "downloaded_videos"

        cwd = os.getcwd()

        outout_folder_path = os.path.join(cwd, output_folder_name)

        if not os.path.exists(outout_folder_path):
            os.mkdir(outout_folder_path)

        streams = x.streams
        video = streams.filter(res="720p").first()
        if video == None:
            video = streams.filter(res="480p").first()
        if video == None:
            video = streams.filter(res="360p").first()
        if video == None:
            QMessageBox.warning(self, "Error :(", "This resolution is not available.",
                                QMessageBox.Ok)

        video.download(outout_folder_path, title)
        QMessageBox.information(self, "Success!", "Video downloaded successfully.", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Main()
    sys.exit(app.exec_())