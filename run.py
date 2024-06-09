print("Starting run.py")

from app import create_app

print("Imported create_app")

app = create_app()

print("Created app")

if __name__ == "__main__":
    print("Running app")
    app.run(debug=True)
