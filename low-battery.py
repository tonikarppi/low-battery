import psutil
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play


def get_beep_sound():
    beep_sound = AudioSegment.from_wav("sounds/beep.wav")
    beep_sound -= 20  # Lowers the volume
    return beep_sound


def get_battery_info():
    battery = psutil.sensors_battery()
    battery_percentage = battery[0]
    power_plugged_in = battery[2]
    return battery_percentage, power_plugged_in


def get_date_string():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def main():
    date_string = get_date_string()
    print(f"Script started on: {date_string}.")
    battery_percentage, power_plugged_in = get_battery_info()

    if battery_percentage <= 10 and not power_plugged_in:
        beep_sound = get_beep_sound()
        play(beep_sound)


if __name__ == "__main__":
    main()
