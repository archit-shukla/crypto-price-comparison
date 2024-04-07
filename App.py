import csv


def readCSV(filename):
  lists=[]   
  with open (filename, newline='', encoding="utf-8") as file:
        reader=csv.reader(file)
        header=next(reader)
        
        for lines in reader:
            dict1 = {}
            for i in range(0,len(header)):
                dict1[header[i]] = lines[i]
            lists.append(dict1)
  
  return lists

def openDate(dict):
  for i,j in dict.items():
    if i=="Date":
      return j[0:4]
      
def openPrices(dict):
  for x,y in dict.items():
   if x=='Price':
    return y


def openPrices1(dict):
  for x,y in dict.items():
   if x=='Price1':
    return y


def filter(list_of_dictionaries, low, high):
  result = []
  for i in range (0,len(list_of_dictionaries)):
    if int(low) <= int(openDate(list_of_dictionaries[i])) < int(high):
      result.append(list_of_dictionaries[i])
  return result


def datat(dict):
  for i,j in dict.items():
   if i=='Date':
    return j


ALL_DATA=readCSV('Bitcoin.csv')
def dataBTC(di):
  year1=int(di["year_start"])
  year2=int(di["year_end"])
  result=[]
  dates_result=[]
  prices=[]
  for i in range (year1,year2+1):
    new_Dict={}
    dates= filter(ALL_DATA,i,i+1)
    for i in dates:
      dates_result.append(datat(i))
      prices.append(openPrices(i))
  new_Dict["x"]=dates_result
  new_Dict["y"]=prices
  new_Dict["type"]='scatter'
  result.append(new_Dict)
  return result

def dataETH(dict):
  year1=int(dict["year_start"])
  year2=int(dict["year_end"])
  result=[]
  dates_result=[]
  prices=[]
  for i in range (year1,year2+1):
    new_Dict={}
    dates= filter(ALL_DATA,i,i+1)
    for i in dates:
      dates_result.append(datat(i))
      prices.append(openPrices1(i))
  new_Dict["x"]=dates_result
  new_Dict["y"]=prices
  new_Dict["type"]='scatter'
  result.append(new_Dict)
  return result

def dataCompare(dict):
  year1=int(dict["year_start"])
  year2=int(dict["year_end"])
  result=[]
  prices1=[]
  prices2=[]
  dates_result=[]
  for i in range(year1,year2+1):
    newDict1={}
    newDict2={}
    dates=filter(ALL_DATA,i,i+1)
    for i in dates:
      dates_result.append(datat(i))
      prices1.append(openPrices(i))
      prices2.append(openPrices1(i))
  newDict1["x"]=str(dates_result)
  newDict1["y"]=prices1
  newDict1["name"]='Bitcoin'
  newDict1["type"]='bar'
  newDict1["x"]=str(dates_result)
  newDict2["y"]=prices2
  newDict2["name"]='Ethereum'
  newDict2["type"]='bar'
  result.append(newDict1)
  result.append(newDict2)
  return result

def dataCompare1(dict):
  year1=int(dict["year_start"])
  year2=int(dict["year_end"])
  result=[]
  prices1=[]
  prices2=[]
  dates_result=[]
  for i in range(year1,year2+1):
    newDict1={}
    newDict2={}
    dates=filter(ALL_DATA,i,i+1)
    for i in dates:
      dates_result.append(datat(i))
      prices1.append(openPrices(i))
      prices2.append(openPrices1(i))
  newDict1["type"]='scatter'
  newDict1["mode"]='lines'
  newDict1["name"]='Bitcoin'
  newDict1["x"]=dates_result
  newDict1["y"]=prices1
  newDict2["type"]='scatter'
  newDict2["mode"]='lines'
  newDict2["name"]='Ethereum'
  newDict2["x"]=dates_result
  newDict2["y"]=prices2
  result.append(newDict1)
  result.append(newDict2)
  return result
    
    