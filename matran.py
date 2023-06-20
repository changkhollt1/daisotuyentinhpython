import array as arr 
class MaTran:
    def __init__(self, m, n, r = -1):
        self.hang = m
        self.cot = n
        self.rank = r
        self.matrix_full = []
        # for i in range(0,m):
        #     hang = []
        #     for j in range(0,n):
        #         hang.append(int(input('nhap phan tu thu %d cua hang %d: '%(j,i))))
        #     self.matrix_full.append(hang)
        self.matrix_full.append([0, 0, 0, 6])
        self.matrix_full.append([5, 8, 3, 5])
        self.matrix_full.append([0, 1, 4, 9])

        self.matrix_origin = self.matrix_full

    def get_cot(self, chiso_cot):
        cotj = []
        for hangi in self.matrix_full:
            cotj.append(hangi[chiso_cot])
        return cotj 
    def set_cot(self, chiso_cot, cotj):
        for hangi in self.matrix_full:
            hangi[chiso_cot] = cotj[self.matrix_full.index(hangi)]
    def swap_hang(self, chiso_hang1, chiso_hang2):
        temp = self.matrix_full[chiso_hang1]
        self.matrix_full[chiso_hang1] = self.matrix_full[chiso_hang2]
        self.matrix_full[chiso_hang2] = temp
    # def check_bien_chinh(self, chiso_cot):
    #     cotj = self.get_cot(chiso_cot)
    #     for aij in cotj:
    #         if aij == 1 or aij == -1:
    #             print('phan tu chinh: %d tai vi tri A(%d,%d)' %(aij,cotj.index(aij), chiso_cot ))
    #             return aij
    # def duyet_matrix(self):
    #     for cotj in range(self.cot):
    #         self.check_bien_chinh(cotj)
    def check_khackhong(self, arr):
        for aij_check in arr:
            if aij_check !=0:
                print(aij_check)
                return aij_check
        return None
    def biendoi_bacthang(self):
        j = 0
        for i in range(self.hang):
            # hoan vi hang khac 0 
            while(True):
                print('j la %d, i la %d'  %(j,i))
                cotj = self.get_cot(j)
                # xet diem moc khac 0
                i_moc_value = self.check_khackhong(cotj[i:])
                
                if(i_moc_value is not None):
                    self.swap_hang(i,cotj.index(i_moc_value))                   
                    break               
                else: 
                    if(j >= self.cot):
                        break
                    j = j + 1
                
            j = j + 1          
# main 
# n = int(input('nhap so cot'))
# m = int(input('nhap so hang'))
m = 3
n = 4
matrix = MaTran(m,n)
print(matrix.matrix_full)
matrix.biendoi_bacthang()
print(matrix.matrix_full)
# arr = [1,1,3,0, 1, 1,2]
# print(arr[2:])
# def test(i, arr):
#     for a in arr[i:]:
#         if a == 0:
#             return a
#     return None
# a = test(2, arr)
# if a is None: 
#     print('ko co so ko nao')