f = open('../input', 'r')

nums = []
for line in f.readlines():
    nums.append(int(line))
f.close()

def run_loops(nums):
    for num1 in nums:
        for num2 in nums:
            if num1 + num2 == 2020:
                print (num1 * num2)
                return
run_loops(nums)