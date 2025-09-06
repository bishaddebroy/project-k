class Solution:
    # Sliding Window. Time Complexity: O(N), Space Complexity: O(1).
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L, total, cnt = 0, 0, 0

        for R in range(len(arr)):
            total += arr[R]

            if R - L + 1 == k:
                if total >= threshold * k:
                    cnt += 1
                total -= arr[L]
                L += 1
        
        return cnt
    
    # Sliding Window (Optimized). Time Complexity: O(N), Space Complexity: O(1).
    def numOfSubarrays2(self, arr: List[int], k: int, threshold: int) -> int:
        total = sum(arr[:k])
        cnt = 1 if total >= threshold * k else 0

        for i in range(k, len(arr)):
            total += arr[i] - arr[i - k]
            if total >= threshold * k:
                cnt += 1
        
        return cnt