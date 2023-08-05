from exceptions.Exception import Exception


class IllegalCharException(Exception):

    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)