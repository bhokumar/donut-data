import pdfkit

# HTML content to be converted to PDF
passportTitle = 'Dummy Indian Passport'
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{passportTitle}</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .passport {
            width: 700px;
            height: 500px;
            padding: 20px;
            background-color: #002060;
            color: #ffd700;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            position: relative;
        }
        .passport-header {
            text-align: center;
            border-bottom: 2px solid #ffd700;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .passport-header h1 {
            margin: 0;
            font-size: 28px;
        }
        .passport-header h2 {
            margin: 5px 0 0;
            font-size: 22px;
            font-weight: normal;
        }
        .passport-photo {
            position: absolute;
            top: 150px;
            right: 50px;
            width: 100px;
            height: 120px;
            background-color: #ccc;
            border: 2px solid #ffd700;
        }
        .passport-photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .passport-details {
            color: #fff;
            padding-left: 20px;
        }
        .detail {
            margin-bottom: 10px;
        }
        .detail span {
            font-weight: bold;
            width: 150px;
            display: inline-block;
            color: #ffd700;
        }
    </style>
</head>
<body>
    <div class="passport">
        <div class="passport-header">
            <h1>Republic of India</h1>
            <h2>Passport</h2>
        </div>
        <div class="passport-details">
            <div class="detail"><span>Passport No:</span> A1234567</div>
            <div class="detail"><span>Type:</span> P</div>
            <div class="detail"><span>Surname:</span> Sharma</div>
            <div class="detail"><span>Given Name:</span> Rohan</div>
            <div class="detail"><span>Nationality:</span> Indian</div>
            <div class="detail"><span>Sex:</span> M</div>
            <div class="detail"><span>Date of Birth:</span> 01-Jan-1990</div>
            <div class="detail"><span>Place of Birth:</span> New Delhi, India</div>
            <div class="detail"><span>Date of Issue:</span> 01-Jan-2020</div>
            <div class="detail"><span>Date of Expiry:</span> 01-Jan-2030</div>
            <div class="detail"><span>Place of Issue:</span> New Delhi</div>
        </div>
        <div class="passport-photo">
            <img src="https://picsum.photos/100/120" alt="Dummy Photo">
        </div>
    </div>
</body>
</html>
'''

# Path to wkhtmltopdf executable
path_wkhtmltopdf = r'/usr/local/bin/wkhtmltopdf'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Convert HTML to PDF
pdfkit.from_string(html_content, 'output.pdf', configuration=config)
