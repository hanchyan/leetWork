class Test(object):
    def myFunciton(self, list):
        rlist = []
        listofLists = []
        indexList = []
        pairs = []
        # below is the boilerplate for avoiding the out of index error, the -1. this apparently always works 
        for i in range(len(list) -1):
            num = list[i]
            # the print command below prints the index of the minuend
            # print(i, end='*')
            # below appends the index of the number being subtracted from (also see line 25)
            pairs.append(str(i) + "*")
            while i < len(list) -1:
                i = i +1
                result = num -list[i]
                minuend = i
                subtrahend = i
                # print(minuend, end='*')
                # print(subtrahend, end='@')
                # print(pairs)
                rlist.append(result)
                indexList.append(minuend)
                indexList.append(subtrahend)
                # below appends the endex of the different numbers being subtracted
                # below appends the index of the value being subtracted
                pairs.append(i)
                # below appends the value of the number being subtracted
                pairs.append(list[i])

                # at this point it will loop through and print out all the correct numbers for the subtractions
                # now i need to write something to determine the lowest negative number which is one step in determining the answer
                # but more difficult, i need to trace back from there to determine what the purchase sale date pair... 
                # it should be a unique pair (or even if their are duplicates, the result would be the same) so one possibility is 
                # finding what pair of numbers subtracted produces that unique result... 
                # print(result, end= ',')
                # print(indexList)
                # print(plist)
        print(pairs)
        print(rlist)


t = Test()
t.myFunciton([1,5,2,5,3,6,6,2,8])



# first step is to make a sorting algorithm that determines the lowest number 

# i can sort the list 
# then take the top result and search the original list to find the index
# after i find the index... how can i use that to trace back to the two originals numbers and their indexes that 
# gave rise to it? 


