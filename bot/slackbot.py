from common.logger import Logger


class SlackBot(object):
    logger = Logger('SlackBot')

    def __init__(self):
        return None
    
    def  handle_command(self, command):
        response = None
        try:
            if command == 'help' or command == '도움말':
                response = "관련 단어를 사용합니다."
            
            if command == 'all' or command == '전체':
                from menu.views import search_all
                response = search_all()
                
        except Exception as e:
            self.logger.debug(e)
            response = "오류"

        return response
    
    def start(self):
        self.logger.debug('Starter Bot connected and running!')
        return None
