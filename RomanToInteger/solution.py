class Solution:
    def romanToInt(self, s: str) -> int:
        last_char = ''
        total = 0
        # loop through each character and add the appropriate amount
        for c in s:
            if(c == 'I'):
                total += 1
            elif(c == 'V'):
                if(last_char == 'I'):
                    total += 3
                else:
                    total += 5
            elif(c == 'X'):
                if(last_char == 'I'):
                    total += 8
                else:
                    total += 10
            elif(c == 'L'):
                if(last_char == 'X'):
                    total += 30
                else:
                    total += 50
            elif(c == 'C'):
                if(last_char == 'X'):
                    total += 80
                else:
                    total += 100
            elif(c == 'D'):
                if(last_char == 'C'):
                    total += 300
                else:
                    total += 500
            elif(c == 'M'):
                if(last_char == 'C'):
                    total += 800
                else:
                    total += 1000
            # store last character for if statement checks
            last_char = c
        return total