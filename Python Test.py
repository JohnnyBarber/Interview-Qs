# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:36:44 2019

@author: Jiaqi Li
"""

import numpy as np
import pandas as pd

class TaskScheduler(object):    
    def __init__(self,namelist = pd.DataFrame(columns = ['name','type','task']), tasklist = pd.DataFrame(columns = ['type','id','priority'])):
        self.namelist = namelist
        self.tasklist = tasklist
        
    def insertAnalyst(self,Analyst,Type):
        try:
            assert isinstance(Analyst,str) == True
            assert isinstance(Type,str) == True
        except AssertionError:
            print('Analyst names/task type is not recognized')
        
        if self.namelist.name.str.match(Analyst).tolist() == []:
            self.namelist = self.namelist.append({'name':Analyst,'type':Type,'task':{}},ignore_index = True)
        elif True not in self.namelist.name.str.match(Analyst).tolist():
            self.namelist = self.namelist.append({'name':Analyst,'type':Type,'task':{}},ignore_index = True)
        else:
            print('Analyst already exist, do you want to modify his/her task type? Enter Y/N: ')
            cond = input()
            if cond == 'Y':
                Index = self.namelist.index[self.namelist.name.str.match(Analyst)].tolist()[0]
                self.namelist.iloc[Index].type = Type
            else:
                return None
        return self.namelist
        
    def insertTask(self, ID, Type, Priority):
        try:
            assert isinstance(Type,str) == True
            assert isinstance(ID,str) == True
            assert isinstance(Priority,str) == True
        except AssertionError:
            print('Task type/ID/Priority is not recognized')
        
        if self.tasklist.id.str.match(ID).tolist() == []:
            self.tasklist = self.tasklist.append({'type':Type,'id':ID,'priority':Priority},ignore_index = True)
        elif True not in self.tasklist.id.str.match(ID).tolist():
            self.tasklist = self.tasklist.append({'type':Type,'id':ID,'priority':Priority},ignore_index = True)
        else:
            print('Task ID already exist, do you want to modify this task? Enter Y/N: ')
            cond = input()
            if cond == 'Y':
                Index = self.tasklist.index[self.tasklist.id.str.match(ID)].tolist()[0]
                self.tasklist.iloc[Index].type = Type
                self.tasklist.iloc[Index].priority = Priority
            else:
                return None
        return self.tasklist
        
#        if Task_Type in self.namelist.type.tolist():
#            Assign(Task_Type, Task_ID, Task_Priority)
#        else:
#            print('Task type does not match any analyst preference')
#        return self.namelist
    
    def Assign(self,ID):
        available = self.tasklist.index[self.tasklist.id.str.match(ID)].tolist()
        marker = 0
        if available == []:
            print('No task found for the id number')
            return self.tasklist
        elif available != []:
            Ready = self.tasklist.iloc[available].type.tolist()[0]
            OnBoard = self.namelist.index[self.namelist.type.str.match(Ready)].tolist()
            go = available[0]
            for i in OnBoard:
                if self.namelist.iloc[i].task == {}:
                    self.namelist.iloc[i].task = {'ID':self.tasklist.iloc[go].id, 'Priority':self.tasklist.iloc[go].priority}
                    self.tasklist = self.tasklist.drop(go)
                    marker = 1
                    break
            return self.namelist
        elif marker == 0:
            print('No analyst currently available for this type of task')
            return self.namelist
        return None

# =============================================================================
# Run Now
# =============================================================================
Test = TaskScheduler()
Test.insertAnalyst('Jiaqi','T1')
Test.insertAnalyst('Jiaqi','T2')
Test.insertTask('A123','T2','Low')
Test.insertTask('A123','T2','High')
Test.Assign('A123')
Test.insertAnalyst('Xiangui','T1')
Test.insertTask('B123','T1','High')
Test.Assign('B123')
Test.Assign('KKK')
