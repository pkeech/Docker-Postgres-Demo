## IMPORT APPLICAITON
from src import create_app

## CREATE APPLICATION
app = create_app()

## RUN APPLICATION
if __name__ == "__main__":
    app.run()