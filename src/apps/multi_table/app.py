class MultiTable:
    def __init__(self, settings):
        self.settings = settings

        self.tasks = [
            {
                'text': '1 \u00d7 4',
                'answer': '4',
            },
            {
                'text': '2 \u00d7 4',
                'answer': '8',
            },
            {
                'text': '3 \u00d7 4',
                'answer': '12',
            },
        ]
        # self.num_tasks = len(self.tasks)

    def get_task(self):
        for item in self.tasks:
            item = {
                'task': item,
                'num_tasks': len(self.tasks)
            }
            yield item

# class MultiTable:
#     def __init__(self, settings):
#         pass


