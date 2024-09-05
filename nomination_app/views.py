from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from .forms import NomineeForm

def generate_pdf(form_data):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Add content to the PDF
    p.drawString(100, 800, "Nomination Form")
    p.drawString(100, 780, f"Subscriber Name: {form_data['subscriber_name']}")
    p.drawString(100, 760, f"Marital Status: {form_data['marital_status']}")
    p.drawString(100, 740, f"Account Number: {form_data['account_number']}")
    
    # Add nominees
    p.drawString(100, 700, "Nominee Details")
    p.drawString(100, 680, f"Nominee Name: {form_data['nominee_name']}")
    p.drawString(100, 660, f"Nominee Address: {form_data['nominee_address']}")
    p.drawString(100, 640, f"Aadhar Number: {form_data['nominee_aadhar']}")
    p.drawString(100, 620, f"Relationship with Subscriber: {form_data['nominee_relationship']}")

    p.drawString(100, 580, f"Place: {form_data['place']}")
    p.drawString(100, 560, f"Date: {form_data['date']}")

    # Save the PDF to the buffer
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer
    pdf = buffer.getvalue()
    buffer.close()

    return pdf

def nomination_form_view(request):
    if request.method == 'POST':
        form = NomineeForm(request.POST)
        if form.is_valid():
            # Get the form data
            form_data = form.cleaned_data

            # Generate PDF
            pdf = generate_pdf(form_data)

            # Email the generated PDF
            email = EmailMessage(
                'Nomination Form',
                'Here is your filled nomination form.',
                'from@example.com',  # Replace with your email
                [form_data.get('subscriber_email')]  # Send to user's email
            )
            email.attach('FormB_Nomination.pdf', pdf, 'application/pdf')
            email.send()

            return redirect('success')  # Redirect to a success page

    else:
        form = NomineeForm()

    return render(request, 'nomination_form.html', {'form': form})
