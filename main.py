from data_manager import MovieDatabase
from display_manager import DisplayManager
from filters import *
import pandas as pd

'test comment to see if commit works'

class MovieApp:
    def __init__(self, excel_file):
        self.db = MovieDatabase(excel_file)
        self.display = DisplayManager()
        self.excel_file = excel_file
    
    def show_menu(self):
        print("\n" + "="*50)
        print("MOVIE & TV SHOW DATABASE")
        print("="*50)
        print("1. Show all entries")
        print("2. Filter by class (Movie/TV Show)")
        print("3. Filter by genre")
        print("4. Filter by status")
        print("5. Filter by rating range")
        print("6. Search by name")
        print("7. Add new entry")
        print("8. Remove entry")
        print("9. Show statistics")
        print("0. Exit")
        print("="*50)
    
    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                self.display.display_dataframe(self.db.get_all_data(), "All Entries")
            
            elif choice == '2':
                class_type = input("Enter class (Movie/TV Show): ").strip()
                result = filter_by_class(self.db.get_all_data(), class_type)
                self.display.display_dataframe(result, f"{class_type} Results")
            
            elif choice == '3':
                genre = input("Enter genre: ").strip()
                result = filter_by_genre(self.db.get_all_data(), genre)
                self.display.display_dataframe(result, f"{genre} Results")
            
            elif choice == '4':
                status = input("Enter status: ").strip()
                result = filter_by_status(self.db.get_all_data(), status)
                self.display.display_dataframe(result, f"{status} Results")
            
            elif choice == '5':
                min_rating = float(input("Enter minimum rating: "))
                max_rating = float(input("Enter maximum rating: "))
                result = filter_by_rating(self.db.get_all_data(), min_rating, max_rating)
                self.display.display_dataframe(result, f"Rating {min_rating}-{max_rating}")
            
            elif choice == '6':
                name = input("Enter name to search: ").strip()
                result = search_by_name(self.db.get_all_data(), name)
                self.display.display_dataframe(result, f"Search: {name}")
            
            elif choice == '7':
                self.add_new_entry()
            
            elif choice == '8':
                self.remove_one_entry()
            
            elif choice == '9':
                self.show_statistics()
            
            elif choice == '0':
                save = input("Save changes? (y/n): ").lower()
                if save == 'y':
                    self.db.save_data(self.excel_file)
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice!")
    
    def add_new_entry(self):
        print("\nAdd New Entry:")
        name = input("Name: ")
        class_type = input("Class (Movie/TV Show): ")
        genre = input("Genre: ")
        length = input("Length: ")
        status = input("Status: ")
        rating = float(input("Rating (0-10): "))
        
        self.db.add_entry(name, class_type, genre, length, status, rating)
        print("Entry added successfully!")
    
    def remove_one_entry(self):
        self.db.remove_entry()
        
    
    def show_statistics(self):
        df = self.db.get_all_data()
        print(f"\nSTATISTICS:")
        print(f"Total entries: {len(df)}")
        print(f"Movies: {len(filter_by_class(df, 'Movie'))}")
        print(f"TV Shows: {len(filter_by_class(df, 'TV Show'))}")
        print(f"Average rating: {df['Rating'].mean():.2f}")
        print(f"Genres: {', '.join(df['Genre'].unique())}")

#if __name__ == "__main__":
#    app = MovieApp("data/movies_shows.xlsx")
#    app.run()