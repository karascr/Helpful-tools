import os
import pyautogui
import time
from pynput.keyboard import Listener


def ekrani_cek(tus):
    if tus.char == "q":
        # pyautogui ile ekran görüntüsünü alıyoruz.
        ekran_goruntusu = pyautogui.screenshot()

        # her ekran görüntüsünü için farklı bir isim belirliyoruz.
        # Şu anki zamanı kullanıyoruz böylece isim hiçbir zqqaman aynı olmuyor.
        dosya_adi = str(time.time_ns()) + ".jpg"

        # ekran görüntüsünün kaydedileceği yolu belirliyoruz, bu örnekte masaüstü.
        # kullanici_adi yazan kısmı kendi windows kullanıcı isminizle değiiştirmeyi unutmayın!
        dosya_yolu = os.path.join('C:\\Users\kara\Desktop\ss', dosya_adi)

        # ekran görüntüsünü save() fonksiyonu ile kaydediyoruz
        ekran_goruntusu.save(dosya_yolu)


with Listener(on_release=ekrani_cek) as listener:
    listener.join()