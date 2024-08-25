import numpy as np
import matplotlib.pyplot as plt


def getScore(redFlag,greenFlag):
    if greenFlag==3:
        print("Everything is under the recommended limit.")
    elif redFlag==3:
        print("You need to control your expenses and EMIs since the EMIs and expenses all crosses the max recommended limit.")
    elif greenFlag>redFlag:
        print("You are doing good but it can be further improved.")         
    elif redFlag>greenFlag:
        print("You need to improve and you don't have space for more EMIs and expenses.")


def analysis(totalIncome,totalEMIs,restOfExpenses):
    ### All EMI limits should be less than or equal to 25% of your total income.
    TotalEMIsLimit = totalIncome/4.0

    ### Total Fundamental costs(excludes EMIs) should be less than or equal to 25% of your total income.
    TotalRemainingExpenseLimit = totalIncome/4.0

    ### IdealCashflow should be atleast 50% of total income.
    IdealCashflow = totalIncome/2.0

    print("=======================Recommended Limits========================")
    print("Calculation is done for your Total Income=",totalIncome)
    print("Maximum EMIs limit is: ",TotalEMIsLimit)
    print("Maximum Remaining expense limit is: ",TotalRemainingExpenseLimit)
    print("Total Fundamental Costs(EMIs+ Remaining expenses) limit is: ",TotalEMIsLimit+TotalRemainingExpenseLimit)
    print("Ideal Cashflow should be geater than: ",IdealCashflow)
    print("================================================================")

    print("\n")
    print("=======================Current==================================")
    print("Calculation is done for your Total Income=",totalIncome)

    ### Total net cashflow
    TotalCashFlow = totalIncome-(totalEMIs+restOfExpenses)
    print("Your total net Cashflow is: ",TotalCashFlow)

    redFlag=0
    greenFlag=0

    if TotalCashFlow >= IdealCashflow:
        greenFlag+=1
    else:
        redFlag+=1

    if totalEMIs <= TotalEMIsLimit:
        print("You still have a window to include more EMIs of: ",TotalEMIsLimit-totalEMIs)
        greenFlag+=1
    else:
        print("You don't have a window to include more EMIs.")
        print("You are exceeding the given EMIs limit by: ",totalEMIs-TotalEMIsLimit)
        print("Try to reduce your EMIs by pre-paying the higher interest loan.")
        redFlag+=1


    if restOfExpenses <= TotalRemainingExpenseLimit:
        greenFlag+=1
    else:
        redFlag+=1

    getScore(redFlag,greenFlag)
    print("=================================================================")

    showInPieChart(IdealCashflow,TotalEMIsLimit,TotalRemainingExpenseLimit,"Ideal Cashflow Distribution")
    showInPieChart(TotalCashFlow,totalEMIs,restOfExpenses,"Yours Cashflow Distribution")


def showInPieChart(cashflow,emis,expenses,title):
    totalIncome = ["Net CashFlow","EMIs","RemaningExpenses"]
    data = [cashflow,emis,expenses]


    # Creating explode data
    explode = (0.1, 0.1, 0.1)

    # Creating color parameters
    colors = ("orange", "cyan", "brown")

    # Wedge properties
    wp = {'linewidth': 1, 'edgecolor': "green"}

    # Creating autocpt arguments


    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)


    # Creating plot
    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(data,autopct=lambda pct: func(pct, data),explode=explode,labels=totalIncome,shadow=True,colors=colors,startangle=90,wedgeprops=wp,textprops=dict(color="magenta"))

    # Adding legend
    ax.legend(wedges,totalIncome ,title="Labels",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title(title)


    plt.show()


def main():
    analysis(yourTotalIncome,yourEMIs,yourRestOfExpenses)


if __name__ == '__main__':
    main()