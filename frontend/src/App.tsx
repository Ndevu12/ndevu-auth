import SuperTokens, { SuperTokensWrapper } from "supertokens-auth-react";
import { getSuperTokensRoutesForReactRouterDom } from "supertokens-auth-react/ui";
import { SessionAuth } from "supertokens-auth-react/recipe/session";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import * as ReactRouter from "react-router-dom";
import Dashboard from "./Dashboard";
import { PreBuiltUIList, SuperTokensConfig, ComponentWrapper } from "./config";
import Home from "./Home";

// Initialize SuperTokens - ideally in the global scope
SuperTokens.init(SuperTokensConfig);

function App() {
    return (
        <SuperTokensWrapper>
            <BrowserRouter>
                <main className="App app-container">
                    <header>
                        <nav className="header-container">
                            <Link to="/">
                                <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#333' }}>
                                    Ndevu Auth
                                </div>
                            </Link>
                            <ul className="header-container-right">
                                <li>
                                    <a
                                        href="https://github.com/ndevu12"
                                        target="_blank"
                                        rel="noopener noreferrer"
                                    >
                                        GitHub
                                    </a>
                                </li>
                            </ul>
                        </nav>
                    </header>
                    <div className="fill" id="home-container">
                        <ComponentWrapper>
                            <Routes>
                                <Route path="/" element={<Home />} />
                                {/* This shows the login UI on "/auth" route */}
                                {getSuperTokensRoutesForReactRouterDom(ReactRouter, PreBuiltUIList)}

                                {/* This protects the "/dashboard" route so that it shows
                                <Dashboard /> only if the user is logged in.
                                Else it redirects the user to "/auth" */}
                                <Route
                                    path="/dashboard"
                                    element={
                                        <SessionAuth>
                                            <Dashboard />
                                        </SessionAuth>
                                    }
                                />
                            </Routes>
                        </ComponentWrapper>
                        <footer>
                            Built with ❤️ by{" "}
                            <a href="https://github.com/ndevu" target="_blank" rel="noopener noreferrer">
                                Ndevu
                            </a>
                            {" "}using SuperTokens
                        </footer>
                        <img className="separator-line" src="/assets/images/separator-line.svg" alt="separator" />
                    </div>
                </main>
            </BrowserRouter>
        </SuperTokensWrapper>
    );
}

export default App;
