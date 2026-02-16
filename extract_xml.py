import xml.etree.ElementTree as ET
import csv

XML_URL = '/home/eneko/Documentos/workspaces/arratek-workspace/aplicaciones/sme-app/wetransfer_archivos-pendientes-del-sindicato-medico-de-gipuzkoa_2025-01-29_0948/Afiliados SMG a 28-01-2025 - B.Sabadell.XML'
CSV_URL = '/home/eneko/Documentos/workspaces/arratek-workspace/aplicaciones/extract_xml/iban.csv'

# Define the namespace
ns = {'ns': 'urn:iso:std:iso:20022:tech:xsd:pain.008.001.02'}

# Load XML file
tree = ET.parse(XML_URL)  # Update with your actual file path
root = tree.getroot()

# Open CSV file for writing
with open(CSV_URL, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(["Debtor Name", "IBAN"])
    
    # Find all direct debit transactions
    for drct_dbt_tx in root.findall(".//ns:DrctDbtTxInf", ns):
        # Extract Debtor Name
        nm_element = drct_dbt_tx.find(".//ns:Dbtr/ns:Nm", ns)
        debtor_name = nm_element.text.strip() if nm_element is not None and nm_element.text else "Not Provided"

        # Extract IBAN
        iban_element = drct_dbt_tx.find(".//ns:DbtrAcct/ns:Id/ns:IBAN", ns)
        iban = iban_element.text.strip() if iban_element is not None and iban_element.text else "Not Provided"

        # Debugging: Print extracted values to check
        print(f"Extracted: Name = '{debtor_name}', IBAN = '{iban}'")

        # Write to CSV
        writer.writerow([debtor_name, iban])

