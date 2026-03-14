import re
from urllib.parse import urlparse

from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from core.constants import GITHUB_REPOSITORY_VALID_PATTERN


def validate_github_repo_url(value):
    """
    Валидатор для проверки ссылки на конкретный репозиторий GitHub.
    Проверяет формат: github.com/<username>/<repository>
    """
    parsed_url = urlparse(value)
    domain = parsed_url.netloc.lower()

    if domain not in settings.ALLOWED_GITHUB_DOMAINS:
        raise ValidationError(
            _('Ссылка должна вести на github.com'),
            code='invalid_domain'
        )

    path = parsed_url.path.strip('/')

    if not GITHUB_REPOSITORY_VALID_PATTERN.match(path):
        raise ValidationError(
            _('Некорректный формат URL репозитория. Ожидаемый формат: github.com/username/repository'),
            code='invalid_repo_format'
        )

    return value
