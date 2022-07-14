
import time
import requests

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.get(url=url)
#print(response.text)
data = response.json()
token = data['token']
job_pause = data['seconds'] # получение времени необходимого беку на выполнение джобы
#print(token)
#print(time)
response2 = requests.get(url=url, params={"token": token})
#print(response2.json())
data2 = response2.json()
stat = data2['status']  # получение статуса джобы
if stat == "Job is NOT ready":
    time.sleep(job_pause)  # использование полученного времени на выполнение джобы беком

response3 = requests.get(url=url, params={"token": token})
#print(response3.json())
data3 = response3.json()
stat2 = data3['status']
if stat2 == "Job is ready":
    print("Job is ready")
check_answer = (response3.json())
#print(check_answer)
key = 'result'
if key in check_answer:
    print("Result is found")
else:
    print("Result not found")

