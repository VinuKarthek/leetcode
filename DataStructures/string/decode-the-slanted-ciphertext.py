https://leetcode.com/problems/decode-the-slanted-ciphertext/

class Solution:
    def decodeCiphertext_mysolution(self, encodedText: str, rows: int) -> str:
        cols = int(len(encodedText)/rows)
        matrix = [[encodedText[col+row*cols] for col in range(cols)] for row in range(rows)]
        #print(matrix)
        
        out = ''
        for col in range(cols):
            for row in range(rows):
                if col<cols:
                    out = out+ matrix[row][col]
                col = col+1
        return out.rstrip()
    
    
    def decodeCiphertext_best(self, encodedText: str, rows: int) -> str:
        cols = int(len(encodedText) / rows)
        res = []
        for i in range(cols):
            while i < len(encodedText):
                res.append(encodedText[i])
                i += cols + 1
        return ''.join(res).rstrip()