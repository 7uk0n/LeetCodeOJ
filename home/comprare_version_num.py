# issue Compare Version Numbers 

class Solution:

    # @param version1, a string

    # @param version2, a string

    # @return an integer

    def compareVersion(self, version1, version2):

        def removeTailZero(v_list):

            for i in xrange(len(v_list)-1,-1,-1):

                if int(v_list[i])!=0:

                    break

                del v_list[i]

        v1 = version1.split('.')

        v2 = version2.split('.')

        removeTailZero(v1)

        removeTailZero(v2)

        length = min(len(v1),len(v2))

        for i in range(length):

            f1 = int(v1[i])

            f2 = int(v2[i])

            if f1 > f2:

                return 1

            elif f2 > f1:

                return -1

        if len(v1) > len(v2):

            return 1

        elif len(v2) > len(v1):

            return -1

        return 0
