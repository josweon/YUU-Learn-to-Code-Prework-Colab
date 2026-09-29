nums = [2,1,5,0,4,6]
i = 0
window_size = 3

answer = False

for i in range(len(nums) - window_size + 1):
    window = nums[i:i+window_size]

    print(window)        
    if window[0] < window[1] < window[2]:
        answer = True
        break
        
print(answer)
