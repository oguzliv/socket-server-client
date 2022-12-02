class Message:
    def __init__(self, imei, lock_status, battery, network_value, charging_status, eol):
        self.imei = imei
        self.lock_status = lock_status
        self.battery = battery
        self.network_value = network_value
        self.charging_status = charging_status
        self.eol = eol

    def __str__(self):
        return f"{self.imei},{self.lock_status},{self.battery},{self.network_value},{self.charging_status},{self.eol}"

    def objectify_message(self):
        return {
            "imei": self.imei,
            "lock_status": self.lock_status,
            "battery": self.battery,
            "network_value": self.network_value,
            "charging_status": self.charging_status
        }
