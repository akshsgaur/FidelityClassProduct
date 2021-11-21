from math import ceil
from fidelityfunds import funds
from FutureReturns import future_return



def risk_factor_analysis(time, aptitude_for_risk):
    profile = 5
    if time < 10:
        profile = 5
    elif time > 10 or time < 20:
        profile = 4
    elif time > 20 or time < 30:
        profile = 3
    elif time > 30 or time < 40:
        profile = 2
    else:
        profile = 1
    temp = ceil((aptitude_for_risk)/2)
    profile = ceil((temp+profile)/2)
    return profile

# def get_future_returns(amount, duration, starter_amount,list):
#     ll = []
#     for i in range(len(list)):
#         ll.append(future_return(amount,duration,starter_amount,list[i]))
#     return ll

def select_fund(funds, profile):
    selected = []
    risk = "Low"
    if profile == 1:
        risk = "Low"
    elif profile == 2:
        risk = "Low-to-Medium"
    elif profile == 3:
        risk = "Medium"
    elif profile == 4:
        risk = "High-to-Medium"
    else:
        risk = "High"
    print(risk)
    i = 0;
    for fund in funds:
        if fund.risk_factor == risk:
            selected.append(fund)
        i = i + 1
    selected.sort(key=lambda x: x.oneyearp, reverse=True)
    newlist = sorted(selected, key=lambda x: x.oneyearp, reverse=True)
    another_newlist = []
    for i in range(5):
        # print(newlist[i].name)
        # print(newlist[i].oneyearp)
        another_newlist.append(newlist[i].name)
    print(another_newlist)
    return another_newlist

def get_future_returns(amount, duration, starter_amount,list):
    ll = []
    for i in range(len(list)):
        ll.append(future_return(amount,duration,starter_amount,list[i]))
    print(ll)
    return ll



funds = funds()
get_future_returns(400,40,100000,select_fund(funds,4))
# profile = risk_factor_analysis(20, 8)
# selected = select_fund(funds, profile)
# #selected.sort(key=lambda x: x.oneyearp, reverse =True)
# newlist = sorted(selected, key=lambda x: x.oneyearp, reverse = True)
# anl =[]
# for i in range(5):
#      print(newlist[i].name)
#      print(newlist[i].oneyearp)
#      anl.append(newlist[i])
#
# ll1 = get_future_returns(20, 10, 90000, anl)
# print(ll1)
# # selected_top_5 = selected.sort(selected.oneyearp)
# # print(selected_top_5)
# # for i in range(5):
# #      print(newlist[i].name)
# #      print(newlist[i].oneyearp)




