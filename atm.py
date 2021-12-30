print("wellcome")
card = input("enter the your card")
if card=="credit card" or "debit card":
    print("loading")
    language = input("enter the language")
    if language=="hindi" or "english":
        print("process")
        pin = int(input("enter your pin"))
        if pin==1234:
            print("next")
            type= input("enter the type")
            if type=="current account" or "saving account":
                print("inprosses")
                trans = input("enter the transection")
                if trans=="withdrawal":
                    print("ok")
                    balance = int(input("enter your amount"))
                    if balance>=0 and balance<=10000:
                        print("go next")
                        total_balance = int(input("enter the total balance"))
                        if total_balance==30000:
                            print("balance-total_balance")
                            reciept = input("do you reciept your ammount")
                            if reciept=="yes":
                                print("you have recieve your balance,thank you")
                            else:
                                print("not velid")  
                        else:
                            print("not balance")
                    else:
                        print("10000 rupey can't take over") 
                else:
                    print("machine problem") 
            else:
                print("other account not allowed")  
        else:
            print("it is not pin ")
    else:
        print("other language not allowed") 
else:
    print("other card not allowed")   