#!/usr/bin/env python
# coding=utf-8
import argparse


class ArgParseMain:

    def __init__(self):
        self.args = None
        self.parse_args()
        if self.check():
            self.run()

    @property
    def executors(self) -> dict:
        return {}

    def additional_argument(self, parser):
        pass

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--command', type=str, required=True,
                            choices=list(self.executors.keys()))
        parser.add_argument('-o', '--option', action='append', metavar=('name', 'value'), nargs=2, required=False)
        self.additional_argument(parser)
        parser.set_defaults(option=[])
        self.args = parser.parse_args()

    def check(self):
        return True

    def kwargs(self):
        res = {}
        for name, value in self.args.option:
            res[name] = value
        for k, v in self.args._get_kwargs():
            if k == 'command':
                continue
            if k != "option" and v is not None:
                res[k] = v

        return res

    def run(self):
        func = self.executors.get(self.args.command)
        if func is not None:
            func(**self.kwargs())
