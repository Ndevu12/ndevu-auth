import { Link } from "react-router-dom";
import { useSessionContext } from "supertokens-auth-react/recipe/session";

export default function Home() {
    const session = useSessionContext();

    if (session.loading) {
        return null;
    }

    return (
        <>
            <section className="logos">
                <div style={{ fontSize: '48px', fontWeight: 'bold', color: '#333' }}>
                    🔐 Ndevu Auth
                </div>
            </section>
            <section className="main-container">
                <div className="inner-content">
                    <h1>
                        <strong>Ndevu Auth</strong> <br /> Secure Multi-Factor Authentication System
                    </h1>
                    <div>
                        {session.doesSessionExist ? (
                            <p>
                                Welcome back! You're securely authenticated. <br /> Access your dashboard below 👇
                            </p>
                        ) : (
                            <p>Sign in with Google, Apple, or Email to get started</p>
                        )}
                    </div>
                    <nav className="buttons">
                        {session.doesSessionExist ? (
                            <Link to="/dashboard" className="dashboard-button">
                                Dashboard
                            </Link>
                        ) : (
                            <Link to="/auth" className="dashboard-button">
                                Sign-up / Login
                            </Link>
                        )}
                    </nav>
                </div>
            </section>
        </>
    );
}
