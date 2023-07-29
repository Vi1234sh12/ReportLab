from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from pdf_generator import PDFGenerator

app = Flask(__name__)

# Replace 'your_database_uri' with your actual database connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/application'
db = SQLAlchemy(app)

# Define the 'tweets' table model and map it to the existing table
class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True)
    userhandle = db.Column(db.String(100), nullable=False)
    tweetdate = db.Column(db.String(100), nullable=False)
    tweet = db.Column(db.Text, nullable=False)
    profile_image = db.Column(db.String(200), nullable=False)

# Create a function to initialize the database
def initialize_database():
    with app.app_context():
        db.create_all()

# Call the function to initialize the database when the app starts
initialize_database()

# Route to display data on the frontend
@app.route('/')
def index():
    # Fetch data from the database
     # Fetch data from the database
    tweets = Tweet.query.all()
    

    # Pass the data to the frontend template
    return render_template('index.html', tweets=tweets)


# Route to generate the PDF
@app.route('/generate_pdf')
def generate_pdf():
    # Fetch data from the database
    tweets = Tweet.query.all()

    # Prepare data for the PDF table
    pdf_data = [['Name', 'Tweet Date', 'Tweet']]
    for tweet in tweets:
        pdf_data.append([tweet.userhandle, str(tweet.tweetdate), tweet.tweet])

    # Replace 'pdf_output_path' with the desired path for the generated PDF
    pdf_output_path = 'output/tweets_report.pdf'

    # Generate the PDF using PDFGenerator
    pdf_generator = PDFGenerator(pdf_output_path)
    pdf_generator.create_pdf(data=pdf_data)
    return f"PDF generated at {pdf_output_path}"

if __name__ == '__main__':
    app.run(debug=True)
