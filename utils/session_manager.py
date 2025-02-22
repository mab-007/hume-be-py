from flask import current_app

class SessionManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SessionManager, cls).__new__(cls)
            cls._instance.current_session_id = None
            cls.conversation_session_id = None
            cls.conversation_history = []
            cls.user_id = None
            cls.current_conversation_interation_count = 0
            cls.previous_context_and_instructions_generated = 0
        return cls._instance
    
    @property
    def session_id(self):
        return self.current_session_id
    
    @session_id.setter
    def session_id(self, session_id):
        self.current_session_id = session_id

    @property
    def conversation_session_id(self):
        return self.conversation_session_id
    
    @conversation_session_id.setter
    def conversation_session_id(self, conversation_session_id):
        self.conversation_session_id = conversation_session_id

    @property
    def user_id(self):
        return self.user_id
    
    @user_id.setter
    def user_id(self, user_id):
        self.user_id = user_id
        
