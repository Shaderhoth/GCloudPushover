# PushoverAlerts
This is a project using python, flask and pushover to send a custom notification from a https web request

## To use
Upload code to google cloud run, and set up environment variables

You can set minimum instances to 1 to prevent false starts
>BOT_TOKEN=...
>
>USR_TOKEN=...
>
>FLASK_SECRET=...

Test using the cloud run url e.g https://custom_app_link_msg.a.run.app/?title=test
