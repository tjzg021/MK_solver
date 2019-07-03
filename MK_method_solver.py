# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 22:37:58 2019

@author: tjzg
"""
import random


class Family:
    Fid = 0
    NonAccess = []
    AccessHistory = {}
    NonAccessHistory = {}
    AtHome = 0
    
    def __init__(self, FamilyId, TotalFamilyNum):
        self.Fid = FamilyId
        self.AtHome = 0
        self.AccessHistory = {}
        self.NonAccessHistory = {}
        self.NonAccess = [i for i in range(1, TotalFamilyNum+1)]
        self.NonAccess.pop(FamilyId-1)
        
    def FamilyID(self):
        print("Family ID: %d" %(self.Fid))
        
    def GetNonAccess(self):
        print("Family ID: %d" %(self.Fid))
        print("Non-access family ID:\n", self.NonAccess)
        
    def GetHistory(self):
        print("Family ID: %d" %(self.Fid))
        print("Access history:\n", self.AccessHistory)
        print("NonAccess history:\n", self.NonAccessHistory)
     
def random_index(rate):
    # """随机变量的概率函数"""
    # 参数rate为list<int>
    # 返回概率事件的下标索引
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))
    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index

       
def OneNight(F, NightNum, TotalFamily):
    AtHomeList = []
    for i in range(0, TotalFamily):
        #F[i].AtHome = random.randint(0,1)
        F[i].AtHome = random_index([80,10])
        if F[i].AtHome == 1:
            AtHomeList.append(F[i].Fid)
    #print("AtHomeList: \n", AtHomeList)
        
    for i in range(0, TotalFamily):
        F[i].AccessHistory[NightNum] = []
        F[i].NonAccessHistory[NightNum] = []
        if F[i].AtHome == 0:
            F[i].AccessHistory[NightNum].append(AtHomeList)
            F[i].NonAccess = list( set(F[i].NonAccess) - set(AtHomeList) )
            F[i].NonAccessHistory[NightNum].append(F[i].NonAccess)
        else:
            F[i].AccessHistory[NightNum].append([0])
            F[i].NonAccessHistory[NightNum].append(['athome'])
            
def CheckResult(F, NightNum, TotalFamily, min_NightNum):
    for i in range(0, TotalFamily):
        if len(F[i].NonAccess) > 0:
            #F[i].GetNonAccess
            #F[i].FamilyID
            #print("Family ID: %d" %(F[i].Fid))
            return 1,min_NightNum
   
    min_NightNum = NightNum
    print("Night Number %d \n" %(NightNum))
    print("Access history:\n")
    for i in range(0, TotalFamily):
        F[i].GetHistory()
    return 0,min_NightNum



TotalFamily = 30
min_NightNum = 15
Final = []
for n in range(1,50000): 
    F = []
    ifcontinue = 1
    #print("Iteration: %d\n" %n)
    
    for i in range(0,TotalFamily):
        F.append( Family(i+1, TotalFamily) )
        #F[i].FamilyID()
        #F[i].GetNonAccess()
        
    for NightNum in range(1, min_NightNum):
        OneNight(F, NightNum, TotalFamily)
        #print("night: %d\n" %NightNum)
        ifcontinue,min_NightNum = CheckResult(F, NightNum, TotalFamily, min_NightNum)
        #print("ifcontinue: %d\n" %ifcontinue)
        if ifcontinue == 0:
            Final = F
            break
if min_NightNum < 10:
    print("Final Night Number %d \n" %(min_NightNum))
    print("Final Access history:\n")
    for i in range(0, TotalFamily):
        Final[i].GetHistory()
    
    
