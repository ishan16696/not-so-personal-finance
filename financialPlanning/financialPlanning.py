

def getTotalRetirementCorpus(totalExpenses):
    # totalCorpus will be totalExpenses/3%
    totalCorpus = (totalExpenses*100)/3
    return totalCorpus

def getManageRiskPortfolio(totalIncome,totalEMIs,restOfExpenses,totalExpenses):

    netPersonalCashflow= totalIncome-(totalEMIs+restOfExpenses)

    # 12 months of emergency fund
    emergencyFund = totalEMIs*12+restOfExpenses*12

    totalCorpus = getTotalRetirementCorpus(totalExpenses)

    print("=======================Financial Plan==================================")
    print("Calculation is done for your Total Income=",totalIncome)
    print("Net Personal Cashflow: ",netPersonalCashflow)
    print("You have to save per month ", emergencyFund/12, "to build EmergencyFund for 12 months of: ",emergencyFund)

    print("You would require totalCorpus of: ",(totalEMIs+restOfExpenses)*5, "crore for atleast 4years of financial freedom.")
    print("You would require totalCorpus of: ",totalCorpus/(10**7), "crore for atleast 25years of financial freedom.")


    print("=======================================================================")


def calculate_sip(totalCorpus, rateOfReturn, n):
    """
    Calculate the amount invested at regular intervals (P) for a given totalCorpus.
    
    Parameters:
    totalCorpus: Future value of the investment
    rateOfReturn: Expected annual rate of return
    n (int): Total number of investments (number of years)
    """
    monthly_rate = rateOfReturn / 12
    total_investments = n * 12
    
    # Calculate P using the rearranged formula
    sip = (totalCorpus * monthly_rate) / ((1 + monthly_rate) * ((1 + monthly_rate) ** total_investments - 1))
    
    return sip




#def showlineChart(cashflow,emis,expenses,title):

def calculate_totalCorpus(P, r, n):
    """
    Calculate the future value of a SIP investment.

    Parameters:
    P : Amount invested at regular intervals (SIP amount)
    r : Expected annual rate of return (as a decimal)
    n : Total number of investments (number of years)

    """
    # Convert annual rate to monthly and total investments
    monthly_rate = r / 12
    total_investments = n * 12
    
    # Calculate future value using the SIP formula
    FV = P * (((1 + monthly_rate) ** total_investments - 1) / monthly_rate) * (1 + monthly_rate)
    
    return FV



def main():
    # Example usage
    totalCorpus = 5000000  # Future Value
    annual_rate = .12  # 12% annual return
    investment_years = 4  # Duration in years

    sip_amount = calculate_sip(totalCorpus, annual_rate, investment_years)
    print(f"Amount to be invested monthly: {sip_amount:.2f}")

    # Example usage
    sip_amount = 100000  # Amount invested monthly
    annual_rate = 0.12  # 12% annual return
    investment_years = 5  # Duration in years

    future_value = calculate_totalCorpus(sip_amount, annual_rate, investment_years)
    print(f"Future Value of SIP investment: {future_value/10**7:.2f}","cr")
    #getManageRiskPortfolio(yourTotalIncome,yourEMIs,yourRestOfExpenses,yourTotalAnnualExpenses)
    


if __name__ == '__main__':
    main()