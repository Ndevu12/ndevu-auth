from supertokens_python.recipe import session
from supertokens_python.recipe import dashboard
from supertokens_python.recipe import userroles
from supertokens_python.recipe import emailpassword
from supertokens_python.recipe import thirdparty
from supertokens_python.recipe.thirdparty.provider import ProviderInput, ProviderConfig, ProviderClientConfig
from supertokens_python.recipe import passwordless
from supertokens_python.recipe import multifactorauth
from supertokens_python.recipe import emailverification
from supertokens_python.recipe import accountlinking
from supertokens_python.recipe.passwordless import ContactEmailOnlyConfig
from supertokens_python.recipe.accountlinking.types import AccountInfoWithRecipeIdAndUserId, ShouldAutomaticallyLink, ShouldNotAutomaticallyLink
from supertokens_python.recipe.session.interfaces import SessionContainer
from supertokens_python.types import User
from supertokens_python.recipe.multifactorauth.interfaces import RecipeInterface as MFARecipeInterface
from supertokens_python.recipe.multifactorauth.types import MFARequirementList, FactorIds
from typing import Optional, Dict, Any, Union, Callable, Awaitable, List

from supertokens_python import init, InputAppInfo, SupertokensConfig
import os

def override_multifactor_functions(original_implementation: MFARecipeInterface):
    async def get_mfa_requirements_for_auth(
        tenant_id: str,
        access_token_payload: dict,
        completed_factors: dict,
        user,
        factors_set_up_for_user,
        required_secondary_factors_for_user,
        required_secondary_factors_for_tenant,
        user_context: dict,
    ) -> MFARequirementList:
        return [
            {
                "oneOf": [
                    FactorIds.OTP_EMAIL
                ],
            }
        ]

    async def get_required_secondary_factors_for_user(
        tenant_id: str,
        user_id: str,
        user_context: dict,
    ) -> list:
        return [FactorIds.OTP_EMAIL]

    original_implementation.get_mfa_requirements_for_auth = get_mfa_requirements_for_auth
    original_implementation.get_required_secondary_factors_for_user = get_required_secondary_factors_for_user
    return original_implementation


async def async_should_do_linking(
    new_account_info: AccountInfoWithRecipeIdAndUserId,
    user: Optional[User],
    session: Optional[SessionContainer],
    tenant_id: str,
    user_context: Dict[str, Any],
) -> Union[ShouldNotAutomaticallyLink, ShouldAutomaticallyLink]:
    return ShouldAutomaticallyLink(should_require_verification=False)




def get_api_domain() -> str:
    api_port = str(3008)
    api_url = f"http://localhost:{api_port}"
    return api_url

def get_website_domain() -> str:
    website_port = str(3000)
    website_url = f"http://localhost:{website_port}"
    return website_url

supertokens_config = SupertokensConfig(
    connection_uri="http://localhost:3567"
)

app_info = InputAppInfo(
    app_name="Ndevu Auth",
    api_domain=get_api_domain(),
    website_domain=get_website_domain(),
    api_base_path="/auth",
    website_base_path="/auth"
)

recipe_list = [
    session.init(),
    dashboard.init(),
    userroles.init(),
    emailpassword.init(),
    thirdparty.init(
        sign_in_and_up_feature=thirdparty.SignInAndUpFeature(
            providers=[
                ProviderInput(
                    config=ProviderConfig(
                        third_party_id="google",
                        clients=[
                            ProviderClientConfig(
                                client_id="1060725074195-kmeum4crr01uirfl2op9kd5acmi9jutn.apps.googleusercontent.com",
                                client_secret="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"
                            )
                        ]
                    )
                ),
                ProviderInput(
                    config=ProviderConfig(
                        third_party_id="apple",
                        clients=[
                            ProviderClientConfig(
                                client_id="4398792-io.supertokens.example.service",
                                additional_config={
                                    "keyId": "7M48Y4RYDL",
                                    "privateKey": "-----BEGIN PRIVATE KEY-----\nMIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgu8gXs+XYkqXD6Ala9Sf/iJXzhbwcoG5dMh1OonpdJUmgCgYIKoZIzj0DAQehRANCAASfrvlFbFCYqn3I2zeknYXLwtH30JuOKestDbSfZYxZNMqhF/OzdZFTV0zc5u5s3eN+oCWbnvl0hM+9IW0UlkdA\n-----END PRIVATE KEY-----",
                                    "teamId": "YWQCXGJRJL"
                                }
                            )
                        ]
                    )
                )
            ]
        )
    ),
    passwordless.init(
        flow_type="USER_INPUT_CODE",
        contact_config=ContactEmailOnlyConfig()
    ),
    multifactorauth.init(
        first_factors=["emailpassword", "otp-email", "thirdparty"],
        override=multifactorauth.OverrideConfig(
            functions=lambda original_implementation:
                override_multifactor_functions(original_implementation)
        )
    ),
    emailverification.init(
        mode="REQUIRED"
    ),
    accountlinking.init(
        should_do_automatic_account_linking=async_should_do_linking
    )
]

print("Initializing SuperTokens...")
print(f"App info: {app_info}")
print(f"Recipe list length: {len(recipe_list)}")

init(
    supertokens_config=supertokens_config,
    app_info=app_info,
    framework="fastapi",
    recipe_list=recipe_list,
    mode="asgi",
    telemetry=False
)

print("SuperTokens initialization completed successfully!")
