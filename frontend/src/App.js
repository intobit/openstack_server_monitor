import './App.css';
import CheckServerSocket from "./components/server_ws";
import CheckRouterSocket from "./components/router_ws";

function App() {
  return (
      <>
        <CheckServerSocket />
        <CheckRouterSocket />
      </>
  );
}

export default App;
