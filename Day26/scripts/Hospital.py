import mysql.connector

class Hospital:
    def __init__(self, host, port, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def add_doctor(self, doctors_id, name, specialty):
        query = "INSERT INTO doctors (id, name, specialty) VALUES (%s, %s, %s)"
        values = (doctors_id, name, specialty)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_doctors(self):
        query = "SELECT * FROM doctors"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def add_patient(self, name, age, gender):
        query = "INSERT INTO patients (name, age, gender) VALUES (%s, %s, %s)"
        values = (name, age, gender)
        self.cursor.execute(query, values)
        self.connection.commit()

    def details_patient(self, patient_id, doctor_id):
        query = "SELECT id, name, age, gender, doctor_id, doctor_name FROM patients WHERE id = %s AND doctor_id = %s"
        values = (patient_id, doctor_id)
        self.cursor.execute(query, values)
        row = self.cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "name": row[1],
                "age": row[2],
                "gender": row[3],
                "doctor_id": row[4],
                "doctor_name": row[5]
            }
        else:
            return None
        
    def get_patients(self):
        query = "SELECT * FROM patients"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def assign_doctor_to_patient(self, patient_id, doctor_id):
        query = "UPDATE patients SET doctor_id = %s WHERE id = %s"
        values = (doctor_id, patient_id)
        self.cursor.execute(query, values)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            # Fetch the doctor's name to update in the patient's record
            self.cursor.execute("SELECT name FROM doctors WHERE id = %s", (doctor_id,))
            doctor = self.cursor.fetchone()
            if doctor:
                doctor_name = doctor[0]
                update_query = "UPDATE patients SET doctor_name = %s WHERE id = %s"
                update_values = (doctor_name, patient_id)
                self.cursor.execute(update_query, update_values)
                self.connection.commit()
                return True
        return False
# Now lets add console inputs to add doctors and patients
def main():
    print("#################### Welcome to the Hospital Management System ####################")
    print("########### ------------------  Connecting to the database... ------------------ ###########")
    hospital = Hospital(host="localhost", port=3306, user="root", password="Root", database="hospital")
    print("########### ------------------ Connected to the database. ------------------ ###########")
    print("Please choose an option:")
    while True:
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Assign Doctor to Patient")
        print("4. View Doctors")
        print("5. View Patients")
        print("6. Exit")
        choice = input("Enter your choice: ")
        # add doctor option
        if choice == '1':
            doctors_id = int(input("Enter Doctor ID: "))
            name = input("Enter Doctor Name: ")
            specialty = input("Enter Doctor Specialty: ")
            hospital.add_doctor(doctors_id, name, specialty)
            print("-------------------------------")
            print("Doctor added successfully.")
            print("-------------------------------")
        # Add patient option
        elif choice == '2':
            name = input("Enter Patient Name: ")
            age = int(input("Enter Patient Age: "))
            gender = input("Enter Patient Gender: ")
            hospital.add_patient(name, age, gender)
            print("-------------------------------")
            print("Patient added successfully.")
            print("-------------------------------")
        # Assign doctor to patient option
        elif choice == '3':
            patient_id = int(input("Enter Patient ID: "))
            doctor_id = int(input("Enter Doctor ID: "))
            if hospital.assign_doctor_to_patient(patient_id, doctor_id):
                print("-------------------------------")
                print("Doctor assigned to patient successfully.")
                print("-------------------------------")
            else:
                print("Failed to assign doctor. Please check the IDs.")
        # View doctors option
        elif choice == '4':
            doctors = hospital.get_doctors()
            for doc in doctors:
                print("-------------------------------")
                print(f"ID: {doc[0]}, Name: {doc[1]}, Specialty: {doc[2]}")
                print("-------------------------------")
        # View patients option
        elif choice == '5':
            patients = hospital.get_patients()
            for pat in patients:
                print("-------------------------------")
                print(f"ID: {pat[0]}, Name: {pat[1]}, Age: {pat[2]}, Gender: {pat[3]}, Doctor ID: {pat[4]}, Doctor Name: {pat[5]}")
                print("-------------------------------")
        # Exit option
        elif choice == '6':
            hospital.close()
            print("Exiting...")
            break
main()