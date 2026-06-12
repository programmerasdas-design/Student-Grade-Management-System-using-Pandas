import  pandas as pd
Student_Grade_Management_System={"name":["Abdallah","mohammed","sarah","mena","ahmed","maraim"],"Age":[17,15,11,10,14,12],
                                 "math":[50,40,30,20,15,30]}
data=pd.DataFrame(Student_Grade_Management_System,index=["the first student","the second student","the third student","the fourth student","the fifth student","the sixth student"])
data["science"]=[50,20,20,30,40,70]
data["english"]=[40,20,50,30,42,60]
data11=pd.DataFrame([{"name":"abdalrahman"}])
data=pd.concat([data,data11])
print(data["science"].idxmax(),data["science"].max())
print(data[["math",'science',"english"]].mean(axis=0))

print(data["math"].idxmax(),data["math"].max())
the_highest_math=data["math"].idxmax()
print(f"The top student in Math is :", data.loc[the_highest_math, "name"])
print(data["math"].mean())
data["average"] = data[["math", "science", "english"]].mean(axis=1)
print(data[data["average"] <85])
data = data.sort_values(by="average", ascending=False)
print(data)
data.to_csv("students.csv", index=True)