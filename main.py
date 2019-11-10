"""
Question 2 - Programming

We're looking at your programming ability. It must not only work, it should be maintainable.

Let us assume you are a crypto investor. You have made transactions over a period of time which is logged in a CSV file. Write a command line program that does the following

Given no parameters, return the latest portfolio value per token in USD
Given a token, return the latest portfolio value for that token in USD
Given a date, return the portfolio value per token in USD on that date
Given a date and a token, return the portfolio value of that token in USD on that date
The CSV file has the following columns

timestamp: Integer number of seconds since the Epoch
transaction_type: Either a DEPOSIT or a WITHDRAWAL
token: The token symbol
amount: The amount transacted
You may obtain the exchange rates from cryptocompare where the API is free. You may write the program in any language.
"""

import sys
import time
import datetime
import pandas as pd
import cryptocompare 

# Add file path from ur local setup.
tran_file = './transactions.csv'


def retPortfolioValueTokenCurr(df, qToken, qCurr):
    df_qtoken = df[df['token'] == qToken ]
    df_qtoken_deposit = df_qtoken[df_qtoken['transaction_type'] == 'DEPOSIT']
    df_qtoken_withdrawal = df_qtoken[df_qtoken['transaction_type'] == 'WITHDRAWAL']

    withdrawal_tokens = df_qtoken_withdrawal['amount'].sum()
    deposit_tokens = df_qtoken_deposit['amount'].sum()

    portfolio_tokens = deposit_tokens - withdrawal_tokens

    token_unit_current_price = cryptocompare.get_price(qToken,curr= qCurr)
    token_price_qcurr = token_unit_current_price[qToken][qCurr]
    # portfolio worth in the requested currency for requested token 
    portfolio_value_qcurr = token_price_qcurr * portfolio_tokens
    # print the portfolio 
    print("%s tokens worth  %s : %s"%(qToken,qCurr,format(portfolio_value_qcurr, '.2f')))
    return portfolio_value_qcurr

def retAllPortfolio(df, qCurr):
    tradedTokens = tradedTokensList(df)
    for token in tradedTokens:
        retPortfolioValueTokenCurr(df,token,qCurr)


def tradedTokensList(df):
    tokens_traded = df['token'].value_counts()
    return list(tokens_traded.keys())

# the date should be in string : dd/mm/yy
# gives tiemstamp of 24 hours given a day
def returnUnixPosixTime(qdate):
    qdate_min = time.mktime(datetime.datetime.strptime(qdate, "%d/%m/%Y").timetuple())
    qdate_max = qdate_min + 86400  # 24 hours accounted since midnight
    return qdate_min, qdate_max

def retDatePortfolioValueTokenCurr(df, qdate, qToken, qCurr):
    qdate_min, qdate_max = returnUnixPosixTime(qdate)    
    df_date = df[(df['timestamp'] >= qdate_min) & (df['timestamp'] <= qdate_max)]
    retPortfolioValueTokenCurr(df_date,qToken,qCurr)

def retDateAllPortfolio(df, qdate, qCurr):
    tradedTokens = tradedTokensList(df)
    for token in tradedTokens:
        try:
            retDatePortfolioValueTokenCurr(df,qdate,token,qCurr)
        except:
            pass # Note: This is not an optimal step but makes for better code 
                 #       modularity. An optimal application will be pre-process
                 #       on data (date) and then loop over the tokens. TODO: 

if __name__ == "__main__":
    args = sys.argv[1:]
    qCurr = 'USD'
    # read the csv file 
    df = pd.read_csv(tran_file)

    # main(args)
    if len(args) >= 1:
        for param in args:
            print(param, '****')
            arr = param.split('=')
            exec(arr[0] + " = '" + arr[1] + "'")

        if 'token' in locals() and token:
            # 2 - Passed Token
            retPortfolioValueTokenCurr(df, qToken=token, qCurr=qCurr)   # single token in USD
        if 'qdate' in locals() and qdate:
            # 3 - Passed Date
            retDateAllPortfolio(df, qdate, qCurr=qCurr)
        if 'token' in locals() and 'qdate' in locals() and token and qdate:
            # 4 - Passed Date and Token
            retDatePortfolioValueTokenCurr(df, qdate, qToken=token, qCurr=qCurr)
    else:
        # 1 - No Values Passed
        retAllPortfolio(df, qCurr=qCurr)# all tokens in USD