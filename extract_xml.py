import os
import xml.etree.ElementTree as ET
import csv

XML_URL = os.environ['XML_URL', '']
CSV_URL = os.environ['CSV_URL', '']


namespace = {'ns': 'urn:iso:std:iso:20022:tech:xsd:pain.008.001.02'}

tree = ET.parse(XML_URL)
root = tree.getroot()

with open(CSV_URL, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(["Debtor Name", "IBAN"])
    
    for drct_dbt_tx in root.findall(".//ns:DrctDbtTxInf", namespace):
        nm_element = drct_dbt_tx.find(".//ns:Dbtr/ns:Nm", namespace)
        debtor_name = nm_element.text.strip() if nm_element is not None and nm_element.text else "Not Provided"

        iban_element = drct_dbt_tx.find(".//ns:DbtrAcct/ns:Id/ns:IBAN", namespace)
        iban = iban_element.text.strip() if iban_element is not None and iban_element.text else "Not Provided"

        print(f"Extracted: Name = '{debtor_name}', IBAN = '{iban}'")

        writer.writerow([debtor_name, iban])