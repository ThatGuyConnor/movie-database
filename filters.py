def filter_by_class(df, class_type):
    """Filter by Movie or TV Show"""
    return df[df['Class'].str.contains(class_type, case=False, na=False)]

def filter_by_genre(df, genre):
    """Filter by genre"""
    return df[df['Genre'].str.contains(genre, case=False, na=False)]

def filter_by_status(df, status):
    """Filter by status"""
    return df[df['Status'].str.contains(status, case=False, na=False)]

def filter_by_rating(df, min_rating=0, max_rating=10):
    """Filter by rating range"""
    return df[(df['Rating'] >= min_rating) & (df['Rating'] <= max_rating)]

def search_by_name(df, name):
    """Search by name"""
    return df[df['Name'].str.contains(name, case=False, na=False)]

def get_top_rated(df, n=10):
    """Get top N rated entries"""
    return df.nlargest(n, 'Rating')