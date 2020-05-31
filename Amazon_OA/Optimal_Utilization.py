class Solution:

    def optimal(self, a, b, target):

        alist = sorted(a, key=lambda x: x[1])
        blist = sorted(b, key=lambda x: x[1])

        res = []
        left = 0
        right = len(b) - 1
        temp = float("-inf")

        while left < len(alist) and right >= 0:

            sumAB = alist[left][1] + blist[right][1]

            if sumAB > target:
                right -= 1

            else:

                if sumAB >= temp:
                    if sumAB > temp:
                        res = []
                        temp = sumAB

                    res.append([alist[left][0], blist[right][0]])
                    count = right

                    while count > 0 and blist[count][1] == blist[count - 1][1]:
                        res.append([alist[left][0], blist[count - 1][0]])
                        count -= 1

                left += 1

        if not res:
            return [[]]

        return res


if __name__ == "__main__":
    a = [[1, 8], [2, 7], [3, 14]]
    b = [[1, 5], [2, 10], [3, 14]]
    target = 20

    print (Solution().optimal(a, b, target))
