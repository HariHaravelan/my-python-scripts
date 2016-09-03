from googlefinance import getQuotes
from colored import fg, bg, attr
import time
import os
     
select      =[1,1,1]
STOCK       =['GOOGL','TWX','AMD']
iPRICE      =[26.81,77.24,6.42]
SHARES      =[49,25,3]
THRESHOLD   =[500,80,1]
Tceiling    =[]
Tfloor      =[]
     
def stock():
  body = ''
  for i in range(len(STOCK)):
    cPRICE = getQuotes(STOCK[i])[0]['LastTradeWithCurrency']
    PRFT = float(cPRICE)-float(iPRICE[i])
    PQ = PRFT*SHARES[i]
    TOTAL = float(SHARES[i])*float(cPRICE)
    ENDc = attr(0)
     
    if select[i] == 1:
      if THRESHOLD[i] <= PQ:
        ACTION = "SELL"
        BEGINc = ('%s%s' % (fg(46),bg(20)))
      elif 0.00 <= PQ < MARGIN[i]:
        ACTION = "HOLD"
        BEGINc = ('%s%s' % (fg(6),bg(20)))
      else:
        ACTION = "SWIM"
        BEGINc = ('%s%s' % (fg(9),bg(20)))
    else:
      BEGINc = ('%s%s' % (fg(15),bg(8)))
     
      body += ("\t%s%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s%s\n" % (BEGINc,STOCK[i],SHARES[i],iPRICE[i],cPRICE,PRFT,PQ,THRESHOLD[i],TOTAL,ACTION,ENDc))
     
  head = ("\n\n\033[4m\t%s%sSYM\tQTY\tINIT\tCURR\tPRFT\tP*Q\tTHRES\tTOTAL\tRCMND\033[0m%s\n" % (fg(16),bg(15),attr(0)))
  tail = "\t"+time.asctime( time.localtime(time.time()) )+"\n\n"
     
  print (head,body,tail)
     
     
stock()
