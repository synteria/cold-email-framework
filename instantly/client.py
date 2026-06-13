import os

import requests
from dotenv import load_dotenv


class InstantlyAPIError(Exception):
    def __init__(self, status_code, message, response_body=None):
        self.status_code = status_code
        self.message = message
        self.response_body = response_body
        super().__init__(f"{status_code}: {message}")


class InstantlyClient:
    BASE_URL = "https://api.instantly.ai"

    def __init__(self, api_key=None, client=None):
        if api_key is None:
            load_dotenv()
            if client:
                # Slugs may contain hyphens (e.g. "acme-co"); env var
                # names cannot, so normalize hyphens to underscores to match
                # the .env key naming.
                env_var = f"INSTANTLY_API_KEY_{client.replace('-', '_').upper()}"
                api_key = os.environ.get(env_var)
                if not api_key:
                    raise ValueError(
                        f"No API key for client '{client}'. Set {env_var} in .env "
                        f"(per-workspace key naming: INSTANTLY_API_KEY_<CLIENT_SLUG>)."
                    )
            else:
                api_key = os.environ.get("INSTANTLY_API_KEY")
        if not api_key:
            raise ValueError(
                "No API key provided. Pass api_key=, client=<slug>, "
                "or set INSTANTLY_API_KEY in .env"
            )
        self.api_key = api_key

    def create_campaign(self, payload):
        return self._request("POST", "/api/v2/campaigns", json=payload)

    def activate_campaign(self, campaign_id):
        return self._request("POST", f"/api/v2/campaigns/{campaign_id}/activate")

    def update_campaign(self, campaign_id, payload):
        # PATCH (not DELETE + recreate): the delete endpoint is finicky and
        # recreate churns IDs. PATCH /campaigns/{id} with {"sequences": ...}
        # updates copy in place on an existing draft.
        return self._request("PATCH", f"/api/v2/campaigns/{campaign_id}", json=payload)

    def get_campaign(self, campaign_id):
        # GET /campaigns/{id} - fetch a single campaign (sequences, status, etc.).
        return self._request("GET", f"/api/v2/campaigns/{campaign_id}")

    def list_accounts(self, limit=100):
        # GET /accounts - paginate every connected sending account in the
        # workspace via the `starting_after` cursor. Returns the full list of
        # account dicts. Used to auto-populate a campaign's sending accounts.
        out = []
        starting_after = None
        while True:
            params = {"limit": limit}
            if starting_after:
                params["starting_after"] = starting_after
            data = self._request("GET", "/api/v2/accounts", params=params)
            items = data.get("items", data) if isinstance(data, dict) else data
            if not items:
                break
            out.extend(items)
            starting_after = (
                data.get("next_starting_after") if isinstance(data, dict) else None
            )
            if not starting_after:
                break
        return out

    def _request(self, method, endpoint, json=None, params=None):
        url = f"{self.BASE_URL}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        response = requests.request(method, url, headers=headers, json=json, params=params)

        if response.status_code == 401:
            raise InstantlyAPIError(401, "Authentication failed. Check your API key.")
        if response.status_code == 422:
            body = response.json() if response.text else {}
            detail = body.get("detail", body)
            raise InstantlyAPIError(422, f"Validation error: {detail}", body)
        if response.status_code == 429:
            raise InstantlyAPIError(429, "Rate limited. Wait a moment and retry.")
        if response.status_code >= 500:
            raise InstantlyAPIError(
                response.status_code, "Instantly server error. Try again shortly."
            )
        if not response.ok:
            body = response.json() if response.text else {}
            raise InstantlyAPIError(response.status_code, str(body), body)

        return response.json()
