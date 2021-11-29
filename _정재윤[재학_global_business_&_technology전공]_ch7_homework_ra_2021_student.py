# -*- coding: utf-8 -*-
"""‍정재윤[재학 / Global Business & Technology전공] - ch7_homework_RA-2021-student.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AMb72HZQxB-FOuhB7_7w8j5rBayrhAts

# Homework 2. Relational Algebra

1. Use Google Colabortory and do your homework.
3. (In Google colaboratory) Before you submit your homework, restart kernel and run all the cells.(채점자가 cell을 실행하지 않음)
4. Save (File->Save) the file
5. Submit your homework (this file) in Google classroom
6. **Don't forget to click "제출" button** ("Submit", "완료로 표시", 또는 "제출" 버턴을 누르지 않으면 제출된 것이 아님)
7. No late homeworks will be accepted for any reason!

To edit this cell, double click here
```
이름:__________정재윤_____________
학번:__________201703262_____________
학과:__________GBT학부_____________
제출일:________21.10.19______________
```

## CompanyDB Schema

### Note that attribute names are capitalized
```
E(Fname,Minit,Lname,Ssn,Bdate,Address,Sex,Salary,Superssn,Dno)
D(Dname,Dnumber,Mgrssn,Mgrstartdate)
DL(Dnumber,Dlocation)
P(Pname,Pnumber,Plocation,Dnum)
WO(Essn,Pno,Hours)
DE(Essn,Dependent_name,Sex,Bdate,Relationship)
```

## First, run the following cell before you do your homework

## DB setup
"""

EMPLOYEE_csv = 'Fname,Minit,Lname,Ssn,Bdate,Address,Sex,Salary,Superssn,Dno\r\nJohn,B,Smith,123456789,1965-01-09,731-Fondren-Houston-TX,M,30000.00,333445555,5\r\nFranklin,T,Wong,333445555,1955-12-08,638-Voss-Houston-TX,M,40000.00,888665555,5\r\nJoyce,A,English,453453453,1972-07-31,5631-Rice-Houston-TX,F,25000.00,333445555,5\r\nRamesh,K,Narayan,666884444,1962-09-15,975-Fire-Oak-Humble-TX,M,38000.00,333445555,5\r\nJames,E,Borg,888665555,1937-11-10,450-Stone-Houston-TX,M,55000.00,,1\r\nJennifer,S,Wallace,987654321,1941-06-20,291-Berry-Bellaire-TX,F,43000.00,888665555,4\r\nAhmad,V,Jabbar,987987987,1969-03-29,980-Dallas-Houston-TX,M,25000.00,987654321,4\r\nAlicia,J,Zelaya,999887777,1968-01-19,3321-Castle-Spring-TX,F,25000.00,987654321,4\r\n'
DEPARTMENT_csv = 'Dname,Dnumber,Mgrssn,Mgrstartdate\r\nHeadquarters,1,888665555,1981-06-19\r\nAdministration,4,987654321,1995-01-01\r\nResearch,5,333445555,1988-05-22\r\n'
DEPT_LOCATIONS_csv = 'Dnumber,Dlocation\r\n1,Houston\r\n4,Stafford\r\n5,Bellaire\r\n5,Houston\r\n5,Sugarland\r\n'
PROJECT_csv = 'Pname,Pnumber,Plocation,Dnum\r\nProductX,1,Bellaire,5\r\nProductY,2,Sugarland,5\r\nProductZ,3,Houston,5\r\nComputerization,10,Stafford,4\r\nReorganization,20,Houston,1\r\nNewbenefits,30,Stafford,4\r\n'
WORKS_ON_csv = 'Essn,Pno,Hours\r\n123456789,1,32.5\r\n123456789,2,7.5\r\n333445555,2,10.0\r\n333445555,3,10.0\r\n333445555,10,10.0\r\n333445555,20,10.0\r\n453453453,1,20.0\r\n453453453,2,20.0\r\n666884444,3,40.0\r\n888665555,20,\r\n987654321,20,15.0\r\n987654321,30,20.0\r\n987987987,10,35.0\r\n987987987,30,5.0\r\n999887777,10,10.0\r\n999887777,30,30.0\r\n'
DEPENDENT_csv = 'Essn,Dependent_name,Sex,Bdate,Relationship\r\n123456789,Alice,F,1988-12-30,Daughter\r\n123456789,Elizabeth,F,1967-05-05,Spouse\r\n123456789,Michael,M,1988-01-04,Son\r\n333445555,Alice,F,1986-04-05,Daughter\r\n333445555,Joy,F,1958-05-03,Spouse\r\n333445555,Theodore,M,1983-10-25,Son\r\n987654321,Abner,M,1942-02-28,Spouse\r\n'

# import packages

import pandas as pd
from io import StringIO 
import re

# Tables
EMPLOYEE = pd.read_csv(StringIO(EMPLOYEE_csv))
DEPARTMENT = pd.read_csv(StringIO(DEPARTMENT_csv))
DEPT_LOCATIONS = pd.read_csv(StringIO(DEPT_LOCATIONS_csv))
PROJECT = pd.read_csv(StringIO(PROJECT_csv))
WORKS_ON = pd.read_csv(StringIO(WORKS_ON_csv))
DEPENDENT = pd.read_csv(StringIO(DEPENDENT_csv))

# short_names for Tables
E = EMPLOYEE
D = DEPARTMENT
DL = DEPT_LOCATIONS
P = PROJECT
WO = WORKS_ON
DE = DEPENDENT

def rename(R, C):
    return R.rename(columns=C)

def select(R, C):
    # The following substitution may NOT work 
    # when column name is equal to a string value in C
    tokens = re.split(r'(\W+)', C)
    new_tokens = ["R." + token  if token in R.columns else token \
                  for token in tokens] 
    selected = eval(''.join(new_tokens))
    return R[selected].reset_index(drop=True)

def project(R, C):
    return R[C].drop_duplicates().reset_index(drop=True)

def union(R, S):
    S.columns = R.columns
    T = pd.concat([R, S], ignore_index=True)
    T = T.drop_duplicates().reset_index(drop=True)
    return T

def intersect(R, S):
    S.columns = R.columns
    return R.merge(S).reset_index(drop=True)

def minus(R, S):
    S.columns = R.columns
    return pd.concat([R, S, S]).drop_duplicates(keep=False).reset_index(drop=True)

def product(R, S):
    """Determine Cartesian product of two data frames."""
    key = 'key'
    while key in R.columns or key in S.columns:
        key = '_' + key
    key_d = {key: 0}
    return pd.merge(R.assign(**key_d), S.assign(**key_d), on=key)\
           .drop(key, axis=1).reset_index(drop=True)

def natural_join(R, S):
    return pd.merge(R, S).reset_index(drop=True)

def natural_join2(R, S, keys_R, keys_S):
    return pd.merge(R, S, left_on=keys_R, right_on=keys_S)\
           .drop(keys_S, axis=1).reset_index(drop=True)

def division(R, S):
    Z = set(R.columns)
    X = set(S.columns)
    assert X <= Z
    Y = pd.Index(Z - X)
    T1 = project(R, Y)
    T2 = project(minus(product(T1, S), R), Y)
    T = minus(T1, T2)
    return T.reset_index(drop=True)

"""## <font color='red'>Query Statement에 나타나지 않은 상수(값)을 사용하면 무조건 0점 처리됨. 예를 들어, Query 1에서 "Research"라는 상수값만 나타나야 함</font>

## 각 질의당 10점

### Query 1: Retrieve the last name, first name, and address of employees who work for the "Research" department. (Use cartesian product. Do NOT use join)
"""

# YOUR CODE HERE 10

T = select(D, "Dname=='Research'")
U = select(product(E, T), "Dno==Dnumber")
project(U, ['Lname', 'Fname', 'Address'])

"""### Query 2: Retrieve the last name, first name, and address of employees who work for the "Research" department. (Do NOT use cartesian product. Use natural join)"""

# YOUR CODE HERE 10

department_name = select(D, "Dname=='Research'")

E_list=rename(E,{'Dno':'Dnumber'}) #자연조인을 위해 attribute일치화
merged=natural_join(E_list,department_name)

project(select(merged, "Dname=='Research'"), ['Lname','Fname','Address'])

"""### Query 3: For every project located in "Stafford", list the project name, the controlling department name, and the department manager's last name, first name. (Use natural_join2, No cartesian products and natural joins are allowed)"""

# YOUR CODE HERE 10

dnum_location=project(select(DL, "Dlocation=='Stafford'"), ["Dnumber"])
# print(dnum_location)
re_D=rename(D,{'Dnumber':'Dno'})

merge_D=natural_join2(re_D,dnum_location,['Dno'],['Dnumber'])
merge_P=natural_join2(dnum_location,P,['Dnumber'],['Dnum'])

merge_DP=natural_join2(merge_D,merge_P,['Dno'],['Dnumber'])
# print(merge_DP)

merge_E=natural_join2(merge_DP, E, ['Mgrssn'],['Ssn'])
# print(merge_E)

project(merge_E, ['Pname','Dname','Fname','Lname'])

"""### Query 4: Find the last name, first name of employees who work on all the projects controlled by department number 4."""

# YOUR CODE HERE 10

WO_essn_pno= project(WO, ['Essn', 'Pno'])

P_dnum = project(select(P, 'Dnum==4'), ['Pnumber'])
P_dnum_re = rename(P_dnum, {'Pnumber':'Pno'})

Department4_essn = division(WO_essn_pno, P_dnum_re)
# print(Department4_essn)
Department4 = natural_join2(E , Department4_essn, 'Ssn' , 'Essn')
project(Department4, ['Lname', 'Fname'])

"""### Query 5: Make a list of project names for projects that involve an employee whose last name is "Wallace", either as a worker or as a manager of the department that controls the project."""

# YOUR CODE HERE 5

#E에서 Wallce의 부서 반환
find_W=select(E,"Lname=='Wallace'")
find_Dno=project(find_W,['Dno'])

#find_Dno와 P 결합
DP=natural_join2(find_Dno, P, ['Dno'],['Dnum'])

project(DP, ['Pname'])

"""### Query 6: List the last name, first name of all employees with two or more dependents. (Do NOT use aggregate operator)"""

# YOUR CODE HERE 0

# 교수님 죄송합니다. 


#DE에서 부양가족이 2명 이상인 직원의 ESSN반환
E_DE=natural_join2(E,DE,['Ssn'],['Essn'])
print(E_DE)



#두가지 조건을 모두 적용하게 되면, 두 조건 모두를 만족하는 값을 조회하므로, 인덱스 안에 값이 없게 된다.
# E_list1=select(E_DE, "(Relationship == 'Daughter') & (Relationship == 'Spouse')")
# E_list2=select(E_DE, "(Relationship == 'Daughter') & (Relationship =='Son')")
# E_list3=select(E_DE, "(Relationship == 'Son') & (Relationship=='Spouse')")

# print(E_list1)
# print(E_list2)
# print(E_list3)
# project(E_list, ['Lname', 'Fname'] )



#위에서 반환한 목록과 E의 병합 후 연산결과 반환
# tmp=[]
# check=E_DE.Lname[0]
# tmp_check=0
# for i in range(1,len(E_DE)):
#   if check==E_DE.Lname[i]:
#     if tmp==None:
#       tmp.append(str(E_DE.Lname[i]))
#     if tmp!=None and tmp[tmp_check] != check:
#       tmp.append(str(E_DE.Lname[i]))
#       tmp_check+=1
#   check=E_DE.Lname[i]
# print(tmp)

"""### Query 7: Retrieve the last name, first name of employees who have no dependents."""

# YOUR CODE HERE 10

DE_essn=project(DE, ['Essn'])
E_ssn=project(E,['Ssn'])
has_dependents=minus(E_ssn,DE_essn)
#print(has_dependents)
#print(product(E,has_dependents))
U=select(product(E,has_dependents),"Ssn_x==Ssn_y") 
project(U, ['Fname', 'Lname'])

"""### Query 8: List the last name, first name of managers who have at least one dependent."""

# YOUR CODE HERE 5

DE_essn = project(DE, ['Essn']) #DE에 명단이 오른 essn조사

has_dependents = select(product(DE_essn,E), "Essn==Ssn")
project(has_dependents, ['Lname', "Fname"])

"""### Query 9: Retrieve the last name, first name of all employees in department 5 who work more than 10 hours per week on the ProductX project."""

# YOUR CODE HERE 10

ProductX_Pname = select(P, "Pname=='ProductX'")
ProductX_list=select(product(WO, ProductX_Pname), "Pno == Pnumber")

More_10H=select(ProductX_list, "Hours >= 10")
# print(More_10H)
Department5=select(D, "Dnumber == 5")
# print(Department5)

Mgr=select(product(Department5,E), "Mgrssn == Superssn")
# print(Mgr)
result=select(product(More_10H,Mgr), "Essn==Ssn")
project(result, ['Lname','Fname'])

"""### Query 10: Retrieve the last name, first name of all employees who is supervised by James Borg"""

# YOUR CODE HERE 10

Superssn_E=select(E, "Fname=='James'"and "Lname=='Borg'")
# print(product(E, Superssn_E))
result=select(product(E,Superssn_E), "Ssn_y==Superssn_x")
# print(U)
project(result, ['Fname_x', 'Lname_x'])