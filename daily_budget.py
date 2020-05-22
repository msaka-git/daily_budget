from datetime import datetime
import os
import matplotlib.pyplot as plt
import sys
import csv

#### BU SCRIPTEKI GRAFIK OLUSTURMA ISLEMINI DECORATOR KULLANARAK YAPMAYA CALIS.

class calculation():

    def __init__(self,budget=None,days=None,result=None):

        self.budget=budget
        self.days=days
        self.result=result

    def main(self):
        print("\n********** Welcome to daily budget calculator **********\n")
        calculation().previous()
        try:

            self.budget=float(input("Enter your montly budget: "))
            self.days=int(input("Enter day number till the end of month: "))

            end_day=datetime.today().strftime('%d') ## Today's day
            end_date_cal=int(end_day)+int(self.days)
            end_date=datetime.today().strftime("%Y-%m-{}").format(end_date_cal)



            self.result=round((self.budget / self.days),2)



            print("You must spend max. {} eur/day till {}".format(self.result,end_date))
            options=input("Do you want to save ? (y/n): ")

            if options == 'y' or options == 'Y':

                file_operations(self.budget,self.days,self.result).save()

            else:
                print("Not saved.")

            file_operations(self.days).daily_graph()

        except ValueError:
            print("You must provide a budget, a number.")



    def previous(self):
        if os.path.exists("saved.txt"):
            ch1=input("Old save is found. Do you want to see details ? (y/n) :")
            if ch1 == 'y' or ch1 == 'Y':
                file_operations(self.budget,self.days,self.result).read()




class file_operations(calculation):
    def __init__(self,budget=None,days=30,result=None,filename="saved.txt"):
        print("\n********** Finishing budget calculator **********\n")
        super().__init__(self,budget,result)
        self.filename=filename



    def save(self):

        with open(self.filename,'a+') as file:
            file.write("\nDATE: {} --- {} eur/day".format(datetime.today(),self.result))


    def read(self):
        ## Read last 2 lines.
        with open(self.filename,'r') as file:

            data=file.readlines()
            for line in data[1:]:
                self.line=line
                print(self.line)

                amount_list=self.line.split(' ')[4]
                #print(amount_list)


                with open('amount.txt','a+') as am_file:

                    am_file.writelines(amount_list + ',')

        with open("amount.txt",'r') as am_file2:
            data2=am_file2.readlines()
            for line2 in data2:
                self.line2=line2.split(',') ## daily amounts in list
                #print(line2.split(','))



    def daily_graph(self):
        # x axis values days
        #print(self.days)

        ############ DAYS 1,2,3,4,5,6,7,8##################
        count = 0
        with open('saved.txt', 'r') as f:
            for line in f:
                count += 1
                self._count=count

        x=[]
        for ia in range(1,self._count):
            x.append(ia)
            self.x=x
        print(type(self.x))
        ####################################
        ################# AMOUNTS Y axes################################

        with open('amount.txt', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                data = row[:-1]
                float_list = sorted([float(x) for x in data])   ## Sorted by amount from min to max.
            self.y=list(float_list)

        #############################################################
        #x = [1, 2, 3, 4, 5, 6]
        # corresponding y axis values
        #y = [2, 4, 1, 5, 2, 6]


        #for da in range(1, self.days + 1):
        #    y.append(da)
        #    self.y = y

        ####### Z is average amount to spend per day ####################

        z = [15, 15, 15, 15,15,15,15,15]
        print(self.x)

        plt.plot(self.x,z,label="Daily Average",color='red')

        # plotting the points
        plt.plot(self.x, self.y, color='grey', linestyle='dashed', linewidth=2,
                 marker='o', markerfacecolor='blue', markersize=9)



        # naming the x axis
        plt.xlabel('Days')
        # naming the y axis
        plt.ylabel('Daily budget EUR')

        # giving a title to my graph
        plt.title('Daily Budget Graph')

        # function to show the plot
        plt.legend()
        plt.show()



if __name__ == "__main__":
    app=calculation()
    app.main()



#os.remove("amount.txt")


