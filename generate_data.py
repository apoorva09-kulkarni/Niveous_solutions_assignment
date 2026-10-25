"""Generates SYNTHETIC applicants + SIMULATED API responses -> data.js
All names and numbers are invented. No real customer data. Run: py generate_data.py"""
import json

# id, name, age, job, city, months_in_job, declared_income, observed_credits,
# existing_emi, active_loans, missed_12m, cibil, requested, tenure_m, slips, stmt_months, aadhaar_name
R = [
 (1,"Anita Deshmukh",34,"Software engineer","Pune",60,85000,85000,8000,1,0,780,500000,48,3,6,None),
 (2,"Rahul Verma",29,"Accounts executive","Jaipur",40,60000,60000,5000,1,0,735,300000,36,2,6,None),
 (3,"Sunil Patil",41,"Sales manager","Nashik",84,45000,45000,15000,2,0,720,400000,60,3,6,None),
 (4,"Kavita Singh",38,"Office clerk","Lucknow",70,55000,55000,6000,1,3,610,250000,36,3,6,None),
 (5,"Imran Sheikh",36,"Technician","Hyderabad",55,65000,65000,7000,1,1,680,350000,36,3,6,None),
 (6,"Gopal Rao",62,"Consultant","Mysuru",200,70000,70000,0,0,0,760,300000,36,3,6,None),
 (7,"Neha Kulkarni",40,"Marketing lead","Bengaluru",48,90000,55000,10000,1,0,740,600000,48,3,6,None),
 (8,"Meera Nair",31,"Nurse","Kochi",36,50000,50000,0,0,0,725,200000,36,3,6,"Meera Menon"),
 (9,"Arjun Mehta",27,"Analyst","Mumbai",6,48000,48000,0,0,0,705,150000,24,3,6,None),
 (10,"Farhan Qureshi",45,"Small-firm director","Delhi",120,120000,120000,12000,1,0,790,1200000,60,3,6,None),
 (11,"Lakshmi Iyer",43,"Teacher","Chennai",150,58000,58000,9000,2,2,690,300000,36,3,6,None),
 (12,"Rohit Joshi",26,"Junior designer","Nagpur",30,52000,52000,0,0,0,750,150000,24,3,6,None),
]
out = []
for (i,n,age,job,city,mj,inc,obs,ex,loans,miss,cb,ask,ten,slips,stm,aad) in R:
    out.append({
      "id":i,"name":n,"age":age,"job":job,"city":city,"monthsInJob":mj,
      "income":inc,"existingEmi":ex,"activeLoans":loans,"requested":ask,"tenure":ten,
      "consent":True,
      "docs":{"pan":True,"aadhaar":True,"slips":slips,"stmtMonths":stm},
      "account":"XXXX"+str(4800+i),
      # SIMULATED external API responses
      "bureau":{"score":cb,"missed12m":miss,"activeAccounts":loans},
      "kyc":{"panName":n,"aadhaarName":aad or n,"panValid":True},
      "stmt":{"avgMonthlyCredits":obs},
    })
open("data.js","w",encoding="utf-8").write("const APPLICANTS="+json.dumps(out,indent=1)+";\n")
print("data.js written with",len(out),"synthetic applicants")
