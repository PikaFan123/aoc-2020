f = open('../input', 'r')

nums = []
for line in f.readlines():
    nums.append(int(line))
f.close()

def run_loops(nums):
    for num1 in nums:
        for num2 in nums:
            for num3 in nums:
                if num1 + num2 + num3 == 2020:
                    print (num1 * num2 * num3)
                    return
run_loops(nums)