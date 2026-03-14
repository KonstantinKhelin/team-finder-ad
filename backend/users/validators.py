import re
from urllib.parse import urlparse

from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from core.constants import PHONE_VALID_PATTERN, PHONE_CLEAN_PATTERN


def validate_no_digits(value):
    value = value.strip()
    if re.search(r'\d', value):
        raise ValidationError(_('Имя не должно содержать цифр.'))
    return value


def validate_phone_number(value):
    """
    Валидатор для номера телефона.
    Принимает форматы: 8XXXXXXXXX или +7XXXXXXXXX.
    Преобразует в формат +7XXXXXXXXX.
    """
    cleaned = PHONE_CLEAN_PATTERN.sub('', value)

    if cleaned.startswith('8'):
        cleaned = '+7' + cleaned[1:]
    elif not cleaned.startswith('+7'):
        raise ValidationError(
            _('Номер должен начинаться с 8 или +7'),
            code='invalid_format'
        )

    if not PHONE_VALID_PATTERN.match(cleaned):
        raise ValidationError(
            _('Некорректный номер телефона (должен быть +7 и 10 цифр после)'),
            code='invalid_phone'
        )

    return cleaned


def validate_github_url(value):
    """
    Валидатор для проверки ссылки на GitHub.
    Проверяет, что URL относится к github.com.
    """
    try:
        parsed = urlparse(value)
        if not parsed.scheme or not parsed.netloc:
            raise ValidationError(
                _('Введите полный URL (например, https://github.com/username)'),
                code='invalid_url'
            )
        if parsed.netloc not in settings.ALLOWED_GITHUB_DOMAINS:
            raise ValidationError(
                _('Ссылка должна вести на github.com'),
                code='invalid_domain'
            )
    except (ValueError, AttributeError):
        raise ValidationError(
            _('Некорректный URL'),
            code='invalid_url'
        )
    return value
