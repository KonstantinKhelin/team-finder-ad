from django.contrib.auth.models import BaseUserManager
from PIL import Image, ImageDraw, ImageFont
import os
from django.conf import settings
import random
import logging
from django.core.files import File
from django.core.files.storage import default_storage
import io

logger = logging.getLogger(__name__)

class CustomUserManager(BaseUserManager):

    def create_user(self, email, name, surname, avatar=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Пользователь должен иметь email')
        if not name:
            raise ValueError('Пользователь должен иметь Имя')
        if not surname:
            raise ValueError('Пользователь должен иметь Фамилию')
        email = self.normalize_email(email)
        print(avatar)
        if avatar is None:
            try:
                avatar_image = self.generate_avatar(name)  # Возвращает PIL.Image
                if avatar_image:
                    # Преобразуем PIL.Image в File
                    image_buffer = io.BytesIO()
                    avatar_image.save(image_buffer, format='PNG')
                    image_buffer.seek(0)

                    # Формируем имя файла
                    avatar_filename = f'avatar_{name}_{random.randint(1000, 9999)}.png'

                    # Сохраняем в хранилище и получаем путь
                    avatar_path = default_storage.save(
                        f'avatars/{avatar_filename}',
                File(image_buffer)
            )
                    avatar = avatar_path  # Теперь это путь, который поймёт ImageField
                else:
                    raise ValueError("Не удалось сгенерировать аватар")
            except Exception as e:
                logger.error(f"Ошибка генерации аватара для {name}: {e}")
                avatar = None  # Продолжаем без аватара

        #    try:
        #        avatar = self.generate_avatar(name)
        #        if not avatar:
        #            raise ValueError("Сгенерированный аватар имеет некорректный путь")
        #    except Exception as e:
        #        logger.error(f"Ошибка генерации аватара для {name}: {e}")
        #        raise ValueError("Не удалось сгенерировать аватар")
        user = self.model(
            email=email,
            name=name,
            surname=surname,
            avatar=avatar,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, surname, avatar=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, name, surname, avatar, password, **extra_fields)

    def generate_avatar(self, name):
        """
        Генерирует аватарку с первой буквой имени на однотонном фоне.
        Сохраняет изображение в media/avatars.
        Возвращает URL аватара.
        """
        # Проверяем, что имя не пустое
        if not name:
            raise ValueError("Name cannot be empty")

        # Палитра пастельных цветов (RGB)
        colors = [
            (255, 182, 193),  # Светло-розовый
            (173, 216, 230),  # Светло-голубой
            (144, 238, 144),  # Светло-зелёный
            (250, 250, 210),  # Светло-жёлтый
            (221, 160, 221),  # Сиреневый
            (240, 230, 140),  # Палевый
            (230, 230, 250),  # Лавандовый
        ]

        bg_color = random.choice(colors)
        text_color = (50, 50, 50)  # Тёмно-серый для контраста

        # Создаём изображение 128x128
        image = Image.new('RGB', (128, 128), bg_color)
        draw = ImageDraw.Draw(image)

        # Получаем первую букву имени
        first_letter = name[0].upper()

        # Подбираем шрифт
        try:
            font = ImageFont.truetype('arial.ttf', 80)
        except OSError:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), first_letter, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (128 - text_width) // 2
        y = (128 - text_height) // 2 - 10  # Немного поднимаем для визуального баланса

        draw.text((x, y), first_letter, fill=text_color, font=font)
        return image
        # Формируем путь сохранения
        #avatar_dir = 'avatars'
        #avatar_filename = f'avatar_{name}_{random.randint(1000, 9999)}.png'
        #avatar_path = os.path.join(avatar_dir, avatar_filename)
        ## Сохраняем изображение в медиа-каталог Django
        #media_path = os.path.join(settings.MEDIA_ROOT, avatar_path)
        #image.save(media_path)
#
        #avatar_url = avatar_path
        #return avatar_url
