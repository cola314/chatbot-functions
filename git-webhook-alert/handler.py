import os

def get_env_str(key):
    return os.getenv(key)

def get_env_boolean(key):
    value = os.getenv(key, 'false')
    return value.lower() in ['true', '1']

kakao_bot_server_api = get_env_str('KAKAO_BOT_SERVER_API')
kakao_bot_api_key = get_env_str('KAKAO_BOT_API_KEY')
use_secret = get_env_boolean('USE_SECRET')
secret = get_env_str('SECRET')

def handle(event, context):
    if event.method != 'GET':
        return {
            "statusCode": 405,
            "body": "Method not allowed"
        }
    return {
        "statuscode" : 200,
        "body": event.path
    }

        
