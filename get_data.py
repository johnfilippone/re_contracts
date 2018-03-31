import urllib
import json
import xmltodict

def getARV(principal_sqft, comps, score):
    priceSum = 0
    priceNum = 0
    for comp in comps:
        compScore = float(comp["@score"])
        if compScore >= score:
            price = float(comp["lastSoldPrice"]["#text"])/float(comp["finishedSqFt"])
            priceSum += price
            priceNum += 1
    if priceNum > 0:
        print str((priceSum/priceNum)*principal_sqft) + " ----- " + str(priceNum)
    else:
        print "no comps with score of at least " + str(score)

getDeepSearch = "http://www.zillow.com/webservice/GetDeepSearchResults.htm"
getDeepComps = "http://www.zillow.com/webservice/GetDeepComps.htm"

# get params
zws_id = "X1-ZWz1gbsxf0iqyz_a57uf"
address = "44 Pitcher Ave"
citystatezip = "Medford,MA"

# get zpid
call = getDeepSearch + "?" + urllib.urlencode({"zws-id":zws_id,"address":address,"citystatezip":citystatezip})
result = urllib.urlopen(call)
data = result.read()
parsed = xmltodict.parse(data)
zpid = parsed["SearchResults:searchresults"]["response"]["results"]["result"]["zpid"]

# get comps
call = getDeepComps + "?" + urllib.urlencode({"zws-id":zws_id,"zpid":zpid,"count":25})
result = urllib.urlopen(call)
data = result.read()
parsed = xmltodict.parse(data)
comps = parsed["Comps:comps"]["response"]["properties"]["comparables"]["comp"]
principal_sqft = float(parsed["Comps:comps"]["response"]["properties"]["principal"]["finishedSqFt"])

# arv analysis
for i in range(20):
    getARV(principal_sqft, comps, i)



# print comps
"""
for i, comp in enumerate(comps):
    score = int(float(comp["@score"]))
    if score > 12:
        print "########## COMP " + str(i) + " ########"
        print "score= " + comp["@score"]
        print "sqft= " + comp["finishedSqFt"]
        print comp["address"]["street"] + " " + comp["address"]["city"]
        print "lastsold= $" + comp["lastSoldPrice"]["#text"] + " on " + comp["lastSoldDate"]
"""


#print addrs
"""
addrs = []
for comp in comps:
    addrs.append(" ".join(comp["address"]["street"].split(" " )[1:]) + " " + comp["address"]["city"])

#print addrs
addrs.sort()
for addr in addrs:
    print addr
"""

