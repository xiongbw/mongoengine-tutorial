from config import create_app

app = create_app('flask-mongoengine-tutorial')

if __name__ == '__main__':
    app.run()
