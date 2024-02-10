import {useEffect, useState} from "react";
import useWebSocket, {ReadyState} from "react-use-websocket";
import Accordion from 'react-bootstrap/Accordion';
import Charts from "./charts";
import './server_ws.css'

function CheckServerSocket() {

    const socketUrl = "ws://localhost:8000/ws_server";
    const {lastJsonMessage} = useWebSocket(socketUrl,
        {onOpen: () => console.log("Server WebSocket connected"),
            shouldReconnect: (closeEvent) => true, })
    const [serverData, setServerData] = useState([]);
    const [dataReceived, setDataReceived] = useState(false);
    const date = new Date();
    const currentTime = new Intl.DateTimeFormat('de-DE', {
        hour: "numeric",
        minute: "numeric",
    }).format(date)

    useEffect(() => {

        if (lastJsonMessage !== null && ReadyState.OPEN) {
            const data = lastJsonMessage;
            console.log("Message from server ", data);
            if (data[0].name === 'demo') {
                setServerData(data);
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
        <Accordion defaultActiveKey={['0']} alwaysOpen className={"accordion-top-server"}>
            <p className={"pseudo-h1"}>Server Data</p>
            {serverData.map((item) => (
                <Accordion.Item key={item.id} eventKey={item.id} className="rounded-2">
                    <Accordion.Header className={"accordion_header"}>
                        <Charts activeStatus = {item.active_status} />
                        <div
                            className="font-monospace"
                            onClick={() => toggleCollapse(item.id)}
                            aria-controls={`collapse_${item.id}`}
                        >
                            <strong>Name:</strong> {item.name}
                            <span className={'text-span-server'}>  <strong>Active:</strong> {item.active_status.toString()}</span>
                            <span className={"time-span"}>{currentTime}</span>
                        </div>
                    </Accordion.Header>
                    <Accordion.Body id={`collapse_${item.id}`}>
                        <ul className="list-styled font-monospace">
                            <li><strong>ID:</strong> {item.id}</li>
                            <li><strong>Image ID:</strong> {item.image_id}</li>
                            <li><strong>Flavor ID:</strong> {item.flavor_id}</li>
                            <li><strong>RAM:</strong> {item.flavor_info.ram} MB</li>
                            <li><strong>CPUs:</strong> {item.flavor_info.vcpus}</li>
                            <li><strong>Disk:</strong> {item.flavor_info.disk} GB</li>
                            <li><strong>Networkname:</strong> {item.networkname}</li>
                            <li><strong>IP Address:</strong> {item.address}</li>
                            <li><strong>Created:</strong> {item.created_at}</li>
                            <li><strong>Update:</strong> {item.updated_at}</li>
                        </ul>
                    </Accordion.Body>
                </Accordion.Item>
            ))}
        </Accordion>
            )}
        </>
    );

}

export default CheckServerSocket;
