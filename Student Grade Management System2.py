import pandas as pd
Student_Grade_Management_System={"Name":["Abdallah","Mohammed","Sara","Mena","Anas","mariam"],"Age":[17,17,16,15,16,16],
                                 "Math":[100,20,60,50,44,30]}
data=pd.DataFrame(Student_Grade_Management_System,index=["the first student","the second student","the third student","the fourth student","the fifth student","the sixth student"])
data["science"]=[50,40,60,20,44,55]
data["english"]=[55,100,20,44,73,52]
data["physics"]=[100,22,45,25,66,44]
data["social_stadies"]=[20,22,45,50,60,90]
data11={"Name":["Mazen"],"Age":[16],"Math":[25],"science":[55],"english":[45],"physics":[22],"social_stadies":[10]}
data1=pd.DataFrame(data11,index=["the seventh student"])
data11=pd.concat([data,data1])
data11["Average"]=data11[["Math","science","english","physics","social_stadies"]].mean(axis=1)
print(data11)
the_highest_student=data11["Math"].idxmax()
print(f"top student in math : {data11.loc[the_highest_student,"Name"]}")
the_BOTTOM_student=data11["Math"].idxmin()
print(f"BOTTOM student in math : {data11.loc[the_BOTTOM_student,"Name"]}")
Top_student_Average=data11["Average"].idxmax()
print(f"Top student (Average): {data11.loc[Top_student_Average,"Name"]}")
BOTTOM_student_Average=data11["Average"].idxmin()
print(f"BOTTOM student (Average): {data11.loc[BOTTOM_student_Average,"Name"]}")
the_highest_student_in_science=data11["science"].idxmax()
print(f"top student in science : {data11.loc[the_highest_student_in_science,"Name"]}")
the_bottom_student_in_science=data11["science"].idxmin()
print(f"BOTTOM student in science : {data11.loc[the_bottom_student_in_science,"Name"]}")
print(f"the average score in english : {data11["english"].mean()}")
print(f"the average score in math : {data11["Math"].mean()}")
print(f"the average score in science : {data11["science"].mean()}")
print(f"the average score in physics : {data11["physics"].mean()}")
print(f"the average score in social_stadies : {data11["social_stadies"].mean()}")
print(data11[data11["Average"]>50])
print(data11[data11["Average"]<50])
data11111=data11.sort_values(by="Average",ascending=True)
print(data11)
print(data11111)
#data11.drop("the second student",inplace=True)
#print(data11)
data11.to_csv("students2.csv",index=True)
data11111.to_csv("students3.csv",index=True)
