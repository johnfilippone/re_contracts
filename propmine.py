import urllib
import xmltodict

zws_id = "X1-ZWz1gbsxf0iqyz_a57uf"
getDeepSearch = "http://www.zillow.com/webservice/GetDeepSearchResults.htm"
getDeepComps = "http://www.zillow.com/webservice/GetDeepComps.htm"
# get params
#address = "44 Pitcher Ave"
#citystatezip = "Medford,MA"
#compaddress = "133 Monument St"
#principal_sqft = 3916

def getPropertyData(address, citystatezip):
    # get zpid
    apiurl = getDeepSearch + "?" + urllib.urlencode({"zws-id":zws_id,"address":address,"citystatezip":citystatezip})
    result = urllib.urlopen(apiurl)
    data = result.read()
    parsed = xmltodict.parse(data)
    zpid = parsed["SearchResults:searchresults"]["response"]["results"]["result"]["zpid"]

    # get comps
    apiurl = getDeepComps + "?" + urllib.urlencode({"zws-id":zws_id,"zpid":zpid,"count":25})
    result = urllib.urlopen(apiurl)
    data = result.read()
    parsed = xmltodict.parse(data)
    principal = parsed["Comps:comps"]["response"]["properties"]["principal"]
    comps = parsed["Comps:comps"]["response"]["properties"]["comparables"]["comp"]
    return (principal, comps)

"""
schema for property info
{
    "zpid": "56277671",
    "links": {
        "homedetails": "https://www.zillow.com/homedetails/44-Pitcher-Ave-Medford-MA-02155/56277671_zpid/",
        "graphsanddata": "http://www.zillow.com/homedetails/44-Pitcher-Ave-Medford-MA-02155/56277671_zpid/#charts-and-data",
        "mapthishome": "http://www.zillow.com/homes/56277671_zpid/",
        "comparables": "http://www.zillow.com/homes/comps/56277671_zpid/"
    },
    "address": {
        "street": "44 Pitcher Ave",
        "zipcode": "02155",
        "city": "MEDFORD",
        "state": "MA",
        "latitude": "42.422366",
        "longitude": "-71.140742"
    },
    "taxAssessmentYear": "2017",
    "taxAssessment": "646400.0",
    "yearBuilt": "1910",
    "lotSizeSqFt": "6534",
    "finishedSqFt": "3916",
    "bedrooms": "6",
    "totalRooms": "12",
    "lastSoldDate": "03/03/1992",
    "lastSoldPrice": {
        "@currency": "USD",
        "#text": "122000"
    },
    "zestimate": {
        "amount": {
            "@currency": "USD",
            "#text": "945239"
        },
        "last-updated": "03/31/2018",
        "oneWeekChange": {
            "@deprecated": "true"
        },
        "valueChange": {
            "@duration": "30",
            "@currency": "USD",
            "#text": "-1762"
        },
        "valuationRange": {
            "low": {
                "@currency": "USD",
                "#text": "888525"
            },
            "high": {
                "@currency": "USD",
                "#text": "992501"
            }
        },
        "percentile": "99"
    },
    "localRealEstate": {
        "region": {
            "@name": "Medford",
            "@id": "53250",
            "@type": "city",
            "zindexValue": "466,300",
            "links": {
                "overview": "http://www.zillow.com/local-info/MA-Medford/r_53250/",
                "forSaleByOwner": "http://www.zillow.com/medford-ma/fsbo/",
                "forSale": "http://www.zillow.com/medford-ma/"
            }
        }
    }
}
"""
