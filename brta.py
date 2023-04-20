class BRTA:
    def __init__(self) -> None:
        self._license = {}

    def take_driving_test(self, email):
        score = random.randint(0, 100)

        if score >= 33:
            print('Congrats , you have passed')
            license_number = random.randint(5000, 9999)
            self._license[email] = license_number
            return license_number
        else:
            print("soory failed")
            return False

    def validate_license(self, email, license):
        for key, value in self._license.items():
            if key == email and value == license:
                return True
        return False
