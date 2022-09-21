class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < numRows or numRows == 1:
            return s
        s = list(s)
        rows = [[] for i in range(numRows)]
        sequence = [n for n in range(numRows)]
        up = sequence[:-1][::-1]
        down = sequence[1:]
        moving_up_ind = 0
        moving_down_ind = 0
        for i in range(numRows):
            rows[i].append(s[i])
        moving_up = True
        for j in range(numRows, len(s)):
            if moving_up:
                rows[up[moving_up_ind]].append(s[j])
                moving_up_ind += 1
                if moving_up_ind == len(up):
                    moving_up = False
                    moving_up_ind = 0
            else:
                rows[down[moving_down_ind]].append(s[j])
                moving_down_ind += 1
                if moving_down_ind == len(down):
                    moving_up = True
                    moving_down_ind = 0
        full_str = ''.join([''.join(x) for x in rows])
        return full_str


if __name__ == '__main__':
    sol = Solution()
    sol.convert('A', 2)
