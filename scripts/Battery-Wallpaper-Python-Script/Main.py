from psutil import sensors_battery
import os , time
def setWallpaper( dirAdderss):
    battery = sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged==False: type="/battery_"
    else: type="/charge_"

    if  percent > 0 and percent < 20:
        image = "1.png"
    elif percent > 20 and percent< 40:
        image = "2.png"
    elif percent > 40 and percent < 60:
        image = "3.png"
    elif percent > 60 and percent < 80:
        image = "4.png"
    else:
        image = "5.png"
    
    return str("gsettings set org.gnome.desktop.background picture-uri file://"+ dirAdderss + type + image)
if __name__=="__main__":
    dirAdderss = str(os.getcwd()) # Add directory address when you change it
    cmd = None
    precmd = None
    while True:
        try:
            cmd = setWallpaper(dirAdderss)
            if cmd != precmd:
                os.system(cmd)
                precmd = cmd
            time.sleep(10)
        except Exception as error:
            print(f"exiting {error}")
            break
