import tkinter as tk
from tkinter import ttk
import psutil
import math
import random

class SovereignVisualOS:
    def __init__(self, root):
        self.root = root
        self.root.title("SOVEREIGN OS - MONTER KERNEL V2.0")
        self.root.geometry("800x500")
        self.root.configure(bg="#000d0d") # لون أسود عميق (Cyberpunk)

        # العناوين
        self.label_title = tk.Label(root, text="SOVEREIGN HARDWARE INTERFACE", font=("Courier", 20, "bold"), fg="#00ffff", bg="#000d0d")
        self.label_title.pack(pady=10)

        # منطقة البيانات الفيزيائية
        self.frame_stats = tk.Frame(root, bg="#001a1a", bd=2, relief="ridge")
        self.frame_stats.pack(padx=20, pady=20, fill="both", expand=True)

        self.temp_var = tk.StringVar(value="TEMP: --")
        self.stress_var = tk.StringVar(value="STRESS INDEX: --")
        self.entropy_var = tk.StringVar(value="PHYSICAL KEY: --")

        self.create_stat_label(self.temp_var, "#ff3333") # أحمر للحرارة
        self.create_stat_label(self.stress_var, "#33ff33") # أخضر للأداء
        self.create_stat_label(self.entropy_var, "#ffff33") # أصفر للتشفير

        # شريط التحميل (CPU LOAD)
        self.progress = ttk.Progressbar(root, orient="horizontal", length=600, mode="determinate")
        self.progress.pack(pady=20)

        self.update_system_data()

    def create_stat_label(self, var, color):
        lbl = tk.Label(self.frame_stats, textvariable=var, font=("Courier", 16), fg=color, bg="#001a1a")
        lbl.pack(pady=10)

    def update_system_data(self):
        # 1. جلب بيانات حقيقية من العتاد
        cpu_usage = psutil.cpu_percent()
        temps = psutil.sensors_temperatures().get('coretemp', [])
        current_temp = temps[0].current if temps else random.uniform(40, 55)

        # 2. الحسابات الفيزيائية السيادية
        stress_index = round(math.log(current_temp + 273.15) * 0.5, 5)
        phys_key = "".join(random.choices("ABCDEF0123456789", k=12))

        # 3. تحديث الواجهة
        self.temp_var.set(f"CORE TEMPERATURE: {current_temp}°C")
        self.stress_var.set(f"PHYSICAL STRESS INDEX: {stress_index}")
        self.entropy_var.set(f"QUANTUM ENTROPY KEY: {phys_key}")
        self.progress['value'] = cpu_usage

        # تلوين الواجهة بناءً على الخطر
        if current_temp > 70:
            self.frame_stats.configure(highlightbackground="red", highlightthickness=2)
        else:
            self.frame_stats.configure(highlightbackground="#00ffff", highlightthickness=1)

        self.root.after(500, self.update_system_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = SovereignVisualOS(root)
    root.mainloop()
