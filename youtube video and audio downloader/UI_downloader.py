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

        title = QLabel("Youtube Downloader")
        title.setFont(titleFont)

        self.url_edit = QLineEdit()
        self.url_edit.setPlaceholderText("Enter video url.")

        radio_btn_1 = QRadioButton("Video")
        radio_btn_1.toggled.connect(lambda: self.btn_toggled(radio_btn_1))

        radio_btn_2 = QRadioButton("Audio")
        radio_btn_2.toggled.connect(lambda: self.btn_toggled(radio_btn_2))

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
        layout_h3.addWidget(radio_btn_1)
        layout_h3.addWidget(radio_btn_2)
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

        self.download_type = "Video"

    def btn_toggled(self, button):

        self.download_type = button.text()


    def download(self):

        url = self.url_edit.text()

        x = YouTube(url)

        title = x.title

        if title == "YouTube":
            title = x.author + str(time())

        if self.download_type == "Video":

            output_folder_name = "downloaded_videos"

            cwd = os.getcwd()

            outout_folder_path = os.path.join(cwd, output_folder_name)

            if not os.path.exists(outout_folder_path):
                os.mkdir(outout_folder_path)

            prog_streams = x.streams.filter(progressive=True)
            video = prog_streams.filter(res="720p").first()
            if video == None:
                video = prog_streams.filter(res="480p").first()
            if video == None:
                video = prog_streams.filter(res="360p").first()
            if video == None:
                QMessageBox.warning(self, "Error :(", "This resolution is not available.",
                                    QMessageBox.Ok)

            video.download(outout_folder_path, title)
            QMessageBox.information(self, "Success!", "Video downloaded successfully.", QMessageBox.Ok)

        elif self.download_type == "Audio":

            output_folder_name = "downloaded_audios"

            cwd = os.getcwd()

            outout_folder_path = os.path.join(cwd, output_folder_name)

            if not os.path.exists(outout_folder_path):
                os.mkdir(outout_folder_path)

            audio = x.streams.filter(only_audio=True).first()

            if audio == None:
                QMessageBox.warning(self, "Error :(", "This video is not available.",
                                    QMessageBox.Ok)
            else:
                audio.download(outout_folder_path, title)
                tgt_folder = "downloaded_audios"

                for file in [n for n in os.listdir(tgt_folder) if re.search('mp4', n)]:
                    full_path = os.path.join(tgt_folder, file)
                output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
                clip = mp.AudioFileClip(full_path)
                clip.write_audiofile(output_path)
                os.remove(full_path)
                QMessageBox.information(self, "Success!", "Audio file downloaded successfully.", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Main()
    sys.exit(app.exec_())