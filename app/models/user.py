import requests

def list_users() -> list:
    '''
    Obtém todos os usuários da API

    Returns:
        list(users): uma lista de usuários
    '''
    response = requests.get("https://reqres.in/api/users")
    if response.status_code == 200:
        return response.json()['data']
    
    print("Ocorreu um erro")
    return []
    

def get_user(user_id:int) -> dict:
    '''
    Obtém um usuário da API

    Returns:
        dict(users): uma dict de um usuário
    '''
    response = requests.get(f"https://reqres.in/api/users/{str(user_id)}")
    if response.status_code == 200:
        return response.json()['data']
    print("Ocorreu um erro")
    return {}
