import random


class MultiTable:
    def __init__(self, settings):
        self.tasks = []

        for mult, value in settings.items():
            if value:
                for i in range(1, 10):
                    self.tasks.append({
                        'text': f'{i} \u00d7 {mult}',
                        'answer': str(i * mult)
                    })
        self.num_tasks = len(self.tasks)

    def get_task(self):
        while self.tasks:
            item = random.choice(self.tasks)
            self.tasks.remove(item)
            context = {
                'task': item,
                'num_tasks': self.num_tasks
            }
            yield context
