import pandas as pd
data={
    "name":[1,2,33],
    "age":[17,15,11]
}

ddd=pd.DataFrame(data,index=[1,"the brother 2","the brother 3"])
# add a new colum
ddd["jop"]=["cooik","n/a","gh"]
# add a new a row 
new_roiw=pd.DataFrame([{"name":"sandy"},{"name":"abdallah"}],index=["asda","dfsd"]
                    )
ddd=pd.concat([ddd,new_roiw])

print(ddd)
