import mysql
import mysql.connector
import functools
import nltk
import operator
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

def convertTuple(tup): 
    str = functools.reduce(operator.add, (tup)) 
    return str

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Root",
  database="question set"
)

email=input("Enter your Email id:")
email=email.replace('@',"")
email=email.replace('.',"")
m=[]
qu=[]
quest=[]
tok=[]
f=0
gram=[]
srno=1
qtag=["what","where","how","when","if","is","does","have","do","are","can","whose","did","who","should","could","am","would"]
cquest=["can","would","do","did","will","are","whose","have","should","was","does","is","am"]
exception=["this","that","there","here"]
mycursor = mydb.cursor()
mycursor.execute("Select question from quest group by srno")
myresult = mycursor.fetchall()
for i in range(len(myresult)):
    qu.append("No Questions")
while(srno<(len(myresult)+1)):
    if(srno==3):
        if(m[1].lower()=='yes'):
            srno+=2
    q=convertTuple(myresult[srno-1])
    print("Bot:",q)
    message=(input("You:")).strip()
    if(srno!=len(myresult)):
        f=0
        me=message.split(".")
        for i in me:
            tok=word_tokenize(i)
            for j in tok:
                if j in cquest:
                    if(nltk.pos_tag([tok[tok.index(j)+1]])[0][1]=='PRP' or nltk.pos_tag([tok[tok.index(j)+1]])[0][1]=='NN' and nltk.pos_tag([tok[tok.index(j)+1]])[0][1] not in exception):
                        f=1
                        break
    for j in me:
        j=j.strip()
        mes=j.split(" ")
        l=len(mes)
        if(mes[0].strip().lower() in qtag):
            f=1
        else:
            for x in mes:
                if(x.endswith("?")):
                    f=1
    if(f==1):
        print("\n###### LOOKS LIKE YOU HAVE SOME QUERIES. LET ME FORWARD IT TO THE RECRUITER. YOU CAN CONTINUE ######\n")
        qu[srno-1]=message
        print("*******Insert in database******")
        continue
    if(srno==2):
        if(message!='Yes' and message!="No" and message!="yes" and message!="YEs"and message!="no" and message!="NO" and message!="YES"):
            print("\n\n***********\nBot: I don't understand what you say, Please try again. \n #*#** Tip: Try to maintain the format specified! **#*#\n")
            continue
    if(srno==3):
        s=message.split()
        try:
            x=int(s[0])
            if(s[1]!="years" and s[1]!="Years" and s[1]!="months" and s[1]!="Months" and s[1]!="days" and s[1]!="Days" and s[1]!="year" and s[1]!="Year" and s[1]!="Month" and s[1]!="month"):
                print("\n\n***********\nBot: Oops! That doesn't look like a valid time period! \n #*#** Tip: Try to maintain the format specified! **#*#\n")
                continue
        except:
            print("\n\n***********\nBot: Oops! That doesn't look like a valid time period! \n #*#** Tip: Try to maintain the format specified! **#*#\n")
            continue
    m.append(message)
    mycursor.execute("update quest set userans=('%s') where srno=(%d)" %(message,srno))
    mydb.commit()
    quest.append(q)
    srno+=1
    print("\n****************\n")
print("\n Bot: Thank you for your co-operation! Your answers have been submitted successfully!")

srno=len(quest)
if(srno<=5):
    qu.pop(2)
    qu.pop(2)
mycursor=mydb.cursor()
query="create table if not exists "+email+" (Sr_No INTEGER PRIMARY KEY , Questions varchar(300) , Answers varchar(300), Asked_ques varchar(300) )"
mycursor.execute(query)
mydb.commit()
for q in range(srno):
        mycursor.execute("insert into "+email+" values (('%d'),('%s'),('%s'),('%s'))" %((q+1), (quest[q]), (m[q]), (qu[q])))
        mydb.commit()