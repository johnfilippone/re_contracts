import json
import propmine


#pick comps that are similar in sqft and take median of $/sqft
def getARV1(principal, comps):
    principal_sqft = float(principal["finishedSqFt"])
    threshhold = 100
    priceSum = 0
    priceNum = 0
    for comp in comps:
        sqft = float(comp["finishedSqFt"])
        if principal_sqft - sqft <= threshhold and sqft - principal_sqft <= threshhold:
            price = float(comp["lastSoldPrice"]["#text"])/float(comp["finishedSqFt"])
            priceSum += price
            priceNum += 1
    if priceNum > 2:
        return (priceSum/priceNum)*principal_sqft
    else:
	return 0

#similar to method 1 except allow more sqft difference on the bigger side
def getARV2(principal, comps):
    principal_sqft = float(principal["finishedSqFt"])
    threshhold1 = 100
    threshhold2 = 500
    priceSum = 0
    priceNum = 0
    for comp in comps:
        sqft = float(comp["finishedSqFt"])
        if (principal_sqft - sqft >= 0 and principal_sqft - sqft <= threshhold1) or (sqft - principal_sqft > 0 and sqft - principal_sqft <= threshhold2):
            price = float(comp["lastSoldPrice"]["#text"])/float(comp["finishedSqFt"])
            priceSum += price
            priceNum += 1
    if priceNum > 2:
        return (priceSum/priceNum)*principal_sqft
    else:
	return 0

def get_price(address, citystatezip):
    property_data = propmine.getPropertyData(address, citystatezip)
    principal = property_data[0]
    comps = property_data[1]

    price = getARV1(principal, comps)
    if price == 0:
	price = getARV2(principal, comps)
    return price
