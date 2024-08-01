# emulation of compuerer
# ********************************* using single if *************************************************************
n1=float(input("enter number "))
n2=float(input("enter number "))
dict={"+":n1+n2,"-":n1-n2,"*":n1*n2,"/":n1/n2,}
string=input("enter operation ")
if string=="+"or"-"or"/"or"*":
    print(dict.get(string))
