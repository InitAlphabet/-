from router import app
import tool
from comments import Comment
from flask import request


@app.route("/get_comments", methods=["GET"])
def get_comments():
    table_name = "comments"
    res = tool.get_all(table_name)
    comments = []
    for comment in res:
        comments.append(Comment(index=comment[0], content=comment[1], likes=comment[2]).to_dict())
    return comments


@app.route("/add_comment", methods=["GET"])
def add_comment():
    table_name = "comments"
    content = request.args.get("content")
    likes = "0"
    if tool.add(table_name=table_name, line_dict={"content": content, "likes": likes}):
        return {"index":tool.get_max_id(table_name)[0][0]}


@app.route("/delete_comment", methods={"GET"})
def delete_comment():
    table_name = "comments"
    index = request.args.get("index")
    if tool.delete(table_name, index):
        return {"status": 200}
    return {"status": 400}
