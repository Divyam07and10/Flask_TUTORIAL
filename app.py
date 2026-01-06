import os
from dotenv import load_dotenv
from app import createApp

load_dotenv(".flaskenv")

app = createApp()

if __name__ == "__main__":
    app.run(
        host=os.getenv("FLASK_RUN_HOST", "0.0.0.0"),
        port=int(os.getenv("FLASK_RUN_PORT", 5000)),
        debug=os.getenv("FLASK_DEBUG", "1") == "1",
        reloader_type=os.getenv("FLASK_RELOADER_TYPE", "watchdog")
    )