# Makefile

# Define the name of your FastAPI application module
APP_MODULE = main:app

# Command to start the server using uvicorn
run:
	uvicorn $(APP_MODULE) --reload --host 0.0.0.0 --port 8000

# Additional commands can be added here
