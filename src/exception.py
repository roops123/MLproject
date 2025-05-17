import sys
def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    filelineno=exc_tb.tb_lineno
    error_message=f"The error is raised from script {filename} ,line no: {filelineno}, error :{str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail)

    def __str__(self):
        return self.error_message