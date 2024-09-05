from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_nomination_pdf(subscriber_data, nominees_data):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    # Define starting positions
    x = 100
    y = 750
    
    # Add subscriber details
    p.drawString(x, y, f"Name: {subscriber_data['name']}")
    p.drawString(x, y - 15, f"Marital Status: {subscriber_data['marital_status']}")
    p.drawString(x, y - 30, f"Account Number: {subscriber_data['account_number']}")
    
    # Adjust y for nominees
    y -= 60
    
    # Add nominees details
    for i, nominee in enumerate(nominees_data):
        p.drawString(x, y, f"Nominee {i+1} Name: {nominee['name']}")
        p.drawString(x, y - 15, f"Address: {nominee['permanent_address']}")
        p.drawString(x, y - 30, f"Aadhar Number: {nominee['aadhar_number']}")
        p.drawString(x, y - 45, f"Relationship: {nominee['relationship']}")
        p.drawString(x, y - 60, f"Age: {nominee['age']}")
        p.drawString(x, y - 75, f"Share: {nominee['share']}%")
        p.drawString(x, y - 90, f"Contingencies: {nominee.get('contingencies', '')}")
        p.drawString(x, y - 105, f"Pass On Details: {nominee.get('nominee_pass_on_details', '')}")
        p.drawString(x, y - 120, f"Minor Guardian: {nominee.get('minor_guardian', '')}")
        
        # Adjust y for next nominee
        y -= 150
    
    # Finalize the PDF
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return buffer
