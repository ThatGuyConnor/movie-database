from rich.console import Console
from rich.table import Table
from rich.text import Text
import pandas as pd

class DisplayManager:
    def __init__(self):
        self.console = Console()
    
    def display_dataframe(self, df, title="Results"):
        """Display DataFrame with rich formatting"""
        if df.empty:
            self.console.print(f"[red]No results found![/red]")
            return
        
        table = Table(show_header=True, header_style="bold magenta", title=title)
        
        # Add columns
        for col in df.columns:
            table.add_column(col)
        
        # Add rows with rating-based coloring
        for _, row in df.iterrows():
            rating = float(row['Rating']) if pd.notna(row['Rating']) else 0
            
            styled_row = []
            for col_name, val in row.items():
                if col_name == 'Rating':
                    if rating >= 9.0:
                        styled_cell = Text(str(val), style="bold green")
                    elif rating >= 8.0:
                        styled_cell = Text(str(val), style="bold yellow")
                    elif rating >= 7.0:
                        styled_cell = Text(str(val), style="bold white")
                    else:
                        styled_cell = Text(str(val), style="bold red")
                else:
                    styled_cell = str(val)
                styled_row.append(styled_cell)
            
            table.add_row(*styled_row)
        
        self.console.print(table)
        self.console.print(f"\n[blue]Found {len(df)} results[/blue]")