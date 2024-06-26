class Comment:
    # 评论类 用于映射，类似于java的mapper
    def __init__(self, index=None, content=None, likes=None):
        self.index = index
        self.content = content
        self.likes = likes

    def to_dict(self):
        return {"index": self.index, "content": self.content, "likes": self.likes}
