import enum


class EnumURL(enum.Enum):
    HOMEPAGE = "http://127.0.0.1:8000/" 
    ADMIN_LOGIN = "http://127.0.0.1:8000/admin/login/?next=/admin/" 
    ADMIN_LOGOUT = "http://127.0.0.1:8000/admin/logout/"
    GROUPS_PAGE = "http://127.0.0.1:8000/admin/auth/group/"
    CATEGORIES_PAGE = "http://127.0.0.1:8000/admin/reviews/categories/"
