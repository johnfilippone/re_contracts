import os
import zipfile
import gen_price

contractTemplate = "/home/filippone/Desktop/Real Estate/ContractTemplates/python/markedupOffer.odt"
newContractsLocation = "/home/filippone/Desktop/Real Estate/newContracts/"

#get var values
address = "2 Earhard St Unit 1103"
citystatezip = "Cambridge,MA"
price = gen_price.get_price(address, citystatezip)
seller_name = "Alex Jones"
folder = address.replace(" ", "_")

#make new copy of unziped template
extractLocation = newContractsLocation + folder + "/extracted"
zip_ref = zipfile.ZipFile(contractTemplate, 'r')
zip_ref.extractall(extractLocation)
zip_ref.close()

#read content file
templateContent = ""
with open(extractLocation + "/content.xml", "r") as template:
    templateContent = template.read()

#string replace in the proper values
newContent = templateContent
newContent.replace("##SellerLine1##", seller_name)
newContent.replace("##SellerLine2##", "")

#write new content to the file
with open(extractLocation + "/content.xml", "w") as newFile:
    newFile.write(newContent)

#zip it into odt
zip_ref = zipfile.ZipFile(newContractsLocation + folder + "/" + folder + "_Offer.odt", 'w', zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk(extractLocation):
    for file in files:
        zip_ref.write(os.path.join(root, file))
zip_ref.close()
