import router
from server import *

if __name__ == "__main__":
    table_name = "comments"
    tool.create_table(table_name, ["content", "likes"])
    router.app.run(port=5000, debug=True)
