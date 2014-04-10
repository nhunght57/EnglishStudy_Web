__author__ = 'Nam Xuan'

class Sequence_Number:

    def sx(self,array):
        index1 = 0
        while index1<len(array)-1:
            index2 = index1 + 1
            while index2 < len(array):
                if array[index1] <array[index2]:
                    temp = array[index1]
                    array[index1] = array[index2]
                    array[index2] = temp
                index2 = index2 + 1
            index1 = index1 + 1
        return array

    def f(self):
        array = [0,2,5,1,4,3,10,6]
        array = self.sx(array)

        print('The smallest and biggest number: ', array[0], ' ',  array[len(array)-1] )





d = Sequence_Number()
d.f()


