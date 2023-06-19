class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
#         self = class 안에 있는 함수임을 정의
        Kelvin = celsius +273.15
        Fahrenheit = celsius*1.8 +32.00
        return [Kelvin,Fahrenheit]
           