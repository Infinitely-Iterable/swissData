# includes missingNo code

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


# Reverse Calculator: Function to find combinations that sum to a target value
def reverse_calculator():
    if df is not None:

        def apply_reverse_calculator():
            target_value = float(target_entry.get())
            num_operands = int(num_operands_entry.get())
            tolerance = float(tolerance_entry.get()) / 100

            exclude_first = exclude_first_var.get()
            columns = (
                df.columns.tolist()[1:] if exclude_first == "y" else df.columns.tolist()
            )
            per_column = per_column_var.get() == "y"

            finder = CombinationFinder(df, columns, per_column)
            results = finder.find_combinations(target_value, num_operands, tolerance)
            finder.display_results(results)

        reverse_calc_window = tk.Toplevel(root)
        reverse_calc_window.title("Reverse Calculator")

        tk.Label(reverse_calc_window, text="Target Value:").pack()
        target_entry = tk.Entry(reverse_calc_window)
        target_entry.pack()

        tk.Label(reverse_calc_window, text="Number of Operands (2 or 3):").pack()
        num_operands_entry = tk.Entry(reverse_calc_window)
        num_operands_entry.pack()

        tk.Label(
            reverse_calc_window, text="Tolerance Percentage (e.g., 10 for 10%):"
        ).pack()
        tolerance_entry = tk.Entry(reverse_calc_window)
        tolerance_entry.pack()

        exclude_first_var = tk.StringVar(value="y")
        tk.Label(reverse_calc_window, text="Exclude First Column? (y/n):").pack()
        tk.Entry(reverse_calc_window, textvariable=exclude_first_var).pack()

        per_column_var = tk.StringVar(value="n")
        tk.Label(reverse_calc_window, text="Search Per Column? (y/n):").pack()
        tk.Entry(reverse_calc_window, textvariable=per_column_var).pack()

        tk.Button(
            reverse_calc_window,
            text="Find Combinations",
            command=apply_reverse_calculator,
        ).pack()
    else:
        messagebox.showwarning("Warning", "Load a CSV file first!")


# Reverse Calculator: Supporting classes
class CombinationFinder:
    def __init__(self, dataframe, columns=None, per_column=False):
        self.df = dataframe
        self.per_column = per_column
        if columns:
            self.df = self.df[columns]

    def find_combinations(self, target_value, num_operands, tolerance):
        results = []
        if self.per_column:
            for col in self.df.columns:
                results.extend(
                    self._find_combinations_in_column(
                        target_value, num_operands, tolerance, col
                    )
                )
        else:
            results.extend(
                self._find_combinations_across_columns(
                    target_value, num_operands, tolerance
                )
            )
        return results

    def _find_combinations_in_column(self, target_value, num_operands, tolerance, col):
        entries = [(idx, row[col]) for idx, row in self.df.iterrows()]
        results = []
        for combo in combinations(entries, num_operands):
            sum_val = sum(item[1] for item in combo)
            if abs(sum_val - target_value) <= tolerance * target_value:
                result_entry = {"column": col, "sum": sum_val}
                for i, (index, value) in enumerate(combo):
                    result_entry[f"index{i+1}"] = index
                    result_entry[f"value{i+1}"] = value
                results.append(result_entry)
        return results

    def _find_combinations_across_columns(self, target_value, num_operands, tolerance):
        entries = [
            (idx, row[col])
            for idx, row in self.df.iterrows()
            for col in self.df.columns
        ]
        results = []
        for combo in combinations(entries, num_operands):
            sum_val = sum(item[1] for item in combo)
            if abs(sum_val - target_value) <= tolerance * target_value:
                result_entry = {"sum": sum_val}
                for i, (index, value) in enumerate(combo):
                    result_entry[f"index{i+1}"] = index
                    result_entry[f"value{i+1}"] = value
                results.append(result_entry)
        return results

    def display_results(self, results):
        if results:
            results_window = tk.Toplevel(root)
            results_window.title("Combination Results")
            results_text = tk.Text(results_window, wrap=tk.NONE)
            results_text.insert(tk.END, pd.DataFrame(results).to_string())
            results_text.pack(expand=True, fill=tk.BOTH)
        else:
            messagebox.showinfo("Info", "No combinations found within tolerance.")


# Create main application window with macOS aesthetic
root = ThemedTk(theme="aquativo")
root.title("Data Analysis Swiss Army Tool")
root.geometry("400x700")

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
ttk.Button(root, text="Reverse Calculator", command=reverse_calculator).pack(pady=10)

# Global variable to store the dataframe and filtered dataframe
df = None
filtered_df = None

root.mainloop()
