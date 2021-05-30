import csv

def csv_writer(info_list):
    with open("School_administration_program.csv", "a", newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell == 0:
            writer.writerows=(["Name" ,"Std." , "Roll no." "Phone no."])
        writer.writerows(info_list)

if __name__=='__main__':
    condition= True
    student_num = 1
    while (condition):
            student_info=input(f"Enter the student's information for student {student_num} in the following format(Name Std Roll_num Phone_num):")
            print("The entered info is "+ student_info)
            student_info_list = student_info.split(" ")
            print(student_info_list)
            print("\nThe entered information is - \nName: {} \nStd.: {} \nRoll_no.: {} \nPhone_no.:{} \n"
                  .format(student_info_list[0],student_info_list[1], student_info_list[2] ,student_info_list[3]))
            check=input("Is the entered information correct? (yes/no) ")

            if check == "yes":
                csv_writer(student_info_list)
                student_num += 1

                csv_writer(student_info_list)
                New_info=input ("Enter(yes/no)if you wish to add another student's Information ")
                if New_info=="yes":
                    condition=True
                elif New_info=="no":
                    
                    condition=False
            elif check=="no":
                print("\nPlease re-enter your values :\n")
    

    

   
