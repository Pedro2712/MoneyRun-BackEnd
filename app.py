from fastapi import FastAPI, Response, Request

app = FastAPI()

@app.get('/login/garmin')
def login_garmin():
    client_id = 'YOUR_CLIENT_ID'
    redirect_uri = 'http://localhost:8000/callback'
    scope = 'profile'  # Ajuste conforme necessário
    response_type = 'code'

    auth_url = f"https://connect.garmin.com/oauthConfirm?client_id={client_id}&redirect_uri={redirect_uri}&response_type={response_type}&scope={scope}"
    return Response(status_code=303, headers={"Location": auth_url})

@app.get('/callback')
def callback(request: Request):
    code = request.query_params.get('code')
    return {"message": "Authorization code received", "code": code}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
