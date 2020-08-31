class Config():
    """
    Base Configurations
    """
    APP_HOST="" #Defaults to 127.0.0.1
    APP_PORT="" #Defaults to 5000
    BASE_URL_API="" #Beta
    DEBUG=True #Set False for production

    """
    Static Files Configuration
    """
    STATIC_FOLDER="./templates/jinjaTemplate/assets" #Folder for static files
    TEMPLATE_FOLDER="./templates/jinjaTemplate" #Folder For html files
    HOME_PAGE="pages/main.html" #Landing Page

    """
    Database Configuration
    """
    DB_HOST="localhost"
    DB_NAME="test"
    DB_USERNAME="root"
    DB_PASSWORD=""

    """
    Log Configuration
    """
    LOG_FILE_PATH="logs/"
    LOG_FILE_NAME="app.log"
    #LOG_LEVEL = INFO/DEBUG/WARNING
    LOGGING_LEVEL=""
    #LOGGING_TYPE = FILE/DB/ALL
    LOGGING_TYPE=""