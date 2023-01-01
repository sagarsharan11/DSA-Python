## Time Complexity: O(nlogn)
class mergeSort:

    def divide(self, lst, si, ei):
        ## O(logn)
        if si >= ei:
            return
        # mid = int(si + (si - ei)/2) ### (si + ei)/2
        mid = len(lst) //2
        self.divide(lst, si, mid)
        self.divide(lst, mid+1, ei)
        self.conquer(lst, si, mid, ei)


    def conquer(self, lst, si, mid, ei):
        merged = []
        idx1 = si
        idx2 = mid + 1
        x = 0
        
        ## O(n)
        while (idx1 <= mid & idx2  <= ei):
            if lst[idx1] <= lst[idx2]:
                merged[x] = lst[idx1]
                x+=1
                idx1+=1
            else:
                merged[x] = lst[idx2]
                x+=1
                idx2+=1
        
        while idx1 <= mid:
            merged[x] = lst[idx1]
            x+=1
            idx1+=1

        while idx2 <= ei:
            merged[x] = lst[idx2]
            x+=1
            idx2+=1

        j = si
        for i in range(len(merged)):
            lst[j] = merged[i]
            j+=1

if __name__ == '__main__':
    lst = [6,3,9,5,2,8]
    n = len(lst)

    ms = mergeSort()
    print(ms.divide(lst=lst, si=0, ei=n-1))