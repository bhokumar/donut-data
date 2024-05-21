import pdfkit
import random
import json
# HTML content to be converted to PDF
def generateSamplePdf(outPutDir, jsonOutputDirectory, index):
    country = 'Republic of India Passport'
    # Generate 9 digit random passport number
    passportNo = 'A' + ''.join([str(random.randint(0, 9)) for _ in range(6)])
    passportType = 'P'
    # Generate random surname
    surname = random.choice(['Sharma', 'Verma', 'Singh', 'Gupta', 'Kumar', 'Patel', 'Reddy', 'Rathore', 'Mishra'])
    # Generate random given name
    given_name = random.choice(['Rohan', 'Aarav', 'Aryan', 'Anaya', 'Ishaan', 'Anika', 'Aisha', 'Amit', 'Riya'])
    nationality = 'Indian'
    gender = random.choice(['M', 'F'])
    # Generate date of birth in format 01-Jan-1990
    date_of_birth = f'{random.randint(1, 28):02}-' \
                    f'{random.choice(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}-' \
                    f'{random.randint(1950, 2000)}'
    # Generate place of birth
    place_of_birth = f'{random.choice(["New Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru", "Hyderabad", "Pune", "Ahmedabad", "Jaipur"])}' \
                        f', {random.choice(["India", "USA", "UK", "Canada", "Australia", "UAE", "Singapore", "Malaysia", "Germany"])}'

    date_of_issue = f'{random.randint(1, 28):02}-' \
                    f'{random.choice(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}-' \
                    f'{random.randint(2010, 2020)}'
    
    date_of_expiry = f'{random.randint(1, 28):02}-' \
                    f'{random.choice(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}-' \
                    f'{random.randint(2020, 2030)}'
    place_of_issue = f'{random.choice(["New Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru", "Hyderabad", "Pune", "Ahmedabad", "Jaipur"])}'

    # prepare json file
    # country, passportNo, passportType, surname, given_name, nationality, gender, date_of_birth, place_of_birth, date_of_issue, date_of_expiry, place_of_issue
    json_content = {
        "country": country,
        "passportNo": passportNo,
        "passportType": passportType,
        "surname": surname,
        "name": given_name,
        "nationality": nationality,
        "gender": gender,
        "dateOfBirth": date_of_birth,
        "placeOfBirth": place_of_birth,
        "dateOfIssue": date_of_issue,
        "dateOfExpiry": date_of_expiry,
        "placeOfIssue": place_of_issue
    }
    json_string = json.dumps(json_content)

    # Write JSON to file
    with open(f'{jsonOutputDirectory}/passport_{index}.json', 'w') as json_file:
        json_file.write(json_string)

    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dummy passports</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .passport {{
                width: 700px;
                height: 500px;
                padding: 20px;
                background-color: #002060;
                color: #ffd700;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
                border-radius: 10px;
                position: relative;
            }}
            .passport-header {{
                text-align: center;
                border-bottom: 2px solid #ffd700;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }}
            .passport-header h1 {{
                margin: 0;
                font-size: 28px;
            }}
            .passport-header h2 {{
                margin: 5px 0 0;
                font-size: 22px;
                font-weight: normal;
            }}
            .passport-photo {{
                position: absolute;
                top: 150px;
                right: 50px;
                width: 100px;
                height: 120px;
                background-color: #ccc;
                border: 2px solid #ffd700;
            }}
            .passport-photo img {{
                width: 100%;
                height: 100%;
                object-fit: cover;
            }}
            .passport-details {{
                color: #fff;
                padding-left: 20px;
            }}
            .detail {{
                margin-bottom: 10px;
            }}
            .detail span {{
                font-weight: bold;
                width: 150px;
                display: inline-block;
                color: #ffd700;
            }}
        </style>
    </head>
    <body>
        <div class="passport">
            <div class="passport-header">
                <h1>{}</h1>
            </div>
            <div class="passport-details">
                <div class="detail"><span>Passport No:</span> {}</div>
                <div class="detail"><span>Type:</span> {}</div>
                <div class="detail"><span>Surname:</span> {}</div>
                <div class="detail"><span>Given Name:</span> {}</div> 
                <div class="detail"><span>Nationality:</span> {}</div>
                <div class="detail"><span>Sex:</span> {}</div>
                <div class="detail"><span>Date of Birth:</span> {}</div>
                <div class="detail"><span>Place of Birth:</span> {}</div>
                <div class="detail"><span>Date of Issue:</span> {}</div>
                <div class="detail"><span>Date of Expiry:</span> {}</div>
                <div class="detail"><span>Place of Issue:</span> {}</div>
            </div>
            <div class="passport-photo">
                <img src="https://picsum.photos/100/120" alt="Dummy Photo">
            </div>
        </div>
    </body>
    </html>
    '''.format(country, passportNo, passportType, surname, given_name, nationality, gender, date_of_birth, place_of_birth, date_of_issue, date_of_expiry, place_of_issue)

    # Path to wkhtmltopdf executable
    path_wkhtmltopdf = r'/usr/local/bin/wkhtmltopdf'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    # Convert HTML to PDF
    pdfkit.from_string(html_content, f'{outPutDir}/passport_{index}.pdf', configuration=config)

def main():
    outPutDir = './docs/input/invoices/Dataset with valid information'
    jsonOutputDirectory = '../sparrow-ui/docs/json/key'
    for i in range(1000):
        generateSamplePdf(outPutDir, jsonOutputDirectory, i)

if __name__ == '__main__':
    main()
