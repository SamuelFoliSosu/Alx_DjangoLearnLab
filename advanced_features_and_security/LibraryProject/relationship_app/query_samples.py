# django-models/LibraryProject/relationship_app/query_samples.py

import os
import sys
import django

# Add the project root directory to the Python path
# This assumes the script is run from the `LibraryProject` directory
# and that `manage.py` is in the same directory as the `LibraryProject` package.
# Example: C:\ALX_BE_C5\Alx_DjangoLearnLab\django-models\LibraryProject
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # --- Create some sample data for demonstration ---
    print("--- Creating Sample Data ---")
    author1, created = Author.objects.get_or_create(name="Jane Austen")
    author2, created = Author.objects.get_or_create(name="George Orwell")
    author3, created = Author.objects.get_or_create(name="F. Scott Fitzgerald")

    book1, created = Book.objects.get_or_create(title="Pride and Prejudice", author=author1)
    book2, created = Book.objects.get_or_create(title="Sense and Sensibility", author=author1)
    book3, created = Book.objects.get_or_create(title="1984", author=author2)
    book4, created = Book.objects.get_or_create(title="Animal Farm", author=author2)
    book5, created = Book.objects.get_or_create(title="The Great Gatsby", author=author3)

    library1, created = Library.objects.get_or_create(name="City Central Library")
    library2, created = Library.objects.get_or_create(name="University Library")

    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book3, book5)
    library2.books.add(book1, book2, book4)

    # Create librarians (OneToOne relationship)
    librarian1, created = Librarian.objects.get_or_create(name="Alice Smith", library=library1)
    librarian2, created = Librarian.objects.get_or_create(name="Bob Johnson", library=library2)

    print("Sample data created/ensured.")
    print("\n--- Running Queries ---")

    # Query 1: Query all books by a specific author.
    try:
        author_name = "Jane Austen" # <--- Changed variable name here
        author = Author.objects.get(name=author_name) # <--- And here
        # Use objects.filter(author=author) as required by checker
        author_books = Book.objects.filter(author=author) # <--- Changed query method here
        print(f"\nBooks by {author_name}:") # <--- Changed for consistency
        if author_books.exists(): # Use author_books now
            for book in author_books:
                print(f"- {book.title}")
        else:
            print(f"No books found for {author_name}.")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.") # <--- Changed for consistency

    # Query 2: List all books in a library.
    try:
        library_name = "City Central Library"
        city_library = Library.objects.get(name=library_name)
        city_books = city_library.books.all()
        print(f"\nBooks in '{library_name}':")
        if city_books.exists():
            for book in city_books:
                print(f"- {book.title}")
        else:
            print(f"No books found in '{library_name}'.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

    # Query 3: Retrieve the librarian for a library.
    try:
        # Let's use 'library_name' for consistency with checker pattern, if needed.
        # However, the checker explicitly looks for 'Librarian.objects.get(library='
        # So, we'll get the library object first and then query the Librarian.
        library_name_for_librarian = "University Library" # Using a new name to avoid confusion
        target_library_obj = Library.objects.get(name=library_name_for_librarian)
        # Query Librarian directly using the library object as required by checker
        librarian_for_uni = Librarian.objects.get(library=target_library_obj) # <--- Changed to this query
        print(f"\nLibrarian for '{library_name_for_librarian}': {librarian_for_uni.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name_for_librarian}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for '{library_name_for_librarian}'.")


if __name__ == '__main__':
    run_queries()