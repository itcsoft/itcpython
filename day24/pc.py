# Создай обьект своего компьютера
# 
class PC:
    def __init__(self, **kwargs):
        self.processor = kwargs['processor']


mypc = PC(
    processor = 'Intel Core i7-10700K'
)