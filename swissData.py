import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from ttkthemes import ThemedTk


# Function to load CSV file
def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        global df
        df = pd.read_csv(file_path)
        messagebox.showinfo("Success", "CSV file loaded successfully!")
    else:
        messagebox.showwarning("Warning", "No file selected!")


# Function to show first few rows of the dataset
def show_head():
    if df is not None:
        head_window = tk.Toplevel(root)
        head_window.title("First 5 Rows")
        head_text = tk.Text(head_window, wrap=tk.NONE)
        head_text.insert(tk.END, df.head().to_string())
        head_text.pack(expand=True, fill=tk.BOTH)
    else:
        messagebox.showwarning("Warning", "Load a CSV file first!")


# Function to describe the dataset
def describe_data():
    if df is not None:
        describe_window = tk.Toplevel(root)
        describe_window.title("Dataset Description")
        describe_text = tk.Text(describe_window, wrap=tk.NONE)
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
                filter_text = tk.Text(filter_window, wrap=tk.NONE)
                filter_text.insert(tk.END, filtered_df.to_string())
                filter_text.pack(expand=True, fill=tk.BOTH)
            else:
                messagebox.showwarning("Warning", "Column not found!")

        filter_window = tk.Toplevel(root)
        filter_window.title("Filter Rows")
        tk.Label(filter_window, text="Column Name:").pack()
        column_entry = tk.Entry(filter_window)
        column_entry.pack()
        tk.Label(filter_window, text="Value:").pack()
        value_entry = tk.Entry(filter_window)
        value_entry.pack()
        tk.Button(filter_window, text="Apply Filter", command=apply_filter).pack()
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
        tk.Label(plot_window, text="Column Name:").pack()
        column_entry = tk.Entry(plot_window)
        column_entry.pack()
        tk.Button(plot_window, text="Plot", command=apply_plot).pack()
    else:
        messagebox.showwarning("Warning", "Load a CSV file first!")


# Function to show correlation matrix
def show_correlation_matrix():
    if df is not None:
        corr_window = tk.Toplevel(root)
        corr_window.title("Correlation Matrix")
        corr_text = tk.Text(corr_window, wrap=tk.NONE)
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
                counts_text = tk.Text(counts_window, wrap=tk.NONE)
                counts_text.insert(tk.END, df[column_name].value_counts().to_string())
                counts_text.pack(expand=True, fill=tk.BOTH)
            else:
                messagebox.showwarning("Warning", "Column not found!")

        counts_window = tk.Toplevel(root)
        counts_window.title("Value Counts")
        tk.Label(counts_window, text="Column Name:").pack()
        column_entry = tk.Entry(counts_window)
        column_entry.pack()
        tk.Button(
            counts_window, text="Show Value Counts", command=apply_value_counts
        ).pack()
    else:
        messagebox.showwarning("Warning", "Load a CSV file first!")


# Function to summarize missing values
def summarize_missing_values():
    if df is not None:
        missing_window = tk.Toplevel(root)
        missing_window.title("Missing Values Summary")
        missing_text = tk.Text(missing_window, wrap=tk.NONE)
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
                groupby_text = tk.Text(groupby_window, wrap=tk.NONE)
                groupby_text.insert(tk.END, grouped_df.to_string())
                groupby_text.pack(expand=True, fill=tk.BOTH)
            else:
                messagebox.showwarning(
                    "Warning", "Column not found or invalid function!"
                )

        groupby_window = tk.Toplevel(root)
        groupby_window.title("Group By and Aggregate")
        tk.Label(groupby_window, text="Group By Column:").pack()
        group_entry = tk.Entry(groupby_window)
        group_entry.pack()
        tk.Label(groupby_window, text="Aggregate Column:").pack()
        agg_entry = tk.Entry(groupby_window)
        agg_entry.pack()
        tk.Label(groupby_window, text="Aggregation Function (e.g., sum, mean):").pack()
        agg_func_entry = tk.Entry(groupby_window)
        agg_func_entry.pack()
        tk.Button(groupby_window, text="Apply Group By", command=apply_groupby).pack()
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


# Create main application window with macOS aesthetic
root = ThemedTk(theme="aquativo")
root.title("Data Analysis Swiss Army Tool")
root.geometry("400x600")

# Buttons for the different tools
ttk.Button(root, text="Load CSV", command=load_csv).pack(pady=10)
ttk.Button(root, text="Show First 5 Rows", command=show_head).pack(pady=10)
ttk.Button(root, text="Describe Dataset", command=describe_data).pack(pady=10)
ttk.Button(root, text="Filter Rows", command=filter_rows).pack(pady=10)
ttk.Button(root, text="Plot Column", command=plot_column).pack(pady=10)
ttk.Button(root, text="Show Correlation Matrix", command=show_correlation_matrix).pack(
    pady=10
)
ttk.Button(root, text="Show Value Counts", command=show_value_counts).pack(pady=10)
ttk.Button(
    root, text="Summarize Missing Values", command=summarize_missing_values
).pack(pady=10)
ttk.Button(root, text="Group By and Aggregate", command=group_by_and_aggregate).pack(
    pady=10
)
ttk.Button(root, text="Export Filtered Data", command=export_filtered_data).pack(
    pady=10
)

# Global variable to store the dataframe and filtered dataframe
df = None
filtered_df = None

root.mainloop()
