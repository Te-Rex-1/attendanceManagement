import firebase_admin
from firebase_admin import credentials, db
import pandas as pd
def upload(file_path):
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate(r"C:/Users/tar30/OneDrive/Desktop/mini Projects/attendanceManagement\ServiceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://mini-project-6e128-default-rtdb.firebaseio.com/"
    })

    # Load CSV file
    #csv_file = r"C:\Users\tar30\OneDrive\Desktop\mini Projects\attendanceManagement\StudentDetails\StudentDetails.csv"
    csv_file= file_path

    data = pd.read_csv(csv_file)

    # Reference the Firebase databasez
    # Reference to the Firebase database
    # Reference to the Firebase database
    # Reference to the Firebase database
    ref = db.reference("subjects")  # "subjects" is the root node

    # Update data in Firebase
    for index, row in data.iterrows():
        user_id = row["Enrollment"]  # Unique identifier for each user (e.g., Enrollment)
        #subject_name = row["Subject"]  # Subject name (e.g., Math, Chemistry)
        user_data = {
            "Enrollment": row["Enrollment"],
            "Name": row["Name"],  # Assuming you have a "Name" column in your CSV
            "Date": row["Date"],
            "Time": row["Time"]
        }

        # Reference to the subject node
        #subject_ref = ref.child(subject_name)  # Reference to a specific subject

        # Create or update the user details under the subject node
        ref.child(str(user_id)).update(user_data)  # This will add or update the user data for the specific subject
       # subject_ref.child(str(user_id)).update(user_data)




    print("Data has been updated successfully in Firebase.")
