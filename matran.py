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
        self.hang = 3
        self.cot = 6
        self.matrix_full.append([0, -3, 6, -6, -4, 5])
        self.matrix_full.append([-3, 9, -12, 9, -6, -15])
        self.matrix_full.append([-3, 7, -8, 5, -8, -9])
        self.matrix_origin = self.matrix_full

    def print_matrix(self):
         for hangi in self.matrix_full:
              print(hangi)

    def get_cot(self, chiso_cot):       
        cotj = []
        if chiso_cot >= self.cot:
            print('khong the lay cot %d' %chiso_cot)
            return cotj
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
    def length_arr(self, arr):
         len = 0
         for i in arr:
              len = len + 1
         return len
    def check_khackhong(self, i_moc, cotj):
        for i_check in range(i_moc, self.length_arr(cotj)):
            if cotj[i_check] !=0:
                print(cotj[i_check])
                return i_check
        return None
    def find_phantumoc(self, i_moc, j_moc):
        while(True):
            # cuoi hang thi dung
            if(j_moc >= self.cot or i_moc >= self.hang):
                    print('hang hoac cot lon hon kich thuoc ma tran %d %d' %(i_moc, j_moc))
                    break                
            cotj = self.get_cot(j_moc)
            # xet diem moc khac 0
            i_moc_check = self.check_khackhong(i_moc, cotj)
            # neu co 1 vi tri khac 0 trong cot thi swap vi tri khac 0 gan nhat len hang dau 
            # neu cot tại diem moc toan 0 thi xe cot tiep theo ben phai           
            if(i_moc_check is not None):
                if(i_moc == i_moc_check):
                     break
                
                print('i moc la %d, i moc check la %d' %(i_moc, i_moc_check))
                self.swap_hang(i_moc, i_moc_check)                   
                break
            else:                               
                j_moc = j_moc + 1
        return j_moc
    
    def ucln(self, a, b): 
        if b == 0: 
            return a
        return self.ucln(b, a%b)
    def bcnn(self, a, b): 
        return int((a*b)/self.ucln(a,b))
    def biendoi_hang_0(self, i_moc, i_moc_temp, boiso_hang_moc, boiso_hang_moc_temp):
         for j in range(self.cot):
              self.matrix_full[i_moc_temp][j] = self.matrix_full[i_moc_temp][j]*boiso_hang_moc_temp -self.matrix_full[i_moc][j]*boiso_hang_moc
         return
    def biendoi_cot0(self, i_moc, j_moc):
        # xet i, j 
        if(j_moc >= self.cot or i_moc >= self.hang):
                    print('hang hoac cot lon hon kich thuoc ma tran %d %d' %(i_moc, j_moc))
                    return
        
        if(i_moc == self.hang - 1):
             return
        
        cotj = self.get_cot(j_moc)

        for i_moc_temp in range(i_moc+1, self.hang):
             if(cotj[i_moc_temp]==0):
                  continue            
             boiso = self.bcnn(cotj[i_moc],cotj[i_moc_temp])
             boiso_hang_moc = boiso / cotj[i_moc]
             boiso_hang_moc_temp = boiso / cotj[i_moc_temp]
             self.biendoi_hang_0(i_moc, i_moc_temp, boiso_hang_moc, boiso_hang_moc_temp)
        return
    def biendoi_bacthang(self):
        j_moc = 0
        for i_moc in range(self.hang):
            # tim phan tu moc khac 0
            j_moc_check = self.find_phantumoc(i_moc, j_moc)
            # bien doi hang khac 0 
            self.biendoi_cot0(i_moc, j_moc_check)
            print('phan tu moc aij la A(%d, %d) '  %(i_moc,j_moc))   
            self.print_matrix()
            j_moc = j_moc + 1

    def biendoi_khunnguoc_hang_0(self, i_moc, i_moc_temp, boiso_hang_moc, boiso_hang_moc_temp):
         for j in range(self.cot):
              self.matrix_full[i_moc_temp][j] = self.matrix_full[i_moc_temp][j]*boiso_hang_moc_temp -self.matrix_full[i_moc][j]*boiso_hang_moc
         return
    def biendoi_cot0_khunguoc(self, i_moc_nguoc, j_moc_check):
        # xet i, j 
        if(j_moc_check >= self.cot or i_moc_nguoc >= self.hang):
                    print('hang hoac cot lon hon kich thuoc ma tran %d %d' %(i_moc_nguoc, j_moc_check))
                    return       
        if(i_moc_nguoc == 0):
             return       
        cotj = self.get_cot(j_moc_check)
        for i_moc_nguoc_temp in range(0, i_moc_nguoc):
             if(cotj[i_moc_nguoc_temp]==0):
                  continue            
             boiso = self.bcnn(cotj[i_moc_nguoc],cotj[i_moc_nguoc_temp])
             boiso_hang_moc_nguoc = boiso / cotj[i_moc_nguoc]
             boiso_hang_moc_nguoc_temp = boiso / cotj[i_moc_nguoc_temp]
             self.biendoi_khunnguoc_hang_0(i_moc_nguoc, i_moc_nguoc_temp, boiso_hang_moc_nguoc, boiso_hang_moc_nguoc_temp)
        return
    def khunguoc_bacthang(self):

        for i_moc in range(self.hang):
            i_moc_nguoc = self.hang - 1 -i_moc
            # tim phan tu moc khac 0
            j_moc_check = self.find_phantumoc(i_moc_nguoc, 0)
            # bien doi hang khac 0 
            self.biendoi_cot0_khunguoc(i_moc_nguoc, j_moc_check)
            print('phan tu moc aij la A(%d, %d) '  %(i_moc_nguoc,j_moc_check))   
            self.print_matrix()


    def biendoi_tilephantumoc(self, i_moc, j_moc_check, boiso):
         j = 0
         for aij in self.matrix_full[i_moc]: 
              self.matrix_full[i_moc][j] = aij/boiso
              j = j + 1
         return    
    def biendoi_phantucoso(self):
            j_moc = 0
            for i_moc in range(self.hang):
                # tim phan tu moc khac 0
                j_moc_check = self.find_phantumoc(i_moc, j_moc)
                boiso = self.matrix_full[i_moc][j_moc_check]
                self.biendoi_tilephantumoc(i_moc, j_moc_check, boiso)
                print('phan tu moc aij la A(%d, %d) '  %(i_moc,j_moc))   
                self.print_matrix()
                j_moc = j_moc + 1       
# main 
# n = int(input('nhap so cot'))
# m = int(input('nhap so hang'))
m = 3
n = 4
matrix = MaTran(m,n)
matrix.print_matrix()
print('bien doi bac thang--------------------------------')
matrix.biendoi_bacthang()
print('khu nguoc bac thang-------------------------------')
matrix.khunguoc_bacthang()
print('giam he so----------------------------------------')
matrix.biendoi_phantucoso()

# ----------------------------------------------------
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
# def tong(i,j):
#     i = i +1
#     j = j +1
#     return (i,j)
# arr = tong(2,5)
# print(arr[1])

# Example usage
# print(matrix.matrix_full[1][3])

# def ucln( a, b): 
#         if b == 0: 
#             return a
#         return ucln(b, a%b)
# def bcnn( a, b): 
#     return int((a*b)/ucln(a,b))
# a = 4/3
# b = 1.0
# print(bcnn(a,b))
# a1 = bcnn(a,b)/a
# b1 = bcnn(a,b)/b
# print(a*a1-b*b1)
