import { useSessionContext, signOut } from "supertokens-auth-react/recipe/session";
import { getApiDomain } from "../config";
import { useNavigate } from "react-router-dom";

export default function Dashboard() {
    const navigate = useNavigate();
    const sessionContext = useSessionContext();

    async function callAPIClicked() {
        try {
            const response = await fetch(getApiDomain() + "/sessioninfo");
            const data = await response.json();
            window.alert("Session Information:\n" + JSON.stringify(data, null, 2));
        } catch (err) {
            window.alert("Error calling API: " + err.message);
        }
    }

    async function logoutClicked() {
        await signOut();
        navigate("/");
    }

    return (
        <>
            <div className="main-container">
                <div className="top-band success-title bold-500">
                    <img src="/assets/images/celebrate-icon.svg" alt="Authentication successful" className="success-icon" />
                    🔐 Authentication Successful
                </div>
                <div className="inner-content">
                    <h2>Welcome to Ndevu Auth Dashboard!</h2>
                    <div>Your secure user ID is:</div>
                    <div className="truncate" id="user-id">
                        {sessionContext.userId}
                    </div>
                    <p style={{ marginTop: '20px', color: '#666' }}>
                        You have successfully authenticated with Multi-Factor Authentication enabled.
                    </p>
                    <div className="buttons">
                        <button onClick={callAPIClicked} className="dashboard-button">
                            View Session Info
                        </button>
                        <button onClick={logoutClicked} className="dashboard-button">
                            Secure Logout
                        </button>
                    </div>
                </div>
            </div>
        </>
    );
}
