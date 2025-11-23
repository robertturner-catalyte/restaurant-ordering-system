from pathlib import Path
from .setup import create_app

root_folder = Path(__file__).parent
env_file = Path(root_folder, "environments/.env")


app = create_app(env_file)