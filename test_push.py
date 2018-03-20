from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AIzaSyDF2DbF1kufjM0PW_1vSJ7xfcU6MLsrpzg")

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "202763365202"
message_title = "New visitor"
message_body = "Hi Harsh, You have a visitor at your office"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

print(result)
