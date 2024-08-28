import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from ttkthemes import ThemedTk
from itertools import combinations


# Function to load CSV file
def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        global df
        df = pd.read_csv(file_path)
        messagebox.showinfo("Success", "CSV file loaded successfully!")
        show_column_info()  # Show column info after loading
    else:
        messagebox.showwarning("Warning", "No file selected!")


# Function to show first few rows of the dataset
def show_head():
    if df is not None:
        head_window = tk.Toplevel(root)
        head_window.title("First 5 Rows")
        head_text = tk.Text(head_window, wrap=tk.NONE, bg="#333333", fg="#ffffff")
        head_text.insert(tk.END, df.head().to_string())
        head_text.pack(expand=True, fill=tk.BOTH)
    else:
        messagebox.showwarning("Warning", "Load a CSV file first!")


# Function to describe the dataset
def describe_data():
    if df is not None:
        describe_window = tk.Toplevel(root)
        describe_window.title("Dataset Description")
        describe_text = tk.Text(
            describe_window, wrap=tk.NONE, bg="#333333", fg="#ffffff"
        )
        describe_text.insert(tk.END, df.describe().to_string())
        describe_text.pack(expand=True, fill=tk.BOTH)
    else:
        messagebox.showwarning("Warning", "Load a CSV file first!")


# Function to filter rows by a column value
def filter_rows():
    if df is not None:

        def apply_filter():
            column_name = column_entry.get()
            filter_value = value_entry.get()
            if column_name in df.columns:
                global filtered_df
                filtered_df = df[df[column_name] == filter_value]
                filter_window = tk.Toplevel(root)
                filter_window.title("Filtered Rows")
                filter_text = tk.Text(
                    filter_window, wrap=tk.NONE, bg="#333333", fg="#ffffff"
                )
                filter_text.insert(tk.END, filtered_df.to_string())
                filter_text.pack(expand=True, fill=tk.BOTH)
            else:
                messagebox.showwarning("Warning", "Column not found!")

        filter_window = tk.Toplevel(root)
        filter_window.title("Filter Rows")
        tk.Label(filter_window, text="Column Name:", bg="#222222", fg="#ffffff").pack()
        column_entry = tk.Entry(filter_window, bg="#444444", fg="#ffffff")
        column_entry.pack()
        tk.Label(filter_window, text="Value:", bg="#222222", fg="#ffffff").pack()
        value_entry = tk.Entry(filter_window, bg="#444444", fg="#ffffff")
        value_entry.pack()
        tk.Button(
            filter_window,
            text="Apply Filter",
            command=apply_filter,
            bg="#555555",
            fg="#ffffff",
        ).pack()
    else:
        messagebox.showwarning("Warning", "Load a CSV file first!")


# Function to plot a column
def plot_column():
    if df is not None:

        def apply_plot():
            column_name = column_entry.get()
            if column_name in df.columns:
                df[column_name].plot(kind="hist")
                plt.title(f"Histogram of {column_name}")
                plt.show()
            else:
                messagebox.showwarning("Warning", "Column not found!")

        plot_window = tk.Toplevel(root)
        plot_window.title("Plot Column")
        tk.Label(plot_window, text="Column Name:", bg="#222222", fg="#ffffff").pack()
        column_entry = tk.Entry(plot_window, bg="#444444", fg="#ffffff")
        column_entry.pack()
        tk.Button(
            plot_window, text="Plot", command=apply_plot, bg="#555555", fg="#ffffff"
        ).pack()
    else:
        messagebox.showwarning("Warning", "Load a CSV file first!")


# Function to show correlation matrix
def show_correlation_matrix():
    if df is not None:
        corr_window = tk.Toplevel(root)
        corr_window.title("Correlation Matrix")
        corr_text = tk.Text(corr_window, wrap=tk.NONE, bg="#333333", fg="#ffffff")
        corr_text.insert(tk.END, df.corr().to_string())
        corr_text.pack(expand=True, fill=tk.BOTH)
    else:
        messagebox.showwarning("Warning", "Load a CSV file first!")


# Function to show value counts of a column
def show_value_counts():
    if df is not None:

        def apply_value_counts():
            column_name = column_entry.get()
            if column_name in df.columns:
                counts_window = tk.Toplevel(root)
                counts_window.title(f"Value Counts for {column_name}")
                counts_text = tk.Text(
                    counts_window, wrap=tk.NONE, bg="#333333", fg="#ffffff"
                )
                counts_text.insert(tk.END, df[column_name].value_counts().to_string())
                counts_text.pack(expand=True, fill=tk.BOTH)
            else:
                messagebox.showwarning("Warning", "Column not found!")

        counts_window = tk.Toplevel(root)
        counts_window.title("Value Counts")
        tk.Label(counts_window, text="Column Name:", bg="#222222", fg="#ffffff").pack()
        column_entry = tk.Entry(counts_window, bg="#444444", fg="#ffffff")
        column_entry.pack()
        tk.Button(
            counts_window,
            text="Show Value Counts",
            command=apply_value_counts,
            bg="#555555",
            fg="#ffffff",
        ).pack()
    else:
        messagebox.showwarning("Warning", "Load a CSV file first!")


# Function to summarize missing values
def summarize_missing_values():
    if df is not None:
        missing_window = tk.Toplevel(root)
        missing_window.title("Missing Values Summary")
        missing_text = tk.Text(missing_window, wrap=tk.NONE, bg="#333333", fg="#ffffff")
        missing_text.insert(tk.END, df.isnull().sum().to_string())
        missing_text.pack(expand=True, fill=tk.BOTH)
    else:
        messagebox.showwarning("Warning", "Load a CSV file first!")


# Function to group by a column and aggregate
def group_by_and_aggregate():
    if df is not None:

        def apply_groupby():
            group_column = group_entry.get()
            agg_column = agg_entry.get()
            agg_func = agg_func_entry.get()
            if group_column in df.columns and agg_column in df.columns:
                grouped_df = df.groupby(group_column)[agg_column].agg(agg_func)
                groupby_window = tk.Toplevel(root)
                groupby_window.title("Group By and Aggregate")
                groupby_text = tk.Text(
                    groupby_window, wrap=tk.NONE, bg="#333333", fg="#ffffff"
                )
                groupby_text.insert(tk.END, grouped_df.to_string())
                groupby_text.pack(expand=True, fill=tk.BOTH)
            else:
                messagebox.showwarning(
                    "Warning", "Column not found or invalid function!"
                )

        groupby_window = tk.Toplevel(root)
        groupby_window.title("Group By and Aggregate")
        tk.Label(
            groupby_window, text="Group By Column:", bg="#222222", fg="#ffffff"
        ).pack()
        group_entry = tk.Entry(groupby_window, bg="#444444", fg="#ffffff")
        group_entry.pack()
        tk.Label(
            groupby_window, text="Aggregate Column:", bg="#222222", fg="#ffffff"
        ).pack()
        agg_entry = tk.Entry(groupby_window, bg="#444444", fg="#ffffff")
        agg_entry.pack()
        tk.Label(
            groupby_window,
            text="Aggregation Function (e.g., sum, mean):",
            bg="#222222",
            fg="#ffffff",
        ).pack()
        agg_func_entry = tk.Entry(groupby_window, bg="#444444", fg="#ffffff")
        agg_func_entry.pack()
        tk.Button(
            groupby_window,
            text="Apply Group By",
            command=apply_groupby,
            bg="#555555",
            fg="#ffffff",
        ).pack()
    else:
        messagebox.showwarning("Warning", "Load a CSV file first!")


# Function to export filtered data
def export_filtered_data():
    if filtered_df is not None:
        export_path = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )
        if export_path:
            filtered_df.to_csv(export_path, index=False)
            messagebox.showinfo("Success", "Filtered data exported successfully!")
        else:
            messagebox.showwarning("Warning", "No file path provided!")
    else:
        messagebox.showwarning("Warning", "No filtered data to export!")


# Function to show current column names and data types
def show_column_info():
    if df is not None:
        column_info_text.delete(1.0, tk.END)  # Clear previous content
        column_info_text.insert(tk.END, df.dtypes.to_string())
    else:
        messagebox.showwarning("Warning", "Load a CSV file first!")


# Reverse calculator function to find combinations
def run_reverse_calculator():
    output_text.delete(1.0, tk.END)
    try:
        target = float(target_entry.get())
        num_operands = int(operands_entry.get())
        tolerance = float(tolerance_entry.get()) / 100
        finder = CombinationFinder(
            df, columns_to_use, settings["Search per column"].lower() == "y"
        )
        results = finder.find_combinations(target, num_operands, tolerance)
        display_results(results)
    except ValueError:
        output_text.insert(tk.END, "Invalid input. Please enter valid numbers.\n")


# Helper functions for reverse calculator
def display_results(results):
    if results:
        output_text.insert(tk.END, "~~~~~~~~~~ Matches Found ~~~~~~~~~~\n")
        output_text.insert(tk.END, pd.DataFrame(results).to_string() + "\n")
    else:
        output_text.insert(tk.END, "~~~ None Found Within Tolerance ~~~\n")


def list_columns(df, settings):
    exclude_first = settings["Exclude first column"]
    columns_to_use = (
        df.columns.tolist()[1:] if exclude_first.lower() == "y" else df.columns.tolist()
    )
    output_text.insert(
        tk.END, "Available columns for analysis: " + str(columns_to_use) + "\n"
    )


def handle_settings_menu(settings):
    output_text.insert(tk.END, "\n~~~~~~ Settings Menu ~~~~~~\n")
    for letter, (key, value) in zip("abcdef", settings.items()):
        output_text.insert(tk.END, f"{letter.upper()}. {key}: {value}\n")
    output_text.insert(tk.END, "Settings can be adjusted within the code for now.\n")


# Create main application window with macOS aesthetic
root = ThemedTk(theme="black")
root.title("Data Analysis Swiss Army Tool")
root.geometry("900x900")

# Create a frame for the column info
column_info_frame = tk.Frame(root, bg="#222222")
column_info_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Label for column info section
tk.Label(
    column_info_frame, text="Column Names and Data Types:", bg="#222222", fg="#ffffff"
).pack()

# Text widget for displaying column names and data types
column_info_text = tk.Text(
    column_info_frame, wrap=tk.NONE, height=10, bg="#333333", fg="#ffffff"
)
column_info_text.pack(expand=True, fill=tk.BOTH)

# Buttons for the different tools
button_frame = tk.Frame(root, bg="#222222")
button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

ttk.Button(button_frame, text="Load CSV", command=load_csv).pack(pady=5)
ttk.Button(button_frame, text="Show First 5 Rows", command=show_head).pack(pady=5)
ttk.Button(button_frame, text="Describe Dataset", command=describe_data).pack(pady=5)
ttk.Button(button_frame, text="Filter Rows", command=filter_rows).pack(pady=5)
ttk.Button(button_frame, text="Plot Column", command=plot_column).pack(pady=5)
ttk.Button(
    button_frame, text="Show Correlation Matrix", command=show_correlation_matrix
).pack(pady=5)
ttk.Button(button_frame, text="Show Value Counts", command=show_value_counts).pack(
    pady=5
)
ttk.Button(
    button_frame, text="Summarize Missing Values", command=summarize_missing_values
).pack(pady=5)
ttk.Button(
    button_frame, text="Group By and Aggregate", command=group_by_and_aggregate
).pack(pady=5)
ttk.Button(
    button_frame, text="Export Filtered Data", command=export_filtered_data
).pack(pady=5)

# Frame for Reverse Calculator Section
reverse_calculator_frame = tk.Frame(root, bg="#222222")
reverse_calculator_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Label for the Reverse Calculator section
tk.Label(
    reverse_calculator_frame,
    text="Reverse Calculator",
    bg="#222222",
    fg="#ffffff",
    font=("Helvetica", 16),
).pack(pady=5)

# Target value input
tk.Label(
    reverse_calculator_frame, text="Target Value:", bg="#222222", fg="#ffffff"
).pack()
target_entry = tk.Entry(reverse_calculator_frame, bg="#333333", fg="#ffffff")
target_entry.pack(fill=tk.X)

# Number of operands input
tk.Label(
    reverse_calculator_frame, text="Number of Operands:", bg="#222222", fg="#ffffff"
).pack()
operands_entry = tk.Entry(reverse_calculator_frame, bg="#333333", fg="#ffffff")
operands_entry.pack(fill=tk.X)

# Tolerance percentage input
tk.Label(
    reverse_calculator_frame, text="Tolerance Percentage:", bg="#222222", fg="#ffffff"
).pack()
tolerance_entry = tk.Entry(reverse_calculator_frame, bg="#333333", fg="#ffffff")
tolerance_entry.pack(fill=tk.X)

# Button to run reverse calculator
tk.Button(
    reverse_calculator_frame,
    text="Run Reverse Calculator",
    command=run_reverse_calculator,
    bg="#555555",
    fg="#ffffff",
).pack(pady=10)

# Textbox for displaying output
output_text = tk.Text(
    reverse_calculator_frame, wrap=tk.NONE, height=10, bg="#333333", fg="#ffffff"
)
output_text.pack(expand=True, fill=tk.BOTH)

# Global variable to store the dataframe and filtered dataframe
df = None
filtered_df = None

# Settings for reverse calculator
settings = {
    "Exclude first column": "y",
    "Columns to use": "",
    "Search per column": "n",
    "Target value": "1000",
    "Number of operands": "2",
    "Tolerance percentage": "10",
}

columns_to_use = []

root.mainloop()
