from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for, render_template
from flask.json import jsonify
import os


app = Flask(__name__, template_folder='templates')
# app.config.from_pyfile('config.cfg')

# This information is obtained upon registration of a new GitHub OAuth
# application here: https://github.com/settings/applications/new
client_id = "########################################"
client_secret = "@@@@@@@@@@@@@@@@@@@@@@@@@"
authorization_base_url = "https://accounts.google.com/o/oauth2/v2/auth"
redirect_uri = 'http://localhost:5000/callback'
token_url = "https://www.googleapis.com/oauth2/v4/token"
scope = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile"
    ]

@app.route("/", methods=['GET'])
def demo():
    """Step 1: User Authorization.
    Redirect the user/resource owner to the OAuth provider (i.e. Github)
    using an URL with a few key OAuth parameters.
    """
    google = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
    authorization_url, state = google.authorization_url(authorization_base_url,access_type="offline", prompt="select_account")

    return redirect(authorization_url)

# Step 2: User authorization, this happens on the provider.

@app.route("/callback", methods=["GET"])
def callback():
    """ Step 3: Retrieving an access token.

    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """
    # Fetch the access token
    google = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
    google.fetch_token(token_url, client_secret=client_secret, authorization_response=request.url)
    
    # At this point you can fetch protected resources but lets save
    # the token and show how this is done from a persisted token
    # in /profile.
    r = google.get('https://www.googleapis.com/oauth2/v1/userinfo')
    return jsonify(r.json())

if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = "1"
    app.secret_key = os.urandom(24)
    app.run(debug=True)