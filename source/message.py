class Message():

    def __init__(self, type='0', is_end='0', message_length='0',
                 user_name='', pass_word='', content=''):
        self.type = type
        self.is_end = is_end
        self.message_length = message_length
        self.user_name = user_name
        self.pass_word = pass_word
        self.content = content

    def get_message(self):
        return self.type + self.is_end + self.message_length + \
               self.user_name.ljust(20, '0') + self.pass_word.ljust(20, '0') + self.content.ljust(512, '0')


class Respond():

    def __init__(self, type, status):
        self.type = type
        self.status = status
