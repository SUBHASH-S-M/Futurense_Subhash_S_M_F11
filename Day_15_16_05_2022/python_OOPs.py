import time
import numpy as np
import datetime
import pandas as pd

class Company():
    def __init__(self,company,student_id,batch_id,name,phone_number,email_id):
        self.company=company
        self.student_id=student_id
        self.batch_id=batch_id
        self.name=name
        self.__phone_number=phone_number
        self.__email_id=email_id
    def get_email(self):
        return self.__email_id
    def get_phone(self):
        return self.__phone_number
    def set_email_id(self,email_id):
        self.__email_id=email_id
    def set_phone_number(self,phone_num):
        self.__phone_number=phone_num
    @staticmethod
    def welcome_mesage(name):
        print("----------------------")
        print(f"Welcome {name} , Explore the Futurense MIS portal")
        print("----------------------")
        time.sleep(2)
class report_card(Company):
    def __init__(self,company,student_id,batch_id,name,phone_number,email_id,marks):
        super().__init__(company,student_id,batch_id,name,phone_number,email_id)

        self.marks=marks
    def generate_progress_card(self):
        self.percentage={}
        for i in sorted(self.marks):
            self.percentage[i]=(self.marks[i][0]/self.marks[i][1])*100
        self.current_time = datetime.datetime.now()
    def display_progress_card(self):
        arr_total=[]
        print(f"Progress Card Generated on {self.current_time}")
        print("Student Name : ", self.name)
        print("Student Id :", self.student_id)
        for i in sorted(self.percentage):
            val_per="%0.2f"%(self.percentage[i])
            print(f"Test_name:{i} Percentage Score:{val_per}")
            arr_total.append(float(val_per))

        arr_total = np.array(arr_total)
        avg_percentage = np.mean(arr_total)
        max_percentage = np.max(arr_total)
        min_percentage = np.min(arr_total)

        print(f"Performance Score (out of 100) :",avg_percentage)
        print(f"Best Score :",max_percentage)
        print(f"Least Score : ",min_percentage)
        print("------------------------------")
        time.sleep(2)
        return (self.name,avg_percentage,max_percentage,min_percentage,pd.datetime.now().date())

#arrya of objects
student_detials=[("Futurense","FT-376","F11","subhash","9442699741","smsubhashrasi@futurense.com",
                     {'test_id_1':[20,30],'test_id_2':[44,45],'test_id_3':[30,45]}),
                 ("Futurense", "FT-456", "F11", "Vaibhav", "8835679606", "excel_vaibhav@futurense.com",
                  {'test_id_1': [25, 30], 'test_id_2': [45, 45], 'test_id_3': [40, 45]})
                 ]


print("Enter u r name:")
name=input()
Company.welcome_mesage(name)

obj_ref=[]
details=[]
for i in range(len(student_detials)):
    obj_ref.append(report_card(*student_detials[i]))
    obj_ref[i].generate_progress_card()
    detail=obj_ref[i].display_progress_card()
    details.append(detail)
df = pd.DataFrame(details, columns =['Student_name','Peformance Score','Best Score','Least Score','Report Generated Time'])
print(df)
df.to_csv("Progress_Report.csv")




