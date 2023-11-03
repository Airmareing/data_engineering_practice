import math

with open("../src_data/text_3_var_42") as data:
    lines = data.readlines()

res = list()

for line in lines:
    sqrt_only = list()
    nums = line.strip().split(",")
    for i in range(len(nums)):
        if nums[i] == 'NA':
            nums[i] = str((int(nums[i-1])+int(nums[i+1]))/2)

    for item in nums:
        num = float(item)
        if math.sqrt(num) > 92:
            sqrt_only.append(num)
            
    res.append(sqrt_only)

with open("../results/output_data_3.txt", 'w') as output:
    for row in res:
        for num in row:
            output.write(str(num)+',')
        output.write("\n")