import os
# ميزة 9: قطع اتصال خوادم جوجل نهائياً من جذور النظام
def kill_telemetry():
    domains = ["telemetry.google.com", "stats.g.doubleclick.net", "ad-delivery.net"]
    with open("/etc/hosts", "a") as f:
        for d in domains:
            f.write(f"127.0.0.1 {d}\n")
    print("Shadow Protocol: Google is officially BLIND.")

kill_telemetry()
