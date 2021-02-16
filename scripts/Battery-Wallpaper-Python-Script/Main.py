import psutil
import os , time
def setWallpaper( dirAdderss ):
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged==False: plugged="Discharging"
    else: plugged="Charging"

    background_address: "None"
    if plugged == "Discharging":
        if  percent > 0 and percent < 20:
            background_address = dirAdderss+"/battery_1.png"
        elif percent>20 and percent<40:
            background_address = dirAdderss+"/battery_2.png"
        elif percent > 40 and percent < 60:
            background_address = dirAdderss+"/battery_3.png"
        elif percent >60 and percent < 80:
            background_address = dirAdderss+"/battery_4.png"
        else:
            background_address = dirAdderss+"/battery_5.png"
    else:
        if  percent > 0 and percent < 20:
            background_address = dirAdderss+"/charge_1.png"
        elif percent>20 and percent<40:
            background_address = dirAdderss+"/charge_2.png"
        elif percent > 40 and percent < 60:
            background_address = dirAdderss+"/charge_3.png"
        elif percent >60 and percent < 80:
            background_address = dirAdderss+"/charge_4.png"
        else:
            background_address = dirAdderss+"/charge_5.png"
    cmd = str("gsettings set org.gnome.desktop.background picture-uri file://"+background_address)
    os.system(cmd)

if __name__=="__main__":
    pwd = os.getcwd()
    dirAdderss = str(pwd) #Add directory address when you change it
    while True:
        try:    
            setWallpaper(dirAdderss)
            time.sleep(2)
        except:
            print("exiting")
            break
