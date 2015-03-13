# issue 169 

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        temp=[]
        for i in num:
            if not temp or temp[-1]==i:
                temp.append(i)
            else:
                temp.pop() 
        return temp[0]
    def majorityElement_2(self,num):
        candidate = None
        count = 0
        for n in num:
            if candidate == None:
                candidate = n
                count += 1
            elif n == candidate:
                count += 1
            elif n != candidate and count == 1:
                candidate = None
                count -= 1
            elif n != candidate:
                count -= 1
        return candidate

if __name__=='__main__':
    t1=[1,2,1,1,1,3,5]
    t2=[1,2,3,5,7,9,4,4,4,4,4,4,4,4]
    t3=[1]
    tt=[t1,t2,t3]
    for t in tt:
	print Solution().majorityElement(t)
