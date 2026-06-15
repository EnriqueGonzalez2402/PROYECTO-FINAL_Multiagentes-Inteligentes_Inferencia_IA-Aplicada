class LocalizationAgent:

    SPEED_SOUND = 343.0

    def calculate_distance(self, rtt):

        tof = rtt / 2

        distance = tof * self.SPEED_SOUND

        return {
            "rtt": rtt,
            "tof": tof,
            "distance": round(distance, 3)
        }