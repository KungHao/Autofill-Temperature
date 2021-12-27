import requests

url = "https://notify-api.line.me/api/notify"

#發送line notify的function
def lineNotifyMessage(token, message):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    
    msg = {'message': message}
    req = requests.post(url, headers = headers, params = msg)
    return req.status_code

if __name__ == '__main__':
  message = '[LINE Notify] Hello World' # 要傳送的訊息內容
  token = '196YlNGoW1ufiDV71VhFzP1SzirT2Xls2Tz6PNSYyR7' # 權杖值
  lineNotifyMessage(token, message)
  print('Done!')

  # 勇者試煉 196YlNGoW1ufiDV71VhFzP1SzirT2Xls2Tz6PNSYyR7

  # 新貴派 ilHZdst8RoNKQ6BIil9eb07s03BjebhB0YMmJ64W6un

  # 這個就 swVB9l0nKNETNscqFz8HkzhqCNot9W0fKSYg8Z0R9yj