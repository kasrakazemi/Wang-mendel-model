import random as rnd
import prettytable as prettytable
import plotly.graph_objects as go

POPULATION_SIZE = 12
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
Crossover_rate= 0.4
MUTATION_RATE = 0.1

import tkinter as tk
root = tk.Tk()
root.title("برنامه ریزی هفتگی")
# global rooms, times, prof
# rooms, times, prof = 0,0,0
############################

############################
label_01 = tk.Label(root,text="Class size:",width = 20)
label_01.grid(row=0,column=0)

entry_0 = tk.Entry(root,width = 80)
entry_0.grid(row=0,column=1)

label_02 = tk.Label(root,text="Enter the size like: class1,30, ...",width=30,height=2)
label_02.grid(row=0,column=2)

###########################
label_11 = tk.Label(root,text="Class time:",width = 20)
label_11.grid(row=1,column=0)

entry_1 = tk.Entry(root,width = 80)
entry_1.grid(row=1,column=1)

label_12 = tk.Label(root,text="Enter the time like: time1,MWF 08:00 - 10:00, ...",width=40,height=2)
label_12.grid(row=1,column=2)

###########################
label_21 = tk.Label(root,text="Professor:",width = 20)
label_21.grid(row=2,column=0)

entry_2 = tk.Entry(root,width = 80)
entry_2.grid(row=2,column=1)

label_22 = tk.Label(root,text="Enter the prof like: p1, name, ...",width=40,height=2)
label_22.grid(row=2,column=2)

###########################
label_31 = tk.Label(root,text="Course:",width = 20)
label_31.grid(row=3,column=0)

entry_3 = tk.Entry(root,width = 80)
entry_3.grid(row=3,column=1)

label_32 = tk.Label(root,text="Enter the course like: 'course#','name',prof#,size#,...",width=40,height=2)
label_32.grid(row=3,column=2)

###########################
label_41 = tk.Label(root,text="Soft Constraint:",width = 20)
label_41.grid(row=4,column=0)

entry_4 = tk.Entry(root,width = 80)
entry_4.grid(row=4,column=1)

label_42 = tk.Label(root,text="Enter Soft Constraint like: Prof name , time1 ,...",width=40,height=2)
label_42.grid(row=4,column=2)
###########################

def createNestedList(listt):
    out_list=[]
    movaghat=[]
    for  i in range(len(listt)):
        movaghat.append(listt[i])
        if len(movaghat)==2:
            out_list.append(movaghat)
            movaghat=[]
    return out_list



def addData():
     global rooms,times,prof,crs,sc
     rooms = entry_0.get()
     rooms = createNestedList(rooms.split(","))
     rooms = [[lst[0], int(lst[1])] for lst in rooms]
    ###########
     times = entry_1.get()
     times = createNestedList(times.split(","))
    ###########
     prof1 = entry_2.get()
     prof = createNestedList(prof1.split(","))
     ###########
     crs1 = entry_3.get()
     crs = crs1
     ###########
     sc1 = entry_4.get()
     sc = createNestedList(sc1.split(","))


     root.destroy()




def clear():
    entry_0.delete(0, tk.END)
    entry_1.delete(0,tk.END)
    entry_2.delete(0,tk.END)
    entry_3.delete(0, tk.END)



#############################
btn_Run = tk.Button(root,text="generate",command=addData)
btn_Run.grid(row=5,column=1)
#############################
btn_Run = tk.Button(root,text="clear ",command=clear)
btn_Run.grid(row=5,column=0)



root.mainloop()


# print(f">>prof>{prof}")
# def createCourseNestedList(listt):
#     out_list = []
#     movaghat = []
#     for i in range(len(listt)):
#         movaghat.append(listt[i])
#         if type(movaghat[-1]) == int and (movaghat[-1] / 2) > 5:
#             out_list.append(movaghat)
#             if len(movaghat) == 4:
#                 print(f"1 >>>{movaghat}")
#                 movaghat[2] = [prof[int(movaghat[2]) - 1]]
#             if len(movaghat) == 5:
#                 print(f"2 >>>{movaghat}")
#                 movaghat[2] = [prof[int(movaghat[2]) - 1]] + [prof[int(movaghat[3]) - 1]]
#                 del movaghat[3]
#             movaghat = []
#     return out_list
# print(f">>>crs>>>{crs}")
# # print(f">>crssplt>>{[crs.split('','')]}")
# global crs1
# crs1 = createCourseNestedList([crs.split(",")])
# print(f">>crs1>>>>{crs1}")

class Data:
    # Rooms = [["R1",25],["R2",45],["R3",35]]
    # MEETING_TIMES = [["MT1","MWF 09:00 - 10:30"],
    #                  ["MT2","MWF 10:00 - 11:00"],
    #                  ["MT3","TTH 09:00 - 10:45"],
    #                  ["MT4","TTH 10:30 - 12:00"],
    #                  ["MT5","MWF 19:00 - 20:30"]]
    #
    # INSTRUCTORS = [["I1","Dr Afsari"],
    #                ["I2","Dr Eftekhari"],
    #                ["I3","Dr Nik nafs"],
    #                ["I4","Dr Mohseni"]]
    Rooms = rooms
    MEETING_TIMES = times
    INSTRUCTORS = prof
    def __init__(self):
        self._rooms = []; self._meetingTimes = [] ; self._instructors = []
        for i in range(0,len(self.Rooms)):
            self._rooms.append(Room(self.Rooms[i][0],self.Rooms[i][1]))
        for i in range(0,len(self.MEETING_TIMES)):
            self._meetingTimes.append(MeetingTime(self.MEETING_TIMES[i][0],self.MEETING_TIMES[i][1]))
        for i in range(0,len(self.INSTRUCTORS)):
            self._instructors.append(Instructor(self.INSTRUCTORS[i][0],self.INSTRUCTORS[i][1]))
        #     print(f">>id>>{self.INSTRUCTORS[i][0]}")
        #     print(f">>name>>{self.INSTRUCTORS[i][1]}")
        # print(f">>INSTructor>>{self._instructors[0]}")
        # print([self._instructors[0],self._instructors[1]])
        # print("@@@")
        ins = self._instructors
        print(f">>>>INS>>{ins}")
        # course1 = Course("C1" , "325K" , [self._instructors[0],self._instructors[1]],25)
        # course2 = Course("C2" , "319K" , [self._instructors[0],self._instructors[1],self._instructors[2]],35)
        # course3 = Course("C3" , "462k" , [self._instructors[0],self._instructors[1]],25)
        # course4 = Course("C4" , "464K" , [self._instructors[2],self._instructors[3]],30)
        # course5 = Course("C5", "360C", [self._instructors[3]],35)
        # course6 = Course("C6", "303K", [self._instructors[0], self._instructors[2]], 45)
        # course7 = Course("C7", "303L", [self._instructors[1], self._instructors[3]], 45)
        ##############################
        def createCourseNestedList(listt):
            out_list = []
            movaghat = []
            for i in range(len(listt)):
                movaghat.append(listt[i])
                if type(movaghat[-1]) == int and (movaghat[-1] / 2) > 5:
                    out_list.append(movaghat)
                    if len(movaghat) == 4:
                        print(f"1 >>>{movaghat}")
                        # movaghat[2] = [prof[int(movaghat[2]) - 1][1]]
                        # movaghat[0] = str(movaghat[0])
                        # movaghat[1] = str(movaghat[1])
                        movaghat[2] = [ins[int(movaghat[2]) - 1]]
                        print(f"1 >>>{movaghat}")
                    if len(movaghat) == 5:
                        print(f"2 >>>{movaghat}")
                        # movaghat[2] = [prof[int(movaghat[2]) - 1][1]] + [prof[int(movaghat[3]) - 1][1]]
                        movaghat[2] = [ins[int(movaghat[2]) - 1] , ins[int(movaghat[3]) - 1]]
                        del movaghat[3]
                        print(f"2 >>>{movaghat}")
                    if  len(movaghat) == 6:
                       print(f"3 >>>{movaghat}")
                       movaghat[2] = [ins[int(movaghat[2]) - 1] , ins[int(movaghat[3]) - 1],ins[int(movaghat[3]) - 1]]
                       del movaghat[3]
                       del movaghat[4]
                    if len(movaghat) == 7:
                       movaghat[2] = [ins[int(movaghat[2]) - 1], ins[int(movaghat[3]) - 1], ins[int(movaghat[3]) - 1],ins[int(movaghat[4]) - 1]]
                       del movaghat[3]
                       del movaghat[4]
                       del movaghat[5]
                    movaghat = []
            return out_list

        from ast import literal_eval as make_tuple
        z = make_tuple(crs)
        xx = list(z)
        crss = createCourseNestedList(xx)
        ##############################

        # zzz = [['C1', '325K', [['I1', 'Dr Afsari'], ['I2', 'Dr Eftekhari']], 25], ['C2', '319K', [['I2', 'Dr Eftekhari'], ['I3', 'Dr Nik nafs']], 35], ['C3', '462k', [['I1', 'Dr Afsari'], ['I2', 'Dr Eftekhari']], 25], ['C4', '464K', [['I3', 'Dr Nik nafs'], ['I4', 'Dr Mohseni']], 30], ['C5', '360C', ['I4', 'Dr Mohseni'], 35], ['C6', '303K', [['I1', 'Dr Afsari'], ['I3', 'Dr Nik nafs']], 45], ['C7', '303L', [['I2', 'Dr Eftekhari'], ['I4', 'Dr Mohseni']], 45]]
        # bb = Course(crss[0][0],crss[0][1],crss[0][2],crss[0][3])
        # print(f">>B>>{bb}")
        x = []
        for i in range(len(crss)):
            # a,b,c,d = crs[i][0],crs[i][1],crs[i][2],crs[i][3]
            a, b, c, d = crss[i][0], crss[i][1], crss[i][2], crss[i][3]
            # print(f">>crs2>>{crss[i][2]}")
            x.append(Course(a,b,c,d))
            # print(f">>>A>>>{b}")
            # print(type(b))
            # print(f"<<>>{Course(a,b,c,d)}")
            # print(type(Course(a,b,c,d)))
        #
        self._courses = x
        #
        # print(f">>>X>>>>{x}")
        # print(f"@>>>>>>{crs}")
        # print(f"@>>>>>>{x}")

        # self._courses = [course1,course2,course3,course4,course5,course6,course7]

        # dept1 = Department("MATH" , [course1,course3])
        # dept2 = Department("EE" , [course2,course4,course5])
        # dept3 = Department("PHY" , [course6,course7])
        # self._depts = [dept1,dept2,dept3]
        # self._numberofClasses = 0
        # for i in range(0,len(self._depts)):
        #     self._numberofClasses += len(self._depts[i].get_courses())
    def get_rooms(self):
        return self._rooms
    def get_instructors(self):
        return self._instructors
    def get_courses(self):
        return self._courses
    # def get_depts(self):
    #     return self._depts
    def get_courses(self): # new def after delete dept
        return self._courses
    def get_meetingTimes(self):
        return self._meetingTimes
    # def get_numberofClasses(self):
    #     return self._numberofClasses

class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numbofConflicts_H = 0
        self._numbofConflicts_S = 0
        self.finall_numbofconlicts = 0
        self._fitness = 0
        self._classNumb = 0
        self._isFitnessChanged = True
    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes
    def get_numbofConflicts(self):
        return self.finall_numbofconlicts
    def get_fitness(self):
        if (self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):
        # new code after delete dept :
        courses = self._data.get_courses()
        # for i in range(0,len(depts)):
        # courses = depts[i].get_courses()
        for j in range(0, len(courses)):
            newClass = Class(self._classNumb, courses[j])
            self._classNumb += 1
            newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(0, len(data.get_meetingTimes()))])
            newClass.set_rooms(data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])
            newClass.set_instructor(courses[j].get_instructors()[rnd.randrange(0, len(courses[j].get_instructors()))])
            self._classes.append(newClass)
        return self

    def calculate_fitness(self):
        self._numbofConflicts_H = 0
        self._numbofConflicts_S = 0
        self.finall_numbofconlicts=0
        classes = self.get_classes()
        for i in range(0,len(classes)):
            if (classes[i].get_room().get_seatingCapacity() < classes[i].get_course().get_maxNumbofStudents() ):
                self._numbofConflicts_H += 1  # hard constraint now 1
            for j in range(0,len(classes)):
                if (j >= i):
                    if (classes[i].get_meetingTime() == classes[j].get_meetingTime() and
                        classes[i].get_id() != classes[j].get_id()):
                        if (classes[i].get_room() == classes[j].get_room()):
                            self._numbofConflicts_H += 1  # hard constraint now 2
                        if (classes[i].get_instructor() == classes[j].get_instructor()):
                            self._numbofConflicts_H += 1  # hard constraint now 3
            m1= classes[i].get_instructor()
            # if (str(classes[i].get_instructor())== "Dr Eftekhari" and  "MT2" == classes[i]._meetingTime.get_id()  ):
            if (str(classes[i].get_instructor()) == sc[0][0] and sc[0][1] == classes[i]._meetingTime.get_id()):
                 self._numbofConflicts_S+=1   # soft constraint now 1

            m2=  classes[i].get_meetingTime()

            # if (str(classes[i].get_instructor())== "Dr Afsari" and  "MT5"  ==  classes[i]._meetingTime.get_id() ):
            if (str(classes[i].get_instructor()) == sc[1][0] and sc[1][1] == classes[i]._meetingTime.get_id()):
                  self._numbofConflicts_S += 1  # soft constraint now 2

            if (str(classes[i].get_instructor())== sc[2][0] and sc[2][1] ==  str(classes[i]._room.get_number() )):
                  self._numbofConflicts_S += 1  # soft constraint now 3

        self.finall_numbofconlicts = (self._numbofConflicts_H*1)+(self._numbofConflicts_S*0.8)  # 0.8 and 1 are factors for soft and hard constranints

        # we have soft constranint now!!!
        return 1 / (self.finall_numbofconlicts + 1)# 1 to avoid divide by zero

    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes) -1):
            returnValue += str(self._classes[i]) + ", "
            returnValue += str(self._classes[len(self._classes)-1])
        return  returnValue



class Population:
    def __init__(self,size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0,size):
            self._schedules.append(Schedule().initialize())
    def get_schedules(self):
        return self._schedules




##########################################################################################
class GeneticAlgorithm:
    def evolve(self, population):
        return self.mutation(self.crossover(population))

    def crossover(self, pop):
        crossover_popu = Population(0)

        for i in range(POPULATION_SIZE ):
            crossover_popu.get_schedules().append(pop.get_schedules()[i])
            i = 0  # nothing is mysteries now !! dast dast !!
        while i < POPULATION_SIZE:
            crossoverShedule = Schedule().initialize()
            sci1 = self.selection(pop).get_schedules()[rnd.randrange(0, 3)]  # its random
            sci2 = self.selection(pop).get_schedules()[rnd.randrange(0, 3)]  # its random
            i += 1

            for i in range(0, len(crossoverShedule.get_classes())):
                if (rnd.random() < Crossover_rate):
                    crossoverShedule.get_classes()[i] = sci1.get_classes()[i]
                else:
                    crossoverShedule.get_classes()[i] = sci2.get_classes()[i]
                crossover_popu.get_schedules().append(crossoverShedule)

            return crossover_popu

    def selection(self, pop):
        out_selection = Population(0)
        for index in range(0, TOURNAMENT_SELECTION_SIZE):
            tournament_pop = Population(0)
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, 4)])
            tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
            out_selection.get_schedules().append(tournament_pop.get_schedules()[0])

        return out_selection

    # def mutation(self, pop):
    #     schedule = Schedule().initialize()
    #     for i in range(0, POPULATION_SIZE):
    #         self.muto = (pop.get_schedules()[i])
    #         for i in range(0, len(self.muto.get_classes())):
    #             if (MUTATION_RATE > rnd.random()):
    #                 self.muto.get_classes()[i] = schedule.get_classes()[i]

        # return pop
    def mutation(self,pop):
        schedule = Schedule().initialize()
        mutatation_pop= Population(0)
        for i in range(0,POPULATION_SIZE):
            self.muto= (pop.get_schedules()[i])
            for i in range(0, len(self.muto.get_classes())):
                if (MUTATION_RATE > rnd.random()):
                    self.muto.get_classes()[i] = schedule.get_classes()[i]
            mutatation_pop.get_schedules().append(self.muto)

        return mutatation_pop


#########################################################################
#done
class Course:
    def __init__(self,number, name , instructors, maxNumbofStudents):
        self._number = number
        self._name = name
        self._maxNumbofStudents = maxNumbofStudents
        self._instructors = instructors
    def get_number(self):
        return self._number
    def get_name(self):
        return self._name
    def get_instructors(self):
        return self._instructors
    def get_maxNumbofStudents(self):
        return self._maxNumbofStudents
    def __str__(self):
        return self._name

#done
class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def __str__(self):
        return self._name

#done
class Room:
    def __init__(self, number , seatingCapacity):
        self._number = number
        self._seatingCapacity = seatingCapacity
    def get_number(self):
        return self._number
    def get_seatingCapacity(self):
        return self._seatingCapacity

#done
class MeetingTime:
    def __init__(self, id, time):
        self._id = id
        self._time = time
    def get_id(self):
        return self._id
    def get_time(self):
        return self._time

#done
# class Department:
#     def __init__(self,name, courses):
#         self._name = name
#         self._courses = courses
#     def get_name(self):
#         return self._name
#     def get_courses(self):
#         return self._courses

class Class:
    #def __init__(self,id, dept , course):
    def __init__(self, id, course):
        self._id = id
        #self._dept = dept
        self._course = course
        self._instructors = None
        self._meetingTime = None
        self._room = None

    def get_id(self):
        return self._id
    # def get_dept(self):
    #     return self._dept
    def get_course(self):
        return self._course
    def get_instructor(self):
        return self._instructors
    def get_meetingTime(self):
        return self._meetingTime
    def get_room(self):
       return self._room
    def set_instructor(self, instructor):
        self._instructors = instructor
    def set_meetingTime(self,meetingTime):
        self._meetingTime = meetingTime
    def set_rooms(self,room):
       self._room = room

    def __str__(self):
        # return str(self._dept.get_name()) + "," + \
        #   print(f">>>get.id>>>{str(self._instructors.get_id())}")
          return str(self._course.get_number()) + "," + \
               str(self._room.get_number()) + "," + str(self._instructors.get_id()) + "," + \
               str(self._meetingTime.get_id())


class Table:
    def showData(self):
        self.dataTabel()

    def dataTabel(self):
        global c1, c2, c3, c4
        c1, c2, c3, c4 = [], [], [], []
        #Show Prof
        instructors = data.get_instructors()
        for i in range(0, len(instructors)):
            c1.append(instructors[i].get_id() + " - " + instructors[i].get_name())
        #Show Rooms
        rooms = data.get_rooms()
        for i in range(0, len(rooms)):
            c2.append(str(rooms[i].get_number()) + " (" + str(rooms[i].get_seatingCapacity()) + ")" )
        #Show Meeting times
        meetingTimes = data.get_meetingTimes()
        for i in range(0, len(meetingTimes)):
            c3.append(meetingTimes[i].get_id() + " - " + meetingTimes[i].get_time())
    # Show Courses
        courses = data.get_courses()
        for i in range(0, len(courses)):
            instructors = courses[i].get_instructors()
            # instructors = [instructors]
            print(courses[0].get_instructors())
            print(f">>instaructor>>{instructors}")
            print(type(instructors))
            tempStr = ""
            for j in range(0, len(instructors) - 1):
                tempStr += instructors[j].__str__() + ", "
            tempStr += instructors[len(instructors) - 1].__str__()
            c4.append(courses[i].get_number() + " - " + courses[i].get_name() + " (" + tempStr + ' ,' + str(
                courses[i].get_maxNumbofStudents()) + ")")

    def print_generation(self,population):
        global g1,g2, eachGen,eachFitCon
        g1,g2, eachGen,eachFitCon= [],[],[],[]
        table1 = prettytable.PrettyTable(["schedule #","classes [dept,class,room,instructor,meeting-time]", "fitness" ,"# of conflicts" ])
        schedules = population.get_schedules()
        for i in range(0,len(schedules)):
            table1.add_row([str(i),schedules[i], "Fitness = " +  str(round(schedules[i].get_fitness(),3)), "Conflicts = " + str(schedules[i].get_numbofConflicts())])
            g1.append([str(i) + " - " +  str(schedules[i])])
            g2.append("  F = " +str(round(schedules[i].get_fitness(),3))+ " - " +  "C = "+str(schedules[i].get_numbofConflicts()))
        eachGen += g1
        eachFitCon += g2

    def print_schedule_as_table(self,schedule):
        #Show  Schedule table
        classes = schedule.get_classes()
        global l1, l2, l3, l4, l5
        l1, l2, l3, l4, l5 = [], [], [], [], []
        for i in range(0,len(classes)):
            l1.append(str(i))
            l2.append(classes[i].get_course().get_name() + "(" +
                           classes[i].get_course().get_number() + ", " +
                           str(classes[i].get_course().get_maxNumbofStudents()) + ")")
            l3.append(classes[i].get_room().get_number() + "(" + str(classes[i].get_room().get_seatingCapacity()) + ")")
            l4.append(classes[i].get_instructor().get_name() + "(" + str(classes[i].get_instructor().get_id()) + ")")
            l5.append(classes[i].get_meetingTime().get_time() + "(" + str(classes[i].get_meetingTime().get_id()) + ")")



#############################################################################################
#############################################################################################
data = Data()
showTable = Table()
showTable.showData()
population = Population(POPULATION_SIZE)
geneticAlgorithm = GeneticAlgorithm()


column1,column2 = [],[]
generationNumber = 0

while (population.get_schedules()[0].get_fitness() != 1.0):
    generationNumber += 1
    population = geneticAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x:x.get_fitness(),reverse=True)
    showTable.print_generation(population)
    showTable.print_schedule_as_table(population.get_schedules()[0])
    column1 +=  ["Generation " + str(generationNumber)] + eachGen
    column2 +=  [""] + eachFitCon

# Data Table
fig1 = go.Figure(data=[go.Table(header=dict(values=["id - instructor","room (capacity)","id - Metting Time","id - course (instructors, capacity )"]),
                 cells=dict(values=[c1,c2,c3,c4]))
                     ])
# Generation Table
fig2 = go.Figure(data=[go.Table(columnwidth = [220,25],header=dict(values=["Generations "," Fitness - Conflicts"]),
                                        cells=dict(values=[column1,column2], height = 30) )
                               ])
#  Schedule Table
fig3 = go.Figure(data=[go.Table(header=dict(values=['Class #','Course (number, max # of students)','Room(capacity)','Instructor(id','Meeting Time(id)']),
                 cells=dict(values=[l1, l2,l3,l4,l5]))
                     ])

fig1.show()
fig2.show()
fig3.show()


