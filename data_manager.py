import pandas as pd
import os

class MovieDatabase:
    def __init__(self, excel_file):
        self.df = None
        self.load_data(excel_file)
    
    def load_data(self, excel_file):
        """Load data from Excel file"""
        if os.path.exists(excel_file):
            self.df = pd.read_excel(excel_file)
            print(f"Loaded {len(self.df)} entries from {excel_file}")
        else:
            print(f"File {excel_file} not found!")
    
    def get_all_data(self):
        return self.df
    
    def get_unique_values(self, column):
        """Get unique values from a column"""
        return self.df[column].unique().tolist()
    
    def add_entry(self, name, class_type, genre, length, status, rating):
        """Add new movie/show entry"""
        new_entry = pd.DataFrame({
            'Name': [name],
            'Class': [class_type],
            'Genre': [genre],
            'Length': [length],
            'Status': [status],
            'Rating': [rating]
        })
        self.df = pd.concat([self.df, new_entry], ignore_index=True)
    
    def remove_entry(self):
        """Remove an existing entry"""
        name = input("Enter name of entry to remove: ").strip()
        print('Entries to be deleted:')
        print(self.df['Name'] == name)
        print('==========')
        action = input('Proceed to delete? (y/n)')
        if action == 'y':
            self.df = self.df[~(self.df['Name'] == name)]
        if action == 'n':
            print('Deletion cancelled')
    
    def save_data(self, excel_file):
        """Save data back to Excel"""
        self.df.to_excel(excel_file, index=False)
        print(f"Data saved to {excel_file}")