# LibraryProject

This is the initial setup for the LibraryProject, a Django web application.
by Sosu

# Django Permissions and Groups Setup

This project implements a custom user model and leverages Django's built-in permissions and groups system to control access to various functionalities, particularly around the management of `Book` instances.

## Custom User Model

-   The `CustomUser` model is defined in `bookshelf/models.py`.
-   It extends Django's `AbstractUser` and uses `email` as the primary authentication field.
-   Additional fields: `date_of_birth` (Date), `profile_photo` (Image), and `role` (CharField with choices).
-   `AUTH_USER_MODEL` in `settings.py` is set to `bookshelf.CustomUser`.

## Custom Permissions

Custom permissions are defined in the `Meta` class of the `Book` model located in `relationship_app/models.py`. These permissions are:

-   `relationship_app.can_view_book`: Allows viewing the details of a book.
-   `relationship_app.can_create_book`: Allows creating new book entries.
-   `relationship_app.can_edit_book`: Allows modifying existing book entries.
-   `relationship_app.can_delete_book`: Allows deleting book entries.

## Groups and Permission Assignments

The following groups are set up via the Django Admin interface (`/admin/auth/group/`) and have specific permissions assigned:

-   **Admins**:
    -   Permissions: All `relationship_app.can_*_book` permissions (view, create, edit, delete). This group grants full management access to books.
-   **Editors**:
    -   Permissions: `relationship_app.can_view_book`, `relationship_app.can_create_book`, `relationship_app.can_edit_book`. This group allows users to view, create, and modify books but not delete them.
-   **Viewers**:
    -   Permissions: `relationship_app.can_view_book`. This group allows users to only view book details.

## Permission Enforcement in Views

Views that interact with `Book` instances in `books/views.py` enforce these permissions using the `@permission_required` decorator from `django.contrib.auth.decorators`.

-   `book_detail`: Protected by `@permission_required('relationship_app.can_view_book', raise_exception=True)`.
-   `book_create`: Protected by `@permission_required('relationship_app.can_create_book', raise_exception=True)`.
-   `book_edit`: Protected by `@permission_required('relationship_app.can_edit_book', raise_exception=True)`.
-   `book_delete`: Protected by `@permission_required('relationship_app.can_delete_book', raise_exception=True)`.

The `raise_exception=True` argument ensures that users without the required permission receive a 403 Forbidden error.

## Testing

To test the permission system:

1.  Log in to Django Admin as a superuser.
2.  Create test users (e.g., `viewer@example.com`, `editor@example.com`, `admin@example.com`).
3.  Assign each user to their respective group (`Viewers`, `Editors`, `Admins`).
4.  Log out of the superuser account.
5.  Log in as each test user and attempt to access and perform actions (view, create, edit, delete) on book entries to verify that permissions are enforced as expected.