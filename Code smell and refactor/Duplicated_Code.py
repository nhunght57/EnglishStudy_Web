__author__ = 'Nam Xuan'

class Sequence_Number:
    def Soft(self,array):
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

    def Three_King(self):
        array = [0,2,5,1,4,3,10,6]
        array = self.Soft(array)

        print('Three king: ', array[0], ' ' , array[1] , ' ' , array[2] )


    def Four_King(self):
         array = [0,2,5,1,4,3,10,6]
         array = self.Soft(array)

         print('Four king: ', array[0], ' ' , array[1] , ' ' , array[2] , ' ' , array[3])


d = Sequence_Number()
d.Three_King()
d.Four_King()


