import tkinter as tk
from tkinter import ttk
import numpy as np
import joblib

# Load the trained model
model = joblib.load('california_housing_model.pkl')

# Function to handle the prediction
def predict():
    try:
        # Retrieve input values
        med_inc = float(med_inc_entry.get())
        house_age = float(house_age_entry.get())
        ave_rooms = float(ave_rooms_entry.get())
        ave_bedrms = float(ave_bedrms_entry.get())
        population = float(population_entry.get())
        ave_occup = float(ave_occup_entry.get())
        latitude = float(latitude_entry.get())
        longitude = float(longitude_entry.get())

        # Create a numpy array with the input values
        input_data = np.array([[med_inc, house_age, ave_rooms, ave_bedrms,
                                population, ave_occup, latitude, longitude]])

        # Make prediction
        prediction = model.predict(input_data)
        result_label.config(text=f"Predicted Median House Value: ${prediction[0] * 100000:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numerical values.")

# Create the main window
root = tk.Tk()
root.title("California Housing Price Prediction")

# Create a frame for the form
form_frame = ttk.Frame(root, padding="10")
form_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Define labels and entry fields
fields = [
    ("MedInc", "Median Income in block group:"),
    ("HouseAge", "Median House Age in block group:"),
    ("AveRooms", "Average Number of Rooms per Household:"),
    ("AveBedrms", "Average Number of Bedrooms per Household:"),
    ("Population", "Block Group Population:"),
    ("AveOccup", "Average Number of Household Members:"),
    ("Latitude", "Block Group Latitude:"),
    ("Longitude", "Block Group Longitude:")
]

entries = {}

for i, (field_name, label_text) in enumerate(fields):
    label = ttk.Label(form_frame, text=label_text)
    label.grid(row=i, column=0, sticky=tk.W, pady=2)

    entry = ttk.Entry(form_frame, width=20)
    entry.grid(row=i, column=1, pady=2)
    entries[field_name] = entry

# Assign entries to variables for easier access
med_inc_entry = entries["MedInc"]
house_age_entry = entries["HouseAge"]
ave_rooms_entry = entries["AveRooms"]
ave_bedrms_entry = entries["AveBedrms"]
population_entry = entries["Population"]
ave_occup_entry = entries["AveOccup"]
latitude_entry = entries["Latitude"]
longitude_entry = entries["Longitude"]

# Create the Predict button
predict_button = ttk.Button(root, text="Predict", command=predict)
predict_button.grid(row=1, column=0, pady=10)

# Label to display the prediction result
result_label = ttk.Label(root, text="", foreground="blue")
result_label.grid(row=2, column=0, pady=10)

# Start the Tkinter event loop
root.mainloop()
