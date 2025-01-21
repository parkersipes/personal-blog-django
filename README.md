# Django Personal Blog Project

A personal blog application built with Django, PostgreSQL, and Materialize CSS. Features include a clean, responsive design, rich text editing with CKEditor 5, and secure authentication.

## Features

- User authentication (admin-only posting)
- Rich text editor for blog posts (CKEditor 5)
- Responsive design using Materialize CSS
- Image upload capabilities
- Mobile-friendly layout
- SEO-friendly URLs with slugs
- PostgreSQL database backend

## Project Structure

```
DjangoBlogProject/
├── blog/                      # Blog application
│   ├── migrations/
│   ├── static/
│   ├── templates/blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/                    # Project-wide static files
│   └── css/
│       └── blog.css
├── templates/                 # Project-wide templates
│   ├── base.html
│   └── registration/
│       └── login.html
├── manage.py
├── requirements.txt
└── .env
```

## Dependencies

- Python 3.8+
- Django 5.0+
- PostgreSQL 14+
- django-ckeditor-5
- Pillow (Python Imaging Library)
- python-dotenv

## Local Development Setup

1. Clone the repository:
```bash
git clone [repository-url]
cd DjangoBlogProject
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root:
```
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=your_db_name
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

5. Configure PostgreSQL:
- Install PostgreSQL
- Create a database named 'your_db_name'
- Update .env with your database credentials

6. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

## Key Components

### Models

The main model is `Post` in `blog/models.py`:
- Title
- Slug (auto-generated from title)
- Content (CKEditor field)
- Excerpt
- Featured Image
- Creation/Update timestamps
- Author (linked to User model)

### Views

- PostListView: Displays all blog posts
- PostDetailView: Shows individual post
- PostCreateView: Create new posts (auth required)
- PostUpdateView: Edit posts (auth required)
- PostDeleteView: Delete posts (auth required)

### Templates

- base.html: Main template with navigation and structure
- post_list.html: Blog post listing
- post_detail.html: Individual post view
- post_form.html: Create/Edit post form
- login.html: Authentication page

## Styling

- Materialize CSS for main styling
- Custom CSS in static/css/blog.css for:
  - Responsive images
  - CKEditor content styling
  - Mobile-friendly adjustments

## Environment Variables

Required environment variables:
```
DJANGO_SECRET_KEY
DJANGO_DEBUG
DJANGO_ALLOWED_HOSTS
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
```

## Deployment Notes

- Set DEBUG=False in production
- Configure proper ALLOWED_HOSTS
- Set up proper PostgreSQL database credentials
- Configure static files serving
- Set up media files handling
- Configure proper security settings

## Future Enhancements

Potential improvements to consider:
- Categories/Tags for posts
- Search functionality
- Social media sharing
- Comments system
- RSS feed
- Newsletter integration
- SEO optimizations
- Analytics integration
- Automated testing
- CI/CD pipeline

## Maintenance

Regular maintenance tasks:
1. Database backups
2. Security updates
3. Django and dependency updates
4. Performance monitoring
5. Content backup

## Security Considerations

- Admin-only posting enforced through LoginRequiredMixin
- CSRF protection enabled
- Secure password storage
- File upload restrictions
- XSS protection through Django's template system
- SQL injection protection through Django's ORM

## License

MIT

## Author

C. Parker Sipes