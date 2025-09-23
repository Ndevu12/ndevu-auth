import uvicorn

from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

from supertokens_python import init, get_all_cors_headers
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python.recipe.session import SessionContainer
from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.multitenancy.asyncio import list_all_tenants

import config

# SuperTokens init should happen in config.py
print("SuperTokens configuration loaded successfully")


app = FastAPI(
    title="Ndevu Auth API",
    description="Secure Multi-Factor Authentication System API",
    # Disable automatic trailing slash redirection
    redirect_slashes=False
)

# Add SuperTokens middleware FIRST (this is crucial for route registration)
print("Adding SuperTokens middleware...")
app.add_middleware(get_middleware())
print("SuperTokens middleware added successfully")

# Add CORS middleware after SuperTokens
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        config.app_info.website_domain,
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type", "Authorization"] + get_all_cors_headers(),
)

async def get_session_info(s: SessionContainer = Depends(verify_session())):
    return {
        "sessionHandle": s.get_handle(),
        "userId": s.get_user_id(),
        "accessTokenPayload": s.get_access_token_payload(),
    }

# Add routes for both with and without trailing slash
app.get("/sessioninfo")(get_session_info)
app.get("/sessioninfo/")(get_session_info)

@app.get("/tenants")
@app.get("/tenants/")
async def get_tenants():
    tenantReponse = await list_all_tenants()

    tenantsList = []

    for tenant in tenantReponse.tenants:
        tenantsList.append(tenant.to_json())

    return {
        "status": "OK",
        "tenants": tenantsList,
    }



if __name__  == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3008)
