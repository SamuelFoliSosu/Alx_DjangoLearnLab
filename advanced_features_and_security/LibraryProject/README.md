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


# Security Measures Implemented

This project incorporates several security best practices:

## 1. Secure Settings (`LibraryProject/settings.py`)

-   **DEBUG Mode**: `DEBUG` is set to `False` for production environments (requires `ALLOWED_HOSTS` configuration).
-   **Browser Protections**:
    -   `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME type sniffing.
    -   `SECURE_BROWSER_XSS_FILTER = True`: Activates browser's built-in XSS protection.
    -   `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking by disallowing embedding the site in iframes.
-   **Secure Cookies**:
    -   `CSRF_COOKIE_SECURE = True`: Ensures CSRF cookies are only sent over HTTPS.
    -   `SESSION_COOKIE_SECURE = True`: Ensures session cookies are only sent over HTTPS.
-   **HTTPS Enforcement (Optional but Recommended for Production)**:
    -   `SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_HSTS_PRELOAD`: Configured for HTTP Strict Transport Security (HSTS) to force HTTPS connections.
    -   `SECURE_SSL_REDIRECT`: Configured to redirect all HTTP traffic to HTTPS.
    -   `SECURE_PROXY_SSL_HEADER`: Necessary when running behind a reverse proxy (e.g., Nginx).

## 2. CSRF Protection in Forms (`templates/bookshelf/*.html`)

-   All forms (`book_form.html`, `book_confirm_delete.html`) explicitly include `{% csrf_token %}` within their `<form>` tags. This utilizes Django's built-in CSRF protection middleware to prevent Cross-Site Request Forgery attacks.

## 3. Secure Data Access in Views (`bookshelf/views.py`)

-   **SQL Injection Prevention**: All database interactions are performed exclusively through Django's Object-Relational Mapper (ORM). The ORM inherently parameterizes queries, eliminating the risk of SQL injection vulnerabilities from user input. Direct raw SQL queries with unsanitized user input are strictly avoided.
-   **Input Validation**: User inputs in forms are automatically validated and sanitized by Django Forms (`BookForm.is_valid()`), ensuring that only expected and safe data reaches the database.

## 4. Content Security Policy (CSP) (`LibraryProject/settings.py` and `csp` app)

-   `django-csp` middleware is integrated.
-   `CSP_DEFAULT_SRC`, `CSP_SCRIPT_SRC`, `CSP_STYLE_SRC`, `CSP_IMG_SRC`, `CSP_FONT_SRC`, `CSP_CONNECT_SRC`, `CSP_OBJECT_SRC`, `CSP_FRAME_ANCESTORS`, `CSP_FORM_ACTION`, `CSP_BASE_URI` are configured to restrict content loading to trusted sources (`'self'` by default), significantly reducing the risk of Cross-Site Scripting (XSS) attacks.

## Testing Approach

Basic security testing can be performed manually:

-   **CSRF**: Try to submit a form without the `{% csrf_token %}` or with an invalid token (by manipulating HTML in browser dev tools). Django should return a 403 Forbidden error.
-   **XSS**: Attempt to inject malicious script tags (e.g., `<script>alert('XSS');</script>`) into text input fields. The application should either escape the output, or the CSP should block the script execution.
-   **SQL Injection**: (Less applicable if always using ORM correctly) Attempt to inject SQL commands into input fields. The application should not execute them as database commands.
-   **Clickjacking**: Attempt to embed your site in an iframe on an external domain. The `X_FRAME_OPTIONS` and `CSP_FRAME_ANCESTORS` policies should prevent this, resulting in a blank iframe or browser console errors.
-   **HTTPS (Production only)**: Ensure your site consistently redirects to HTTPS and that all assets are loaded over HTTPS (check browser console for mixed content warnings).