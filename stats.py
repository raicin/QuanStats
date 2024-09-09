import tkinter as tk
from tkinter import messagebox
from statistics import mean, median, mode, variance, stdev

# Helper function to format results, removing .0 if it's a whole number
def format_result(value):
    return int(value) if value.is_integer() else value

def calculate_stats():
    try:
        # Get input numbers from the user
        numbers = list(map(float, entry.get().split(',')))
        
        # Calculate the statistics
        result_mean = format_result(mean(numbers))
        result_median = format_result(median(numbers))
        result_mode = format_result(mode(numbers))
        result_range = format_result(max(numbers) - min(numbers))
        result_variance = format_result(variance(numbers))
        result_stdev = format_result(stdev(numbers))
        
        # Display the results
        result_text = f"Mean: {result_mean}\n"
        result_text += f"Median: {result_median}\n"
        result_text += f"Mode: {result_mode}\n"
        result_text += f"Range: {result_range}\n"
        result_text += f"Variance: {result_variance}\n"
        result_text += f"Standard Deviation: {result_stdev}\n"
        
        messagebox.showinfo("Statistics Results", result_text)
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the Tkinter window
window = tk.Tk()
window.title("Rawr Calculator")

# Create a label for instructions
label = tk.Label(window, text="Enter numbers separated by commas:")
label.pack()

# Create an entry box for input
entry = tk.Entry(window, width=50)
entry.pack()

# Create a button to calculate statistics
button = tk.Button(window, text="Calculate", command=calculate_stats)
button.pack()

# Run the application
window.mainloop()