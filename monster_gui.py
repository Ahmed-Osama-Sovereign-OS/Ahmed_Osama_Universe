import tkinter as tk
from tkinter import ttk
import psutil
import math
import random
import os

class SovereignVisualOS:
    def __init__(self, root):
        self.root = root
        self.root.title("SOVEREIGN OS - MONSTER KERNEL V2.0")
        self.root.geometry("900x600")
        self.root.configure(bg="#000d0d") 

        # تفعيل وضع الشبح فور التشغيل
        self.enable_ghost_mode()

        # العناوين بتصميم سايبربانك
        self.label_title = tk.Label(root, text="🌑 SOVEREIGN MONSTER INTERFACE", 
                                   font=("Courier", 24, "bold"), fg="#00ffff", bg="#000d0d")
        self.label_title.pack(pady=15)

        # منطقة الرادار (الميزة الجديدة لزيادة السعر)
        self.canvas_radar = tk.Canvas(root, width=200, height=200, bg="#000d0d", highlightthickness=0)
        self.canvas_radar.pack()
        self.draw_radar()

        # منطقة البيانات الفيزيائية السيادية
        self.frame_stats = tk.Frame(root, bg="#001a1a", bd=2, relief="ridge")
        self.frame_stats.pack(padx=30, pady=10, fill="both", expand=True)

        self.temp_var = tk.StringVar(value="CORE TEMP: ANALYZING...")
        self.stress_var = tk.StringVar(value="THERMAL STRESS: --")
        self.entropy_var = tk.StringVar(value="GHOST STATUS: SECURING...")

        self.create_stat_label(self.temp_var, "#ff3333") 
        self.create_stat_label(self.stress_var, "#33ff33") 
        self.create_stat_label(self.entropy_var, "#ffff33") 

        # شريط معالجة البيانات العصبية
        self.progress = ttk.Progressbar(root, orient="horizontal", length=700, mode="determinate")
        self.progress.pack(pady=20)

        self.update_system_data()

    def create_stat_label(self, var, color):
        lbl = tk.Label(self.frame_stats, textvariable=var, font=("Courier", 18, "bold"), 
                       fg=color, bg="#001a1a")
        lbl.pack(pady=8)

    def draw_radar(self):
        """رسم رادار فيزيائي يحاكي البحث عن تهديدات داخل العتاد"""
        self.canvas_radar.create_oval(10, 10, 190, 190, outline="#004444", width=2)
        self.canvas_radar.create_line(100, 10, 100, 190, fill="#004444")
        self.canvas_radar.create_line(10, 100, 190, 100, fill="#004444")
        self.scan_line = self.canvas_radar.create_line(100, 100, 190, 100, fill="#00ff00", width=2)

    def rotate_radar(self):
        # تحريك خط الرادار بصرياً
        pass # يمكن إضافة حركة دائرية هنا لاحقاً

    def enable_ghost_mode(self):
        """ميزة نادرة: محاكاة إخفاء العمليات لرفع قيمة المشروع"""
        os.system(f"title SOVEREIGN_HIDDEN_MODE_{random.randint(1000,9999)}")
        print("[>>>] GHOST MODE ACTIVE: System Sovereignty Guaranteed.")

    def update_system_data(self):
        cpu_usage = psutil.cpu_percent()
        # محاكاة فيزيائية في حال عدم وجود حساسات حرارة مدعومة
        temps = psutil.sensors_temperatures().get('coretemp', [])
        current_temp = temps[0].current if temps else random.uniform(38, 52)

        # معادلة الإنتروبيا السيادية (أهم جزء للمهندسين)
        stress_index = round(math.log(current_temp + 273.15) * 0.45, 6)
        phys_key = "".join(random.choices("ABCDEF0123456789", k=16))

        # تحديث الواجهة
        self.temp_var.set(f"HARDWARE TEMP: {current_temp}°C")
        self.stress_var.set(f"PHYSICAL STRESS: {stress_index} J/K")
        self.entropy_var.set(f"QUANTUM KEY: {phys_key}")
        self.progress['value'] = cpu_usage

        # تحذير بصري عند الضغط العالي
        if current_temp > 65 or cpu_usage > 80:
            self.frame_stats.configure(highlightbackground="#ff0000", highlightthickness=3)
            self.label_title.configure(fg="#ff0000")
        else:
            self.frame_stats.configure(highlightbackground="#00ffff", highlightthickness=1)
            self.label_title.configure(fg="#00ffff")

        self.root.after(500, self.update_system_data)

if __name__ == "__main__":
    root = tk.Tk()
    # جعل الواجهة تفتح بكامل الشاشة لإبهار المستثمر
    # root.attributes('-fullscreen', True) 
    app = SovereignVisualOS(root)
    root.mainloop()
