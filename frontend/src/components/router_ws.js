import {useEffect, useState} from "react";
import useWebSocket, {ReadyState} from "react-use-websocket";
import Accordion from 'react-bootstrap/Accordion';
import './router_ws.css'

function CheckRouterSocket() {

    const socketUrl = "ws://localhost:8001/ws_router";
    const {lastJsonMessage} = useWebSocket(socketUrl,
        {onOpen: () => console.log("Router WebSocket connected"),
            shouldReconnect: (closeEvent) => true, })
    const [routerData, setRouterData] = useState([]);
    const [dataReceived, setDataReceived] = useState(false);
    const date = new Date();
    const currentTime = new Intl.DateTimeFormat('de-DE', {
        hour: "numeric",
        minute: "numeric",
    }).format(date)

    useEffect(() => {

        if (lastJsonMessage !== null && ReadyState.OPEN) {
            const data = lastJsonMessage;
            console.log("Message from router ", data);
            if (data[0].name === 'router_main') {
                setRouterData(data);
                setDataReceived(true);
            }
        }
    }, [lastJsonMessage]);

    const toggleCollapse = (itemId) => {
        const collapseId = `collapse_${itemId}`;
        const collapseElement = document.getElementById(collapseId);
        if (collapseElement) {
            const isCollapsed = collapseElement.classList.contains("show");
            if (isCollapsed) {
                collapseElement.classList.remove("show");
            } else {
                collapseElement.classList.add("show");
            }
        }
    };

    return (
        <>
            {dataReceived && (
                <Accordion defaultActiveKey={['0']} alwaysOpen className={"accordion-top-router"}>
                    <p className={"pseudo-h1"}>Router Data</p>
                    {routerData.map((router) => (
                        <Accordion.Item key={router.id} eventKey={router.id} className="rounded-2">
                            <Accordion.Header className={"accordion_header"}>
                                <div className="status-circle"
                                     style={{backgroundColor: router.active_status ? 'rgba(37,180,69,0.81)' : '#bd4358'}}></div>
                                <div
                                    className="font-monospace"
                                    onClick={() => toggleCollapse(router.id)}
                                    aria-controls={`collapse_${router.id}`}
                                >
                                    <strong>Name:</strong> {router.name}
                                    <span
                                        className={'text-span'}>  <strong>Active:</strong> {router.active_status.toString()}</span>
                                    <span>{currentTime}</span>
                                </div>
                            </Accordion.Header>
                            <Accordion.Body id={`collapse_${router.id}`}>
                                <ul className="list-styled font-monospace">
                                    <li><strong>ID:</strong> {router.id}</li>
                                    <li><strong>Created:</strong> {router.created_at}</li>
                                    <li><strong>Updated:</strong> {router.updated_at}</li>
                                    <li><strong>Ports:</strong></li>
                                    <Accordion defaultActiveKey={['0']} alwaysOpen className={"nested-accordion"}>
                                        {router.ports.map((port) => (
                                            <Accordion.Item key={port.id} eventKey={port.id} className="rounded-2">
                                                <Accordion.Header className={"accordion_header"}>
                                                    <div className="status-circle"
                                                         style={{backgroundColor: port.active_status ? '#37bd53' : '#c93849'}}></div>
                                                    <div className={"port-name"}><strong>Name:</strong> {port.name}  <strong className={"active-status"}>Active:</strong> {port.active_status.toString()}
                                                        <span className={'time-span'}>{currentTime}</span>
                                                    </div>
                                                </Accordion.Header>
                                                <Accordion.Body>
                                                    <ul className="list-styled font-monospace">
                                                        {Object.entries(port).map(([key, value]) => (
                                                            <li key={key}>
                                                                <strong>{key}:</strong> {value.toString()}
                                                            </li>
                                                        ))}
                                                    </ul>
                                                </Accordion.Body>
                                            </Accordion.Item>
                                        ))}
                                    </Accordion>
                                </ul>
                            </Accordion.Body>
                        </Accordion.Item>
                    ))}
                </Accordion>
            )}
        </>
    );
}

export default CheckRouterSocket;
