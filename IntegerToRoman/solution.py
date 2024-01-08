class Solution:
    def intToRoman(self, num: int) -> str:
        # modular divides out each part while adding it
        result = ""
        # M = 1000
        for i in range(num//1000):
            result += 'M'
        num %= 1000
        # CM = 900
        for i in range(num//900):
            result += "CM"
        num %= 900
        # D = 500
        for i in range(num//500):
            result += 'D'
        num %= 500
        # CD = 400
        for i in range(num//400):
            result += "CD"
        num %= 400
        # C = 100
        for i in range(num//100):
            result += 'C'
        num %= 100
        # XC = 90
        for i in range(num//90):
            result += "XC"
        num %= 90
        # L = 50
        for i in range(num//50):
            result += 'L'
        num %= 50
        # XL = 40
        for i in range(num//40):
            result += "XL"
        num %= 40
        # X = 10
        for i in range(num//10):
            result += 'X'
        num %= 10
        # IX = 9
        for i in range(num//9):
            result += "IX"
        num %= 9
        # V = 5
        for i in range(num//5):
            result += 'V'
        num %= 5
        # IV = 4
        for i in range(num//4):
            result += "IV"
        num %= 4
        # I = 1
        for i in range(num):
            result += 'I'
        return result