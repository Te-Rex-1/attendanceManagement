import firebase_admin
from firebase_admin import credentials, db
import pandas as pd

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\tar30\OneDrive\Desktop\mini Projects\attendanceManagement\ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://mini-project-6e128-default-rtdb.firebaseio.com/"
})

# Load CSV file
#csv_file = "C:\Users\tar30\OneDrive\Desktop\mini Projects\attendanceManagement\StudentDetails\StudentDetails.csv"
csv_file= r"C:\Users\tar30\OneDrive\Desktop\mini Projects\attendanceManagement\StudentDetails\StudentDetails.csv"

data = pd.read_csv(csv_file)

# Reference the Firebase database
ref = db.reference("users")  # "users" is the root node for this example

# Update data in Firebase
for index, row in data.iterrows():
    user_id = row["Enrollment"]  # Assume 'id' is the unique identifier
    user_data = {
        "Enrollment": row["Enrollment"],
        "Name": row["Name"],
        "Date": row["Date"],
        "Time":row["Time"]
    }
    ref.child(str(user_id)).update(user_data)  # Update data for the given user_id

print("Data has been updated successfully in Firebase.")
