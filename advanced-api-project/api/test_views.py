# advanced-api-project/api/test_views.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Author, Book
from django.contrib.auth.models import User # Required for creating a test user
from django.utils import timezone
import datetime

class BookAPITests(APITestCase):
    """
    Comprehensive test suite for the Book API endpoints.
    Covers CRUD operations, filtering, searching, ordering, and permission enforcement.
    """

    def setUp(self):
        """
        Set up test data for all test methods.
        This method runs before each test.
        """
        # Create a test user for authenticated requests
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

        # Create authors
        self.author1 = Author.objects.create(name='Jane Austen')
        self.author2 = Author.objects.create(name='George Orwell')
        self.author3 = Author.objects.create(name='J.R.R. Tolkien')

        # Create books
        self.book1 = Book.objects.create(
            title='Pride and Prejudice',
            publication_year=1813,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title='Sense and Sensibility',
            publication_year=1811,
            author=self.author1
        )
        self.book3 = Book.objects.create(
            title='1984',
            publication_year=1949,
            author=self.author2
        )
        self.book4 = Book.objects.create(
            title='Animal Farm',
            publication_year=1945,
            author=self.author2
        )
        self.book5 = Book.objects.create(
            title='The Hobbit',
            publication_year=1937,
            author=self.author3
        )

        # Define URLs for convenience
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})
        self.update_url = lambda pk: reverse('book-update', kwargs={'pk': pk})
        self.delete_url = lambda pk: reverse('book-delete', kwargs={'pk': pk})

    # --- Test GET (List and Detail) operations ---

    def test_book_list_unauthenticated(self):
        """
        Ensure unauthenticated users can retrieve the list of books.
        Permissions: IsAuthenticatedOrReadOnly (allows read for unauthenticated)
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5) # Check if all 5 books are returned

    def test_book_detail_unauthenticated(self):
        """
        Ensure unauthenticated users can retrieve a single book by ID.
        Permissions: IsAuthenticatedOrReadOnly (allows read for unauthenticated)
        """
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_book_list_filter_by_title(self):
        """
        Test filtering the book list by title.
        """
        response = self.client.get(self.list_url, {'title': '1984'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_book_list_filter_by_publication_year(self):
        """
        Test filtering the book list by publication_year.
        """
        response = self.client.get(self.list_url, {'publication_year': 1813})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Pride and Prejudice')

    def test_book_list_filter_by_author_name(self):
        """
        Test filtering the book list by author's name (nested lookup).
        """
        response = self.client.get(self.list_url, {'author__name': 'Jane Austen'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) # Pride and Prejudice, Sense and Sensibility

    def test_book_list_search_by_title(self):
        """
        Test searching the book list by title.
        """
        response = self.client.get(self.list_url, {'search': 'Farm'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Animal Farm')

    def test_book_list_search_by_author_name(self):
        """
        Test searching the book list by author's name.
        """
        response = self.client.get(self.list_url, {'search': 'Orwell'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) # 1984, Animal Farm

    def test_book_list_order_by_title_ascending(self):
        """
        Test ordering the book list by title in ascending order.
        """
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if titles are sorted alphabetically
        expected_titles = sorted([b.title for b in Book.objects.all()])
        actual_titles = [item['title'] for item in response.data]
        self.assertEqual(actual_titles, expected_titles)

    def test_book_list_order_by_publication_year_descending(self):
        """
        Test ordering the book list by publication year in descending order.
        """
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if publication years are sorted in descending order
        expected_years = sorted([b.publication_year for b in Book.objects.all()], reverse=True)
        actual_years = [item['publication_year'] for item in response.data]
        self.assertEqual(actual_years, expected_years)

    # --- Test POST (Create) operations ---

    def test_create_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create a book.
        Permissions: IsAuthenticated (requires authentication)
        """
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author1.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 5) # No new book should be created

    def test_create_book_authenticated(self):
        """
        Ensure authenticated users can create a book.
        Permissions: IsAuthenticated
        """
        # Use self.client.login() for authentication as per checker requirement
        self.assertTrue(self.client.login(username=self.username, password=self.password))
        data = {
            'title': 'New Book by Authored User',
            'publication_year': 2023,
            'author': self.author1.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 6) # One new book should be created
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book by Authored User')

    def test_create_book_with_future_publication_year_validation(self):
        """
        Test custom validation for future publication year during book creation.
        """
        self.assertTrue(self.client.login(username=self.username, password=self.password))
        future_year = timezone.now().year + 1
        data = {
            'title': 'Future Book',
            'publication_year': future_year,
            'author': self.author1.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)
        self.assertIn("Publication year cannot be in the future.", response.data['publication_year'])
        self.assertEqual(Book.objects.count(), 5) # No new book should be created

    # --- Test PUT/PATCH (Update) operations ---

    def test_update_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot update a book.
        Permissions: IsAuthenticated (requires authentication)
        """
        original_title = self.book1.title
        data = {'title': 'Updated Title', 'publication_year': 1813, 'author': self.author1.id}
        response = self.client.put(self.update_url(self.book1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.book1.refresh_from_db() # Reload the book from the database
        self.assertEqual(self.book1.title, original_title) # Title should not have changed

    def test_update_book_authenticated(self):
        """
        Ensure authenticated users can update a book.
        Permissions: IsAuthenticated
        """
        self.assertTrue(self.client.login(username=self.username, password=self.password))
        data = {'title': 'Updated Pride and Prejudice', 'publication_year': 1813, 'author': self.author1.id}
        response = self.client.put(self.update_url(self.book1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Pride and Prejudice')

    def test_partial_update_book_authenticated(self):
        """
        Ensure authenticated users can partially update a book (PATCH).
        Permissions: IsAuthenticated
        """
        self.assertTrue(self.client.login(username=self.username, password=self.password))
        data = {'publication_year': 1814} # Only update publication year
        response = self.client.patch(self.update_url(self.book1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.publication_year, 1814)
        self.assertEqual(self.book1.title, 'Pride and Prejudice') # Title should remain unchanged

    # --- Test DELETE operations ---

    def test_delete_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot delete a book.
        Permissions: IsAuthenticated (requires authentication)
        """
        response = self.client.delete(self.delete_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 5) # Book should not be deleted

    def test_delete_book_authenticated(self):
        """
        Ensure authenticated users can delete a book.
        Permissions: IsAuthenticated
        """
        self.assertTrue(self.client.login(username=self.username, password=self.password))
        initial_book_count = Book.objects.count()
        response = self.client.delete(self.delete_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) # 204 No Content for successful deletion
        self.assertEqual(Book.objects.count(), initial_book_count - 1) # Book count should decrease by 1
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists()) # Book should no longer exist