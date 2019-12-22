class Message():

    def __init__(self, type, is_end, message_length,
                 user_name, pass_word, content):
        self.type = type
        self.is_end = is_end
        self.message_length = message_length
        self.user_name = user_name
        self.pass_word = pass_word
        self.content = content


class Respond():

    def __init__(self, type, status):
        self.type = type
        self.status = status