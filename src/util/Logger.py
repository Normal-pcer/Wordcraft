import time
import colorama
import os
from typing import Union, List
from util.codec import Serializers, Serializer


class Logger:
    """
    wordcraft.util.logger
    """

    name: str
    logFile: str
    debugTags: Union[None, List[str]]
    serializer: Serializer

    @staticmethod
    def _time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def _message(self, *messages: any, split=' '):
        return split.join([msg if isinstance(msg, str) else self.serializer.serialize(msg) 
                           for msg in messages])

    def __init__(self, name: str, debug: Union[None, List[str]] = None,
                 serializer: Serializer = Serializers.Repr):
        self.name = name
        self.logFile = "logs/log.txt"
        self.debugTags = debug
        self.serializer = serializer

        if not os.path.exists(os.path.dirname(self.logFile)):
            os.makedirs(os.path.dirname(self.logFile))
        
        if debug is None:
            self.debugTags = list()

    def debug(self, *messages, split=' ', tag: str = "general"):
        if tag in self.debugTags or "everything" in self.debugTags:
            log_file = open(self.logFile, "a", encoding="UTF-8")
            text = f"[{self.name}][DEBUG #{tag} at {self._time()}]{self._message(*messages, split)}"
            print(text)
            log_file.write(text+'\n')
            log_file.close()

    def info(self, *messages, split=' '):
        log_file = open(self.logFile, "a", encoding="UTF-8")
        text = f"[{self.name}][INFO at {self._time()}]{self._message(*messages, split)}"
        print(text)
        log_file.write(text+'\n')
        log_file.close()

    def warning(self, *messages, split=' '):
        log_file = open(self.logFile, "a", encoding="UTF-8")
        text = f"[{self.name}][WARNING at {self._time()}]{self._message(*messages, split)}"
        print(colorama.Fore.YELLOW, text, colorama.Style.RESET_ALL)
        log_file.write(text+'\n')
        log_file.close()

    def error(self, *messages, split=' '):
        log_file = open("log.txt", "a", encoding="UTF-8")
        text = f"[{self.name}][ERROR at {self._time()}]{self._message(*messages, split)}"
        print(colorama.Fore.RED, text, colorama.Style.RESET_ALL)
        log_file.write(text+'\n')
        log_file.close()
