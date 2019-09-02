from app_init import app
from blueprints import register_blueprints

register_blueprints(app)

print()
print(app.url_map)
print()

if __name__ == '__main__':
    app.run()
