class Alarm:
    def __init__(self, hour, minute, repeat_days):
        self.hour = hour
        self.minute = minute
        self.repeat_days = repeat_days

    def save(self):
        print(f"알람이 {self.hour}시 {self.minute}분에 설정되었습니다. 반복 요일: {', '.join(self.repeat_days)}")


class AlarmApp:
    def __init__(self):
        self.alarms = []

    def add_alarm(self, hour, minute, repeat_days):
        alarm = Alarm(hour, minute, repeat_days)
        alarm.save()
        self.alarms.append(alarm)


if __name__ == "__main__":
    app = AlarmApp()
    app.add_alarm(7, 30, ['월', '화', '수', '목', '금'])
