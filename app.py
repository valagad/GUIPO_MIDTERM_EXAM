from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def contact_form():
    return render_template('contact_form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        subject = request.form.get('subject')
        other_subject = request.form.get('other_subject')
        preferred_methods = request.form.getlist('preferred_contact')
        agreement = request.form.get('agreement')

        errors = []

        if not name:
            errors.append("Name is required")
        if not email:
            errors.append("Email is required")
        if not phone or not phone.isdigit():
            errors.append("Valid phone number is required")
        if not message:
            errors.append("Message is required")
        if not agreement:
            errors.append("You must agree to the term and condition")
        if subject == "Other":
            errors.append("Please specify the subject")
        else:
            subject = other_subject

        if errors:
            return render_template(
                'contact_form.html',
                errors=errors,
                name=name,
                email=email,
                phone=phone,
                message=message,
                subject=subject,
                preferred_methods=preferred_methods
            )
        return render_template(
            'confirmation.html',name=name, email=email, phone=phone, message=message, subject=subject, preferred_methods=','.join(preferred_methods), agreement='Yes' if agreement else'No'
         )

if __name__ == '__main__':
    app.run(debug=True)