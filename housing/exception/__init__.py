from distutils.log import error
from email import message
import os
import sys


class Housing_exception(Exception):

    def __init__(self, error message:Exception,error_detail:sys):
        super().__init__(error_message)


        self.error_message=error_message


        @staticmethod
        def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:


            return error_message

