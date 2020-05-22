from datetime import datetime
import os
from development import db_operations
import matplotlib.pyplot as plt
import sys
import csv

print('-'*56)
print("Welcome to daily budget calculator\n")
print("Your daily budget is set to 15 euros/day by default.")
print('-'*56)



class calculation():
    def __init__(self,budget=None,days=30,result=None):
        self.budget = budget
        self.days = days
        self.result = result


    def main(self):

        calculation.previous(self)

        try:

            self.budget=float(input("Enter your montly budget: "))
            self.days=int(input("Enter day number till the end of month: "))

            end_day=datetime.today().strftime('%d') ## Today's day
            this_month=datetime.today().strftime('%m') ## Today's month
            this_year=datetime.today().strftime('%Y') ## This year
            sql_date_insert=end_day + ',' + this_month + ',' + this_year

            end_date_cal=int(end_day)+int(self.days)
            end_date=datetime.today().strftime("%Y-%m-{}").format(end_date_cal)



            self.result=round((self.budget / self.days),2)




            print("You must spend max. {} eur/day till {}".format(self.result,end_date))
            options=input("Do you want to save ? (y/n): ")


            if options == 'y' or options == 'Y':
                res=db_operations.same_entry_check(end_day,this_month)
                if res:
                    ans=input("An existing data has found. Overwrite (y/n)?: ")
                    if ans == 'y' or 'Y':
                        db_operations.update_budgetdata(end_day,this_month,self.result)
                    else:
                        print("Redirecting to the main menu...")
                        pass
                else:
                    db_operations.insert_t_date_budget(sql_date_insert,self.result)


            else:
                print("Not saved.")


        except ValueError:
            print("You must provide a budget, a number.")




    def previous(self):
        count=db_operations.count()
        if count >= 1:
            ch1 = input("Old save is found. Do you want to see details ? (y/n) :")
            if ch1 == 'y' or ch1 == 'Y':
                datas=db_operations.list_all('day,month,year,budget','t_date','budget where idt_date=idbudget','idt_date','t_date.day,month')

                for i in datas:

                    print("Date: " + str(i[0]) + '-' + str(i[1]) + '-' + str(i[2]) + ' --- ' + str(i[3]) + ' Eur/day.')

    def rotation_check(self):
        count=db_operations.count()

        if count == 30:
            print("Database reached to 30 entries and must be cleared.")
            choice=input("Do you agree? (y/n): ")
            if choice == 'y' or 'Y':
                db_operations.delete_all('t_date')
                db_operations.ai_truncate('t_date')

        else:
            pass



class data_operations(calculation):
    def __init__(self,budget=None,days=30,result=None,average=15):

        super().__init__(self,budget,result)
        self.average=average

    def daily_graph(self):
        # x axis values days
        # print(self.days)

        ############ DAYS 1,2,3,4,5,6,7,8##################
        # self.days=db_operations.count()
        #
        # #print(self.days)
        #
        # l_days=[]
        # for i in range(self.days):
        #     i+=1
        #
        #     l_days.append(str(i)) # if no str days are inserted in the graph as float numbers. Ex. 1.25,1.70,1.75 etc...
        # self.x=l_days
        self.days=db_operations.print_days()

        out_days = [item for t in self.days for item in t]
        self.x=out_days

        ####################################
        ################# AMOUNTS Y axes################################

        data = db_operations.b_amount_sorted()

        self.y = [item for t in data for item in t]

        ####### Z is average amount to spend per day ####################

        z = [self.average]
        #print(self.x)
        z_count = db_operations.count()
        z=(z * z_count)


        plt.plot(self.x, z, label="Daily Spending Limit", color='red')

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



app=calculation()




while True:
    app.rotation_check()
    print("\n1-Continue with calculation")
    print("2-Delete all data")
    print("3-Exit\n")
    ch = input("Make your choice: ")

    if ch == "1":
        app.main()
        data_operations().daily_graph()

    elif ch == "2":

        db_operations.delete_all('t_date')
        db_operations.ai_truncate('t_date')
        print("Database was cleared.")

    elif ch == "3":
        print("Terminated...")
        break
    else:
        print("There is a problem")
        break


db_operations.close_connection()