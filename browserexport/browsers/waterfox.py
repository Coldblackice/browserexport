from .common import Path, handle_path
from .firefox import Firefox

# seems to match firefox schema well enough for all of our usage


class Waterfox(Firefox):
    has_form_history_save = False

    @classmethod
    def data_directory(cls) -> Path:
        return handle_path(
            {
                "linux": "~/.waterfox/",
                "darwin": "~/Library/Application Support/Waterfox/Profiles/",
            },
            browser_name=cls.__name__,
        )
