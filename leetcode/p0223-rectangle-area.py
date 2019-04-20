class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        x = 0
        y = 0
        if A <= E < C:
            x = min(G - E, C - E)
            if B < H <= D:
                y = min(H - B, H - F)
            elif B <= F < D:
                y = min(D - F, H - F)
            elif F <= B <= D <= H:
                y = D - B
        elif A < G <= C:
            x = min(G - A, G - E)
            if B < H <= D:
                y = min(H - B, H - F)
            elif B <= F < D:
                y = min(D - F, H - F)
            elif F <= B <= D <= H:
                y = D - B
        elif E <= A <= C <= G:
            x = C - A
            if B < H <= D:
                y = min(H - B, H - F)
            elif B <= F < D:
                y = min(D - F, H - F)
            elif F <= B <= D <= H:
                y = D - B

        return area1 + area2 - x * y

if __name__ == '__main__':
    #print Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
    print Solution().computeArea(-2, -2, 2, 2, 3, 3, 4, 4)
    #print Solution().computeArea(0, 0, 0, 0, -1, -1, 1, 1)
