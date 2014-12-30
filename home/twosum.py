# issue 1

class Solution:

    # @return a tuple, (index1, index2)

    def twoSum(self, num, target):

        num_dict = {}

        for i in range(len(num)):

            if (target - num[i]) in num_dict:

                return (num_dict[target - num[i]], i + 1)

            else:

                num_dict[num[i]] = i + 1

        return None
