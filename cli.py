#!/usr/bin/env python
import fire
from PyInquirer import prompt


class IngestionStage(object):
    def run(self):
        return 'Ingesting! Nom nom nom...'


class DigestionStage(object):
    def __init__(self):
        self.satiated = False

    def run(self, volume: int = 0) -> str:
        questions = [
            {
                'type': 'input',
                'name': 'volume',
                'message': 'How many burps?',
            }
        ]
        if volume == 0:
            volume = int(prompt(questions)['volume'])
        self.satiated = True
        return ' '.join(['Burp!'] * volume)

    def breakfast(self):
        questions = [
            {
                'type': 'list',
                'name': 'breakfast',
                'message': 'What did you want for breakfast?',
                'choices': ['eggs', 'bacon', 'toast']
            }
        ]
        switcher = {
            'eggs': 1,
            'bacon': 2,
            'toast': 3,
        }
        volume = switcher.get(prompt(questions)['breakfast'], 0)

        self.satiated = True
        return ' '.join(['Burp!'] * volume)

    def status(self):
        return 'Satiated.' if self.satiated else 'Not satiated.'


class Pipeline(object):

    def __init__(self):
        self.ingestion = IngestionStage()
        self.digestion = DigestionStage()

    def run(self):
        print(self.ingestion.run())
        print(self.digestion.run())
        print(self.digestion.status())
        return 'Pipeline complete'


if __name__ == '__main__':
    fire.Fire(Pipeline)
