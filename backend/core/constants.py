import re

# users/avatars_utils.py
AVATAR_FONT_SIZE = 80
AVATAR_BACKGROUND_COLORS = (
    (255, 182, 193), (173, 216, 230), (144, 238, 144),
    (250, 250, 210), (221, 160, 221), (240, 230, 140),
    (230, 230, 250), (254, 214, 188), (239, 169, 74),
    (255, 117, 20), (93, 155, 155), (127, 181, 181),
    (222, 247, 254), (255, 254, 224), (250, 248, 246),
    (29, 236, 248), (255, 209, 220), (161, 133, 148)
)
AVATAR_TEXT_COLOR = (50, 50, 50)
AVATAR_RANDOM_RANGE = (1000, 9999)

FONT_PATHS = [
    '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
    'arial.ttf',
]
AVATAR_SIZE = 128
AVATAR_SIZE_TUPLE = (128, 128)
AVATAR_TEXT_VERTICAL_OFFSET = -10

# users/validators.py
PHONE_CLEAN_PATTERN = re.compile(r'[^\d+]')
PHONE_VALID_PATTERN = re.compile(r'\+7\d{10}')

# projects/validators.py
GITHUB_REPOSITORY_VALID_PATTERN = re.compile(r'^[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+$')

# projects/views.py
PARTICIPANT_ACTION_ADD = 'add'
PARTICIPANT_ACTION_REMOVE = 'remove'

SKILLS_AUTOCOMPLETE_LIMIT = 10

PROJECT_STATUS_OPEN = 'open'
PROJECT_STATUS_CLOSED = 'closed'
