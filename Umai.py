import numpy as np
import cv2
import math

class Gravity:
    def __init__(self,Rx = 500 ,Ry = 500) -> None:
        self.Lit = []
        self.Gra = []   
        self.rx = Rx
        self.ry = Ry
        self.rSeta = 0

    def Gravity(self,m1,m2,r,G = 6.673 ):
        try:
            Gp = G*((m1*m2)/(r**2))
        except:
            Gp = 0
        return Gp

    def Motion_s(self):
        self.Fild = self.cov.copy()
        for n in self.Lit:
            axis = n[3]
            self.Pick([axis[0]+self.ry,axis[1]+self.rx],n[2], n[5])

    def sets(self, M, r, Name = "Dokdo",axis = [0,0],color = [0,0,255], Move = "N"):
        for i in self.Lit:
            if i[0] == Name:
                print("이름이 같습니다.")
                raise
                exit()
                break
        
        self.Lit.append([Name,M,r,[axis[0]-self.ry,axis[1]-self.rx],0,color,Move])
        
        self.Pick(axis,r,color)

    def Calculation_G(self, motion = False):
        lethi = []
        for n in self.Lit:
            ap = n[3]
            L3 = []
            al = []
            for i in self.Lit:
                if n[0] != i[0]:
                    al.append(i[3])
                    y = i[3][0] - ap[0]
                    x = i[3][1] - ap[1]
                    Squid = math.sqrt((x*x)+(y*y))
                    Seta = math.atan2(y,x)*(180/math.pi)*-1  + (0)
                    # self.Drow(i,Seta, 50)
                    # self.Drow(i,Seta, self.Gravity(n[1],i[1],Squid))
                    L3.append([Seta,self.Gravity(n[1],i[1],Squid),i])
                    #print(np.arctan2(x,y)*(180/np.pi))

            x = 0
            y = 0
            for L2 in L3:
                x += L2[1]*math.cos(math.radians(L2[0])) 
                y += L2[1]*math.sin(math.radians(L2[0]))
            
            Sert = math.atan2(y,x)*(180/math.pi) + (90)
            pick = math.sqrt((x**2)+(y**2))*0.05
            axio = n[3]
            #print(axio)
            a = self.Drow__(axio,Sert,pick)
            # print(a)
            if n[6] == "Y":
                lethi.append([n[0],n[1],n[2],n[3],n[4],n[5],n[6]])
            else:
                lethi.append([n[0],n[1],n[2],a,n[4],n[5],n[6]])
            #print(x, "::" ,y)
        self.Lit = lethi
        print("a")
        # self.Boom()
        cv2.imshow("ll", self.Fild)
        cv2.waitKey(10)

    def Boom(self):
        for i in (self.Lit):
            # print(self.Lit)
            # print(i)
            axis = i[3]
            # print(axis)
            size = i[2]
            for l in range(2):
                for ip in range(360):
                    rad = np.radians(ip)
                    x = int(axis[1]+size*math.cos(rad))
                    y = int(axis[0]+size*math.sin(rad))
                    # print([axis[0]+y,axis[1]+x])
                    A = self.Fild[axis[0],axis[1]]
                    # print(A)
                    if A[0] != 0 and A[1] != 0 and A[2] != 0:
                        print("kiki")

    def Drow(self, L1,Seta, Lagrangu):
        # print(Lagrangu)
        for i in range(round(Lagrangu)):
            coss = int(i * math.sin(math.radians(Seta + L1[4])) + L1[3][1] + self.rx)
            sins = int(i * math.cos(math.radians(Seta + L1[4])) + L1[3][0] + self.ry)
            
            try:                   
                if coss < 0 or coss > 999:
                    # print("err60")
                    pass
                elif sins < 0 or sins > 999:
                    pass
                else:
                    self.Fild[sins,coss] = [10,10,10]
            
            except:
                pass    

    def Drow__(self, R,Seta, Lagrangu):
        for i in range(round(Lagrangu)):
            coss = int(i * math.sin(math.radians(Seta)) + R[1] + self.rx)
            sins = int(i * math.cos(math.radians(Seta)) + R[0] + self.ry)
            try:
                
                self.px = coss - self.ry
                self.py = sins - self.rx

                if coss < 0 or coss > 999:
                    # print("err60")
                    pass
                elif sins < 0 or sins > 999:
                    # print("err40")
                    pass
                else:
                    self.Fild[sins,coss] = [100,0,100]
                
                # print(coss , "::" , sins)

            except:
                pass            
        try:
            # print(self.py,self.px)
            self.Saves = [self.py,self.px]
            return [self.py,self.px]
        except:
            return R[0] + self.ry,R[1] + self.rx

    def Pick(self,axis, r, color = [0,0,255]):
        for i in range(r-1):
            i += 1
            for ip in range(360):
                rad = math.radians(ip)
                x = int(i*math.cos(rad))
                y = int(i*math.sin(rad))
                
                y = axis[0]+y
                x = axis[1]+x
                #print([axis[0]+y,axis[1]+x])
                try:
                    if x < 0 or x > 999:
                        # print("err60")
                        raise
                    if y < 0 or y > 999:
                        # print("err40")
                        raise
                    self.Fild[y,x] = color
                except:
                    pass
                    # print("err")

    def Base_(self, Size = [1000,1000]):
        self.Fild = np.zeros([Size[0],Size[1],3])
        self.cov = self.Fild.copy()

def rand_ty():
    a = np.random.randint(0,600)
    b = np.random.randint(0,600)
    #print(a," :: ",b)
    return[a+200,b+200] 

for i in range(1):
    a = Gravity()
    a.Base_([1000,1000])
    a.sets(99900,15,"gidi1", [500,500], color=[0,255,100], Move= "N")
    a.sets(91,10,"gidi2", [400,600])
    a.sets(19,10,"gidi3", [400,500])
    a.sets(15,10,"gidi4", [500,400])
    a.sets(25,10,"gidi4_", [500,600])

    for i in range(5):
        a.sets(90,10,"gidi4%d" %i, rand_ty())
    for i in range(100000000000000000000000000000):
        a.Calculation_G()
        a.Motion_s()
    # a.Calculation_G()