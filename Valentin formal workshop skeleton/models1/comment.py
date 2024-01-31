class Comment:
    def __init__(self, content: str, author):
        self.content = content
        self.author = author


    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        if len(content) < 3 or len(content) > 200:
            raise ValueError('Content must be between 3 and 200 characters long!')
        self._content = content

    def __str__(self):
        return f'\n'.join(['----------',f'{self._content}',f'User: {self.author}','----------'])

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file

