# There are several cards arranged in a row, and each card has an associated number of points. The points
# are given in the integer array cardPoints.
#
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
#
# Your score is the sum of the points of the cards you have taken.
#
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
#
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first
# will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final
# score of 1 + 6 + 5 = 12.
#
# Input: cardPoints = [9,7,7,9,7,7,9], k = 7
# Output: 55
# Explanation: You have to take all the cards. Your score is the sum of points of all cards.
#
# Input: cardPoints = [1,1000,1], k = 1
# Output: 1
# Explanation: You cannot take the card in the middle. Your best score is 1.
#
# Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
# Output: 202

class Solution:
    def maxScore(self, cardPoints, k):
        start = 0
        subarraySum = 0
        n = len(cardPoints)
        requiredSubarrayLength = n - k
        currentSubarrayLength = 0
        totalScore = 0

        for num in cardPoints:
            totalScore += num

        minSubarrayScore = totalScore

        if n == k:
            return totalScore

        for i in range(n):
            subarraySum += cardPoints[i]
            currentSubarrayLength = i - start + 1

            if currentSubarrayLength == requiredSubarrayLength:
                minSubarrayScore = min(minSubarrayScore, subarraySum)

                subarraySum -= cardPoints[start]
                start += 1
        return totalScore - minSubarrayScore