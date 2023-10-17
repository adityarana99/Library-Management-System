from app import ui
from app.database import close_session

if __name__ == "__main__":
    try:
        ui.run_library_management_system()
    finally:
        close_session()